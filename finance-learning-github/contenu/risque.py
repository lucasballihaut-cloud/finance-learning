"""Module : Risque de marché."""

MODULE = {
    "id": "risque",
    "titre": "Risque de marché",
    "icone": "📉",
    "statut": "complet",
    "resume": "Volatilité (historique, EWMA, GARCH), VaR, Expected Shortfall, diversification, "
              "backtesting et stress tests.",
    "chapitres": [
        {
            "id": "risk-c1",
            "titre": "1. Mesurer la volatilité",
            "contenu": r"""
On travaille sur les **rendements** plutôt que sur les prix. Le rendement logarithmique du jour $t$ vaut
$r_t = \ln(P_t / P_{t-1})$ ; pour de petites variations il est très proche du rendement simple
$P_t / P_{t-1} - 1$.

**Volatilité historique** : écart-type des rendements sur une fenêtre (par exemple 60 jours). On
l'**annualise** avec la racine du nombre de jours de bourse (environ 252), car les variances
s'additionnent quand les rendements sont indépendants :

$$
\sigma_{an} = \sigma_{jour} \times \sqrt{252}
$$

Ordre de grandeur : $1\,\%$ par jour correspond à environ $16\,\%$ par an.

**La volatilité n'est pas constante** : les journées agitées se suivent (*volatility clustering*).
Deux modèles classiques en tiennent compte.

**EWMA** (moyenne mobile à pondération exponentielle, popularisée par RiskMetrics avec
$\lambda = 0{,}94$ en données journalières) : les observations récentes pèsent plus.

$$
\sigma_t^2 = \lambda\, \sigma_{t-1}^2 + (1 - \lambda)\, r_{t-1}^2
$$

**GARCH(1,1)** : on ajoute une variance de long terme vers laquelle la volatilité revient.

$$
\sigma_t^2 = \omega + \alpha\, r_{t-1}^2 + \beta\, \sigma_{t-1}^2
\qquad
\sigma^2_{LT} = \frac{\omega}{1 - \alpha - \beta} \quad (\alpha + \beta < 1)
$$

$\alpha$ mesure la réaction aux chocs, $\beta$ la persistance. L'EWMA est un GARCH particulier
avec $\omega = 0$ et $\alpha + \beta = 1$ : il n'a pas de retour à la moyenne.
""",
            "points_cles": [
                "σ annuelle = σ journalière × √252.",
                "EWMA : σ²ₜ = λσ²ₜ₋₁ + (1 − λ)r²ₜ₋₁.",
                "GARCH : retour vers la variance de long terme ω/(1 − α − β).",
            ],
        },
        {
            "id": "risk-c2",
            "titre": "2. La Value at Risk (VaR)",
            "widget": "var",
            "contenu": r"""
La **VaR** au niveau de confiance $\alpha$ (par exemple $99\,\%$) sur un horizon $h$ est la perte
qui ne sera **dépassée qu'avec une probabilité** $1 - \alpha$ sur cet horizon. Si $L$ désigne la perte :

$$
P(L > VaR_\alpha) = 1 - \alpha
$$

Exemple : « VaR 1 jour à $99\,\%$ de 1 M€ » signifie qu'on s'attend à perdre plus de 1 M€ environ
un jour sur cent.

**Trois méthodes de calcul**

1. **Paramétrique (variance-covariance)** : on suppose des rendements gaussiens de moyenne nulle.
   Pour une position de valeur $V$ et de volatilité $\sigma$ sur l'horizon :
   $$
   VaR_\alpha = z_\alpha\, \sigma\, V
   \qquad z_{95\%} \approx 1{,}645, \quad z_{99\%} \approx 2{,}326
   $$
2. **Historique** : on rejoue sur le portefeuille actuel les rendements des $N$ derniers jours, on trie
   les P&L obtenus et on lit le quantile (avec 500 scénarios, la VaR 99 % est autour de la 5e pire perte).
   Pas d'hypothèse de loi, mais on suppose que le passé récent est représentatif.
3. **Monte-Carlo** : on simule un grand nombre de scénarios avec un modèle et on **réévalue**
   complètement le portefeuille. Indispensable quand il contient des options (pertes non linéaires).

**Horizon.** Si les rendements sont indépendants, $VaR_{h\ jours} \approx VaR_{1\ jour} \times \sqrt{h}$.
C'est une approximation : elle ignore l'autocorrélation et le fait qu'on peut réduire la position en route.

**Portefeuille.** Avec un vecteur d'expositions $w$ et une matrice de covariance $\Sigma$, la variance du
P&L vaut $w^\top \Sigma\, w$. Pour deux actifs :

$$
\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2\, w_1 w_2\, \rho\, \sigma_1 \sigma_2
$$

Tant que $\rho < 1$, la VaR paramétrique du portefeuille est **inférieure** à la somme des VaR : c'est
l'effet de diversification.
""",
            "points_cles": [
                "VaR = quantile de la distribution des pertes.",
                "Paramétrique : VaR = z · σ · V (z₉₉ ≈ 2,33).",
                "Règle de la racine du temps : VaR(h) ≈ VaR(1 j) · √h.",
            ],
        },
        {
            "id": "risk-c3",
            "titre": "3. Expected Shortfall et limites de la VaR",
            "contenu": r"""
La VaR répond à « quelle perte dans un cas défavorable mais courant ? », mais **pas** à « combien
perd-on quand ça va vraiment mal ? ». Deux portefeuilles peuvent avoir la même VaR et des pertes
extrêmes très différentes (par exemple un vendeur de puts très hors de la monnaie).

**Expected Shortfall** (ou CVaR) : perte moyenne **au-delà** de la VaR.

$$
ES_\alpha = \mathbb{E}\left[\, L \mid L \ge VaR_\alpha \,\right]
$$

Pour une loi normale de moyenne nulle et d'écart-type $\sigma$ (en notant $n$ la densité normale) :

$$
ES_\alpha = \sigma\, \frac{n(z_\alpha)}{1 - \alpha}
$$

Numériquement, l'ES à $97{,}5\,\%$ ($\approx 2{,}34\,\sigma$) est proche de la VaR à $99\,\%$
($\approx 2{,}33\,\sigma$) dans le cas gaussien. C'est ce niveau que retient la réglementation bancaire
actuelle sur le portefeuille de négociation (FRTB), qui a remplacé la VaR par l'ES.

**Mesure de risque cohérente.** Une bonne mesure devrait être **sous-additive** : le risque d'un
portefeuille ne doit pas dépasser la somme des risques de ses parties (sinon on pénaliserait la
diversification). L'ES l'est toujours ; la VaR ne l'est pas dans tous les cas (exemple classique :
deux obligations indépendantes ayant chacune une probabilité de défaut un peu inférieure à
$1 - \alpha$).

**Queues épaisses.** Les rendements réels ont plus d'événements extrêmes que la loi normale
(kurtosis élevée) : une VaR gaussienne sous-estime souvent le risque de krach. D'où les VaR
historiques, les lois de Student et surtout les stress tests.
""",
            "points_cles": [
                "ES = perte moyenne au-delà de la VaR.",
                "ES sous-additive, VaR pas toujours.",
                "Normal : ES 97,5 % ≈ VaR 99 %.",
            ],
        },
        {
            "id": "risk-c4",
            "titre": "4. Backtesting, stress tests et risque des options",
            "contenu": r"""
**Backtesting.** On compare chaque jour la VaR annoncée la veille au P&L réalisé. Un dépassement est
une **exception**. Avec une VaR à $99\,\%$ sur 250 jours, on attend en moyenne $250 \times 1\,\% = 2{,}5$
exceptions. Le cadre bâlois classe le modèle selon le nombre d'exceptions sur un an :
**vert** de 0 à 4, **orange** de 5 à 9, **rouge** à partir de 10. Trop d'exceptions signifie un
modèle qui sous-estime le risque ; trop peu, un modèle trop conservateur. Les exceptions ne doivent
pas non plus arriver en grappes.

**Stress tests.** On applique au portefeuille des scénarios extrêmes mais plausibles :
- **historiques** : rejouer une crise passée (krach actions, choc de taux, crise de liquidité) ;
- **hypothétiques** : construire un scénario cohérent (par exemple actions $-30\,\%$, spreads de crédit
  $+200$ bp, volatilité implicite qui double).
Ils complètent la VaR, qui ne dit rien des événements très rares.

**Risque d'un portefeuille d'options.** La relation entre P&L et spot n'est plus linéaire. Pour un
petit mouvement, l'approximation **delta-gamma** donne :

$$
\Delta V \approx \Delta \cdot \Delta S + \tfrac{1}{2}\, \Gamma\, (\Delta S)^2 + \mathcal{V}\, \Delta\sigma
$$

Un portefeuille **short gamma** (vendeur d'options) perd dans les deux sens lors d'un grand
mouvement : une VaR purement « delta » le sous-estime fortement. On utilise alors la réévaluation
complète (*full revaluation*) et des grilles de scénarios spot × volatilité.

**Limites de risque.** Les desks ont des limites en delta, vega, DV01, VaR et stress, suivies
quotidiennement par le **risque de marché** (middle office), indépendant du front office.
""",
            "points_cles": [
                "VaR 99 % sur 250 j : ≈ 2,5 exceptions attendues.",
                "Zones de Bâle : vert 0-4, orange 5-9, rouge ≥ 10.",
                "Options : approximation delta-gamma ou réévaluation complète.",
            ],
        },
        {
            "id": "risk-c5",
            "titre": "5. Risque de contrepartie et risque de liquidité",
            "contenu": r"""
### Risque de contrepartie

Sur un dérivé OTC, si la contrepartie fait défaut alors que le contrat a une valeur **positive** pour
nous, on perd cette valeur (moins le recouvrement). Les notions clés :

- **Exposition** : $\max(V, 0)$, valeur positive du contrat pour nous ;
- **EE** (*expected exposure*) : exposition moyenne future, date par date ;
- **PFE** (*potential future exposure*) : quantile élevé de l'exposition future (par exemple 95 %) ;
- **Collatéral** : garanties échangées selon un contrat (CSA). La **marge de variation** compense chaque
  jour la valeur de marché ; la **marge initiale** couvre le risque de mouvement le temps de remplacer
  le contrat après un défaut.

**CVA** (*credit valuation adjustment*) : le prix du risque de défaut de la contrepartie, déduit de la
valeur du dérivé. Approximation :

$$
CVA \approx LGD \times \sum_i EE(t_i)\; PD(t_{i-1}, t_i)\; DF(t_i)
$$

Exemple simplifié : exposition moyenne $2$ M€ sur 5 ans, $LGD = 60\,\%$, probabilité de défaut $1\,\%$
par an, actualisation négligée : $CVA \approx 0{,}6 \times 2 \times 5\,\% = 60\,000$ €.

**Wrong-way risk** : l'exposition augmente précisément quand la contrepartie devient plus fragile
(par exemple acheter une protection CDS sur une banque à une banque très liée à la première).

### Risque de liquidité

Deux formes :
- **liquidité de marché** : ne pas pouvoir vendre sans faire baisser fortement le prix ;
- **liquidité de financement** : ne pas pouvoir financer ses positions ou ses appels de marge.

Coût de liquidation approximatif : la moitié de la fourchette bid-ask multipliée par la taille. Pour
$10$ M€ avec une fourchette de $0{,}4\,\%$ : $0{,}2\,\% \times 10$ M€ $= 20\,000$ €. En période de
stress, les fourchettes s'écartent et ce coût peut être multiplié : d'où les VaR « ajustées de la
liquidité » et les limites de concentration.

Les deux risques se renforcent : une perte déclenche des appels de marge, qui forcent à vendre, ce qui
fait baisser les prix et déclenche de nouveaux appels de marge (spirale de liquidité).
""",
            "points_cles": [
                "Exposition = max(V, 0) ; collatéral : marge de variation + marge initiale.",
                "CVA ≈ LGD × Σ EE × PD × DF.",
                "Wrong-way risk : exposition ↑ quand la contrepartie se fragilise.",
                "Coût de liquidation ≈ ½ fourchette × taille, bien plus en stress.",
            ],
        },
        {
            "id": "risk-c6",
            "titre": "6. Les crises de marché et leurs leçons",
            "contenu": r"""
Connaître quelques crises permet de répondre aux questions « Quels risques un modèle de VaR ne
voit-il pas ? » ou « Que retenez-vous de… ? ». Pour chacune : ce qui s'est passé et la leçon.

| Crise | Ce qui s'est passé | Leçon pour le risque |
|---|---|---|
| **Krach d'octobre 1987** | Le Dow Jones perd environ 22,6 % le 19 octobre, en une seule séance | Les rendements extrêmes sont bien plus fréquents que dans une loi normale ; les stratégies d'assurance de portefeuille vendant dans la baisse amplifient le mouvement. Après 1987, le skew des options actions s'installe durablement |
| **LTCM (1998)** | Un fonds très endetté, aux positions de convergence (arbitrages de spreads), perd massivement après le défaut russe ; sauvetage organisé par la Fed de New York | Levier + corrélations qui montent en crise + illiquidité : des positions « sans risque » deviennent mortelles |
| **Crise financière (2007-2008)** | Pertes sur les crédits immobiliers titrisés, crise de liquidité, faillite de Lehman Brothers le 15 septembre 2008 | Risque de contrepartie, risque de modèle (corrélations de défaut sous-estimées), liquidité de financement |
| **Flash crash (6 mai 2010)** | Les indices américains chutent puis rebondissent en quelques minutes | Risque lié au trading automatique et à l'évaporation soudaine de la liquidité |
| **Franc suisse (15 janvier 2015)** | La BNS abandonne le plancher de 1,20 contre l'euro : le franc s'apprécie de plus de 15 % en quelques minutes | **Gap risk** : les ordres stop ne sont pas exécutés au niveau prévu, certains courtiers font faillite |
| **Covid (mars 2020)** | Chute très rapide des actions, le VIX clôture au record de 82,69 le 16 mars ; tensions même sur les emprunts d'État américains | Les actifs refuges peuvent devenir illiquides ; les banques centrales interviennent massivement |
| **Gilts britanniques (septembre 2022)** | Après une annonce budgétaire, les taux longs britanniques bondissent ; les fonds de pension utilisant des stratégies LDI à levier subissent des appels de marge ; la Banque d'Angleterre intervient | Spirale de liquidité : collatéral, appels de marge, ventes forcées |
| **Silicon Valley Bank (mars 2023)** | Pertes latentes sur un gros portefeuille obligataire après la hausse des taux, puis retrait massif des dépôts | Risque de taux (duration) combiné au risque de liquidité de financement |

### Ce qu'il faut en retenir

1. **Les queues sont épaisses** : les événements « à 5 écarts-types » arrivent bien plus souvent que prévu.
2. **Les corrélations montent en crise** : la diversification disparaît quand on en a besoin.
3. **La liquidité disparaît** au pire moment : prix d'exécution, appels de marge, financement.
4. **Le levier transforme une perte en faillite.**
5. D'où l'importance des **stress tests**, des limites de concentration et de l'Expected Shortfall,
   en complément de la VaR.
""",
            "points_cles": [
                "Queues épaisses, corrélations qui montent, liquidité qui disparaît.",
                "Gap risk : un prix peut sauter sans passer par les niveaux intermédiaires.",
                "Levier + illiquidité = spirale de ventes forcées.",
            ],
        },
        {
            "id": "risk-c7",
            "titre": "7. Mesurer la performance et piloter un portefeuille",
            "contenu": r"""
### Les ratios

| Mesure | Formule | Lecture |
|---|---|---|
| **Sharpe** | $\dfrac{R_p - r_f}{\sigma_p}$ | Rendement en excès par unité de risque total |
| **Sortino** | $\dfrac{R_p - r_f}{\sigma_{baisse}}$ | Comme Sharpe, mais ne pénalise que la volatilité des rendements négatifs |
| **Tracking error** | $\sigma(R_p - R_b)$ | Écart de comportement par rapport à l'indice de référence $b$ |
| **Ratio d'information** | $\dfrac{R_p - R_b}{\sigma(R_p - R_b)}$ | Surperformance par unité de risque relatif ; mesure le talent d'un gérant actif |
| **Alpha de Jensen** | $R_p - \big[r_f + \beta (R_m - r_f)\big]$ | Rendement non expliqué par l'exposition au marché |

Exemple : portefeuille $9\,\%$, indice $7\,\%$, tracking error $4\,\%$ : ratio d'information $= 2/4 = 0{,}5$.

### Le maximum drawdown

Plus forte baisse entre un sommet et le creux qui suit. Exemple : un portefeuille passe de $100$ à
$130$, retombe à $91$, puis remonte à $120$. Drawdown maximal $= 91/130 - 1 = -30\,\%$. Retenir
l'asymétrie : après $-30\,\%$, il faut $+42{,}9\,\%$ pour revenir au sommet.

### Couvrir le bêta avec des futures

Pour neutraliser l'exposition au marché d'un portefeuille d'actions de valeur $V$ et de bêta $\beta$,
on vend des futures sur indice :

$$
N_{contrats} = \frac{\beta \times V}{\text{niveau de l'indice} \times \text{multiplicateur}}
$$

Exemple : $V = 10$ M€, $\beta = 1{,}2$, indice à $4\,000$ points, multiplicateur $10$ € par point (un
contrat vaut $40\,000$ €) : $1{,}2 \times 10\,000\,000 / 40\,000 = 300$ contrats à vendre. Il reste le
risque **spécifique** (l'alpha recherché).

### Contribution au risque

Dans un portefeuille, le risque d'une ligne ne dépend pas que de sa volatilité, mais de sa corrélation
avec le reste. La **contribution** d'un actif au risque total vaut
$w_i \dfrac{(\Sigma w)_i}{\sigma_p}$ ; la somme des contributions donne $\sigma_p$. Les approches
*risk parity* cherchent à égaliser ces contributions plutôt que les montants investis.
""",
            "points_cles": [
                "Sortino : ne pénalise que la volatilité à la baisse.",
                "Ratio d'information = surperformance / tracking error.",
                "Après −30 %, il faut +42,9 % pour revenir.",
                "Couverture du bêta : N = β·V / (indice × multiplicateur).",
            ],
        },
    ],
    "quiz": [
        {"id": "risk-q01", "type": "nombre",
         "question": r"Volatilité journalière de $1\,\%$. Volatilité annualisée en % (252 jours, 1 décimale) ?",
         "reponse": 15.87, "tolerance": 0.15,
         "explication": r"$1\,\% \times \sqrt{252} \approx 1\,\% \times 15{,}87 = 15{,}9\,\%$."},
        {"id": "risk-q02", "type": "nombre",
         "question": r"Position de $1$ M€, volatilité journalière $2\,\%$, rendements gaussiens centrés. "
                     r"VaR 1 jour à $99\,\%$, en euros ?",
         "reponse": 46527, "tolerance": 150,
         "explication": r"$2{,}326 \times 0{,}02 \times 1\,000\,000 \approx 46\,500$ €."},
        {"id": "risk-q03", "type": "nombre",
         "question": r"VaR 1 jour de $50\,000$ €. VaR à 10 jours par la règle de la racine du temps, en euros ?",
         "reponse": 158114, "tolerance": 200,
         "explication": r"$50\,000 \times \sqrt{10} \approx 158\,100$ €."},
        {"id": "risk-q04", "type": "nombre",
         "question": "VaR à 99 % backtestée sur 250 jours : combien d'exceptions attend-on en moyenne ?",
         "reponse": 2.5, "tolerance": 0.001,
         "explication": r"$250 \times 1\,\% = 2{,}5$."},
        {"id": "risk-q05", "type": "qcm",
         "question": "Un modèle de VaR 99 % a 7 exceptions sur un an. Dans quelle zone de Bâle se trouve-t-il ?",
         "choix": ["Verte", "Orange", "Rouge", "Aucune, c'est le nombre attendu"],
         "reponse": 1,
         "explication": "Orange de 5 à 9 exceptions : le modèle est suspect et la banque est pénalisée."},
        {"id": "risk-q06", "type": "qcm",
         "question": "Que mesure l'Expected Shortfall que la VaR ne mesure pas ?",
         "choix": ["La probabilité de perte", "La perte moyenne au-delà de la VaR",
                   "La volatilité implicite", "Le gain maximal"],
         "reponse": 1,
         "explication": "L'ES regarde la queue de distribution, alors que la VaR n'en donne que le seuil."},
        {"id": "risk-q07", "type": "qcm",
         "question": "Laquelle de ces mesures est toujours sous-additive ?",
         "choix": ["La VaR historique", "La VaR paramétrique", "L'Expected Shortfall", "Aucune"],
         "reponse": 2,
         "explication": "L'ES est une mesure de risque cohérente ; la VaR peut ne pas récompenser la diversification."},
        {"id": "risk-q08", "type": "nombre",
         "question": r"Deux actifs de volatilité $20\,\%$ chacun, pondérés 50/50, corrélation nulle. "
                     r"Volatilité du portefeuille en % (2 décimales) ?",
         "reponse": 14.14, "tolerance": 0.05,
         "explication": r"$\sigma_p^2 = 2 \times 0{,}25 \times 0{,}04 = 0{,}02$, donc $\sigma_p = \sqrt{0{,}02} \approx 14{,}14\,\%$."},
        {"id": "risk-q09", "type": "nombre",
         "question": r"EWMA avec $\lambda = 0{,}94$ : volatilité d'hier $1\,\%$, rendement d'hier $2\,\%$. "
                     r"Volatilité d'aujourd'hui en % (2 décimales) ?",
         "reponse": 1.09, "tolerance": 0.01,
         "explication": r"$\sigma^2 = 0{,}94 \times 0{,}0001 + 0{,}06 \times 0{,}0004 = 0{,}000118$, "
                        r"soit $\sigma \approx 1{,}09\,\%$."},
        {"id": "risk-q10", "type": "nombre",
         "question": r"GARCH(1,1) avec $\omega = 0{,}000002$, $\alpha = 0{,}08$, $\beta = 0{,}90$. "
                     r"Volatilité journalière de long terme en % ?",
         "reponse": 1, "tolerance": 0.01,
         "explication": r"$\sigma^2_{LT} = 0{,}000002 / (1 - 0{,}98) = 0{,}0001$, donc $\sigma_{LT} = 1\,\%$."},
        {"id": "risk-q11", "type": "qcm",
         "question": "Pourquoi une VaR calculée seulement avec le delta est-elle dangereuse pour un vendeur d'options ?",
         "choix": ["Parce que le delta est toujours nul",
                   "Parce qu'il est short gamma : il perd plus que prévu lors des grands mouvements, dans les deux sens",
                   "Parce que la VaR ne s'applique pas aux dérivés",
                   "Parce que le theta est positif"],
         "reponse": 1,
         "explication": r"Le terme $\tfrac12 \Gamma (\Delta S)^2$ est négatif pour un short gamma et grossit avec le mouvement."},
        {"id": "risk-q12", "type": "nombre",
         "question": r"Exposition moyenne $2$ M€ pendant 5 ans, LGD $60\,\%$, probabilité de défaut $1\,\%$ par an, "
                     r"actualisation négligée. CVA approximative en euros ?",
         "reponse": 60000, "tolerance": 100,
         "explication": r"$0{,}6 \times 2\,000\,000 \times 5 \times 1\,\% = 60\,000$ €."},
        {"id": "risk-q13", "type": "nombre",
         "question": r"Position de $10$ M€, fourchette bid-ask de $0{,}4\,\%$. Coût de liquidation approximatif en euros ?",
         "reponse": 20000, "tolerance": 1,
         "explication": r"Moitié de la fourchette : $0{,}2\,\% \times 10$ M€ $= 20\,000$ €."},
        {"id": "risk-q14", "type": "nombre",
         "question": r"Valeur du portefeuille : $100 \to 130 \to 91 \to 120$. Maximum drawdown en % ?",
         "reponse": -30, "tolerance": 0.05,
         "explication": r"$91 / 130 - 1 = -30\,\%$."},
        {"id": "risk-q15", "type": "nombre",
         "question": r"Portefeuille $9\,\%$, indice $7\,\%$, tracking error $4\,\%$. Ratio d'information ?",
         "reponse": 0.5, "tolerance": 0.001,
         "explication": r"$(9 - 7) / 4 = 0{,}5$."},
        {"id": "risk-q16", "type": "nombre",
         "question": r"Portefeuille de $10$ M€, bêta $1{,}2$. Future sur indice à $4\,000$ points, $10$ € par point. "
                     r"Combien de contrats vendre pour neutraliser le bêta ?",
         "reponse": 300, "tolerance": 0.5,
         "explication": r"$1{,}2 \times 10\,000\,000 / 40\,000 = 300$."},
        {"id": "risk-q17", "type": "qcm",
         "question": "En quoi le ratio de Sortino diffère-t-il du ratio de Sharpe ?",
         "choix": ["Il utilise le rendement de l'indice", "Il ne pénalise que la volatilité des rendements négatifs",
                   "Il ignore le taux sans risque", "Il utilise la VaR au dénominateur"],
         "reponse": 1,
         "explication": "La volatilité à la hausse n'est pas un risque pour l'investisseur : Sortino l'exclut."},
        {"id": "risk-q18", "type": "qcm",
         "question": "Qu'est-ce que le wrong-way risk ?",
         "choix": ["Une erreur de saisie d'un trader", "Une exposition qui augmente quand la contrepartie devient plus fragile",
                   "Un modèle de VaR mal calibré", "Le risque de taux d'une obligation callable"],
         "reponse": 1,
         "explication": "Exposition et probabilité de défaut sont corrélées positivement : le pire scénario cumule les deux."},
        {"id": "risk-q19", "type": "qcm",
         "question": "Quelle leçon tirer de l'abandon du plancher du franc suisse en janvier 2015 ?",
         "choix": ["La VaR est toujours conservatrice", "Le gap risk : un prix peut sauter sans que les ordres stop soient exécutés au niveau prévu",
                   "Les devises refuges baissent en crise", "Les options de change sont inutiles"],
         "reponse": 1,
         "explication": "Le cours a sauté de plusieurs figures en quelques minutes : les protections par stop-loss n'ont pas fonctionné."},
        {"id": "risk-q20", "type": "qcm",
         "question": "Qu'ont combiné les difficultés de Silicon Valley Bank en mars 2023 ?",
         "choix": ["Un risque de change et un risque de matières premières",
                   "Des pertes de taux sur un portefeuille obligataire et un retrait massif des dépôts",
                   "Une fraude comptable", "Un défaut sur des CDS"],
         "reponse": 1,
         "explication": "Risque de taux (duration) plus risque de liquidité de financement."},
    ],
    "flashcards": [
        {"id": "risk-f01", "recto": "Annualiser une volatilité journalière",
         "verso": r"$\sigma_{an} = \sigma_{jour} \sqrt{252}$"},
        {"id": "risk-f02", "recto": "Formule EWMA",
         "verso": r"$\sigma_t^2 = \lambda \sigma_{t-1}^2 + (1-\lambda) r_{t-1}^2$, $\lambda \approx 0{,}94$"},
        {"id": "risk-f03", "recto": "Variance de long terme d'un GARCH(1,1)",
         "verso": r"$\omega / (1 - \alpha - \beta)$"},
        {"id": "risk-f04", "recto": "VaR paramétrique gaussienne",
         "verso": r"$VaR_\alpha = z_\alpha\, \sigma\, V$ avec $z_{95} \approx 1{,}645$, $z_{99} \approx 2{,}326$"},
        {"id": "risk-f05", "recto": "Définition de l'Expected Shortfall",
         "verso": r"$ES_\alpha = \mathbb{E}[L \mid L \ge VaR_\alpha]$ : perte moyenne au-delà de la VaR."},
        {"id": "risk-f06", "recto": "Zones de backtesting de Bâle (VaR 99 %, 250 jours)",
         "verso": "Vert : 0 à 4 exceptions ; orange : 5 à 9 ; rouge : 10 ou plus."},
        {"id": "risk-f07", "recto": "Approximation delta-gamma du P&L",
         "verso": r"$\Delta V \approx \Delta\,\Delta S + \tfrac12 \Gamma (\Delta S)^2$"},
        {"id": "risk-f08", "recto": "Volatilité d'un portefeuille de deux actifs",
         "verso": r"$\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2 w_1 w_2 \rho \sigma_1 \sigma_2$"},
        {"id": "risk-f09", "recto": "CVA", "verso": r"Prix du risque de défaut de la contrepartie : $\approx LGD \times \sum EE \times PD \times DF$."},
        {"id": "risk-f10", "recto": "Marge de variation / marge initiale", "verso": "Variation : compense chaque jour la valeur de marché. Initiale : couvre le risque pendant le remplacement après un défaut."},
        {"id": "risk-f11", "recto": "Wrong-way risk", "verso": "L'exposition augmente quand la contrepartie se fragilise."},
        {"id": "risk-f12", "recto": "Gap risk", "verso": "Le prix saute sans passer par les niveaux intermédiaires : stops et couvertures dynamiques échouent."},
        {"id": "risk-f13", "recto": "Ratio d'information", "verso": r"$(R_p - R_b) / \text{tracking error}$"},
        {"id": "risk-f14", "recto": "Maximum drawdown", "verso": "Plus forte baisse entre un sommet et le creux suivant. Après −30 %, il faut +42,9 % pour revenir."},
        {"id": "risk-f15", "recto": "Nombre de futures pour couvrir le bêta", "verso": r"$\beta V / (\text{indice} \times \text{multiplicateur})$"},
        {"id": "risk-f16", "recto": "Leçons des crises", "verso": "Queues épaisses, corrélations qui montent, liquidité qui disparaît, levier fatal."},
    ],
}
