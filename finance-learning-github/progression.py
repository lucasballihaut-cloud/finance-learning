"""Sauvegarde de la progression.

- Sur ton ordinateur : dans data/progression.json (chemin calculé à partir de ce fichier).
- En ligne (Streamlit Community Cloud) : dans la session de chaque visiteur, pour que chacun ait
  sa propre progression ; on peut la télécharger puis la réimporter (page « Ma progression »).
"""
import json
import os
from datetime import datetime
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "progression.json"

# Streamlit Community Cloud place les applications dans /mount/src/… ;
# FINANCE_LEARNING_WEB=1 permet de tester ce mode sur son ordinateur.
WEB = str(Path(__file__).resolve()).startswith("/mount/src") or os.environ.get("FINANCE_LEARNING_WEB") == "1"
SESSION_KEY = "progression"

EMPTY = {
    "chapitres_lus": {},      # module_id -> [chapitre_id, ...]
    "quiz": [],               # [{module, date, score, total, details: {question_id: bool}}]
    "flashcards": {},         # carte_id -> boîte de Leitner (1 à 5)
    "entretiens": {},         # question_id -> note 0 (à retravailler), 1 (moyen), 2 (maîtrisé)
    "brainteasers": {},       # id -> True si résolu
    "calcul": [],             # [{date, type, score, total, secondes}]
}


def now():
    return datetime.now().isoformat(timespec="seconds")


def empty():
    """Progression vierge (copie profonde de EMPTY)."""
    return json.loads(json.dumps(EMPTY))


def normalize(data):
    """Complète une progression (ancienne ou importée) avec les rubriques manquantes."""
    if not isinstance(data, dict):
        raise ValueError("Format de progression invalide.")
    for key in EMPTY:
        data.setdefault(key, empty()[key])
    return data


def load(path=DATA_PATH):
    if WEB and path == DATA_PATH:
        import streamlit as st
        return st.session_state.setdefault(SESSION_KEY, empty())
    if not path.exists():
        return empty()
    with open(path, encoding="utf-8") as f:
        return normalize(json.load(f))


def save(data, path=DATA_PATH):
    """Écrit d'abord dans un fichier temporaire puis le renomme : pas de fichier à moitié écrit."""
    if WEB and path == DATA_PATH:
        import streamlit as st
        st.session_state[SESSION_KEY] = data
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(path)


def mark_chapter(data, module_id, chapter_id, read=True):
    lus = data["chapitres_lus"].setdefault(module_id, [])
    if read and chapter_id not in lus:
        lus.append(chapter_id)
    if not read and chapter_id in lus:
        lus.remove(chapter_id)


def record_quiz(data, module_id, score, total, details):
    data["quiz"].append({"module": module_id, "date": now(), "score": score, "total": total,
                         "details": details})


def missed_questions(data, module_id):
    """Questions dont la DERNIÈRE réponse était fausse (pour le mode « revoir mes erreurs »)."""
    last = {}
    for attempt in data["quiz"]:
        if attempt["module"] == module_id:
            last.update(attempt["details"])
    return {qid for qid, ok in last.items() if not ok}


def question_stats(data, module_id):
    """Pour chaque question : (nb de bonnes réponses, nb de tentatives)."""
    stats = {}
    for attempt in data["quiz"]:
        if attempt["module"] == module_id:
            for qid, ok in attempt["details"].items():
                good, n = stats.get(qid, (0, 0))
                stats[qid] = (good + int(ok), n + 1)
    return stats


def best_score(data, module_id):
    pcts = [a["score"] / a["total"] for a in data["quiz"] if a["module"] == module_id and a["total"]]
    return max(pcts) if pcts else None


def update_flashcard(data, card_id, known):
    """Système de Leitner : connue -> boîte suivante (max 5) ; ratée -> retour en boîte 1."""
    box = data["flashcards"].get(card_id, 1)
    data["flashcards"][card_id] = min(box + 1, 5) if known else 1


def record_calcul(data, kind, score, total, seconds):
    data["calcul"].append({"date": now(), "type": kind, "score": score, "total": total,
                           "secondes": round(seconds, 1)})


def to_json(data):
    return json.dumps(data, ensure_ascii=False, indent=2)


def from_json(text):
    return normalize(json.loads(text))
