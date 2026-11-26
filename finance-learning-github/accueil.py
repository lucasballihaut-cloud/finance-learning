import streamlit as st

import progression as prog
from contenu import A_VENIR, MODULES

st.title("🎓 Finance Learning")
st.markdown("Apprendre la finance de marché et préparer les entretiens de **stage et d'alternance** "
            "(sales, trading, structuration, recherche quantitative, asset management).")

data = prog.load()

st.subheader("Comment réviser")
c1, c2, c3 = st.columns(3)
with c1.container(border=True):
    st.markdown("**1. Apprendre**")
    st.markdown("Lis un chapitre dans **📘 Cours**, joue avec les calculateurs, marque-le comme lu.")
    st.page_link("vues/1_Cours.py", label="Ouvrir les cours", icon="📘")
with c2.container(border=True):
    st.markdown("**2. Vérifier**")
    st.markdown("Passe le **✅ Quiz** du module, puis refais seulement tes erreurs jusqu'à 100 %.")
    st.page_link("vues/2_Quiz.py", label="Faire un quiz", icon="✅")
with c3.container(border=True):
    st.markdown("**3. Ancrer**")
    st.markdown("Chaque jour : 10 **🃏 flashcards**, une série de **⏱️ calcul mental** et une question d'entretien.")
    st.page_link("vues/3_Flashcards.py", label="Réviser les flashcards", icon="🃏")

st.subheader("Modules disponibles")
for m in MODULES:
    lus = len(data["chapitres_lus"].get(m["id"], []))
    best = prog.best_score(data, m["id"])
    with st.container(border=True):
        a, b = st.columns([3, 1])
        a.markdown(f"**{m['icone']} {m['titre']}**  \n{m['resume']}")
        a.progress(lus / len(m["chapitres"]), text=f"{lus} / {len(m['chapitres'])} chapitres lus")
        b.metric("Meilleur quiz", f"{best:.0%}" if best is not None else "—")
        c1, c2, _ = a.columns([1, 1, 2])
        if c1.button("📘 Ouvrir le cours", key=f"cours_{m['id']}"):
            st.session_state["module_id"] = m["id"]
            st.switch_page("vues/1_Cours.py")
        if c2.button("✅ Faire le quiz", key=f"quiz_{m['id']}"):
            st.session_state["module_id"] = m["id"]
            st.switch_page("vues/2_Quiz.py")

if A_VENIR:
    st.subheader("Bientôt")
for icone, titre, desc in A_VENIR:
    st.markdown(f"- {icone} **{titre}** — {desc}")

if prog.WEB:
    st.caption("Version en ligne : ta progression reste dans cet onglet. Pense à la télécharger dans 📈 Ma progression.")
else:
    st.caption("Toute ta progression est enregistrée localement dans `data/progression.json`.")
