"""Formules de pricing utilisées dans les cours (Black-Scholes, binomial, obligations).

Aucune dépendance externe : la loi normale est calculée avec math.erf.
"""
import math
from statistics import NormalDist


def norm_cdf(x):
    """Fonction de répartition N(x) de la loi normale centrée réduite."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_pdf(x):
    """Densité n(x) de la loi normale centrée réduite."""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def d1_d2(S, K, T, r, sigma, q=0.0):
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    return d1, d1 - sigma * math.sqrt(T)


def black_scholes(S, K, T, r, sigma, q=0.0, kind="call"):
    """Prix Black-Scholes(-Merton) d'une option européenne. q = taux de dividende continu."""
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    if kind == "call":
        return S * math.exp(-q * T) * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    return K * math.exp(-r * T) * norm_cdf(-d2) - S * math.exp(-q * T) * norm_cdf(-d1)


def greeks(S, K, T, r, sigma, q=0.0, kind="call"):
    """Grecques Black-Scholes. Vega et rho pour +1 point (0,01), theta par jour (365 j)."""
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    disc_q, disc_r = math.exp(-q * T), math.exp(-r * T)
    gamma = disc_q * norm_pdf(d1) / (S * sigma * math.sqrt(T))
    vega = S * disc_q * norm_pdf(d1) * math.sqrt(T)
    common = -S * disc_q * norm_pdf(d1) * sigma / (2 * math.sqrt(T))
    if kind == "call":
        delta = disc_q * norm_cdf(d1)
        theta = common - r * K * disc_r * norm_cdf(d2) + q * S * disc_q * norm_cdf(d1)
        rho = K * T * disc_r * norm_cdf(d2)
    else:
        delta = disc_q * (norm_cdf(d1) - 1)
        theta = common + r * K * disc_r * norm_cdf(-d2) - q * S * disc_q * norm_cdf(-d1)
        rho = -K * T * disc_r * norm_cdf(-d2)
    return {"delta": delta, "gamma": gamma, "vega": vega / 100, "theta": theta / 365, "rho": rho / 100}


def binomial_one_step(S, u, d, r, dt, K, kind="call"):
    """Arbre binomial à une période : renvoie (prix, proba risque-neutre p, delta de couverture)."""
    payoff = (lambda s: max(s - K, 0.0)) if kind == "call" else (lambda s: max(K - s, 0.0))
    vu, vd = payoff(S * u), payoff(S * d)
    p = (math.exp(r * dt) - d) / (u - d)
    price = math.exp(-r * dt) * (p * vu + (1 - p) * vd)
    delta = (vu - vd) / (S * (u - d))
    return price, p, delta


def bond_price(face, coupon_rate, ytm, years, freq=1):
    """Prix d'une obligation à taux fixe (rendement actuariel ytm, composé freq fois par an)."""
    n = int(round(years * freq))
    c = face * coupon_rate / freq
    y = ytm / freq
    return sum(c / (1 + y) ** k for k in range(1, n + 1)) + face / (1 + y) ** n


def macaulay_duration(face, coupon_rate, ytm, years, freq=1):
    """Duration de Macaulay en années."""
    n = int(round(years * freq))
    c = face * coupon_rate / freq
    y = ytm / freq
    price = bond_price(face, coupon_rate, ytm, years, freq)
    flows = [(k, c + (face if k == n else 0.0)) for k in range(1, n + 1)]
    return sum((k / freq) * cf / (1 + y) ** k for k, cf in flows) / price


def modified_duration(face, coupon_rate, ytm, years, freq=1):
    return macaulay_duration(face, coupon_rate, ytm, years, freq) / (1 + ytm / freq)


# ---------- Risque ----------

def z_score(confidence):
    """Quantile de la loi normale : z_score(0.99) ≈ 2,326."""
    return NormalDist().inv_cdf(confidence)


def var_normal(value, sigma_daily, confidence=0.99, days=1):
    """VaR paramétrique gaussienne (moyenne nulle), règle de la racine du temps."""
    return z_score(confidence) * sigma_daily * math.sqrt(days) * value


def es_normal(value, sigma_daily, confidence=0.99, days=1):
    """Expected Shortfall gaussienne : sigma · n(z) / (1 − alpha)."""
    z = z_score(confidence)
    return sigma_daily * math.sqrt(days) * value * norm_pdf(z) / (1 - confidence)


# ---------- Produits structurés ----------

def capital_garanti(years, rate, sigma, margin=1.0, q=0.0):
    """Capital garanti 100 % : renvoie (prix du zéro-coupon, budget, prix du call ATM, participation).

    rate est un taux annuel (composé annuellement) ; il est converti en taux continu pour Black-Scholes.
    Tous les montants sont en % du nominal.
    """
    zc = 100 / (1 + rate) ** years
    budget = 100 - zc - margin
    call = black_scholes(100, 100, years, math.log(1 + rate), sigma, q)
    return zc, budget, call, budget / call


def autocall_flows(levels, kind="athena", coupon=0.08, autocall=1.0, coupon_barrier=0.7,
                   protection=0.6, step_down=0.0):
    """Flux d'un autocall pour 100 investis, avec une observation par période.

    levels : niveaux du sous-jacent en fraction du niveau initial (1.0 = 100 %), le dernier = maturité.
    kind : "athena", "phoenix" ou "phoenix_memoire".
    step_down : baisse du seuil de rappel à chaque période (0.05 = −5 points par an).
    Renvoie une liste de dicts {periode, niveau, seuil, flux, evenement}.
    """
    flows, missed, n = [], 0, len(levels)
    for i, x in enumerate(levels, start=1):
        seuil = autocall - step_down * (i - 1)
        last = i == n
        cash, events = 0.0, []
        if kind != "athena":
            if x >= coupon_barrier:
                paid = 1 + (missed if kind == "phoenix_memoire" else 0)
                cash += 100 * coupon * paid
                events.append(f"{paid} coupons versés (effet mémoire)" if paid > 1 else "coupon versé")
                missed = 0
            else:
                missed += 1
                events.append("pas de coupon")
        if x >= seuil:
            cash += 100 + (100 * coupon * i if kind == "athena" else 0)
            events.append("rappel anticipé" if not last else "remboursement à 100 %")
            flows.append({"periode": i, "niveau": x, "seuil": seuil, "flux": cash, "evenement": ", ".join(events)})
            return flows
        if last:
            if x >= protection:
                cash += 100
                events.append("capital protégé : 100 %")
            else:
                cash += 100 * x
                events.append(f"barrière franchie : perte en capital ({100 * x:.0f} %)")
        flows.append({"periode": i, "niveau": x, "seuil": seuil, "flux": cash,
                      "evenement": ", ".join(events) or "pas de rappel"})
    return flows


def barrier_payoff(product, x, hit, barrier=0.6, bonus=1.2, participation=1.0, rebate=0.05):
    """Remboursement à maturité (pour 100) selon la performance finale x = S_T/S_0.

    hit : la barrière a-t-elle été touchée pendant la vie du produit ?
    - "twin_win" : 100·(1 + |x − 1|) si barrière basse jamais touchée, sinon 100·x
    - "bonus"    : 100·max(bonus, x) si barrière basse jamais touchée, sinon 100·x
    - "shark"    : capital garanti ; 100·(1 + participation·max(x − 1, 0)) si barrière haute
                   jamais touchée, sinon 100·(1 + rebate)
    """
    if product == "twin_win":
        return 100 * (1 + abs(x - 1)) if not hit else 100 * x
    if product == "bonus":
        return 100 * max(bonus, x) if not hit else 100 * x
    if product == "shark":
        return 100 * (1 + participation * max(x - 1, 0)) if not hit else 100 * (1 + rebate)
    raise ValueError(product)


# ---------- Stratégies d'options ----------

# Jambes : (type, strike, quantité). Type "call", "put" ou "stock" ; K1 < K2 < K3.
STRATEGIES = {
    "Long call": [("call", "K2", 1)],
    "Long put": [("put", "K2", 1)],
    "Bull call spread": [("call", "K2", 1), ("call", "K3", -1)],
    "Bear put spread": [("put", "K2", 1), ("put", "K1", -1)],
    "Long straddle": [("call", "K2", 1), ("put", "K2", 1)],
    "Short straddle": [("call", "K2", -1), ("put", "K2", -1)],
    "Long strangle": [("put", "K1", 1), ("call", "K3", 1)],
    "Short strangle": [("put", "K1", -1), ("call", "K3", -1)],
    "Long butterfly": [("call", "K1", 1), ("call", "K2", -2), ("call", "K3", 1)],
    "Protective put": [("stock", None, 1), ("put", "K1", 1)],
    "Covered call": [("stock", None, 1), ("call", "K3", -1)],
    "Collar": [("stock", None, 1), ("put", "K1", 1), ("call", "K3", -1)],
    "Risk reversal": [("call", "K3", 1), ("put", "K1", -1)],
}


def strategy_pnl(name, s_final, strikes, premiums, spot):
    """P&L à maturité d'une stratégie. strikes = {"K1":..}, premiums = {("call", K): prix, ...}."""
    total = 0.0
    for kind, key, qty in STRATEGIES[name]:
        if kind == "stock":
            total += qty * (s_final - spot)
            continue
        k = strikes[key]
        payoff = max(s_final - k, 0.0) if kind == "call" else max(k - s_final, 0.0)
        total += qty * (payoff - premiums[(kind, k)])
    return total


# ---------- Valorisation d'entreprise ----------

def dcf(fcf0, growth, years, wacc, g_terminal, net_debt=0.0, shares=1.0):
    """DCF simple : FCF de l'année 0 qui croît de `growth` pendant `years` ans, puis valeur terminale de Gordon.

    Renvoie un dict : flux projetés, valeur actuelle des flux, valeur terminale (et actualisée),
    valeur d'entreprise, valeur des fonds propres et valeur par action.
    """
    if wacc <= g_terminal:
        raise ValueError("Le WACC doit être supérieur à la croissance perpétuelle.")
    flows = [fcf0 * (1 + growth) ** t for t in range(1, years + 1)]
    pv_flows = sum(f / (1 + wacc) ** t for t, f in enumerate(flows, start=1))
    tv = flows[-1] * (1 + g_terminal) / (wacc - g_terminal)
    pv_tv = tv / (1 + wacc) ** years
    ev = pv_flows + pv_tv
    equity = ev - net_debt
    return {"flux": flows, "va_flux": pv_flows, "vt": tv, "va_vt": pv_tv, "ve": ev,
            "fonds_propres": equity, "par_action": equity / shares}


def wacc(equity, debt, ke, kd, tax):
    total = equity + debt
    return equity / total * ke + debt / total * kd * (1 - tax)


# ---------- Matières premières ----------

def commodity_forward(spot, r, storage, convenience, T):
    """Prix à terme par le coût de portage : S·e^((r + u − y)T)."""
    return spot * math.exp((r + storage - convenience) * T)


def crack_321(crude, gasoline, diesel):
    """Crack spread 3:2:1 en $ par baril."""
    return (2 * gasoline + diesel - 3 * crude) / 3


def spark_spread(power, gas, heat_rate, co2_price=0.0, emission_factor=0.0):
    """Spark spread (clean si l'on fournit le prix et le facteur d'émission du CO₂)."""
    return power - heat_rate * gas - co2_price * emission_factor
