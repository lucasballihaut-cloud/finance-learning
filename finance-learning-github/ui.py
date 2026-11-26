"""Outils d'interface partagés par toutes les pages."""
import math

import pandas as pd
import streamlit as st

import formules
from contenu import MODULES, get_module


def module_picker(label="Module"):
    """Un bouton par module, en haut de la page ; le choix est conservé d'une page à l'autre."""
    ids = [m["id"] for m in MODULES]
    current = st.session_state.get("module_id", "options")
    choice = st.pills(f"**{label}** — clique pour changer", ids, default=current,
                      format_func=lambda i: f"{get_module(i)['icone']} {get_module(i)['titre']}")
    if choice is None:  # clic sur le module déjà choisi : on le garde
        choice = current
    if choice != current:
        st.session_state["module_id"] = choice
        st.rerun()
    st.session_state["module_id"] = choice
    return get_module(choice)


def widget_black_scholes():
    st.markdown("#### 🧪 À toi de jouer : calculateur Black-Scholes")
    c1, c2, c3 = st.columns(3)
    S = c1.number_input("Spot S", value=100.0, min_value=1.0, step=1.0)
    K = c1.number_input("Strike K", value=100.0, min_value=1.0, step=1.0)
    T = c2.slider("Maturité T (années)", 0.02, 3.0, 1.0, 0.01)
    r = c2.slider("Taux r (%)", -1.0, 8.0, 0.0, 0.25) / 100
    sigma = c3.slider("Volatilité σ (%)", 5.0, 80.0, 20.0, 1.0) / 100
    q = c3.slider("Dividende q (%)", 0.0, 6.0, 0.0, 0.25) / 100

    call = formules.black_scholes(S, K, T, r, sigma, q, "call")
    put = formules.black_scholes(S, K, T, r, sigma, q, "put")
    m1, m2, m3 = st.columns(3)
    m1.metric("Prix du call", f"{call:.3f}")
    m2.metric("Prix du put", f"{put:.3f}")
    m3.metric("Approx. ATM 0,4·S·σ·√T", f"{0.4 * S * sigma * T ** 0.5:.3f}")
    st.caption(f"Vérification de la parité : C − P = {call - put:.3f} et "
               f"S·e^(−qT) − K·e^(−rT) = {S * math.exp(-q * T) - K * math.exp(-r * T):.3f}")

    g_call = formules.greeks(S, K, T, r, sigma, q, "call")
    g_put = formules.greeks(S, K, T, r, sigma, q, "put")
    table = pd.DataFrame({"Call": g_call, "Put": g_put}).rename(index={
        "delta": "Delta", "gamma": "Gamma", "vega": "Vega (pour +1 pt de vol)",
        "theta": "Theta (par jour)", "rho": "Rho (pour +1 % de taux)"})
    st.dataframe(table.style.format("{:.4f}"), width="stretch")

    spots = [K * (0.5 + i / 100) for i in range(101)]
    curve = pd.DataFrame({
        "Spot": spots,
        "Call (prix)": [formules.black_scholes(s, K, T, r, sigma, q, "call") for s in spots],
        "Call (payoff à maturité)": [max(s - K, 0) for s in spots],
    }).set_index("Spot")
    st.line_chart(curve)
    st.caption("L'écart entre les deux courbes est la valeur temps : maximale près du strike.")


def widget_binomial():
    st.markdown("#### 🧪 À toi de jouer : arbre binomial à une période")
    c1, c2, c3 = st.columns(3)
    S = c1.number_input("S₀", value=100.0, min_value=1.0, key="bin_S")
    K = c1.number_input("Strike K", value=100.0, min_value=0.0, key="bin_K")
    u = c2.number_input("u (hausse)", value=1.2, min_value=1.0001, step=0.05, key="bin_u")
    d = c2.number_input("d (baisse)", value=0.8, min_value=0.01, max_value=0.9999, step=0.05, key="bin_d")
    r = c3.number_input("r (% par période)", value=0.0, step=0.5, key="bin_r") / 100
    kind = c3.radio("Type", ["call", "put"], horizontal=True, key="bin_kind")
    growth = math.exp(r)
    if not d < growth < u:
        st.error("Il faut d < e^r < u, sinon il existe un arbitrage (l'action domine ou est dominée par le placement sans risque).")
        return
    price, p, delta = formules.binomial_one_step(S, u, d, r, 1.0, K, kind)
    m1, m2, m3 = st.columns(3)
    m1.metric("Probabilité risque-neutre p", f"{p:.4f}")
    m2.metric("Prix de l'option", f"{price:.4f}")
    m3.metric("Delta de réplication", f"{delta:.4f}")


def widget_var():
    st.markdown("#### 🧪 À toi de jouer : VaR et Expected Shortfall gaussiennes")
    c1, c2, c3 = st.columns(3)
    value = c1.number_input("Valeur de la position (€)", value=1_000_000.0, min_value=0.0, step=100_000.0)
    sigma = c2.slider("Volatilité journalière (%)", 0.2, 5.0, 1.5, 0.1) / 100
    conf = c3.select_slider("Niveau de confiance", [0.90, 0.95, 0.975, 0.99, 0.995],
                            value=0.99, format_func=lambda x: f"{x:.1%}")
    days = c1.slider("Horizon (jours)", 1, 20, 1)
    var = formules.var_normal(value, sigma, conf, days)
    es = formules.es_normal(value, sigma, conf, days)
    m1, m2, m3 = st.columns(3)
    m1.metric("z", f"{formules.z_score(conf):.3f}")
    m2.metric("VaR", f"{var:,.0f} €".replace(",", " "))
    m3.metric("Expected Shortfall", f"{es:,.0f} €".replace(",", " "))
    st.caption(f"Volatilité annualisée équivalente : {sigma * math.sqrt(252):.1%}. "
               "L'ES est toujours au-dessus de la VaR : c'est la perte moyenne quand on dépasse la VaR.")


def widget_capital_garanti():
    st.markdown("#### 🧪 À toi de jouer : fabriquer un capital garanti")
    c1, c2, c3 = st.columns(3)
    years = c1.slider("Maturité (années)", 1, 10, 5)
    rate = c2.slider("Taux zéro-coupon (% par an)", 0.0, 6.0, 3.0, 0.25) / 100
    sigma = c3.slider("Volatilité de l'indice (%)", 5.0, 40.0, 18.0, 1.0) / 100
    margin = c1.slider("Marge émetteur (%)", 0.0, 4.0, 1.0, 0.25)
    q = c2.slider("Dividendes de l'indice (%)", 0.0, 5.0, 0.0, 0.25) / 100
    zc, budget, call, part = formules.capital_garanti(years, rate, sigma, margin, q)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Zéro-coupon", f"{zc:.2f} %")
    m2.metric("Budget options", f"{budget:.2f} %")
    m3.metric("Call ATM", f"{call:.2f} %")
    m4.metric("Participation", f"{part:.0%}" if budget > 0 else "impossible")
    if budget <= 0:
        st.error("Le zéro-coupon et la marge consomment tout le capital : produit infaisable.")
    st.caption("Teste les sensibilités : monte les taux (participation ↑), monte la vol (participation ↓).")


AUTOCALL_SCENARIOS = {
    "Hausse rapide": [105, 110, 115, 120, 125, 130, 135, 140],
    "Rappel tardif": [90, 85, 95, 102, 105, 108, 110, 112],
    "Chahuté": [90, 75, 65, 98, 101, 100, 100, 100],
    "Stagnation à 80 %": [80, 82, 78, 80, 81, 79, 80, 80],
    "Baisse puis krach": [90, 75, 60, 55, 50, 52, 48, 50],
}
AUTOCALL_TYPES = {"athena": "Athena", "phoenix": "Phoenix", "phoenix_memoire": "Phoenix mémoire"}


def widget_autocall():
    st.markdown("#### 🧪 Simulateur d'autocall : choisis un produit et un scénario")
    c1, c2, c3 = st.columns(3)
    kind = c1.radio("Produit", list(AUTOCALL_TYPES), format_func=AUTOCALL_TYPES.get, key="ac_kind")
    coupon = c1.slider("Coupon annuel (%)", 2.0, 12.0, 8.0 if kind == "athena" else 6.0, 0.5, key=f"ac_cp_{kind}") / 100
    autocall = c2.slider("Seuil de rappel (%)", 80, 110, 100, 5, key="ac_rappel") / 100
    step = c2.slider("Step-down par an (points)", 0, 5, 0, 1, key="ac_step") / 100
    barrier_c = c3.slider("Barrière de coupon (%)", 50, 100, 70, 5, key="ac_bc",
                          disabled=kind == "athena") / 100
    protection = c3.slider("Barrière de protection (%)", 40, 80, 60, 5, key="ac_prot") / 100

    scen = st.selectbox("Scénario de marché (niveau de l'indice à chaque date annuelle, en % du niveau initial)",
                        list(AUTOCALL_SCENARIOS), key="ac_scen")
    cols = st.columns(8)
    levels = [cols[i].number_input(f"An {i + 1}", 0, 300, AUTOCALL_SCENARIOS[scen][i], 5,
                                   key=f"ac_{scen}_{i}") / 100 for i in range(8)]

    flows = formules.autocall_flows(levels, kind, coupon, autocall, barrier_c, protection, step)
    total = sum(f["flux"] for f in flows)
    years = len(flows)
    m1, m2, m3 = st.columns(3)
    m1.metric("Total reçu pour 100 investis", f"{total:.1f}")
    m2.metric("Durée de vie", f"{years} an{'s' if years > 1 else ''}")
    m3.metric("Gain ou perte", f"{total - 100:+.1f}")
    table = pd.DataFrame([{"Année": f["periode"], "Indice": f"{100 * f['niveau']:.0f} %",
                           "Seuil de rappel": f"{100 * f['seuil']:.0f} %", "Flux reçu": round(f["flux"], 2),
                           "Ce qui se passe": f["evenement"]} for f in flows])
    st.dataframe(table, hide_index=True, width="stretch")
    chart = pd.DataFrame({"Indice": [100 * x for x in levels],
                          "Seuil de rappel": [100 * (autocall - step * i) for i in range(8)],
                          "Barrière de protection": [100 * protection] * 8},
                         index=range(1, 9))
    if kind != "athena":
        chart["Barrière de coupon"] = 100 * barrier_c
    st.line_chart(chart, x_label="Année", y_label="% du niveau initial")
    st.caption("Modifie les niveaux année par année pour inventer tes propres scénarios. "
               "Après un rappel, les années suivantes ne comptent plus.")


def widget_barrieres():
    st.markdown("#### 🧪 Remboursement à maturité selon la performance finale")
    c1, c2 = st.columns(2)
    product = c1.radio("Produit", ["twin_win", "bonus", "shark"], horizontal=True, key="bar_prod",
                       format_func={"twin_win": "Twin Win", "bonus": "Bonus", "shark": "Shark"}.get)
    if product == "shark":
        barrier = c2.slider("Barrière haute (%)", 110, 180, 130, 5, key="bar_up") / 100
        part = c2.slider("Participation (%)", 50, 150, 100, 10, key="bar_part") / 100
        rebate = c2.slider("Rebate si barrière touchée (%)", 0, 15, 5, 1, key="bar_reb") / 100
        kw = {"participation": part, "rebate": rebate}
    else:
        barrier = c2.slider("Barrière basse (%)", 40, 90, 60 if product == "twin_win" else 70, 5,
                            key=f"bar_down_{product}") / 100
        bonus = c2.slider("Niveau du bonus (%)", 100, 150, 120, 5, key="bar_bonus",
                          disabled=product != "bonus") / 100
        kw = {"bonus": bonus}
    xs = [0.3 + i * 0.01 for i in range(141)]
    rows = []
    for x in xs:
        # La barrière basse est forcément touchée si l'on finit en dessous ; idem pour la barrière haute.
        ok = (x < barrier) if product == "shark" else (x > barrier)
        rows.append({"Performance finale (%)": round(100 * x),
                     "Barrière jamais touchée": formules.barrier_payoff(product, x, False, barrier, **kw) if ok else None,
                     "Barrière touchée": formules.barrier_payoff(product, x, True, barrier, **kw),
                     "Action seule": 100 * x})
    st.line_chart(pd.DataFrame(rows).set_index("Performance finale (%)"), y_label="Remboursement pour 100")
    x_test = st.slider("Teste une performance finale (%)", 30, 170, 80, 5, key="bar_x") / 100
    a, b = st.columns(2)
    possible = (x_test < barrier) if product == "shark" else (x_test > barrier)
    a.metric("Si la barrière n'a jamais été touchée",
             f"{formules.barrier_payoff(product, x_test, False, barrier, **kw):.1f}" if possible else "impossible")
    b.metric("Si la barrière a été touchée", f"{formules.barrier_payoff(product, x_test, True, barrier, **kw):.1f}")


def widget_strategies():
    st.markdown("#### 🧪 Simulateur de stratégies : P&L à maturité")
    c1, c2, c3 = st.columns(3)
    name = c1.selectbox("Stratégie", list(formules.STRATEGIES), key="strat_name")
    sigma = c2.slider("Volatilité implicite (%)", 5, 60, 20, 1, key="strat_vol") / 100
    T = c2.slider("Maturité (mois)", 1, 24, 6, 1, key="strat_T") / 12
    k1 = c3.number_input("K1 (strike bas)", 50, 150, 90, 5, key="strat_k1")
    k2 = c3.number_input("K2 (strike central)", 50, 150, 100, 5, key="strat_k2")
    k3 = c3.number_input("K3 (strike haut)", 50, 150, 110, 5, key="strat_k3")
    if not k1 < k2 < k3:
        st.error("Il faut K1 < K2 < K3.")
        return
    spot = 100.0
    strikes = {"K1": k1, "K2": k2, "K3": k3}
    premiums = {(kind, k): formules.black_scholes(spot, k, T, 0.0, sigma, kind=kind)
                for k in (k1, k2, k3) for kind in ("call", "put")}
    legs = []
    for kind, key, qty in formules.STRATEGIES[name]:
        if kind == "stock":
            legs.append(f"{'achat' if qty > 0 else 'vente'} de l'action à 100")
        else:
            k = strikes[key]
            legs.append(f"{'achat' if qty > 0 else 'vente'} de {abs(qty)} {kind} {k} (prime {premiums[(kind, k)]:.2f})")
    st.markdown("**Composition** : " + " ; ".join(legs))

    grid = [spot * i / 200 for i in range(401)]  # spot final de 0 à 200
    pnl = [formules.strategy_pnl(name, x, strikes, premiums, spot) for x in grid]
    shown = [(x, p) for x, p in zip(grid, pnl) if 40 <= x <= 160]
    st.line_chart(pd.DataFrame(shown, columns=["Spot à maturité", "P&L"]).set_index("Spot à maturité"))

    # Au-delà de 200, le P&L continue avec la même pente : si elle n'est pas nulle, le gain ou la perte est illimité.
    slope = pnl[-1] - pnl[-2]
    max_gain = "illimité" if slope > 1e-9 else f"{max(pnl):.2f}"
    max_loss = "illimitée" if slope < -1e-9 else f"{min(pnl):.2f}"
    breakevens = [round((grid[i] + grid[i + 1]) / 2, 1) for i in range(len(grid) - 1)
                  if (pnl[i] < 0) != (pnl[i + 1] < 0)]
    m1, m2, m3 = st.columns(3)
    m1.metric("Gain maximal", max_gain)
    m2.metric("Perte maximale", max_loss)
    m3.metric("Point(s) mort(s)", ", ".join(str(b) for b in breakevens) or "aucun")
    st.caption("Primes calculées avec Black-Scholes (spot 100, taux nuls). Change la vol : les stratégies "
               "acheteuses d'options coûtent plus cher, les vendeuses rapportent plus.")


def widget_dcf():
    st.markdown("#### 🧪 Calculateur DCF")
    c1, c2, c3 = st.columns(3)
    fcf0 = c1.number_input("FCF de l'année écoulée (M€)", value=100.0, min_value=0.0, step=10.0, key="dcf_fcf")
    growth = c1.slider("Croissance des FCF sur l'horizon (%)", -5.0, 25.0, 5.0, 0.5, key="dcf_gr") / 100
    years = c1.slider("Horizon explicite (années)", 3, 10, 5, key="dcf_years")
    ke = c2.slider("Coût des fonds propres kₑ (%)", 4.0, 15.0, 9.0, 0.25, key="dcf_ke") / 100
    kd = c2.slider("Coût de la dette k_d (%)", 1.0, 10.0, 5.0, 0.25, key="dcf_kd") / 100
    weight_d = c2.slider("Part de la dette D/(D+E) (%)", 0, 70, 30, 5, key="dcf_wd") / 100
    tax = c2.slider("Taux d'impôt (%)", 0, 40, 25, 1, key="dcf_tax") / 100
    g = c3.slider("Croissance perpétuelle g (%)", 0.0, 4.0, 2.0, 0.25, key="dcf_g") / 100
    net_debt = c3.number_input("Dette nette (M€)", value=500.0, step=50.0, key="dcf_nd")
    shares = c3.number_input("Nombre d'actions (millions)", value=100.0, min_value=0.1, step=10.0, key="dcf_sh")
    w = formules.wacc(1 - weight_d, weight_d, ke, kd, tax)
    if w <= g:
        st.error(f"Le WACC ({w:.2%}) doit être supérieur à g : sinon la valeur terminale est infinie.")
        return
    r = formules.dcf(fcf0, growth, years, w, g, net_debt, shares)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("WACC", f"{w:.2%}")
    m2.metric("VE (M€)", f"{r['ve']:,.0f}".replace(",", " "))
    m3.metric("Par action (€)", f"{r['par_action']:.2f}")
    m4.metric("Poids de la VT", f"{r['va_vt'] / r['ve']:.0%}")
    st.caption(f"VA des flux explicites : {r['va_flux']:,.0f} M€ · valeur terminale actualisée : {r['va_vt']:,.0f} M€ · "
               f"fonds propres : {r['fonds_propres']:,.0f} M€.".replace(",", " "))
    st.markdown("**Table de sensibilité : valeur par action (€)** — WACC en ligne, g en colonne")
    rows = {}
    for dw in (-0.01, -0.005, 0, 0.005, 0.01):
        ww = w + dw
        rows[f"WACC {ww:.2%}"] = {f"g {gg:.2%}": (round(formules.dcf(fcf0, growth, years, ww, gg, net_debt, shares)["par_action"], 2)
                                                   if ww > gg else None)
                                  for gg in (g - 0.005, g, g + 0.005)}
    st.dataframe(pd.DataFrame(rows).T, width="stretch")


def widget_courbe_commodity():
    st.markdown("#### 🧪 Courbe à terme et coût de roulement")
    c1, c2 = st.columns(2)
    spot = c1.number_input("Prix spot", value=80.0, min_value=1.0, step=1.0, key="cc_spot")
    r = c1.slider("Taux de financement r (%)", 0.0, 8.0, 4.0, 0.25, key="cc_r") / 100
    u = c2.slider("Coût de stockage u (% par an)", 0.0, 15.0, 2.0, 0.5, key="cc_u") / 100
    y = c2.slider("Convenience yield y (% par an)", 0.0, 30.0, 1.0, 0.5, key="cc_y") / 100
    months = list(range(0, 25))
    curve = pd.DataFrame({"Échéance (mois)": months,
                          "Prix à terme": [formules.commodity_forward(spot, r, u, y, m / 12) for m in months]})
    st.line_chart(curve.set_index("Échéance (mois)"))
    carry = r + u - y
    f1 = formules.commodity_forward(spot, r, u, y, 1 / 12)
    m1, m2, m3 = st.columns(3)
    m1.metric("Forme de la courbe", "Contango" if carry > 0 else ("Backwardation" if carry < 0 else "Plate"))
    m2.metric("Future 1 mois", f"{f1:.2f}")
    m3.metric("Roll yield annuel (spot stable)", f"{-carry:+.1%}")
    st.caption(f"Roll yield d'un investisseur long qui roule chaque mois, si le spot ne bouge pas : négatif en contango, "
               f"positif en backwardation. Il s'y ajoute le rendement du collatéral placé au taux r ({r:+.1%}), soit au total "
               f"{-(u - y):+.1%} par an. Monte le convenience yield pour simuler un marché tendu.")


WIDGETS = {"courbe_commodity": widget_courbe_commodity, "dcf": widget_dcf, "strategies": widget_strategies, "black_scholes": widget_black_scholes, "binomial": widget_binomial,
           "var": widget_var, "capital_garanti": widget_capital_garanti,
           "autocall": widget_autocall, "barrieres": widget_barrieres}


def score_color(pct):
    return "🟢" if pct >= 0.8 else ("🟠" if pct >= 0.5 else "🔴")
