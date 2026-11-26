"""Point d'entrée de l'application Finance Learning : définit le menu de navigation.

Lancer avec :  streamlit run app.py
Chaque page vit dans son propre fichier (accueil.py et le dossier vues/).
"""
from pathlib import Path

import streamlit as st

# Chemins calculés à partir de ce fichier : l'app marche même lancée depuis un autre dossier
# (par exemple en ligne, quand le projet est dans un sous-dossier du dépôt GitHub).
ASSETS = Path(__file__).parent / "assets"

st.set_page_config(page_title="Finance Learning", page_icon=str(ASSETS / "logo_icon.svg"), layout="wide")
st.logo(str(ASSETS / "logo.svg"), icon_image=str(ASSETS / "logo_icon.svg"))

PAGES = {
    "": [st.Page("accueil.py", title="Accueil", icon="🏠", default=True)],
    "Apprendre": [
        st.Page("vues/1_Cours.py", title="Cours", icon="📘"),
        st.Page("vues/8_Lexique.py", title="Lexique", icon="📖"),
        st.Page("vues/3_Flashcards.py", title="Flashcards", icon="🃏"),
        st.Page("vues/2_Quiz.py", title="Quiz", icon="✅"),
    ],
    "Préparation entretien": [
        st.Page("vues/9_Culture_generale.py", title="Culture générale", icon="🌍"),
        st.Page("vues/4_Entretiens.py", title="Questions d'entretien", icon="🎤"),
        st.Page("vues/5_Brainteasers.py", title="Brainteasers", icon="🧠"),
        st.Page("vues/6_Calcul_mental.py", title="Calcul mental", icon="⏱️"),
    ],
    "Suivi": [st.Page("vues/7_Progression.py", title="Ma progression", icon="📈")],
}

st.navigation(PAGES).run()
