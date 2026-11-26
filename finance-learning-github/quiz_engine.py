"""Correction des réponses de quiz (fonctions pures, testées dans tests/)."""
import random


def parse_number(text):
    """Convertit une saisie utilisateur en nombre : accepte « 7,88 », « 7.88 », « 12 % », espaces.

    Renvoie None si la saisie est vide ou illisible.
    """
    if text is None:
        return None
    s = str(text).strip().replace(" ", "").replace(" ", "").replace("%", "").replace("€", "")
    s = s.replace(",", ".")
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def is_correct(question, answer):
    """True si la réponse donnée est juste.

    - question QCM : answer = index du choix sélectionné (ou None)
    - question numérique : answer = texte saisi ; juste si |x - réponse| <= tolérance
    """
    if question["type"] == "qcm":
        return answer is not None and answer == question["reponse"]
    value = parse_number(answer)
    if value is None:
        return False
    tol = question.get("tolerance", 1e-9)
    return abs(value - question["reponse"]) <= tol + 1e-12


def grade(questions, answers):
    """Corrige un quiz. answers : dict id -> réponse. Renvoie (score, détail par id)."""
    details = {q["id"]: is_correct(q, answers.get(q["id"])) for q in questions}
    return sum(details.values()), details


def pick_questions(questions, n, missed_ids=None, seed=None):
    """Choisit n questions au hasard ; si missed_ids est fourni, seulement celles déjà ratées."""
    pool = [q for q in questions if missed_ids is None or q["id"] in missed_ids]
    rng = random.Random(seed)
    return rng.sample(pool, min(n, len(pool)))
