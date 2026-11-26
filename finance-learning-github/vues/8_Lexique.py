import unicodedata

import streamlit as st

from contenu.lexique import CATEGORIES, LEXIQUE


def simplify(text):
    """Minuscules sans accents, pour une recherche tolérante (« equite » trouve « équité »)."""
    return "".join(c for c in unicodedata.normalize("NFD", text.lower()) if unicodedata.category(c) != "Mn")


st.title("📖 Lexique")
st.caption(f"{len(LEXIQUE)} termes expliqués simplement, avec un exemple. "
           "Les mêmes termes sont révisables dans 🃏 Flashcards (paquet « Lexique »).")

query = st.text_input("🔎 Rechercher un terme ou un mot de la définition", placeholder="ex. : ITM, down-and-in, skew, gamma…")
cats = st.pills("Catégories", CATEGORIES, selection_mode="multi", default=CATEGORIES)

q = simplify(query.strip())
results = [e for e in LEXIQUE if e["categorie"] in cats
           and (not q or q in simplify(e["terme"]) or q in simplify(e["definition"]))]
st.write(f"**{len(results)}** terme(s)")

for cat in CATEGORIES:
    entries = [e for e in results if e["categorie"] == cat]
    if not entries:
        continue
    st.subheader(cat)
    for e in entries:
        with st.expander(e["terme"], expanded=bool(q)):
            st.markdown(e["definition"])
            if e["exemple"]:
                st.info(f"**Exemple** : {e['exemple']}")
