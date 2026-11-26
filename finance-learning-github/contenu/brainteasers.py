"""Brainteasers de probabilités et de logique, avec solutions rédigées."""

BRAINTEASERS = [
    {"id": "bt-01", "titre": "Attendre le 6", "niveau": "Facile",
     "enonce": "On lance un dé équilibré jusqu'à obtenir un 6. Combien de lancers en moyenne ?",
     "indice": "Le nombre de lancers suit une loi géométrique.",
     "reponse": "6",
     "solution": r"""
Notons $E$ l'espérance. Au premier lancer, avec probabilité $\tfrac16$ on s'arrête, sinon on
recommence avec un lancer déjà consommé : $E = 1 + \tfrac56 E$, donc $E = 6$.
Plus généralement, l'espérance d'une loi géométrique de paramètre $p$ vaut $1/p$.
"""},
    {"id": "bt-02", "titre": "Au moins un 6", "niveau": "Facile",
     "enonce": "Quelle est la probabilité d'obtenir au moins un 6 en 4 lancers de dé ?",
     "indice": "Passer par l'événement contraire.",
     "reponse": "1 − (5/6)⁴ ≈ 51,8 %",
     "solution": r"""
$P(\text{aucun } 6) = (5/6)^4 = 625/1296$, donc $P(\text{au moins un}) = 671/1296 \approx 0{,}518$.
"""},
    {"id": "bt-03", "titre": "Relancer ou pas ?", "niveau": "Moyen",
     "enonce": "Vous lancez un dé et gagnez sa valeur en euros. Après le premier lancer, vous pouvez "
               "choisir de relancer une seule fois (vous gardez alors le second résultat). "
               "Quelle est la valeur du jeu avec la stratégie optimale ?",
     "indice": "Comparer chaque résultat à l'espérance d'un lancer, 3,5.",
     "reponse": "4,25 €",
     "solution": r"""
Un nouveau lancer vaut $3{,}5$ en espérance. On garde donc 4, 5 ou 6 et on relance 1, 2 ou 3.
Valeur $= \tfrac12 \cdot \tfrac{4+5+6}{3} + \tfrac12 \cdot 3{,}5 = 2{,}5 + 1{,}75 = 4{,}25$.
Avec deux relances possibles, on applique la même logique à rebours (seuil $4{,}25$ au premier lancer).
"""},
    {"id": "bt-04", "titre": "Maximum de deux dés", "niveau": "Moyen",
     "enonce": "On lance deux dés. Quelle est l'espérance du plus grand des deux résultats ?",
     "indice": "Calculer P(max ≤ k) puis P(max = k).",
     "reponse": "161/36 ≈ 4,47",
     "solution": r"""
$P(\max \le k) = (k/6)^2$, donc $P(\max = k) = \dfrac{k^2 - (k-1)^2}{36} = \dfrac{2k - 1}{36}$.
$\mathbb{E}[\max] = \sum_{k=1}^{6} k \cdot \dfrac{2k-1}{36} = \dfrac{1 + 6 + 15 + 28 + 45 + 66}{36} = \dfrac{161}{36}$.
"""},
    {"id": "bt-05", "titre": "Deux faces de suite", "niveau": "Moyen",
     "enonce": "On lance une pièce équilibrée jusqu'à obtenir deux « face » consécutifs. "
               "Combien de lancers en moyenne ?",
     "indice": "Définir des états : aucun face en cours / un face en cours.",
     "reponse": "6",
     "solution": r"""
Soit $E_0$ l'espérance depuis le départ et $E_1$ après un face.
$E_0 = 1 + \tfrac12 E_1 + \tfrac12 E_0$ et $E_1 = 1 + \tfrac12 \cdot 0 + \tfrac12 E_0$.
On obtient $E_0 = 2 + E_1$ et $E_1 = 1 + E_0/2$, donc $E_0 = 6$.
(Pour « face puis pile », la réponse est 4 : un échec ne fait pas tout recommencer.)
"""},
    {"id": "bt-06", "titre": "Les fourmis du triangle", "niveau": "Facile",
     "enonce": "Trois fourmis sont aux sommets d'un triangle. Chacune choisit au hasard une direction "
               "et longe un côté. Quelle est la probabilité qu'aucune ne croise une autre ?",
     "indice": "Il n'y a pas de collision seulement si toutes tournent dans le même sens.",
     "reponse": "1/4",
     "solution": r"""
$2^3 = 8$ choix équiprobables ; seuls « toutes dans le sens horaire » et « toutes dans le sens
antihoraire » évitent les collisions : $2/8 = 1/4$. Avec $n$ fourmis sur un polygone : $2/2^n$.
"""},
    {"id": "bt-07", "titre": "L'angle de l'horloge", "niveau": "Facile",
     "enonce": "Quel est l'angle entre les aiguilles d'une horloge à 3 h 15 ?",
     "indice": "L'aiguille des heures avance aussi pendant le quart d'heure.",
     "reponse": "7,5°",
     "solution": r"""
L'aiguille des minutes est sur le 3, soit $90°$. L'aiguille des heures avance de $0{,}5°$ par minute :
à 3 h 15 elle est à $90° + 15 \times 0{,}5° = 97{,}5°$. L'écart vaut $7{,}5°$.
"""},
    {"id": "bt-08", "titre": "Bâton cassé en trois", "niveau": "Difficile",
     "enonce": "On casse un bâton en deux points choisis uniformément et indépendamment. "
               "Quelle est la probabilité que les trois morceaux forment un triangle ?",
     "indice": "Il faut qu'aucun morceau ne dépasse la moitié du bâton.",
     "reponse": "1/4",
     "solution": r"""
Avec un bâton de longueur 1 et deux points $X, Y$ uniformes sur $[0,1]$, un triangle existe si
chaque morceau mesure moins de $\tfrac12$. Dans le carré $[0,1]^2$, la zone favorable est formée de
deux petits triangles d'aire $\tfrac18$ chacun : probabilité $\tfrac14$.
"""},
    {"id": "bt-09", "titre": "Somme égale à 7", "niveau": "Facile",
     "enonce": "On lance deux dés. Quelle est la probabilité que la somme fasse 7 ?",
     "indice": "Compter les couples possibles.",
     "reponse": "1/6",
     "solution": r"""
Six couples sur 36 : $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$, donc $6/36 = 1/6$. C'est la
somme la plus probable.
"""},
    {"id": "bt-10", "titre": "Les 25 chevaux", "niveau": "Difficile",
     "enonce": "25 chevaux, une piste où courent 5 chevaux à la fois, pas de chronomètre. "
               "Combien de courses au minimum pour trouver les 3 plus rapides ?",
     "indice": "Après 5 courses de groupes, faire courir les gagnants : beaucoup de chevaux sont éliminés.",
     "reponse": "7",
     "solution": r"""
5 courses (une par groupe), puis une 6e entre les 5 gagnants : son vainqueur est le plus rapide.
Candidats restants pour les places 2 et 3 : le 2e et le 3e de la 6e course, le 2e et le 3e du groupe
du vainqueur, et le 2e du groupe du deuxième de la 6e course. Soit 5 chevaux : une 7e course suffit.
"""},
    {"id": "bt-11", "titre": "Un pari à prix juste", "niveau": "Moyen",
     "enonce": "On lance une pièce : face, vous gagnez 10 € et le jeu s'arrête ; pile, le gain potentiel "
               "double et on relance. Le jeu s'arrête au plus tard au 3e lancer (si 3 piles, vous gagnez 0). "
               "Combien paieriez-vous au maximum pour jouer, si vous êtes neutre au risque ?",
     "indice": "Lister les scénarios : F, PF, PPF, PPP.",
     "reponse": "15 €",
     "solution": r"""
$\mathbb{E} = \tfrac12 \cdot 10 + \tfrac14 \cdot 20 + \tfrac18 \cdot 40 + \tfrac18 \cdot 0 = 5 + 5 + 5 = 15$ €.
Sans limite de lancers, l'espérance serait infinie (paradoxe de Saint-Pétersbourg) : on
paierait pourtant peu en pratique, ce qui illustre l'aversion au risque.
"""},
]
