# Finance Learning

Application Streamlit pour apprendre la finance de marché et réviser les entretiens
(sales, trading, structuration, recherche quantitative, asset management).

## Installation (première fois, après avoir dézippé le dossier)

Python 3.11 ou plus récent est nécessaire. Dans le **terminal** :

```bash
cd finance-learning
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

(Sous Windows : `.venv\Scripts\activate` au lieu de `source .venv/bin/activate`.)

## Lancer l'application

Dans le **terminal** (à taper ligne par ligne) :

```bash
cd ~/Projets/finance-learning
source .venv/bin/activate
streamlit run app.py
```

Le `(.venv)` doit apparaître au début de la ligne du terminal après la 2e commande.
Pour arrêter l'application : `Ctrl + C` dans le terminal.

## Lancer les tests

Dans le **terminal**, `.venv` activé :

```bash
python -m pytest -q
```

Les tests vérifient les formules (Black-Scholes, grecques, obligations), les réponses
numériques des quiz, la correction et la sauvegarde de la progression.

## Organisation

| Fichier / dossier | Rôle |
|---|---|
| `app.py` | Menu de navigation (`st.navigation`) |
| `accueil.py` | Page d'accueil |
| `vues/` | Une page par fichier : cours, quiz, flashcards, entretiens, brainteasers, calcul mental, progression |
| `contenu/` | Tout le contenu pédagogique (un fichier par module, plus `entretiens.py` et `brainteasers.py`) |
| `formules.py` | Black-Scholes, grecques, arbre binomial, obligations |
| `quiz_engine.py` | Correction des réponses |
| `progression.py` | Sauvegarde dans `data/progression.json` |
| `calcul.py` | Générateur d'exercices de calcul mental |
| `ui.py` | Éléments d'interface partagés (sélecteur de module, calculateurs) |
| `tests/` | Tests automatiques (pytest) |

## Ajouter un module

1. Copier `contenu/taux.py` en `contenu/mon_module.py` et changer `id`, titres, chapitres, quiz, flashcards
   (tous les `id` doivent être uniques).
2. Dans `contenu/__init__.py`, l'importer et l'ajouter à la liste `MODULES`.
3. Relancer les tests : `python -m pytest -q`.

## Attention

- Ne déplace pas le dossier : cela casse le `.venv`. Si c'est fait, recrée-le :
  `rm -rf .venv && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.
- La progression est dans `data/progression.json` : copie ce fichier pour la sauvegarder.

## Version en ligne (Streamlit Community Cloud)

L'application détecte automatiquement qu'elle tourne en ligne : chaque visiteur a alors sa propre
progression, gardée tant que son onglet reste ouvert. Il peut la télécharger puis la réimporter
(page « Ma progression »). Pour tester ce mode sur son ordinateur : `FINANCE_LEARNING_WEB=1 streamlit run app.py`.
