"""Module : Actions (Equity) — métiers, analyse financière, valorisation, portefeuille, stratégies, dérivés."""

MODULE = {
    "id": "actions",
    "titre": "Actions (Equity)",
    "icone": "📊",
    "statut": "complet",
    "resume": "Métiers equity, lecture des comptes, multiples, DCF et WACC, CAPM et facteurs, construction de "
              "portefeuille, stratégies long/short et event-driven, dérivés actions (delta one), pitch d'une action.",
    "chapitres": [
        # ------------------------------------------------------------------ 1
        {
            "id": "eq-c1",
            "titre": "1. Le monde de l'equity : produits et métiers",
            "contenu": r"""
« Equity » désigne tout ce qui touche aux **actions** : titres de propriété d'une entreprise, qui
donnent droit à une part des bénéfices (dividendes) et au vote en assemblée générale. L'actionnaire est
payé **après** tous les créanciers : il porte le risque le plus élevé, donc exige le rendement le plus élevé.

### Les métiers equity dans une banque d'investissement

| Métier | Rôle | Questions typiques en entretien |
|---|---|---|
| **ECM** (*Equity Capital Markets*) | Introductions en bourse, augmentations de capital, placements de blocs | Pourquoi une entreprise entre en bourse ? Qu'est-ce qu'une décote d'IPO ? |
| **Equity research** (analyste sell-side) | Analyse des entreprises d'un secteur, modèles financiers, recommandations (achat / neutre / vente) et objectifs de cours | Valorisez cette entreprise. Pitchez une action. |
| **Sales equity** | Relation avec les investisseurs institutionnels : idées, résumés de recherche, flux | Quelle est votre idée du moment ? |
| **Cash equity trading** | Exécution des ordres clients sur les actions, market making, programmes (paniers) | Comment exécuter un gros ordre sans faire bouger le prix ? |
| **Delta one** | Produits dont le delta vaut 1 : futures sur indices, swaps de performance, ETF, futures sur dividendes | Comment pricer un future sur indice ? |
| **Dérivés actions (flow / exotiques)** | Options sur actions et indices, produits structurés | Les grecques, le skew, l'autocall |
| **Prime brokerage** | Services aux hedge funds : financement, prêt de titres, compensation | Qu'est-ce que la vente à découvert ? |

### Côté buy side

- **Gérant actions** (*long only*) : choisit des actions pour battre un indice de référence.
- **Hedge fund long/short** : achète les actions qu'il juge sous-évaluées, vend à découvert celles qu'il
  juge surévaluées.
- **Gestion quantitative** : sélection systématique par facteurs (value, momentum, qualité…).
- **Gestion passive** : réplique un indice au moindre coût (fonds indiciels, ETF).

### Les grandes familles d'actions

- **Croissance** (*growth*) : bénéfices en forte progression, multiples élevés, très sensibles aux taux.
- **Value** : multiples faibles, entreprises matures ou décotées.
- **Cycliques** (automobile, industrie, matériaux, banques) : suivent le cycle économique.
- **Défensives** (santé, consommation de base, services aux collectivités) : résistent mieux aux récessions.
""",
            "points_cles": [
                "L'actionnaire est payé en dernier : risque et rendement attendus les plus élevés.",
                "ECM, research, sales, cash trading, delta one, dérivés, prime brokerage.",
                "Growth vs value ; cycliques vs défensives.",
            ],
        },
        # ------------------------------------------------------------------ 2
        {
            "id": "eq-c2",
            "titre": "2. Lire les comptes d'une entreprise",
            "contenu": r"""
Trois documents, liés entre eux.

### Le compte de résultat (P&L)

| Ligne | Calcul | À retenir |
|---|---|---|
| Chiffre d'affaires | Ventes de la période | Croissance « organique » = hors acquisitions et effets de change |
| **EBITDA** | Résultat avant intérêts, impôts, dépréciations et amortissements | Proxy de la rentabilité opérationnelle « cash » ; base des multiples VE/EBITDA |
| **EBIT** (résultat opérationnel) | EBITDA − dépréciations et amortissements | Rentabilité de l'activité |
| Résultat net | EBIT − intérêts − impôts | Revient aux actionnaires |
| **BPA** (EPS) | Résultat net / nombre d'actions | Base du PER |

### Le bilan

$$
\text{Actif} = \text{Capitaux propres} + \text{Dettes}
$$

L'actif contient les immobilisations, les stocks, les créances clients et la trésorerie. La **dette
nette** = dettes financières − trésorerie.

### Le tableau des flux de trésorerie

Il distingue les flux d'**exploitation**, d'**investissement** (dont les investissements, ou *capex*) et
de **financement** (dettes, dividendes, rachats d'actions). Le **free cash flow** mesure le cash
réellement disponible :

$$
FCF \approx EBITDA - \text{impôts} - \text{capex} - \Delta BFR
$$

où le **BFR** (besoin en fonds de roulement) = stocks + créances clients − dettes fournisseurs. Une
entreprise en croissance « consomme » du BFR.

### Les ratios essentiels

- **Marge d'EBITDA** = EBITDA / chiffre d'affaires.
- **ROE** (rentabilité des capitaux propres) = résultat net / capitaux propres. Décomposition DuPont :

$$
ROE = \underbrace{\frac{\text{Résultat net}}{\text{CA}}}_{\text{marge}} \times \underbrace{\frac{\text{CA}}{\text{Actif}}}_{\text{rotation}} \times \underbrace{\frac{\text{Actif}}{\text{Capitaux propres}}}_{\text{levier}}
$$

- **ROCE** = EBIT après impôt / capitaux employés : création de valeur si ROCE > coût du capital.
- **Levier** = dette nette / EBITDA : au-delà d'environ 3 à 4x, une entreprise est jugée très endettée
  (seuil variable selon le secteur).

Exemple : marge nette $10\,\%$, rotation $0{,}8$, levier $2{,}5$ : $ROE = 10\,\% \times 0{,}8 \times 2{,}5 = 20\,\%$.
""",
            "points_cles": [
                "EBITDA → EBIT → résultat net → BPA.",
                "Dette nette = dettes financières − trésorerie.",
                "FCF ≈ EBITDA − impôts − capex − ΔBFR.",
                "DuPont : ROE = marge × rotation × levier.",
            ],
        },
        # ------------------------------------------------------------------ 3
        {
            "id": "eq-c3",
            "titre": "3. Valoriser par les multiples",
            "contenu": r"""
### Valeur des fonds propres et valeur d'entreprise

- **Capitalisation boursière** = cours × nombre d'actions : valeur des **fonds propres**.
- **Valeur d'entreprise (VE)** : valeur de l'ensemble de l'activité, pour tous les financeurs :

$$
VE = \text{capitalisation} + \text{dette nette} \ (+ \text{intérêts minoritaires} + \text{provisions retraites}\ldots)
$$

Règle de cohérence : un agrégat **avant intérêts** (CA, EBITDA, EBIT) se compare à la **VE** ; un
agrégat **après intérêts** (résultat net, BPA) se compare à la **capitalisation**.

### Les multiples courants

| Multiple | Formule | Usage |
|---|---|---|
| **PER** (P/E) | Cours / BPA | Le plus connu ; dépend de la structure financière |
| **VE / EBITDA** | VE / EBITDA | Compare des entreprises au niveau de dette différent |
| **VE / CA** | VE / chiffre d'affaires | Entreprises pas encore rentables (tech jeune) |
| **P / B** (cours / actif net) | Capitalisation / capitaux propres | Banques et assurances |
| **Rendement du dividende** | Dividende / cours | Valeurs de rendement |
| **PEG** | PER / croissance du BPA (en %) | PER corrigé de la croissance |

Le **rendement bénéficiaire** est l'inverse du PER : un PER de 20 correspond à $5\,\%$.

### Exemple : valoriser par comparables

Entreprise cible : EBITDA $100$ M€, dette nette $150$ M€, $50$ millions d'actions. Les concurrents
cotés se traitent en moyenne à $9$x l'EBITDA.

1. VE implicite $= 9 \times 100 = 900$ M€.
2. Valeur des fonds propres $= 900 - 150 = 750$ M€.
3. Valeur par action $= 750 / 50 = 15$ €.

Si l'action cote $12$ €, elle paraît **décotée** de $20\,\%$… à condition que les comparables soient
vraiment comparables (croissance, marges, risque, taille, pays).

### Les limites

- Un multiple résume beaucoup d'hypothèses implicites (croissance, risque).
- Il dépend du marché : si tout le secteur est cher, la cible le paraîtra aussi.
- Les **transactions comparables** (prix payés lors de rachats d'entreprises) incluent une **prime de
  contrôle** et sont donc en général plus élevées que les multiples boursiers.
""",
            "points_cles": [
                "VE = capitalisation + dette nette (+ minoritaires…).",
                "Avant intérêts ↔ VE ; après intérêts ↔ capitalisation.",
                "Comparables : VE implicite → − dette nette → ÷ nombre d'actions.",
                "PER 20 = rendement bénéficiaire de 5 %.",
            ],
        },
        # ------------------------------------------------------------------ 4
        {
            "id": "eq-c4",
            "titre": "4. Le DCF et le coût du capital",
            "widget": "dcf",
            "contenu": r"""
Le **DCF** (*discounted cash flows*) valorise une entreprise par la valeur actuelle de ses flux de
trésorerie futurs. C'est la méthode « intrinsèque » de référence, la plus demandée en entretien.

### Étape 1 : projeter les free cash flows

On projette en général 5 à 10 ans de **FCF pour l'entreprise** (avant paiement des intérêts, donc
revenant à tous les financeurs).

### Étape 2 : le taux d'actualisation, le WACC

Le **coût moyen pondéré du capital** combine le coût des fonds propres $k_e$ et le coût de la dette
$k_d$, après impôt (les intérêts sont déductibles) :

$$
WACC = \frac{E}{E + D}\, k_e + \frac{D}{E + D}\, k_d\, (1 - t)
$$

Le coût des fonds propres vient en général du **CAPM** (chapitre 5) : $k_e = r_f + \beta\,(\text{prime de risque du marché})$.

Exemple : $E = 600$, $D = 400$, $k_e = 9\,\%$, $k_d = 5\,\%$, impôt $25\,\%$ :
$WACC = 0{,}6 \times 9\,\% + 0{,}4 \times 5\,\% \times 0{,}75 = 5{,}4\,\% + 1{,}5\,\% = 6{,}9\,\%$.

### Étape 3 : la valeur terminale

Au-delà de l'horizon explicite, on suppose une croissance perpétuelle $g$ (souvent 1,5 à 2,5 %, pas
plus que la croissance nominale de l'économie à long terme) :

$$
VT_n = \frac{FCF_{n+1}}{WACC - g} = \frac{FCF_n\,(1 + g)}{WACC - g}
$$

Exemple : $FCF_5 = 60$, $g = 2\,\%$, $WACC = 8\,\%$ : $VT_5 = 60 \times 1{,}02 / 0{,}06 = 1\,020$.

### Étape 4 : actualiser et passer à l'action

$$
VE = \sum_{t=1}^{n} \frac{FCF_t}{(1 + WACC)^t} + \frac{VT_n}{(1 + WACC)^n}
\qquad
\text{Valeur par action} = \frac{VE - \text{dette nette}}{\text{nombre d'actions}}
$$

Cas le plus simple : FCF de l'an prochain $50$, croissance perpétuelle $2\,\%$, WACC $7\,\%$ :
$VE = 50 / (0{,}07 - 0{,}02) = 1\,000$.

### Les pièges classiques

- La valeur terminale pèse souvent **60 à 80 %** de la VE : le résultat est très sensible à $g$ et au WACC.
  On présente toujours une **table de sensibilité** (WACC en ligne, $g$ en colonne).
- Si $g$ s'approche du WACC, la valeur explose : hypothèse incohérente.
- Cohérence : FCF pour l'entreprise ↔ WACC ↔ VE ; FCF pour l'actionnaire ↔ $k_e$ ↔ fonds propres.
""",
            "points_cles": [
                "WACC = E/(E+D)·kₑ + D/(E+D)·k_d·(1 − t).",
                "VT = FCF·(1 + g)/(WACC − g).",
                "VE − dette nette = fonds propres ; ÷ actions = valeur par action.",
                "La VT pèse souvent 60 à 80 % : toujours une table de sensibilité.",
            ],
        },
        # ------------------------------------------------------------------ 5
        {
            "id": "eq-c5",
            "titre": "5. Risque et rendement : CAPM, bêta et facteurs",
            "contenu": r"""
### Le CAPM (MEDAF)

Seul le risque **non diversifiable** (le risque de marché) est rémunéré. Le rendement attendu d'une
action dépend de son **bêta** :

$$
\mathbb{E}[R_i] = r_f + \beta_i\,\big(\mathbb{E}[R_m] - r_f\big)
\qquad
\beta_i = \frac{\mathrm{Cov}(R_i, R_m)}{\mathrm{Var}(R_m)}
$$

Exemple : $r_f = 3\,\%$, $\beta = 1{,}2$, prime de risque du marché $5\,\%$ :
$\mathbb{E}[R] = 3\,\% + 1{,}2 \times 5\,\% = 9\,\%$.

- $\beta > 1$ : l'action amplifie les mouvements du marché (cycliques, technologie).
- $\beta < 1$ : elle les amortit (défensives).
- L'**alpha** est le rendement en plus de ce que prévoit le CAPM : c'est ce que cherche un gérant actif.

### Bêta et levier financier

Plus une entreprise est endettée, plus ses actions sont risquées. Formule de Hamada (dette sans risque) :

$$
\beta_{levered} = \beta_{unlevered} \times \left(1 + (1 - t)\frac{D}{E}\right)
$$

On l'utilise pour transposer le bêta de concurrents à une entreprise de structure financière différente.

### Les facteurs

Le CAPM explique mal certaines différences de rendement. Les modèles **multifactoriels** ajoutent :

| Facteur | Idée | Exemple de modèle |
|---|---|---|
| **Taille** (SMB) | Les petites capitalisations ont historiquement plus rapporté | Fama-French 3 facteurs |
| **Value** (HML) | Les actions à faible valorisation (P/B bas) aussi | Fama-French 3 facteurs |
| **Momentum** | Les actions qui ont monté continuent souvent à court terme | Carhart 4 facteurs |
| **Qualité / rentabilité** | Les entreprises rentables et peu endettées | Fama-French 5 facteurs |
| **Faible volatilité** | Les actions peu volatiles ont un rendement ajusté du risque élevé | — |

La gestion quantitative et les ETF « smart beta » exploitent ces facteurs. Les primes factorielles
varient beaucoup dans le temps et peuvent disparaître pendant de longues périodes.
""",
            "points_cles": [
                "CAPM : E[R] = r_f + β(E[R_m] − r_f).",
                "β = Cov(R_i, R_m)/Var(R_m) ; alpha = surperformance non expliquée.",
                "Hamada : la dette augmente le bêta des actions.",
                "Facteurs : taille, value, momentum, qualité, faible volatilité.",
            ],
        },
        # ------------------------------------------------------------------ 6
        {
            "id": "eq-c6",
            "titre": "6. Construire un portefeuille d'actions",
            "contenu": r"""
### Markowitz : diversifier efficacement

Pour un portefeuille de poids $w$ et de matrice de covariance $\Sigma$ :

$$
\mathbb{E}[R_p] = \sum_i w_i\, \mathbb{E}[R_i]
\qquad
\sigma_p^2 = w^\top \Sigma\, w
$$

La **frontière efficiente** regroupe les portefeuilles qui offrent le rendement attendu maximal pour
chaque niveau de risque. En ajoutant un actif sans risque, le meilleur portefeuille risqué est celui qui
maximise le **ratio de Sharpe** (portefeuille tangent).

**Portefeuille de variance minimale à deux actifs non corrélés** :

$$
w_1 = \frac{\sigma_2^2}{\sigma_1^2 + \sigma_2^2}
$$

Exemple : $\sigma_1 = 20\,\%$, $\sigma_2 = 10\,\%$ : $w_1 = 0{,}01 / 0{,}05 = 20\,\%$ dans l'actif le plus
volatil, $80\,\%$ dans l'autre.

**Limites pratiques** : les rendements attendus sont très mal estimés, et l'optimisation les amplifie
(portefeuilles extrêmes). D'où les contraintes de poids, les approches robustes, le *risk parity* ou le
modèle de **Black-Litterman** (qui part des poids de marché et y intègre des vues).

### Gestion active ou passive

| | Active | Passive |
|---|---|---|
| Objectif | Battre l'indice | Le répliquer |
| Frais | Plus élevés | Très faibles |
| Mesures | Alpha, ratio d'information, tracking error | Tracking error minimale |
| Risque | Sous-performer | Suivre l'indice à la baisse |

### Pondérations d'un indice

- **Capitalisation** (S&P 500, CAC 40) : les plus grosses entreprises pèsent le plus ; concentration
  possible sur quelques valeurs.
- **Prix** (Dow Jones, Nikkei 225) : une action au cours élevé pèse plus, quelle que soit sa taille.
- **Équipondéré** : chaque action a le même poids, rééquilibrage régulier.

### Rééquilibrage et biais

Un portefeuille dérive avec les marchés : on le rééquilibre périodiquement (ce qui revient à vendre ce
qui a monté). Les biais comportementaux à connaître : excès de confiance, aversion aux pertes (garder
trop longtemps les perdantes), biais domestique (surpondérer son propre pays).
""",
            "points_cles": [
                "σ²ₚ = wᵀΣw ; frontière efficiente ; portefeuille tangent = Sharpe max.",
                "Variance minimale, 2 actifs non corrélés : w₁ = σ₂²/(σ₁² + σ₂²).",
                "Les rendements attendus sont mal estimés : contraintes, Black-Litterman.",
                "Indices pondérés par capitalisation, prix ou équipondérés.",
            ],
        },
        # ------------------------------------------------------------------ 7
        {
            "id": "eq-c7",
            "titre": "7. Les stratégies equity",
            "contenu": r"""
### Long/short et market neutral

Un fonds **long/short** achète des actions jugées sous-évaluées et vend à découvert des actions jugées
surévaluées. Il est **market neutral** si son exposition nette au marché (en bêta) est nulle : il ne
gagne que sur l'écart de performance entre ses longs et ses shorts.

Exemple : long $10$ M€ d'actions de bêta $1{,}0$, short $8$ M€ d'actions de bêta $1{,}25$. Exposition
bêta $= 10 \times 1{,}0 - 8 \times 1{,}25 = 0$ : neutre au marché malgré un montant net de $+2$ M€.

**Pair trading** : on achète une action et on vend une concurrente très proche (même secteur, même
pays) quand l'écart de valorisation entre les deux s'éloigne de sa moyenne, en pariant sur son retour.

### Event-driven

- **Arbitrage de fusion** (*merger arb*) : après l'annonce d'un rachat en cash à $50$ € par action, la
  cible cote $48$ € car l'opération peut échouer (autorités de la concurrence, financement). Acheter à
  $48$ rapporte $2/48 \approx 4{,}2\,\%$ si l'opération se réalise, mais l'action peut retomber vers
  $40$ € en cas d'échec. Le spread mesure la probabilité d'échec perçue et le temps restant. Pour un
  rachat payé en actions, on achète la cible et on vend l'acheteur selon la parité d'échange.
- **Situations spéciales** : scissions (*spin-offs*), restructurations, entrées dans un indice (les
  fonds indiciels doivent acheter).

### Stratégies factorielles et systématiques

- **Value** : acheter les actions bon marché selon leurs multiples.
- **Momentum** : acheter les gagnantes des 12 derniers mois (hors dernier mois), vendre les perdantes.
- **Qualité**, **faible volatilité**, combinaisons multifactorielles.

### Stratégies de rendement

- **Covered call** (vente de calls sur ses actions) : revenu supplémentaire contre l'abandon de la hausse.
- **Capture de dividendes**, stratégies sur futures de dividendes.

### Scénarios pour un portefeuille long/short market neutral

| Scénario | Longs | Shorts | Résultat |
|---|---|---|---|
| Le marché monte de 10 %, sélection neutre | +10 % | −10 % (perte sur les shorts) | ≈ 0 |
| Le marché baisse de 10 %, sélection neutre | −10 % | +10 % | ≈ 0 |
| Les longs battent les shorts de 5 % | | | ≈ +5 % sur la jambe longue |
| *Short squeeze* : les actions vendues bondissent | | Forte perte | Perte, parfois brutale |
""",
            "points_cles": [
                "Market neutral : exposition bêta nulle, pas forcément montant net nul.",
                "Merger arb : spread = probabilité d'échec perçue + temps.",
                "Momentum : gagnantes des 12 derniers mois hors dernier mois.",
                "Risque du short : le short squeeze.",
            ],
        },
        # ------------------------------------------------------------------ 8
        {
            "id": "eq-c8",
            "titre": "8. Les dérivés actions et le delta one",
            "contenu": r"""
### Futures sur indice

Contrat standardisé sur un indice (Euro Stoxx 50, S&P 500, CAC 40…), réglé en cash. Prix théorique :

$$
F = S\, e^{(r - q)T}
$$

où $q$ est le rendement du dividende attendu. Exemple : indice à $5\,000$, taux $3\,\%$, dividende
$2\,\%$, 3 mois : $F \approx 5\,000 \times e^{0{,}01 \times 0{,}25} \approx 5\,012{,}5$.

L'écart entre le future et le spot s'appelle la **base**. Les traders font de l'**arbitrage
cash-and-carry** quand elle s'écarte de sa valeur théorique.

### Futures sur dividendes

Contrat qui paie la somme des dividendes versés par les actions d'un indice sur une année donnée. Les
banques, qui vendent beaucoup d'autocalls, sont naturellement **longues de dividendes** du fait de leurs
couvertures et les revendent via ces futures.

### Swaps de performance (*total return swap*, TRS)

Une partie reçoit la **performance totale** d'une action ou d'un indice (variation du cours plus
dividendes) et paie un taux de financement plus une marge. Le client obtient l'exposition sans acheter
l'action (pas de capital immobilisé) ; la banque se couvre en détenant l'action. Utilisé par les hedge
funds pour le levier et pour vendre à découvert synthétiquement.

### ETF

Fonds coté qui réplique un indice. Les **participants autorisés** peuvent **créer** des parts (en
livrant les actions du panier) ou les **racheter** (en récupérant les actions). Ce mécanisme
maintient le cours de l'ETF très proche de sa valeur liquidative : si l'ETF cote au-dessus, ils créent
des parts et les vendent ; s'il cote en dessous, ils les rachètent. Réplication **physique** (détenir
les actions) ou **synthétique** (via un swap).

### Options sur actions

Voir le module Options : les options sur indices sont dominées par la demande de **puts de protection**
(skew négatif) ; les options sur actions individuelles sont plus chères en volatilité et sensibles aux
annonces de résultats (la vol implicite monte avant, chute après : le *vol crush*).

### Le desk delta one

Il gère des positions de delta 1 : futures, TRS, ETF, prêt-emprunt de titres. Ses risques principaux :
**financement**, **dividendes**, **coût d'emprunt des titres** et exécution. Les marges sont faibles,
les volumes très importants.
""",
            "points_cles": [
                "Future sur indice : F = S·e^((r − q)T) ; base = F − S.",
                "TRS : performance totale contre financement, sans acheter l'action.",
                "ETF : création/rachat par les participants autorisés.",
                "Vol crush : la vol implicite chute après les résultats.",
            ],
        },
        # ------------------------------------------------------------------ 9
        {
            "id": "eq-c9",
            "titre": "9. Pitcher une action en entretien",
            "contenu": r"""
« Pitchez-moi une action » est la question equity la plus fréquente. Voici une structure de 2 minutes.

### 1. La recommandation, tout de suite

« Je recommande **l'achat** de l'entreprise X, avec un objectif de cours de $Y$ €, soit $+Z\,\%$ de
potentiel sur 12 mois. »

### 2. La présentation en une phrase

Ce que fait l'entreprise, sa taille, sa position concurrentielle.

### 3. La thèse : 2 ou 3 arguments

- **Croissance** : un marché porteur, des parts de marché qui progressent.
- **Rentabilité** : des marges qui s'améliorent, un ROCE supérieur au coût du capital.
- **Valorisation** : elle se traite à un multiple inférieur à ses concurrents ou à son historique, sans
  raison durable.
- **Catalyseur** : l'événement qui fera converger le cours vers ta valeur (résultats, nouveau produit,
  rachat d'actions, cession d'une activité).

### 4. La valorisation

Un chiffre clair : « Elle se traite à $8$x l'EBITDA contre $11$x pour ses concurrents. En lui appliquant
$10$x, j'obtiens $Y$ € par action. » Si possible, recoupe avec un DCF.

### 5. Les risques

Deux risques précis et ce qui invaliderait la thèse : « Si la marge passe sous $X\,\%$, je revois ma
recommandation. »

### Préparation

- Choisis une entreprise que tu suis vraiment, idéalement **pas** l'une des plus connues (tout le monde
  pitche les mêmes géants de la tech).
- Connais les chiffres clés : chiffre d'affaires, marge, croissance, dette nette, multiple, cours.
- Prépare les relances : « Qui sont ses concurrents ? », « Pourquoi le marché ne l'a-t-il pas déjà vu ? »,
  « Et si je vous dis de la vendre à découvert, quelle action choisiriez-vous ? »
- Prépare aussi une idée **short** : c'est un excellent signal de maturité.

### Exemple de trame

« Je recommande l'achat d'un équipementier industriel européen, objectif $+25\,\%$. Son carnet de
commandes progresse de $15\,\%$ grâce à l'électrification, sa marge d'EBIT remonte de $10$ à $13\,\%$ avec
la fin d'un plan de restructuration, et elle se traite à $9$x l'EBITDA contre $12$x pour ses pairs. Le
catalyseur est la journée investisseurs de mars, où elle doit présenter ses objectifs de marge. Les
risques : un ralentissement industriel en Europe et l'exécution du plan. »
""",
            "points_cles": [
                "Recommandation et objectif de cours d'emblée.",
                "Thèse : croissance, rentabilité, valorisation, catalyseur.",
                "Un multiple chiffré face aux concurrents.",
                "Deux risques et ce qui invaliderait la thèse.",
            ],
        },
    ],
    "quiz": [
        {"id": "eq-q01", "type": "nombre",
         "question": r"Capitalisation $800$ M€, dette nette $200$ M€. Valeur d'entreprise en M€ ?",
         "reponse": 1000, "tolerance": 0.001,
         "explication": "VE = capitalisation + dette nette = 800 + 200."},
        {"id": "eq-q02", "type": "nombre",
         "question": r"Même entreprise (VE $1\,000$ M€), EBITDA $125$ M€. Multiple VE/EBITDA ?",
         "reponse": 8, "tolerance": 0.001,
         "explication": "1 000 / 125 = 8x."},
        {"id": "eq-q03", "type": "nombre",
         "question": r"Cours $50$ €, bénéfice par action $2{,}5$ €. PER ?",
         "reponse": 20, "tolerance": 0.001,
         "explication": r"$50 / 2{,}5 = 20$ (rendement bénéficiaire de $5\,\%$)."},
        {"id": "eq-q04", "type": "nombre",
         "question": r"Comparables à $9$x l'EBITDA. Cible : EBITDA $100$ M€, dette nette $150$ M€, $50$ millions d'actions. "
                     r"Valeur par action en € ?",
         "reponse": 15, "tolerance": 0.001,
         "explication": r"VE $= 900$ ; fonds propres $= 900 - 150 = 750$ ; $750 / 50 = 15$ €."},
        {"id": "eq-q05", "type": "qcm",
         "question": "Quel agrégat comparer à la valeur d'entreprise (et non à la capitalisation) ?",
         "choix": ["Le résultat net", "Le bénéfice par action", "L'EBITDA", "Le dividende"],
         "reponse": 2,
         "explication": "L'EBITDA est avant intérêts : il revient à tous les financeurs, comme la VE."},
        {"id": "eq-q06", "type": "nombre",
         "question": r"$E = 600$, $D = 400$, $k_e = 9\,\%$, $k_d = 5\,\%$, impôt $25\,\%$. WACC en % (1 décimale) ?",
         "reponse": 6.9, "tolerance": 0.01,
         "explication": r"$0{,}6 \times 9 + 0{,}4 \times 5 \times 0{,}75 = 5{,}4 + 1{,}5 = 6{,}9\,\%$."},
        {"id": "eq-q07", "type": "nombre",
         "question": r"CAPM : $r_f = 3\,\%$, $\beta = 1{,}2$, prime de risque du marché $5\,\%$. Coût des fonds propres en % ?",
         "reponse": 9, "tolerance": 0.001,
         "explication": r"$3 + 1{,}2 \times 5 = 9\,\%$."},
        {"id": "eq-q08", "type": "nombre",
         "question": r"FCF de l'an prochain $50$, croissance perpétuelle $2\,\%$, WACC $7\,\%$. Valeur d'entreprise ?",
         "reponse": 1000, "tolerance": 0.001,
         "explication": r"$50 / (0{,}07 - 0{,}02) = 1\,000$."},
        {"id": "eq-q09", "type": "nombre",
         "question": r"$FCF_5 = 60$, $g = 2\,\%$, WACC $8\,\%$. Valeur terminale en année 5 ?",
         "reponse": 1020, "tolerance": 0.5,
         "explication": r"$60 \times 1{,}02 / 0{,}06 = 1\,020$."},
        {"id": "eq-q10", "type": "qcm",
         "question": "Dans un DCF, que se passe-t-il si la croissance perpétuelle g s'approche du WACC ?",
         "choix": ["La valeur tend vers zéro", "La valeur terminale explose : l'hypothèse est incohérente",
                   "Rien, g n'a pas d'influence", "Le WACC diminue automatiquement"],
         "reponse": 1,
         "explication": "Le dénominateur WACC − g tend vers zéro."},
        {"id": "eq-q11", "type": "nombre",
         "question": r"Marge nette $10\,\%$, rotation de l'actif $0{,}8$, levier (actif / capitaux propres) $2{,}5$. ROE en % ?",
         "reponse": 20, "tolerance": 0.001,
         "explication": r"DuPont : $10\,\% \times 0{,}8 \times 2{,}5 = 20\,\%$."},
        {"id": "eq-q12", "type": "qcm",
         "question": "Une action a un bêta de 1,5. Si le marché baisse de 10 %, elle baisse en moyenne d'environ…",
         "choix": ["5 %", "10 %", "15 %", "1,5 %"],
         "reponse": 2,
         "explication": "Le bêta mesure l'amplification des mouvements du marché : 1,5 × 10 %."},
        {"id": "eq-q13", "type": "nombre",
         "question": r"Deux actifs non corrélés : $\sigma_1 = 20\,\%$, $\sigma_2 = 10\,\%$. Poids de l'actif 1 dans le portefeuille "
                     r"de variance minimale, en % ?",
         "reponse": 20, "tolerance": 0.01,
         "explication": r"$w_1 = \sigma_2^2 / (\sigma_1^2 + \sigma_2^2) = 0{,}01 / 0{,}05 = 20\,\%$."},
        {"id": "eq-q14", "type": "nombre",
         "question": r"Long $10$ M€ d'actions de bêta $1{,}0$. Combien de M€ d'actions de bêta $1{,}25$ vendre à découvert "
                     r"pour être neutre en bêta ?",
         "reponse": 8, "tolerance": 0.001,
         "explication": r"$10 \times 1{,}0 / 1{,}25 = 8$ M€."},
        {"id": "eq-q15", "type": "nombre",
         "question": r"Offre de rachat en cash à $50$ €, la cible cote $48$ €. Gain en % si l'opération se réalise (1 décimale) ?",
         "reponse": 4.2, "tolerance": 0.05,
         "explication": r"$2 / 48 \approx 4{,}2\,\%$."},
        {"id": "eq-q16", "type": "nombre",
         "question": r"Indice à $5\,000$, taux $3\,\%$, rendement du dividende $2\,\%$ (continus), 3 mois. Prix du future (1 décimale) ?",
         "reponse": 5012.5, "tolerance": 0.2,
         "explication": r"$5\,000 \times e^{(0{,}03 - 0{,}02) \times 0{,}25} \approx 5\,012{,}5$."},
        {"id": "eq-q17", "type": "qcm",
         "question": "Un ETF cote au-dessus de sa valeur liquidative. Que font les participants autorisés ?",
         "choix": ["Ils rachètent des parts", "Ils créent des parts en livrant le panier d'actions, puis les vendent",
                   "Ils suspendent la cotation", "Rien"],
         "reponse": 1,
         "explication": "Ils achètent le panier, le livrent contre des parts neuves et vendent ces parts plus cher : l'écart se referme."},
        {"id": "eq-q18", "type": "qcm",
         "question": "Qu'est-ce qu'un total return swap sur une action ?",
         "choix": ["Un échange de deux taux fixes", "On reçoit la performance totale de l'action (cours + dividendes) contre un taux de financement",
                   "Une option sur dividende", "Un échange d'actions entre deux fonds"],
         "reponse": 1,
         "explication": "Il donne l'exposition économique sans détenir l'action."},
        {"id": "eq-q19", "type": "qcm",
         "question": "Plus une entreprise s'endette (toutes choses égales par ailleurs), son bêta actions…",
         "choix": ["baisse", "augmente", "ne change pas", "devient négatif"],
         "reponse": 1,
         "explication": r"Hamada : $\beta_L = \beta_U (1 + (1-t) D/E)$ : le levier amplifie le risque de l'actionnaire."},
        {"id": "eq-q20", "type": "qcm",
         "question": "Les transactions comparables (rachats d'entreprises) donnent en général des multiples…",
         "choix": ["plus faibles que les multiples boursiers", "plus élevés, car ils incluent une prime de contrôle",
                   "identiques", "sans rapport avec la valeur"],
         "reponse": 1,
         "explication": "L'acheteur paie pour prendre le contrôle et réaliser des synergies."},
        {"id": "eq-q21", "type": "qcm",
         "question": "Que désigne le « vol crush » sur une option d'action ?",
         "choix": ["Une hausse de la vol avant une fusion", "La chute de la vol implicite juste après la publication des résultats",
                   "Une vente massive de puts", "La fin du skew"],
         "reponse": 1,
         "explication": "L'incertitude disparaît avec l'annonce : l'acheteur d'options peut perdre même si l'action bouge."},
    ],
    "flashcards": [
        {"id": "eq-f01", "recto": "Valeur d'entreprise", "verso": "Capitalisation + dette nette (+ minoritaires, provisions…)."},
        {"id": "eq-f02", "recto": "EBITDA", "verso": "Résultat avant intérêts, impôts, dépréciations et amortissements."},
        {"id": "eq-f03", "recto": "Free cash flow", "verso": r"$\approx EBITDA - \text{impôts} - \text{capex} - \Delta BFR$"},
        {"id": "eq-f04", "recto": "Décomposition DuPont du ROE", "verso": "ROE = marge nette × rotation de l'actif × levier."},
        {"id": "eq-f05", "recto": "Règle de cohérence des multiples", "verso": "Agrégat avant intérêts ↔ VE ; après intérêts ↔ capitalisation."},
        {"id": "eq-f06", "recto": "PER et rendement bénéficiaire", "verso": "PER = cours / BPA ; rendement bénéficiaire = 1 / PER."},
        {"id": "eq-f07", "recto": "WACC", "verso": r"$\frac{E}{E+D} k_e + \frac{D}{E+D} k_d (1 - t)$"},
        {"id": "eq-f08", "recto": "Valeur terminale (Gordon)", "verso": r"$FCF_n (1 + g) / (WACC - g)$"},
        {"id": "eq-f09", "recto": "CAPM", "verso": r"$\mathbb{E}[R_i] = r_f + \beta_i(\mathbb{E}[R_m] - r_f)$"},
        {"id": "eq-f10", "recto": "Formule de Hamada", "verso": r"$\beta_L = \beta_U \left(1 + (1-t)\frac{D}{E}\right)$"},
        {"id": "eq-f11", "recto": "Facteurs de Fama-French (3)", "verso": "Marché, taille (SMB), value (HML)."},
        {"id": "eq-f12", "recto": "Market neutral", "verso": "Exposition bêta nette nulle : on ne gagne que sur l'écart longs/shorts."},
        {"id": "eq-f13", "recto": "Merger arbitrage", "verso": "Acheter la cible sous le prix d'offre ; le spread reflète le risque d'échec et le temps."},
        {"id": "eq-f14", "recto": "Prix d'un future sur indice", "verso": r"$F = S\,e^{(r - q)T}$ ; base = F − S."},
        {"id": "eq-f15", "recto": "Total return swap", "verso": "Recevoir cours + dividendes d'une action contre un taux de financement."},
        {"id": "eq-f16", "recto": "Pitch d'une action", "verso": "Reco + objectif, thèse (croissance, rentabilité, valorisation, catalyseur), multiple, risques."},
    ],
}
