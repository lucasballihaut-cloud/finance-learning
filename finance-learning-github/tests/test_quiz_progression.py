import pytest

import calcul
import progression as prog
import quiz_engine as qe
from contenu import MODULES, all_flashcards
from contenu.brainteasers import BRAINTEASERS
from contenu.entretiens import QUESTIONS


@pytest.mark.parametrize("text,expected", [("7,88", 7.88), (" 7.88 ", 7.88), ("-2,5 %", -2.5),
                                           ("6 120", 6120), ("", None), ("abc", None), (None, None)])
def test_parse_number(text, expected):
    assert qe.parse_number(text) == expected


def test_correction():
    qcm = {"id": "a", "type": "qcm", "choix": ["x", "y"], "reponse": 1}
    num = {"id": "b", "type": "nombre", "reponse": 7.88, "tolerance": 0.05}
    assert qe.grade([qcm, num], {"a": 1, "b": "7,9"}) == (2, {"a": True, "b": True})
    assert qe.grade([qcm, num], {"a": 0, "b": "8"}) == (0, {"a": False, "b": False})
    assert qe.grade([qcm, num], {}) == (0, {"a": False, "b": False})


def test_contenu_coherent():
    ids = [m["id"] for m in MODULES]
    assert len(ids) == len(set(ids))
    all_ids = [c["id"] for m in MODULES for c in m["chapitres"] + m["quiz"] + m["flashcards"]]
    all_ids += [q["id"] for q in QUESTIONS] + [b["id"] for b in BRAINTEASERS]
    assert len(all_ids) == len(set(all_ids)), "identifiants en double"
    for m in MODULES:
        assert len(m["quiz"]) >= 5 and m["chapitres"] and m["flashcards"]
        for q in m["quiz"]:
            assert q["type"] in ("qcm", "nombre") and q["explication"]
            if q["type"] == "qcm":
                assert 0 <= q["reponse"] < len(q["choix"])
            else:
                assert isinstance(q["reponse"], (int, float))
    assert len(all_flashcards(with_lexique=False)) == sum(len(m["flashcards"]) for m in MODULES)
    cards = all_flashcards()
    assert len({c["id"] for c in cards}) == len(cards), "flashcards en double (lexique compris)"


def test_progression_sauvegarde(tmp_path):
    path = tmp_path / "p.json"
    data = prog.load(path)
    prog.mark_chapter(data, "options", "opt-c1")
    prog.mark_chapter(data, "options", "opt-c1")
    prog.record_quiz(data, "options", 1, 2, {"q1": True, "q2": False})
    prog.record_quiz(data, "options", 1, 2, {"q2": True, "q3": False})
    prog.update_flashcard(data, "f1", True)
    prog.update_flashcard(data, "f1", True)
    prog.update_flashcard(data, "f2", False)
    prog.save(data, path)

    again = prog.load(path)
    assert again["chapitres_lus"] == {"options": ["opt-c1"]}
    assert prog.missed_questions(again, "options") == {"q3"}
    assert prog.question_stats(again, "options")["q2"] == (1, 2)
    assert prog.best_score(again, "options") == 0.5
    assert again["flashcards"] == {"f1": 3, "f2": 1}


def test_calcul_mental():
    for kind in calcul.TYPES:
        for enonce, reponse, tol in calcul.series(kind, 20, seed=1):
            assert enonce and reponse >= 0 and tol >= 0
    assert calcul.series("mix", 5, seed=3) == calcul.series("mix", 5, seed=3)


def test_export_import():
    data = prog.empty()
    prog.record_quiz(data, "options", 3, 4, {"a": True})
    again = prog.from_json(prog.to_json(data))
    assert again["quiz"][0]["score"] == 3
    partial = prog.from_json('{"quiz": []}')  # ancienne version ou fichier partiel : complété
    assert set(partial) == set(prog.EMPTY)
    with pytest.raises(ValueError):
        prog.from_json("[1, 2]")
