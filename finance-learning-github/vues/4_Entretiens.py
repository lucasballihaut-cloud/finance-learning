import random

import streamlit as st

import progression as prog
from contenu.entretiens import METIERS, QUESTIONS

NOTES = ["🔴 À retravailler", "🟠 Moyen", "🟢 Maîtrisé"]

st.title("🎤 Questions d'entretien")
st.caption("Entraîne-toi à répondre **à voix haute** avant d'ouvrir le corrigé, puis note-toi honnêtement. "
           "Les corrigés donnent une structure : adapte-les à ton parcours.")

data = prog.load()
with st.sidebar:
    metier = st.selectbox("Métier visé", METIERS)
    types = st.multiselect("Type", ["Technique", "Comportemental"], default=["Technique", "Comportemental"])
    seulement = st.checkbox("Masquer les questions maîtrisées")

selection = [q for q in QUESTIONS
             if (metier == "Tous" or metier in q["metiers"] or "Tous" in q["metiers"])
             and q["type"] in types
             and not (seulement and data["entretiens"].get(q["id"]) == 2)]

notes = [data["entretiens"].get(q["id"]) for q in selection]
c1, c2, c3 = st.columns(3)
c1.metric("Questions", len(selection))
c2.metric("Maîtrisées", sum(n == 2 for n in notes))
c3.metric("Pas encore notées", sum(n is None for n in notes))


def save_note(qid, key):
    value = st.session_state[key]
    if value is not None:
        data["entretiens"][qid] = NOTES.index(value)
        prog.save(data)


if selection and st.button("🎲 Simulation : une question au hasard"):
    st.session_state["ent_tirage"] = random.choice(selection)["id"]
tirage = st.session_state.get("ent_tirage")

for q in selection:
    note = data["entretiens"].get(q["id"])
    label = f"{NOTES[note][:1] if note is not None else '⚪'} [{q['type']}] {q['question']}"
    with st.expander(label, expanded=q["id"] == tirage):
        st.caption("Métiers : " + ", ".join(q["metiers"]))
        if st.toggle("Afficher le corrigé", key=f"show_{q['id']}"):
            st.markdown(q["corrige"])
        key = f"note_{q['id']}"
        st.radio("Comment t'en es-tu sorti ?", NOTES, index=note, horizontal=True, key=key,
                 on_change=save_note, args=(q["id"], key))
