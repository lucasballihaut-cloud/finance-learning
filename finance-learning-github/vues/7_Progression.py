import pandas as pd
import streamlit as st

import progression as prog
from contenu import MODULES, all_flashcards
from contenu.brainteasers import BRAINTEASERS
from contenu.entretiens import QUESTIONS

st.title("📈 Ma progression")
if prog.WEB:
    st.info("Version en ligne : ta progression est gardée tant que cet onglet reste ouvert. "
            "**Télécharge-la** en bas de page pour la retrouver la prochaine fois (puis réimporte-la).")
else:
    st.caption("Sauvegardée automatiquement dans `data/progression.json`.")

data = prog.load()

# ---------- Vue d'ensemble ----------
n_chap = sum(len(m["chapitres"]) for m in MODULES)
n_lus = sum(len(data["chapitres_lus"].get(m["id"], [])) for m in MODULES)
cards = all_flashcards()
maitrisees = sum(data["flashcards"].get(c["id"], 1) >= 4 for c in cards)
c1, c2, c3, c4 = st.columns(4)
c1.metric("Chapitres lus", f"{n_lus} / {n_chap}")
c2.metric("Quiz passés", len(data["quiz"]))
c3.metric("Flashcards en boîte 4-5", f"{maitrisees} / {len(cards)}")
c4.metric("Questions d'entretien maîtrisées",
          f"{sum(v == 2 for v in data['entretiens'].values())} / {len(QUESTIONS)}")

# ---------- Par module ----------
st.subheader("Par module")
rows = []
for m in MODULES:
    attempts = [a for a in data["quiz"] if a["module"] == m["id"]]
    stats = prog.question_stats(data, m["id"])
    best = prog.best_score(data, m["id"])
    rows.append({
        "Module": f"{m['icone']} {m['titre']}",
        "Chapitres lus": f"{len(data['chapitres_lus'].get(m['id'], []))} / {len(m['chapitres'])}",
        "Quiz passés": len(attempts),
        "Meilleur score": f"{best:.0%}" if best is not None else "—",
        "Dernier score": f"{attempts[-1]['score'] / attempts[-1]['total']:.0%}" if attempts else "—",
        "Questions vues": f"{len(stats)} / {len(m['quiz'])}",
        "À revoir": len(prog.missed_questions(data, m["id"])),
    })
st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch")

if data["quiz"]:
    st.subheader("Évolution des scores de quiz")
    hist = pd.DataFrame([{"Tentative": i + 1, "Module": a["module"], "Score (%)": 100 * a["score"] / a["total"]}
                         for i, a in enumerate(data["quiz"])])
    st.line_chart(hist.pivot_table(index="Tentative", columns="Module", values="Score (%)"))

    st.subheader("Questions les plus ratées")
    worst = []
    for m in MODULES:
        qs = {q["id"]: q for q in m["quiz"]}
        for qid, (good, n) in prog.question_stats(data, m["id"]).items():
            if qid in qs and good < n:
                worst.append({"Module": m["titre"], "Question": qs[qid]["question"],
                              "Réussite": f"{good} / {n}", "_taux": good / n})
    if worst:
        df = pd.DataFrame(worst).sort_values("_taux").drop(columns="_taux").head(10)
        st.dataframe(df, hide_index=True, width="stretch")
    else:
        st.success("Aucune question ratée pour l'instant 👏")

# ---------- Autres activités ----------
col1, col2 = st.columns(2)
with col1:
    st.subheader("Flashcards")
    boxes = pd.Series([data["flashcards"].get(c["id"], 1) for c in cards]).value_counts()
    st.bar_chart(pd.DataFrame({"Cartes": [int(boxes.get(b, 0)) for b in range(1, 6)]},
                              index=[f"Boîte {b}" for b in range(1, 6)]))
with col2:
    st.subheader("Brainteasers et calcul mental")
    st.metric("Brainteasers résolus", f"{sum(bool(v) for v in data['brainteasers'].values())} / {len(BRAINTEASERS)}")
    if data["calcul"]:
        last = data["calcul"][-1]
        st.metric("Dernière série de calcul", f"{last['score']} / {last['total']}",
                  help=f"{last['secondes'] / last['total']:.1f} s par calcul")

# ---------- Sauvegarder / restaurer ----------
st.subheader("Sauvegarder ou restaurer ma progression")
c1, c2 = st.columns(2)
c1.download_button("⬇️ Télécharger ma progression", prog.to_json(data), file_name="progression-finance-learning.json",
                   mime="application/json", type="primary")
fichier = c2.file_uploader("⬆️ Importer une progression (fichier .json)", type="json")
if fichier is not None and st.session_state.get("import_fait") != fichier.file_id:
    try:
        prog.save(prog.from_json(fichier.getvalue().decode("utf-8")))
        st.session_state["import_fait"] = fichier.file_id
        st.success("Progression importée.")
        st.rerun()
    except (ValueError, UnicodeDecodeError) as err:
        st.error(f"Ce fichier n'est pas une progression valide ({err}).")

# ---------- Réinitialiser ----------
with st.expander("⚠️ Remettre ma progression à zéro"):
    st.write("Efface tous les scores, chapitres lus, flashcards et notes. Action irréversible.")
    if st.checkbox("Je confirme vouloir tout effacer"):
        if st.button("Tout effacer", type="primary"):
            prog.save(prog.empty())
            st.session_state.clear()
            st.rerun()
