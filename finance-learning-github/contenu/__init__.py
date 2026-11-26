"""Registre des modules de cours. Pour ajouter un module : créer un fichier ici et l'ajouter à MODULES."""
from contenu import actions, commodities, derives, macro, marches, options, risque, structures, taux

MODULES = [marches.MODULE, actions.MODULE, derives.MODULE, options.MODULE, taux.MODULE, risque.MODULE, macro.MODULE, structures.MODULE, commodities.MODULE]

# Modules prévus, affichés sur la page d'accueil (pas encore rédigés)
A_VENIR = []


def get_module(module_id):
    return next(m for m in MODULES if m["id"] == module_id)


def lexique_flashcards():
    """Les termes du lexique sous forme de flashcards (recto = terme, verso = définition)."""
    import re
    from contenu.lexique import LEXIQUE
    # Identifiant tiré du terme (et non de sa position) : ajouter un terme ne décale pas la progression
    return [{"id": "lex-" + re.sub(r"[^a-z0-9]+", "-", e["terme"].lower()).strip("-"),
             "recto": e["terme"], "verso": e["definition"], "module": "lexique"} for e in LEXIQUE]


def all_flashcards(with_lexique=True):
    """Toutes les flashcards, avec le module d'origine (et le lexique)."""
    cards = [dict(card, module=m["id"]) for m in MODULES for card in m["flashcards"]]
    return cards + (lexique_flashcards() if with_lexique else [])
