"""Vérifie les formules et les réponses numériques des quiz (le contenu pédagogique doit être exact)."""
import math

import pytest

import formules as f
from contenu import get_module


def test_black_scholes_valeur_de_reference():
    # Valeurs classiques : S=K=100, r=5 %, sigma=20 %, T=1
    assert f.black_scholes(100, 100, 1, 0.05, 0.2) == pytest.approx(10.4506, abs=1e-4)
    assert f.black_scholes(100, 100, 1, 0.05, 0.2, kind="put") == pytest.approx(5.5735, abs=1e-4)


@pytest.mark.parametrize("S,K,T,r,sigma,q", [(100, 90, 0.5, 0.03, 0.3, 0.01), (50, 60, 2, 0.0, 0.15, 0.02)])
def test_parite_call_put(S, K, T, r, sigma, q):
    c = f.black_scholes(S, K, T, r, sigma, q)
    p = f.black_scholes(S, K, T, r, sigma, q, kind="put")
    assert c - p == pytest.approx(S * math.exp(-q * T) - K * math.exp(-r * T), abs=1e-10)


def test_grecques_par_differences_finies():
    S, K, T, r, s = 100, 105, 0.75, 0.02, 0.25
    g = f.greeks(S, K, T, r, s)
    h = 1e-3
    price = lambda **kw: f.black_scholes(kw.get("S", S), K, kw.get("T", T), kw.get("r", r), kw.get("s", s))
    assert g["delta"] == pytest.approx((price(S=S + h) - price(S=S - h)) / (2 * h), abs=1e-5)
    assert g["gamma"] == pytest.approx((price(S=S + h) - 2 * price() + price(S=S - h)) / h ** 2, abs=1e-4)
    assert g["vega"] == pytest.approx((price(s=s + h) - price(s=s - h)) / (2 * h) / 100, abs=1e-6)
    assert g["theta"] == pytest.approx(-(price(T=T + h) - price(T=T - h)) / (2 * h) / 365, abs=1e-6)


def test_approximation_atm():
    exact = f.black_scholes(100, 100, 1, 0.0, 0.2)
    assert exact == pytest.approx(7.97, abs=0.01)
    assert 0.4 * 100 * 0.2 == pytest.approx(exact, rel=0.01)


def test_binomial():
    price, p, delta = f.binomial_one_step(100, 1.2, 0.8, 0.0, 1.0, 100)
    assert (price, p, delta) == pytest.approx((10, 0.5, 0.5))


def test_obligations():
    assert f.bond_price(100, 0.04, 0.04, 7) == pytest.approx(100)
    assert f.macaulay_duration(100, 0.0, 0.05, 7) == pytest.approx(7)
    assert f.macaulay_duration(100, 0.08, 0.05, 7) < f.macaulay_duration(100, 0.02, 0.05, 7)


def answers(module_id):
    return {q["id"]: q for q in get_module(module_id)["quiz"]}


def test_reponses_quiz_options():
    q = answers("options")
    assert q["opt-q02"]["reponse"] == pytest.approx(8 - 100 + 105 * math.exp(-0.05), abs=0.01)
    price, _, delta = f.binomial_one_step(100, 1.1, 0.9, 0.0, 1.0, 100)
    assert q["opt-q06"]["reponse"] == pytest.approx(price)
    assert q["opt-q07"]["reponse"] == pytest.approx(delta)
    assert abs(q["opt-q09"]["reponse"] - f.black_scholes(200, 200, 0.25, 0.0, 0.25)) <= q["opt-q09"]["tolerance"]


def test_reponses_quiz_taux_et_marches():
    t, m = answers("taux"), answers("marches")
    assert t["taux-q01"]["reponse"] == pytest.approx(1000 / 1.05 ** 2, abs=0.01)
    assert t["taux-q07"]["reponse"] == pytest.approx(100 * (1.03 ** 2 / 1.02 - 1), abs=0.01)
    assert m["mar-q01"]["reponse"] == pytest.approx(100 * math.exp(0.02), abs=0.01)
    assert m["mar-q02"]["reponse"] == pytest.approx(1.10 * math.exp(0.02), abs=1e-4)


def test_var_et_es():
    assert f.z_score(0.99) == pytest.approx(2.3263, abs=1e-4)
    assert f.var_normal(1_000_000, 0.02, 0.99) == pytest.approx(46_527, abs=1)
    # ES 97,5 % proche de la VaR 99 % en gaussien
    assert f.es_normal(1, 1, 0.975) == pytest.approx(f.var_normal(1, 1, 0.99), abs=0.02)
    assert f.es_normal(1, 1, 0.99) > f.var_normal(1, 1, 0.99)


def test_capital_garanti_sensibilites():
    _, _, _, base = f.capital_garanti(5, 0.03, 0.18)
    assert f.capital_garanti(5, 0.04, 0.18)[3] > base   # taux plus hauts -> participation plus haute
    assert f.capital_garanti(5, 0.03, 0.25)[3] < base   # vol plus haute -> participation plus basse


def test_reponses_quiz_risque_macro_structures():
    r, m, s = answers("risque"), answers("macro"), answers("structures")
    assert abs(r["risk-q01"]["reponse"] - math.sqrt(252)) <= r["risk-q01"]["tolerance"]
    assert abs(r["risk-q02"]["reponse"] - f.var_normal(1e6, 0.02, 0.99)) <= r["risk-q02"]["tolerance"]
    assert abs(r["risk-q03"]["reponse"] - 50_000 * math.sqrt(10)) <= 1
    assert r["risk-q08"]["reponse"] == pytest.approx(100 * math.sqrt(2 * 0.25 * 0.04), abs=0.01)
    assert r["risk-q09"]["reponse"] == pytest.approx(100 * math.sqrt(0.94 * 1e-4 + 0.06 * 4e-4), abs=0.01)
    assert r["risk-q10"]["reponse"] == pytest.approx(100 * math.sqrt(0.000002 / (1 - 0.98)))
    assert abs(m["mac-q01"]["reponse"] - 100 * (1.05 / 1.03 - 1)) <= m["mac-q01"]["tolerance"]
    assert abs(m["mac-q04"]["reponse"] - 100 * (1.02 * 1.03 - 1)) <= m["mac-q04"]["tolerance"]
    assert s["str-q01"]["reponse"] == pytest.approx(100 / 1.03 ** 5, abs=0.01)
    # Discount = action - call = ZC(K) - put : cohérence via Black-Scholes
    S, K, T, rr, sig = 50, 55, 1, 0.03, 0.25
    assert S - f.black_scholes(S, K, T, rr, sig) == pytest.approx(
        K * math.exp(-rr * T) - f.black_scholes(S, K, T, rr, sig, kind="put"))


def total(levels, kind, coupon, **kw):
    return sum(fl["flux"] for fl in f.autocall_flows(levels, kind, coupon, **kw))


def test_autocalls_scenarios_du_cours():
    assert total([1.05], "athena", 0.08) == pytest.approx(108)
    assert total([0.9, 0.85, 0.95, 1.02], "athena", 0.08) == pytest.approx(132)
    assert total([0.8] * 8, "athena", 0.08) == pytest.approx(100)
    assert total([0.9, 0.7, 0.6, 0.55, 0.5, 0.5, 0.5, 0.5], "athena", 0.08) == pytest.approx(50)
    path = [0.9, 0.75, 0.65, 0.98, 1.01]
    assert total(path, "phoenix", 0.06) == pytest.approx(124)
    assert total(path, "phoenix_memoire", 0.06) == pytest.approx(130)
    assert total([0.8] * 8, "phoenix", 0.06) == pytest.approx(148)
    assert total([0.9, 0.75, 0.6, 0.55, 0.5, 0.5, 0.5, 0.5], "phoenix", 0.06) == pytest.approx(62)
    # step-down : rappel à 95 % en année 2
    assert len(f.autocall_flows([0.9, 0.96, 1.0], "athena", 0.08, step_down=0.05)) == 2


def test_reponses_quiz_structures_produits():
    s = answers("structures")
    assert total([0.9, 0.95, 1.03], "athena", 0.08) == s["str-q12"]["reponse"]
    assert f.autocall_flows([0.65, 0.8, 0.8, 0.8], "phoenix_memoire", 0.07)[1]["flux"] == pytest.approx(s["str-q14"]["reponse"])
    assert total([0.9] * 7 + [0.8], "athena", 0.08) == s["str-q15"]["reponse"]
    assert total([0.9] * 7 + [0.55], "athena", 0.08) == pytest.approx(s["str-q16"]["reponse"])
    assert f.barrier_payoff("twin_win", 0.75, False) == pytest.approx(s["str-q18"]["reponse"])
    assert f.barrier_payoff("twin_win", 0.75, True) == pytest.approx(s["str-q19"]["reponse"])
    assert f.barrier_payoff("bonus", 1.10, False, barrier=0.7, bonus=1.2) == pytest.approx(s["str-q21"]["reponse"])
    assert f.barrier_payoff("shark", 1.25, True, barrier=1.3, rebate=0.05) == pytest.approx(s["str-q22"]["reponse"])


def test_strategies_du_cours():
    K = {"K1": 90, "K2": 100, "K3": 110}
    P = {("call", 90): 12, ("call", 100): 6, ("call", 110): 2.5, ("put", 90): 2, ("put", 100): 6, ("put", 110): 12.5}
    pnl = lambda n, x: f.strategy_pnl(n, x, K, P, 100)
    assert pnl("Bull call spread", 103.5) == pytest.approx(0)
    assert pnl("Long straddle", 112) == pytest.approx(0)
    assert pnl("Long butterfly", 100) == pytest.approx(7.5)
    assert pnl("Protective put", 50) == pytest.approx(-12)
    assert pnl("Collar", 150) == pytest.approx(10.5)


def test_reponses_quiz_approfondies():
    o, t, m, r, ma = (answers(x) for x in ("options", "taux", "marches", "risque", "macro"))
    assert abs(o["opt-q21"]["reponse"] - (10 - 4 - 100 + 100 * math.exp(-0.05))) <= o["opt-q21"]["tolerance"]
    assert o["opt-q22"]["reponse"] == pytest.approx(100_000 / 40 * (25 ** 2 - 20 ** 2))
    assert t["taux-q10"]["reponse"] == pytest.approx(98.5 + 3 * 73 / 365)
    assert t["taux-q11"]["reponse"] == pytest.approx(100 * (-5 * 0.01 + 0.5 * 40 * 0.0001))
    assert abs(t["taux-q12"]["reponse"] - 10 * 850 / 190) <= t["taux-q12"]["tolerance"]
    assert abs(m["mar-q12"]["reponse"] - 1e4 * 1.1 * (math.exp(0.02) - 1)) <= m["mar-q12"]["tolerance"]
    assert m["mar-q15"]["reponse"] == pytest.approx(10 / 1.1, abs=0.01)
    assert r["risk-q14"]["reponse"] == pytest.approx(100 * (91 / 130 - 1), abs=0.05)
    assert r["risk-q16"]["reponse"] == pytest.approx(1.2 * 10e6 / (4000 * 10))
    assert ma["mac-q16"]["reponse"] == pytest.approx((0.03 - 0.035) * 110 + 2)


def test_dcf_et_wacc():
    assert f.wacc(600, 400, 0.09, 0.05, 0.25) == pytest.approx(0.069)
    r = f.dcf(100, 0.0, 1, 0.07, 0.02)  # croissance nulle sur 1 an : VE = 100/1,07 + 100·1,02/0,05/1,07
    assert r["ve"] == pytest.approx(100 / 1.07 + 100 * 1.02 / 0.05 / 1.07)
    with pytest.raises(ValueError):
        f.dcf(100, 0.05, 5, 0.02, 0.03)


def test_reponses_quiz_actions_derives():
    e, d = answers("actions"), answers("derives")
    assert e["eq-q06"]["reponse"] == pytest.approx(100 * f.wacc(600, 400, 0.09, 0.05, 0.25))
    assert e["eq-q09"]["reponse"] == pytest.approx(60 * 1.02 / 0.06)
    assert abs(e["eq-q15"]["reponse"] - 100 * 2 / 48) <= e["eq-q15"]["tolerance"]
    assert abs(e["eq-q16"]["reponse"] - 5000 * math.exp(0.01 * 0.25)) <= e["eq-q16"]["tolerance"]
    assert abs(d["der-q03"]["reponse"] - 80 * math.exp(0.05)) <= d["der-q03"]["tolerance"]
    df = [1.03 ** -t for t in (1, 2, 3)]
    assert abs(d["der-q08"]["reponse"] - (4 * sum(df) + 100 * df[-1] - 100)) <= d["der-q08"]["tolerance"]
    assert abs(d["der-q07"]["reponse"] - 0.675 * 2_000_000 / 42_000) <= d["der-q07"]["tolerance"]


def test_commodities():
    c = answers("commodities")
    assert abs(c["com-q03"]["reponse"] - f.commodity_forward(80, 0.04, 0.02, 0.01, 1)) <= c["com-q03"]["tolerance"]
    assert abs(c["com-q07"]["reponse"] - f.crack_321(80, 100, 110)) <= c["com-q07"]["tolerance"]
    assert f.spark_spread(90, 35, 2) == pytest.approx(c["com-q08"]["reponse"])
    assert abs(c["com-q09"]["reponse"] - f.spark_spread(90, 35, 2, 70, 0.37)) <= c["com-q09"]["tolerance"]
    assert f.commodity_forward(80, 0.04, 0.0, 0.10, 1) < 80  # backwardation si y > r + u
