"""Générateur d'exercices de calcul mental (style tests en ligne des banques)."""
import random

TYPES = {
    "mult": "Multiplications",
    "pct": "Pourcentages",
    "div": "Divisions décimales",
    "carre": "Carrés et racines",
    "frac": "Fractions → décimal",
    "mix": "Tout mélangé",
}


def generate(kind, rng):
    """Renvoie (énoncé, réponse exacte, tolérance)."""
    if kind == "mix":
        kind = rng.choice([k for k in TYPES if k != "mix"])
    if kind == "mult":
        a, b = rng.randint(12, 99), rng.choice([rng.randint(3, 9), rng.randint(11, 29)])
        return f"{a} × {b}", a * b, 0
    if kind == "pct":
        p = rng.choice([5, 12.5, 15, 20, 25, 35, 40, 60, 75, 120])
        x = rng.choice([40, 80, 120, 240, 360, 480, 640, 1200, 2500])
        return f"{str(p).replace('.', ',')} % de {x}", p * x / 100, 0.01
    if kind == "div":
        b = rng.choice([4, 8, 16, 25, 40, 125])
        a = rng.randint(3, 60)
        return f"{a} ÷ {b}", a / b, 0.005
    if kind == "carre":
        if rng.random() < 0.6:
            n = rng.randint(11, 35)
            return f"{n}²", n * n, 0
        n = rng.randint(11, 30)
        return f"√{n * n}", n, 0
    # fractions
    num, den = rng.choice([(1, 8), (3, 8), (5, 8), (7, 8), (1, 6), (5, 6), (1, 7), (2, 7), (1, 9),
                           (4, 9), (1, 12), (5, 12), (3, 16), (1, 11)])
    return f"{num}/{den} (3 décimales)", num / den, 0.0005


def series(kind, n, seed=None):
    rng = random.Random(seed)
    return [generate(kind, rng) for _ in range(n)]
