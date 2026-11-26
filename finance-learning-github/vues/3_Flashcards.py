import random

import pandas as pd
import streamlit as st

import progression as prog
from contenu import MODULES, all_flashcards

st.title("🃏 Flashcards")
st.caption("Méthode de Leitner : une carte connue monte d'une boîte (1 → 5), une carte ratée retourne en boîte 1. "
           "Les cartes des petites boîtes reviennent beaucoup plus souvent.")

data = prog.load()
choices = ["Tous les modules", "📖 Lexique"] + [m["titre"] for m in MODULES]
filtre = st.sidebar.selectbox("Paquet", choices)
cards = all_flashcards()
if filtre == "📖 Lexique":
    cards = [c for c in cards if c["module"] == "lexique"]
elif filtre != "Tous les modules":
    module_id = next(m["id"] for m in MODULES if m["titre"] == filtre)
    cards = [c for c in cards if c["module"] == module_id]
by_id = {c["id"]: c for c in cards}


def draw_card(exclude=None):
    """Tirage pondéré : poids 16 en boîte 1, 8 en boîte 2… 1 en boîte 5."""
    pool = [c for c in cards if c["id"] != exclude] or cards
    weights = [2 ** (5 - data["flashcards"].get(c["id"], 1)) for c in pool]
    return random.choices(pool, weights=weights)[0]["id"]


state = st.session_state.setdefault("flash", {"id": None, "revealed": False})
if state["id"] not in by_id:
    state.update(id=draw_card(), revealed=False)
card = by_id[state["id"]]
box = data["flashcards"].get(card["id"], 1)

with st.container(border=True):
    st.caption(f"Boîte {box} / 5 · module {card['module']}")
    st.markdown(f"### {card['recto']}")
    if state["revealed"]:
        st.divider()
        st.markdown(f"#### {card['verso']}")

if not state["revealed"]:
    if st.button("🔄 Retourner la carte", type="primary"):
        state["revealed"] = True
        st.rerun()
else:
    c1, c2 = st.columns(2)
    if c1.button("✅ Je savais", type="primary", width="stretch"):
        prog.update_flashcard(data, card["id"], known=True)
        prog.save(data)
        state.update(id=draw_card(card["id"]), revealed=False)
        st.rerun()
    if c2.button("❌ À revoir", width="stretch"):
        prog.update_flashcard(data, card["id"], known=False)
        prog.save(data)
        state.update(id=draw_card(card["id"]), revealed=False)
        st.rerun()

st.subheader("Répartition du paquet")
counts = pd.Series([data["flashcards"].get(c["id"], 1) for c in cards]).value_counts()
dist = pd.DataFrame({"Cartes": [int(counts.get(b, 0)) for b in range(1, 6)]},
                    index=[f"Boîte {b}" for b in range(1, 6)])
st.bar_chart(dist)
