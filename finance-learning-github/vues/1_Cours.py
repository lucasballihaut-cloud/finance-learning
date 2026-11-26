import streamlit as st

import progression as prog
from ui import WIDGETS, module_picker

module = module_picker()
data = prog.load()
lus = data["chapitres_lus"].get(module["id"], [])
chapitres = module["chapitres"]

st.title(f"{module['icone']} {module['titre']}")
st.caption(module["resume"])
st.progress(len(lus) / len(chapitres), text=f"Chapitres lus : {len(lus)} / {len(chapitres)}")

# Index du chapitre affiché, mémorisé par module
key = f"chap_{module['id']}"
idx = st.session_state.get(key, 0)
labels = [("✅ " if c["id"] in lus else "⬜ ") + c["titre"] for c in chapitres]
idx = st.selectbox("Chapitre", range(len(chapitres)), index=idx, format_func=lambda i: labels[i])
st.session_state[key] = idx
chap = chapitres[idx]

st.header(chap["titre"])
st.markdown(chap["contenu"])

if chap.get("widget") in WIDGETS:
    with st.container(border=True):
        WIDGETS[chap["widget"]]()

st.info("**Points clés à retenir**\n\n" + "\n".join(f"- {p}" for p in chap["points_cles"]))

col1, col2, col3 = st.columns([2, 1, 1])
deja_lu = chap["id"] in lus
if col1.button("↩️ Marquer comme non lu" if deja_lu else "✅ J'ai lu et compris ce chapitre",
               type="secondary" if deja_lu else "primary"):
    prog.mark_chapter(data, module["id"], chap["id"], read=not deja_lu)
    prog.save(data)
    st.rerun()
if col2.button("⬅️ Précédent", disabled=idx == 0):
    st.session_state[key] = idx - 1
    st.rerun()
if col3.button("Suivant ➡️", disabled=idx == len(chapitres) - 1):
    st.session_state[key] = idx + 1
    st.rerun()

if idx == len(chapitres) - 1:
    st.success("Fin du module : teste-toi maintenant avec le quiz !")
    st.page_link("vues/2_Quiz.py", label="Passer le quiz de ce module", icon="✅")
