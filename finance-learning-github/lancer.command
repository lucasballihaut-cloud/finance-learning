#!/bin/zsh
# Double-clic dans le Finder : installe (la première fois) puis lance Finance Learning.
# Laisse cette fenêtre ouverte pendant que tu révises ; ferme-la pour arrêter l'app.
cd "$(dirname "$0")"

if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 n'est pas installé : télécharge-le sur https://www.python.org/downloads/ puis relance ce fichier."
  read -k1 "?Appuie sur une touche pour fermer..."
  exit 1
fi

if [ ! -x .venv/bin/streamlit ]; then
  echo "Première ouverture : installation (1 à 2 minutes)..."
  rm -rf .venv
  python3 -m venv .venv && .venv/bin/pip install -q --upgrade pip && .venv/bin/pip install -q -r requirements.txt || {
    echo "L'installation a échoué. Copie le message ci-dessus et envoie-le."
    read -k1 "?Appuie sur une touche pour fermer..."
    exit 1
  }
fi

(sleep 4 && open http://localhost:8502) &
.venv/bin/streamlit run app.py --server.port 8502 --server.headless true
