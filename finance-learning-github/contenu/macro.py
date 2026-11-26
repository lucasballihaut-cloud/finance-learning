"""Module : Macro-économie et banques centrales."""

MODULE = {
    "id": "macro",
    "titre": "Macro-économie et banques centrales",
    "icone": "🌐",
    "statut": "complet",
    "resume": "Indicateurs clés, inflation et taux réels, politique monétaire, règle de Taylor, "
              "transmission aux marchés et au change.",
    "chapitres": [
        {
            "id": "mac-c1",
            "titre": "1. Les indicateurs à connaître",
            "contenu": r"""
En entretien, on attend surtout que tu saches **ce que mesure** chaque indicateur et **comment le
marché réagit** à une surprise (l'écart entre le chiffre publié et le consensus des économistes).

| Indicateur | Ce qu'il mesure | Lecture |
|---|---|---|
| **PIB** | Production de l'économie sur un trimestre | Croissance réelle (hors inflation) ou nominale |
| **Inflation (IPC / HICP)** | Évolution des prix à la consommation sur un an | L'inflation **sous-jacente** (*core*) exclut énergie et alimentation, plus volatiles |
| **Taux de chômage** | Part de la population active sans emploi | Indicateur de tension sur le marché du travail |
| **Emplois non agricoles (NFP, États-Unis)** | Créations d'emplois du mois | Publication mensuelle très suivie |
| **PMI** | Enquête auprès des directeurs d'achat | Au-dessus de 50 : expansion ; en dessous : contraction |
| **Salaires** | Croissance des rémunérations | Risque de boucle prix-salaires |

**Nominal et réel.** Une grandeur **nominale** est mesurée en euros courants, une grandeur **réelle**
est corrigée de l'inflation. Approximativement :

$$
\text{croissance nominale} \approx \text{croissance réelle} + \text{inflation}
$$

**Équation de Fisher** : le taux d'intérêt nominal $i$, le taux réel $r$ et l'inflation anticipée
$\pi$ sont liés par

$$
(1 + i) = (1 + r)(1 + \pi) \qquad \Rightarrow \qquad i \approx r + \pi
$$

Un taux nominal de $4\,\%$ avec une inflation de $3\,\%$ ne rapporte qu'environ $1\,\%$ de pouvoir d'achat.
""",
            "points_cles": [
                "Le marché réagit à la surprise, pas au chiffre lui-même.",
                "PMI > 50 : expansion.",
                "Fisher : i ≈ r + π.",
            ],
        },
        {
            "id": "mac-c2",
            "titre": "2. Les banques centrales",
            "contenu": r"""
**Mandats.**
- **BCE** : mandat principal de **stabilité des prix**, avec une cible d'inflation de $2\,\%$ à moyen terme.
- **Fed** : **double mandat**, plein emploi et stabilité des prix (cible de $2\,\%$ également).

**Outils.**
1. **Taux directeurs.** Dans la zone euro : taux de la facilité de dépôt, taux des opérations
   principales de refinancement et taux de la facilité de prêt marginal. Aux États-Unis : la fourchette
   cible des *Fed funds*. Ils pilotent les taux à très court terme (€STR, SOFR).
2. **Bilan.** Le *quantitative easing* (QE) consiste à acheter massivement des titres (dettes d'État
   notamment) pour faire baisser les taux longs ; le *quantitative tightening* (QT) est l'inverse.
3. **Communication** (*forward guidance*) : annoncer la trajectoire probable des taux pour agir dès
   maintenant sur les anticipations, donc sur les taux longs.

**Faucon ou colombe.** Un discours *hawkish* (faucon) privilégie la lutte contre l'inflation (taux plus
hauts) ; un discours *dovish* (colombe) privilégie le soutien à l'activité.

**Règle de Taylor.** Repère simple du taux directeur « approprié » :

$$
i = r^* + \pi + 0{,}5\,(\pi - \pi^*) + 0{,}5\,(y - y^*)
$$

avec $r^*$ le taux réel neutre, $\pi^*$ la cible d'inflation et $y - y^*$ l'écart de production (en %).
Quand l'inflation dépasse la cible de 1 point, le taux nominal monte de 1,5 point : le taux **réel**
augmente, ce qui freine l'économie (principe de Taylor). Ce n'est pas une règle appliquée
mécaniquement, mais un point de comparaison.
""",
            "points_cles": [
                "BCE : stabilité des prix (2 %). Fed : emploi + prix.",
                "QE : achats de titres ⇒ taux longs plus bas.",
                "Taylor : i = r* + π + 0,5(π − π*) + 0,5(écart de production).",
            ],
        },
        {
            "id": "mac-c3",
            "titre": "3. Transmission aux marchés",
            "contenu": r"""
Raisonne toujours par **mécanisme** : qu'est-ce qui change dans les anticipations de taux, de
croissance et d'aversion au risque ?

**Hausse de taux plus forte qu'attendu (surprise *hawkish*)** — effets typiques :
- **taux courts** en hausse (ils suivent les anticipations de politique monétaire) ;
- **courbe** qui s'aplatit souvent : les taux longs montent moins, car le marché anticipe une
  inflation et une croissance plus faibles à terme ;
- **devise** qui s'apprécie (rendement plus attractif) ;
- **actions** en baisse : flux futurs actualisés à un taux plus élevé, croissance attendue plus faible ;
  les valeurs de croissance (flux lointains) sont les plus touchées ;
- **spreads de crédit** qui s'écartent (refinancement plus cher pour les entreprises).

Ces réactions sont des tendances, pas des lois : tout dépend de ce qui était déjà anticipé.

**Inflation anticipée par le marché.** Les obligations indexées sur l'inflation donnent un rendement
**réel**. L'écart avec l'obligation nominale de même maturité est le **point mort d'inflation**
(*breakeven*) :

$$
\text{breakeven} \approx y_{nominal} - y_{réel}
$$

C'est l'inflation moyenne qui rendrait les deux placements équivalents (elle contient aussi des primes
de risque et de liquidité).

**Courbe et cycle.** Courbe très pentue : souvent sortie de récession, taux directeurs bas.
Courbe inversée : marché qui anticipe des baisses de taux, historiquement souvent avant un ralentissement.

**Risk-on / risk-off.** En période de stress, les capitaux fuient vers les **valeurs refuges**
(emprunts d'État les mieux notés, or, certaines devises comme le franc suisse ou le yen), tandis que les
actions et le crédit baissent et que la volatilité implicite monte.
""",
            "points_cles": [
                "Surprise hawkish : taux courts ↑, devise ↑, actions ↓, spreads ↑.",
                "Breakeven ≈ rendement nominal − rendement réel.",
                "Risk-off : fuite vers les valeurs refuges, vol ↑.",
            ],
        },
        {
            "id": "mac-c4",
            "titre": "4. Change et macro",
            "contenu": r"""
**Différentiel de taux.** À court terme, la devise d'un pays dont les taux montent relativement aux
autres tend à s'apprécier : les capitaux cherchent le meilleur rendement.

**Parité des taux couverte** (vue dans le module Marchés) : le prix à terme compense exactement le
différentiel de taux, sinon il y aurait un arbitrage :
$F = S\, e^{(r_{dom} - r_{etr})T}$.

**Carry trade.** Emprunter dans une devise à taux bas pour placer dans une devise à taux élevé,
**sans** couvrir le change. On gagne le différentiel de taux tant que la devise à taux élevé ne se
déprécie pas trop. La stratégie gagne souvent un peu et perd parfois beaucoup lors des épisodes de
*risk-off*, quand les positions sont débouclées brutalement.

**Parité de pouvoir d'achat (PPA).** À long terme, le change tendrait à égaliser le prix d'un même
panier de biens entre pays. Version relative : la devise d'un pays à forte inflation se déprécie
d'environ l'écart d'inflation. Elle explique mal le court terme mais sert de repère de valorisation.

**Balance courante.** Un pays en déficit courant important dépend des capitaux étrangers pour se
financer : sa devise est plus fragile quand l'appétit pour le risque recule.

**Méthode d'entretien** pour toute question « que se passe-t-il si… » :
1. identifier le **choc** (surprise de croissance, d'inflation, de politique monétaire, de risque) ;
2. en déduire l'effet sur les **anticipations de taux directeurs** ;
3. dérouler sur taux courts, taux longs, devise, actions, crédit, volatilité ;
4. dire ce qui pourrait **contredire** ce scénario.
""",
            "points_cles": [
                "Taux relatifs ↑ ⇒ devise ↑ (à court terme).",
                "Carry : gagne le différentiel, risque de krach de change.",
                "Méthode : choc → banque centrale → classes d'actifs.",
            ],
        },
        {
            "id": "mac-c5",
            "titre": "5. Le calendrier économique : réagir aux publications",
            "contenu": r"""
### Surprise = publié − consensus

Avant chaque statistique, les économistes publient une prévision moyenne : le **consensus**. Le marché
a déjà intégré ce consensus dans les prix ; il ne réagit qu'à la **surprise** :

$$
\text{surprise} = \text{chiffre publié} - \text{consensus}
$$

Exemple : inflation publiée à $3{,}4\,\%$ pour un consensus de $3{,}1\,\%$ : surprise de $+0{,}3$ point.
Les révisions des mois précédents et le détail (inflation sous-jacente, salaires) comptent aussi.

### Les rendez-vous à connaître

| Publication | Fréquence | Pourquoi le marché la suit |
|---|---|---|
| Inflation (CPI américain, HICP de la zone euro) | Mensuelle | Guide directement les banques centrales |
| Emploi américain (NFP, chômage, salaires) | Mensuelle, en général le 1er vendredi | Mandat d'emploi de la Fed |
| PMI | Mensuelle, en début de mois | Premier indicateur de l'activité |
| PIB | Trimestrielle | Confirme (avec retard) la tendance |
| Réunions de la BCE et de la Fed (FOMC) | Environ toutes les 6 semaines (8 par an) | Décision de taux, communication, projections |

### Scénarios de réaction

| Surprise | Taux 2 ans | Courbe | Devise | Actions | Volatilité |
|---|---|---|---|---|---|
| Inflation **au-dessus** du consensus | ↑ | souvent plus plate | ↑ | ↓ (surtout croissance) | ↑ |
| Inflation **en dessous** | ↓ | souvent plus pentue | ↓ | ↑ | ↓ |
| Emploi très fort (en période d'inflation élevée) | ↑ | plus plate | ↑ | ambigu | — |
| PMI faible (crainte de récession) | ↓ | plus pentue ou plus plate selon les anticipations | ↓ | ↓ (cycliques) | ↑ |
| Banque centrale plus *hawkish* que prévu | ↑ | plus plate | ↑ | ↓ | ↑ |

### Le régime compte

La même nouvelle peut faire monter ou baisser les actions selon le contexte. En période d'inflation
élevée, une mauvaise nouvelle sur l'activité peut faire **monter** les actions (*bad news is good
news*) : le marché anticipe des baisses de taux. En période de crainte de récession, elle les fait
baisser. En entretien, précise toujours **quel est le sujet dominant** pour le marché du moment.
""",
            "points_cles": [
                "Le marché réagit à la surprise : publié − consensus.",
                "Inflation au-dessus du consensus : taux courts ↑, devise ↑, actions ↓.",
                "Bad news is good news quand le marché attend des baisses de taux.",
            ],
        },
        {
            "id": "mac-c6",
            "titre": "6. Le cycle économique et l'allocation d'actifs",
            "contenu": r"""
### Les phases du cycle

| Phase | Croissance | Inflation | Banque centrale | Actifs qui ont tendance à surperformer |
|---|---|---|---|---|
| **Reprise** | Repart depuis un point bas | Basse | Accommodante | Actions cycliques, crédit high yield, petites capitalisations |
| **Expansion** | Solide | En hausse | Commence à resserrer | Actions, matières premières |
| **Ralentissement** | Ralentit | Élevée | Restrictive | Valeurs défensives, liquidités, obligations courtes |
| **Récession** | Négative | En baisse | Baisse ses taux | Emprunts d'État longs, or, valeurs défensives |

Ce sont des **tendances moyennes**, pas des règles : chaque cycle a ses particularités.

### Quelques relations utiles

- **Écart de production** (*output gap*) : écart entre le PIB effectif et le PIB potentiel. Positif :
  économie en surchauffe, pressions inflationnistes.
- **Courbe de Phillips** : relation (instable) entre chômage bas et inflation plus élevée ; un marché du
  travail tendu pousse les salaires et donc les prix.
- **Loi d'Okun** : ordre de grandeur selon lequel une croissance inférieure à son potentiel fait monter
  le chômage (le coefficient varie selon les pays et les périodes).
- **Stagflation** : inflation élevée **et** croissance faible (années 1970). Cas difficile pour les
  banques centrales et pour les portefeuilles mixtes, car actions et obligations peuvent baisser ensemble.

### Corrélation actions-obligations

Dans un régime d'inflation basse, actions et obligations d'État sont souvent **négativement**
corrélées : les obligations protègent un portefeuille lors des baisses d'actions. Quand l'inflation
est le risque principal, la corrélation peut devenir **positive** : les deux baissent ensemble quand
les taux montent. C'est ce qui a rendu l'année 2022 si difficile pour les portefeuilles 60/40.
""",
            "points_cles": [
                "Reprise → expansion → ralentissement → récession.",
                "Récession : emprunts d'État longs et or ont tendance à surperformer.",
                "Stagflation : inflation élevée + croissance faible.",
                "Corrélation actions/obligations positive quand l'inflation domine.",
            ],
        },
        {
            "id": "mac-c7",
            "titre": "7. Politique budgétaire, dette publique et marchés",
            "contenu": r"""
### Déficit et dette

- **Solde budgétaire** : recettes moins dépenses de l'État. Le **solde primaire** exclut les intérêts
  de la dette.
- **Dette publique** en % du PIB : ce qui compte est sa **dynamique**.

En notant $d$ la dette en % du PIB, $r$ le taux d'intérêt apparent de la dette, $g$ la croissance
nominale et $pb$ le solde primaire en % du PIB :

$$
\Delta d \approx (r - g)\, d - pb
$$

Si $r < g$, la dette peut se stabiliser même avec un petit déficit primaire ; si $r > g$, il faut un
excédent primaire pour la stabiliser.

Exemple : $d = 110\,\%$, $r = 3\,\%$, $g = 3{,}5\,\%$, déficit primaire de $2\,\%$ ($pb = -2\,\%$) :
$\Delta d \approx (-0{,}5\,\%) \times 1{,}1 + 2\,\% = 1{,}45$ point de PIB par an : la dette continue
d'augmenter.

### Effets sur les marchés

- Plus de déficit = plus d'émissions de titres d'État : pression à la hausse sur les **taux longs** et la
  **prime de terme**.
- **Spread souverain** : en zone euro, l'écart entre le rendement d'un pays et celui de l'Allemagne
  (par exemple OAT-Bund à 10 ans) mesure le risque perçu de ce pays (finances publiques, politique).
  Un écartement signale une inquiétude ; la BCE dispose d'instruments pour éviter une fragmentation
  désordonnée.
- **Dégradation de la note** d'un État : spread en hausse, parfois ventes forcées si la note passe
  sous un seuil.
- **Multiplicateur budgétaire** : effet d'un euro de dépense publique sur le PIB ; plus élevé en
  récession et quand la politique monétaire est contrainte.

### Politique monétaire et budgétaire ensemble

| Combinaison | Effet typique |
|---|---|
| Relance budgétaire + banque centrale restrictive | Taux en hausse, devise souvent plus forte |
| Austérité + banque centrale accommodante | Taux bas, devise plus faible |
| Relance budgétaire + banque centrale accommodante | Croissance et inflation soutenues, risque de surchauffe |

En entretien, sur une question d'actualité budgétaire, déroule : **déficit → émissions → taux longs et
spread → devise → actions** (banques, secteurs exposés), puis ce que pourrait faire la banque centrale.
""",
            "points_cles": [
                "Δd ≈ (r − g)·d − solde primaire.",
                "Spread OAT-Bund : prime de risque de la France face à l'Allemagne.",
                "Plus de déficit ⇒ plus d'émissions ⇒ taux longs ↑.",
            ],
        },
    ],
    "quiz": [
        {"id": "mac-q01", "type": "nombre",
         "question": r"Taux nominal $5\,\%$, inflation anticipée $3\,\%$. Taux réel approximatif en % ?",
         "reponse": 2, "tolerance": 0.07,
         "explication": r"$i \approx r + \pi$ donne $2\,\%$ (exactement $1{,}05/1{,}03 - 1 \approx 1{,}94\,\%$)."},
        {"id": "mac-q02", "type": "nombre",
         "question": r"Règle de Taylor : $r^* = 1\,\%$, inflation $4\,\%$, cible $2\,\%$, écart de production nul. "
                     r"Taux directeur suggéré en % ?",
         "reponse": 6, "tolerance": 0.001,
         "explication": r"$1 + 4 + 0{,}5 \times 2 + 0 = 6\,\%$."},
        {"id": "mac-q03", "type": "nombre",
         "question": r"Obligation d'État nominale 10 ans à $3{,}0\,\%$, indexée inflation 10 ans à $0{,}8\,\%$ (réel). "
                     r"Point mort d'inflation en % ?",
         "reponse": 2.2, "tolerance": 0.001,
         "explication": r"$3{,}0 - 0{,}8 = 2{,}2\,\%$ d'inflation moyenne anticipée (primes comprises)."},
        {"id": "mac-q04", "type": "nombre",
         "question": r"Croissance réelle $2\,\%$, inflation $3\,\%$. Croissance nominale approximative en % ?",
         "reponse": 5, "tolerance": 0.1,
         "explication": r"$\approx 2 + 3 = 5\,\%$ (exactement $1{,}02 \times 1{,}03 - 1 = 5{,}06\,\%$)."},
        {"id": "mac-q05", "type": "qcm",
         "question": "Un PMI manufacturier publié à 47 indique…",
         "choix": ["une expansion de l'activité", "une contraction de l'activité",
                   "une inflation de 4,7 %", "un chômage en baisse"],
         "reponse": 1,
         "explication": "Le seuil est 50 : en dessous, davantage d'entreprises voient leur activité reculer."},
        {"id": "mac-q06", "type": "qcm",
         "question": "La BCE monte ses taux plus qu'attendu. Réaction la plus probable de l'euro ?",
         "choix": ["Il se déprécie", "Il s'apprécie", "Aucun effet", "Il ne bouge que contre l'or"],
         "reponse": 1,
         "explication": "Rendements en euros plus attractifs : afflux de capitaux et appréciation."},
        {"id": "mac-q07", "type": "qcm",
         "question": "Quel est l'effet recherché du quantitative easing ?",
         "choix": ["Faire monter les taux longs", "Faire baisser les taux longs et assouplir les conditions financières",
                   "Réduire la taille du bilan de la banque centrale", "Augmenter les réserves de change"],
         "reponse": 1,
         "explication": "En achetant des titres, la banque centrale fait monter leurs prix, donc baisser leurs rendements."},
        {"id": "mac-q08", "type": "qcm",
         "question": "Quel est le mandat de la Fed ?",
         "choix": ["Stabilité des prix uniquement", "Plein emploi et stabilité des prix",
                   "Stabilité du dollar", "Équilibre budgétaire"],
         "reponse": 1,
         "explication": "C'est le double mandat, alors que la BCE a un mandat principal de stabilité des prix."},
        {"id": "mac-q09", "type": "qcm",
         "question": "Dans un épisode de risk-off, lequel de ces actifs a tendance à monter ?",
         "choix": ["Les actions des pays émergents", "Les obligations high yield",
                   "Les emprunts d'État les mieux notés", "Les devises à taux élevé (carry)"],
         "reponse": 2,
         "explication": "Fuite vers la qualité : les titres d'État les plus sûrs sont recherchés, leurs rendements baissent."},
        {"id": "mac-q10", "type": "qcm",
         "question": "Un carry trade consiste à…",
         "choix": ["emprunter dans une devise à taux élevé pour placer dans une devise à taux bas",
                   "emprunter dans une devise à taux bas pour placer dans une devise à taux élevé, sans couvrir le change",
                   "acheter des futures sur matières premières",
                   "acheter une obligation et la financer en repo au même taux"],
         "reponse": 1,
         "explication": "On encaisse le différentiel de taux en prenant le risque de change."},
        {"id": "mac-q11", "type": "nombre",
         "question": r"Inflation publiée à $3{,}4\,\%$, consensus à $3{,}1\,\%$. Surprise en points ?",
         "reponse": 0.3, "tolerance": 0.001,
         "explication": "3,4 − 3,1 = +0,3 point : surprise à la hausse."},
        {"id": "mac-q12", "type": "qcm",
         "question": "L'inflation américaine sort nettement au-dessus du consensus. Réaction la plus probable du taux 2 ans américain ?",
         "choix": ["Il baisse", "Il monte", "Il ne bouge pas", "Seul le taux 30 ans réagit"],
         "reponse": 1,
         "explication": "Le marché anticipe une Fed plus restrictive : les taux courts montent."},
        {"id": "mac-q13", "type": "qcm",
         "question": "Qu'est-ce que la stagflation ?",
         "choix": ["Croissance forte et inflation basse", "Inflation élevée et croissance faible",
                   "Déflation et chômage bas", "Taux négatifs et croissance forte"],
         "reponse": 1,
         "explication": "Situation des années 1970 : difficile à traiter pour la banque centrale."},
        {"id": "mac-q14", "type": "qcm",
         "question": "En récession, quel actif a historiquement tendance à surperformer ?",
         "choix": ["Les actions cycliques", "Les emprunts d'État longs", "Le crédit high yield", "Les matières premières industrielles"],
         "reponse": 1,
         "explication": "Les banques centrales baissent leurs taux et les investisseurs cherchent la sécurité : les taux longs baissent."},
        {"id": "mac-q15", "type": "qcm",
         "question": "Que signifie « bad news is good news » ?",
         "choix": ["Les actions montent toujours après une mauvaise nouvelle",
                   "Une mauvaise nouvelle économique fait monter les actions car elle rapproche des baisses de taux",
                   "Les obligations baissent après une bonne nouvelle", "Les marchés ignorent les statistiques"],
         "reponse": 1,
         "explication": "Ce régime apparaît quand l'inflation et les taux sont la préoccupation principale du marché."},
        {"id": "mac-q16", "type": "nombre",
         "question": r"Dette $110\,\%$ du PIB, $r = 3\,\%$, croissance nominale $3{,}5\,\%$, déficit primaire $2\,\%$ du PIB. "
                     r"Variation annuelle de la dette en points de PIB (2 décimales) ?",
         "reponse": 1.45, "tolerance": 0.05,
         "explication": r"$(0{,}03 - 0{,}035) \times 110 + 2 = -0{,}55 + 2 = 1{,}45$ point."},
        {"id": "mac-q17", "type": "qcm",
         "question": "Le spread OAT-Bund 10 ans s'écarte fortement. Que signale-t-il ?",
         "choix": ["Que l'Allemagne devient plus risquée que la France", "Une hausse de la prime de risque exigée sur la dette française",
                   "Une baisse de l'inflation en France", "Une appréciation de l'euro"],
         "reponse": 1,
         "explication": "Les investisseurs exigent plus de rendement pour détenir de la dette française que de la dette allemande."},
        {"id": "mac-q18", "type": "qcm",
         "question": "Pourquoi 2022 a-t-elle été difficile pour les portefeuilles 60 % actions / 40 % obligations ?",
         "choix": ["Les actions ont monté mais pas les obligations", "La hausse des taux face à l'inflation a fait baisser actions et obligations ensemble",
                   "Les obligations ont fait défaut", "Les dividendes ont été supprimés"],
         "reponse": 1,
         "explication": "Quand l'inflation domine, la corrélation actions/obligations devient positive : la diversification ne protège plus."},
    ],
    "flashcards": [
        {"id": "mac-f01", "recto": "Équation de Fisher",
         "verso": r"$(1 + i) = (1 + r)(1 + \pi)$, soit $i \approx r + \pi$"},
        {"id": "mac-f02", "recto": "Règle de Taylor",
         "verso": r"$i = r^* + \pi + 0{,}5(\pi - \pi^*) + 0{,}5(y - y^*)$"},
        {"id": "mac-f03", "recto": "Seuil du PMI", "verso": "50 : au-dessus expansion, en dessous contraction."},
        {"id": "mac-f04", "recto": "Mandats BCE et Fed",
         "verso": "BCE : stabilité des prix (2 % à moyen terme). Fed : double mandat, emploi et prix."},
        {"id": "mac-f05", "recto": "Point mort d'inflation (breakeven)",
         "verso": "Rendement nominal − rendement réel d'une obligation indexée de même maturité."},
        {"id": "mac-f06", "recto": "Hawkish vs dovish",
         "verso": "Hawkish : priorité à la lutte contre l'inflation (taux ↑). Dovish : soutien à l'activité (taux ↓)."},
        {"id": "mac-f07", "recto": "Effets typiques d'une surprise hawkish",
         "verso": "Taux courts ↑, courbe plus plate, devise ↑, actions ↓, spreads de crédit ↑."},
        {"id": "mac-f08", "recto": "Inflation sous-jacente (core)",
         "verso": "Inflation hors énergie et alimentation, composantes les plus volatiles."},
        {"id": "mac-f09", "recto": "Surprise économique", "verso": "Chiffre publié − consensus : seule la surprise fait bouger les prix."},
        {"id": "mac-f10", "recto": "Les 4 phases du cycle", "verso": "Reprise, expansion, ralentissement, récession."},
        {"id": "mac-f11", "recto": "Stagflation", "verso": "Inflation élevée et croissance faible : actions et obligations peuvent baisser ensemble."},
        {"id": "mac-f12", "recto": "Dynamique de la dette publique", "verso": r"$\Delta d \approx (r - g)\,d - pb$"},
        {"id": "mac-f13", "recto": "Spread souverain", "verso": "Écart de rendement avec l'Allemagne (zone euro) : prime de risque du pays."},
        {"id": "mac-f14", "recto": "Bad news is good news", "verso": "Une mauvaise nouvelle fait monter les actions car le marché anticipe des baisses de taux."},
        {"id": "mac-f15", "recto": "Corrélation actions/obligations", "verso": "Négative quand l'inflation est basse ; positive quand l'inflation est le risque dominant."},
    ],
}
