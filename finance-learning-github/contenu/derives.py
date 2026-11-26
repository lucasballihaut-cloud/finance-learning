"""Module : Produits dérivés (Derivatives) — vue d'ensemble, pricing, futures, swaps, risques et cas pratiques."""

MODULE = {
    "id": "derives",
    "titre": "Produits dérivés (Derivatives)",
    "icone": "🔀",
    "statut": "complet",
    "resume": "Les quatre familles de dérivés, l'absence d'arbitrage et le cost of carry, futures et marges, "
              "couverture optimale, swaps (IRS, cross-currency, OIS, CDS), régulation, xVA et cas de couverture.",
    "chapitres": [
        # ------------------------------------------------------------------ 1
        {
            "id": "der-c1",
            "titre": "1. Panorama des produits dérivés",
            "contenu": r"""
Un **dérivé** est un contrat dont la valeur **dépend** (dérive) du prix d'un autre actif, le
**sous-jacent** : action, indice, taux, devise, matière première, crédit, volatilité…

### Les quatre grandes familles

| Famille | Principe | Profil | Exemples |
|---|---|---|---|
| **Forwards et futures** | Engagement ferme d'acheter / vendre à terme à un prix fixé | **Linéaire** | Future sur indice, forward de change |
| **Swaps** | Échange de flux futurs | Linéaire | Swap de taux, cross-currency swap, TRS |
| **Options** | **Droit** (et non obligation) d'acheter / vendre | **Non linéaire** (asymétrique) | Calls, puts, options exotiques |
| **Dérivés de crédit** | Transfert du risque de défaut | Non linéaire (saut au défaut) | CDS, indices iTraxx / CDX |

**Engagement ferme vs optionnel** : un forward oblige les deux parties ; une option ne contraint que le
vendeur. C'est pourquoi une option se paie (une **prime**), alors qu'un forward ou un swap ne coûte rien à
la signature (s'il est conclu au prix de marché).

### Organisés ou de gré à gré

- **Marchés organisés** (bourses comme Eurex, CME, Euronext) : contrats standardisés, chambre de
  compensation, appels de marge quotidiens.
- **De gré à gré (OTC)** : contrats négociés entre deux parties, sur mesure. La grande majorité du
  **notionnel** mondial est OTC, et ce sont surtout des **dérivés de taux**.

Attention : le **notionnel** (montant de référence, souvent énorme) ne mesure pas le risque. La valeur de
marché d'un swap est une petite fraction de son notionnel.

### Les trois usages

1. **Couverture** (*hedging*) : réduire un risque existant (un exportateur vend des dollars à terme).
2. **Spéculation** : prendre une position avec **levier**, car un dérivé demande peu de capital.
3. **Arbitrage** : profiter d'un écart de prix entre un dérivé et sa réplication.

### Qui utilise les dérivés ?

Entreprises (change, taux, matières premières), banques (gestion actif-passif, tenue de marché),
assureurs et fonds de pension (couverture de taux longs, LDI), gérants (couverture, exposition rapide),
hedge funds (spéculation, arbitrage), États et banques centrales (gestion de la dette, du change).
""",
            "points_cles": [
                "Quatre familles : forwards/futures, swaps, options, dérivés de crédit.",
                "Ferme (linéaire, gratuit à l'origine) vs optionnel (asymétrique, prime).",
                "Notionnel ≠ risque ; l'essentiel du notionnel est OTC et en taux.",
                "Usages : couverture, spéculation, arbitrage.",
            ],
        },
        # ------------------------------------------------------------------ 2
        {
            "id": "der-c2",
            "titre": "2. Les principes de pricing",
            "contenu": r"""
### Absence d'opportunité d'arbitrage (AOA)

Deux stratégies qui donnent les **mêmes flux dans tous les scénarios** doivent avoir le **même prix
aujourd'hui**. C'est le socle de toute la valorisation des dérivés.

### Réplication

On valorise un dérivé en construisant un **portefeuille d'actifs simples** (sous-jacent, emprunt,
placement) qui reproduit exactement ses flux. Exemples :
- un forward se réplique en achetant le sous-jacent avec de l'argent emprunté (cash-and-carry) ;
- un swap de taux se réplique par une obligation à taux fixe et une obligation à taux variable ;
- une option se réplique **dynamiquement** avec le sous-jacent (delta hedging).

### Probabilité risque-neutre

Puisque le dérivé est répliqué, les préférences des investisseurs ne comptent pas : on peut le
valoriser **comme si** tout le monde était neutre au risque, c'est-à-dire en actualisant au taux sans
risque l'espérance de ses flux sous une probabilité $\mathbb{Q}$ où chaque actif rapporte en moyenne le
taux sans risque :

$$
V_0 = e^{-rT}\, \mathbb{E}^{\mathbb{Q}}\left[\text{payoff}\right]
$$

### Le coût de portage (cost of carry)

Le prix à terme vaut le spot augmenté de ce que coûte, et diminué de ce que rapporte, le fait de
détenir l'actif jusqu'à l'échéance :

| Sous-jacent | Prix forward | Ce qui entre dans le portage |
|---|---|---|
| Action / indice | $S\, e^{(r - q)T}$ | Financement $r$, dividendes $q$ |
| Devise | $S\, e^{(r_{cot} - r_{base})T}$ | Différentiel de taux |
| Matière première | $S\, e^{(r + u - y)T}$ | Financement, stockage $u$, *convenience yield* $y$ |
| Obligation | (prix + coupon couru) − VA des coupons, capitalisés au taux $r$ | Financement contre coupons |

Un **forward** valait zéro à sa signature. Plus tard, sa valeur pour l'acheteur devient :

$$
V_t = (F_t - K)\, e^{-r(T - t)}
$$

où $K$ est le prix fixé au départ et $F_t$ le prix forward actuel.

### Forward ou future : le même prix ?

Quand les taux sont déterministes, oui. Avec des taux aléatoires corrélés au sous-jacent, le
règlement quotidien des futures crée un petit écart : c'est l'**ajustement de convexité**, important
pour les futures de taux à long terme.
""",
            "points_cles": [
                "AOA : mêmes flux ⇒ même prix.",
                "Réplication statique (forward, swap) ou dynamique (option).",
                "Valorisation risque-neutre : V = e^(−rT)·E^Q[payoff].",
                "Forward = spot + coût de portage ; valeur ultérieure (F_t − K)e^(−r(T−t)).",
            ],
        },
        # ------------------------------------------------------------------ 3
        {
            "id": "der-c3",
            "titre": "3. Les futures en pratique : marges et couverture",
            "contenu": r"""
### Le mécanisme des marges

À l'ouverture d'une position, on dépose une **marge initiale**. Chaque jour, la chambre de compensation
crédite ou débite le compte du gain ou de la perte (**marge de variation**). Si le compte passe sous la
**marge de maintenance**, on reçoit un **appel de marge** pour revenir à la marge initiale.

Exemple : future sur indice à $5\,000$ points, multiplicateur $10$ € par point, soit un notionnel de
$50\,000$ €. Marge initiale $3\,000$ €, maintenance $2\,500$ €.

| Jour | Indice | Gain / perte | Solde du compte | Action |
|---|---|---|---|---|
| 0 | 5 000 | — | 3 000 € | Ouverture |
| 1 | 4 960 | −400 € | 2 600 € | Rien (au-dessus de 2 500) |
| 2 | 4 900 | −600 € | 2 000 € | Appel de marge de **1 000 €** pour revenir à 3 000 € |

Le **levier** est important : $3\,000$ € de marge exposent à $50\,000$ € de notionnel. Une baisse de
$6\,\%$ de l'indice fait perdre l'équivalent de toute la marge initiale.

### Couvrir avec des futures : le ratio optimal

Quand le future ne porte pas exactement sur l'actif à couvrir (par exemple couvrir du kérosène avec un
future sur le pétrole), il reste un **risque de base**. Le **ratio de couverture de variance minimale** :

$$
h^* = \rho\, \frac{\sigma_S}{\sigma_F}
\qquad
N^* = h^* \times \frac{\text{quantité à couvrir}}{\text{taille d'un contrat}}
$$

avec $\rho$ la corrélation entre les variations du prix à couvrir ($\sigma_S$) et du future ($\sigma_F$).

Exemple : une compagnie aérienne achètera $2$ millions de gallons de kérosène ; $\rho = 0{,}9$,
$\sigma_S = 3\,\%$, $\sigma_F = 4\,\%$ ; contrat de $42\,000$ gallons :
$h^* = 0{,}9 \times 3/4 = 0{,}675$, $N^* = 0{,}675 \times 2\,000\,000 / 42\,000 \approx 32$ contrats.

### Couvrir un portefeuille d'actions

Pour ramener le bêta d'un portefeuille de $\beta$ à $\beta^*$ :
$N = (\beta^* - \beta)\, \dfrac{V}{\text{valeur d'un contrat}}$ (négatif = vendre des futures).

### Le roulement

Les futures ont une échéance : pour garder une couverture longue, on **roule** (on ferme le contrat qui
expire et on ouvre le suivant), en payant ou en encaissant l'écart entre les deux échéances.
""",
            "points_cles": [
                "Marge initiale, marge de variation quotidienne, appel de marge vers l'initiale.",
                "Levier : peu de marge pour un gros notionnel.",
                "h* = ρ·σ_S/σ_F ; N* = h* × quantité / taille du contrat.",
                "Couverture imparfaite : risque de base.",
            ],
        },
        # ------------------------------------------------------------------ 4
        {
            "id": "der-c4",
            "titre": "4. Les swaps : taux, devises, crédit, performance",
            "contenu": r"""
### Valoriser un swap de taux après sa signature

Un swap **receveur du fixe** vaut : (valeur de la jambe fixe) − (valeur de la jambe variable).
- La **jambe fixe** se valorise comme une obligation à taux fixe (coupons + nominal fictif).
- La **jambe variable**, juste après une date de fixation, vaut le **pair** (le nominal), car ses coupons
  seront toujours au taux de marché.

Exemple : swap de $100$ M€, on reçoit $4\,\%$ par an, 3 ans restants, juste après un fixing. Taux
zéro-coupon de marché à $3\,\%$ sur toutes les maturités :

$$
V_{fixe} = 4\left(\frac{1}{1{,}03} + \frac{1}{1{,}03^2} + \frac{1}{1{,}03^3}\right) + \frac{100}{1{,}03^3} \approx 102{,}83
$$

La jambe variable vaut $100$ : le swap vaut environ **$+2{,}83$ M€** pour le receveur du fixe (il reçoit
$4\,\%$ alors que le marché n'offre plus que $3\,\%$).

### Les autres swaps à connaître

| Swap | Ce qu'on échange | Usage |
|---|---|---|
| **OIS** | Fixe contre taux au jour le jour composé (€STR, SOFR) | Référence de l'actualisation sans risque des dérivés collatéralisés |
| **Basis swap** | Deux taux variables (par exemple Euribor 3 mois contre €STR) | Gérer l'écart entre indices de taux |
| **Cross-currency swap** | Intérêts **et nominal** dans deux devises, échangés au début et à la fin | Un émetteur lève des dollars et les transforme en euros |
| **Total return swap** | Performance totale d'un actif contre un taux de financement | Exposition sans détenir l'actif, financement |
| **CDS** | Prime périodique contre indemnisation en cas de défaut | Couvrir ou prendre un risque de crédit |
| **Variance swap** | Variance réalisée contre variance fixée | Exposition pure à la volatilité |
| **Inflation swap** | Fixe contre inflation réalisée | Couvrir des engagements indexés (retraites) |

### Le cross-currency swap en exemple

Une entreprise européenne émet $110$ M\$ d'obligations à taux fixe en dollars. Avec un cross-currency
swap au change de $1{,}10$ : elle livre les $110$ M\$ à la banque et reçoit $100$ M€ au départ ; pendant
la vie du swap, la banque lui verse les coupons en dollars (qui servent à payer les investisseurs) et elle
paie des coupons en euros ; à l'échéance, elle rend $100$ M€ et récupère $110$ M\$ pour rembourser
l'obligation. Résultat : une dette synthétique **en euros**, sans risque de change.
""",
            "points_cles": [
                "Swap receveur = jambe fixe (obligation) − jambe variable (≈ pair au fixing).",
                "OIS : référence d'actualisation des dérivés collatéralisés.",
                "Cross-currency swap : nominaux échangés au début et à la fin.",
                "TRS, CDS, variance swap, inflation swap : un swap par risque.",
            ],
        },
        # ------------------------------------------------------------------ 5
        {
            "id": "der-c5",
            "titre": "5. Les options dans la famille des dérivés",
            "contenu": r"""
Les options ont leur propre module complet (**🧮 Options et Black-Scholes**) et les produits qui en
découlent aussi (**🧩 Produits structurés**). Ce chapitre fait le lien et donne la carte d'ensemble.

### Ce qui distingue une option

- **Asymétrie** : l'acheteur a un droit, sa perte est limitée à la prime.
- **Convexité** : le gain accélère quand le marché va dans le bon sens (gamma positif).
- **Exposition à la volatilité** : c'est le seul produit de la famille qui donne une position directe sur
  la volatilité (vega).

### La carte des options

| Famille | Exemples | Où on la retrouve |
|---|---|---|
| Vanilles | Calls, puts européens et américains | Couverture, stratégies (spreads, straddles…) |
| Dépendantes du chemin | Barrières, asiatiques, lookback | Produits structurés, matières premières |
| Digitales | Cash-or-nothing, range accrual | Coupons d'autocalls |
| Multi-sous-jacents | Worst-of, best-of, panier, spread options | Autocalls worst-of, énergie (spark spread) |
| Sur taux | Caps, floors, swaptions | Couverture de dette, assurance-vie |
| Sur volatilité | Options sur VIX, variance swaps | Trading de volatilité |

### Options listées ou OTC

Les options standard sur indices et grandes actions se traitent en bourse ; les options sur taux, change
et les exotiques se traitent surtout de gré à gré.

### Les mêmes grecques partout

Delta, gamma, vega, theta et rho s'appliquent à toutes les options. Pour une couverture, on raisonne
toujours en **sensibilités agrégées** du portefeuille, quelle que soit la famille de dérivé.
""",
            "points_cles": [
                "Option = asymétrie + convexité + exposition à la volatilité.",
                "Vanilles, dépendantes du chemin, digitales, multi-sous-jacents, taux, volatilité.",
                "Détails : modules Options et Produits structurés.",
            ],
        },
        # ------------------------------------------------------------------ 6
        {
            "id": "der-c6",
            "titre": "6. Risques, régulation et xVA",
            "contenu": r"""
### Les risques d'un portefeuille de dérivés

- **Marché** : les sensibilités (delta, vega, DV01…).
- **Contrepartie** : sur un dérivé OTC, la contrepartie peut faire défaut alors qu'elle nous doit de l'argent.
- **Liquidité et financement** : appels de marge à payer, parfois brutalement.
- **Modèle** : un modèle mal adapté ou mal calibré donne un mauvais prix et une mauvaise couverture.
- **Opérationnel** : erreurs de saisie, de règlement, de confirmation.

### La réforme après 2008

Lors du G20 de Pittsburgh (2009), les grands pays se sont engagés à :
1. faire **compenser** les dérivés OTC standardisés par des **chambres de compensation centrales** (CCP) ;
2. **déclarer** toutes les transactions à des référentiels centraux (*trade repositories*) ;
3. exiger plus de **capital** et des **marges** sur les dérivés non compensés.

Mise en œuvre : **Dodd-Frank** aux États-Unis (2010), **EMIR** en Europe (2012), puis les règles de marges
initiales sur les dérivés non compensés (*UMR*), déployées progressivement de 2016 à 2022.

### Le CSA et le collatéral

Un **CSA** (annexe au contrat-cadre ISDA) organise l'échange de **collatéral** entre deux banques : la
partie perdante verse chaque jour la variation de valeur. Le collatéral rémunéré au taux au jour le jour
explique pourquoi les dérivés collatéralisés s'actualisent avec la courbe **OIS**.

### Les xVA : les ajustements de valorisation

Le prix « sans risque » d'un dérivé est corrigé par plusieurs ajustements :

| Ajustement | Ce qu'il mesure |
|---|---|
| **CVA** | Coût du risque de défaut de la **contrepartie** |
| **DVA** | Bénéfice comptable lié à **notre propre** risque de défaut |
| **FVA** | Coût de **financement** des positions non collatéralisées |
| **MVA** | Coût de financement de la **marge initiale** |
| **KVA** | Coût du **capital** réglementaire immobilisé |

Les desks xVA des banques gèrent ces risques de façon centralisée. Ce sont des métiers très demandés pour
les profils quantitatifs.
""",
            "points_cles": [
                "G20 2009 : compensation centrale, déclaration, marges et capital.",
                "EMIR (Europe), Dodd-Frank (États-Unis).",
                "CSA : collatéral quotidien ⇒ actualisation OIS.",
                "xVA : CVA, DVA, FVA, MVA, KVA.",
            ],
        },
        # ------------------------------------------------------------------ 7
        {
            "id": "der-c7",
            "titre": "7. Cas pratiques : quel dérivé pour quel besoin ?",
            "contenu": r"""
La question d'entretien type : « Un client a tel risque, que lui proposez-vous ? » Méthode : identifier
le **risque**, choisir entre **ferme** (on fige le prix) et **optionnel** (on se protège en gardant le
potentiel, contre une prime), puis chiffrer les scénarios.

### 1. Une entreprise endettée à taux variable

Dette de $50$ M€ à €STR + $1\,\%$. Elle craint une hausse des taux.
- **Ferme** : swap **payeur du fixe** à, par exemple, $2{,}5\,\%$. Coût total figé à $3{,}5\,\%$.
- **Optionnel** : achat d'un **cap** à $3\,\%$ : coût plafonné à $4\,\%$ (plus la prime), mais elle profite
  d'une baisse des taux.
- **Intermédiaire** : **collar** (achat du cap financé par la vente d'un floor).

| Taux €STR | Sans couverture | Avec swap | Avec cap 3 % (hors prime) |
|---|---|---|---|
| 1 % | 2 % | 3,5 % | 2 % |
| 3 % | 4 % | 3,5 % | 4 % |
| 5 % | 6 % | 3,5 % | 4 % |

### 2. Une compagnie aérienne et le prix du carburant

- **Ferme** : achat de futures ou de swaps sur le pétrole (prix figé, avec risque de base).
- **Optionnel** : achat de calls (plafond de prix, prime à payer).
- **Collar** : achat d'un call à $90$ \$ financé par la vente d'un put à $70$ \$ : le prix payé reste entre
  $70$ et $90$ \$ le baril, pour une prime nette proche de zéro.

### 3. Un exportateur qui recevra des dollars

- **Forward** : vente des dollars à terme, montant en euros figé.
- **Option** : achat d'un put USD / call EUR : protection contre la baisse du dollar, gain conservé s'il monte.

### 4. Un gérant qui veut protéger un portefeuille d'actions

- **Puts sur indice** (assurance), ou **put spread** pour réduire la prime (protection seulement entre deux niveaux).
- **Vente de futures** si l'objectif est de réduire l'exposition rapidement, sans vendre les actions.
- **Collar** sur indice : protection financée par l'abandon de la hausse au-delà d'un niveau.

### 5. Un assureur ou un fonds de pension avec des engagements longs

Engagements de retraite à $30$ ans, sensibles à la baisse des taux : **swaps receveurs du fixe** longs ou
**swaptions receveuses** pour augmenter la duration de l'actif (stratégie LDI) ; swaps d'inflation si les
engagements sont indexés.

### 6. Un investisseur qui veut s'exposer sans acheter

- **Futures** sur indice (levier, liquidité).
- **TRS** sur une action ou un panier (pas de capital immobilisé).
- **Call** si l'on veut limiter la perte à la prime.

### Les trois questions à toujours poser

1. Le client veut-il **figer** le prix ou garder le **potentiel** favorable ?
2. Peut-il payer une **prime** ? Accepte-t-il d'abandonner une partie du gain pour la financer ?
3. Quelle **comptabilité** et quels **appels de marge** peut-il supporter ?
""",
            "points_cles": [
                "Ferme : prix figé, gratuit à l'origine. Optionnel : protection + potentiel, contre une prime.",
                "Dette variable : swap payeur, cap ou collar.",
                "Collar : protection financée en abandonnant une partie du gain.",
                "LDI : swaps receveurs longs pour couvrir des engagements de retraite.",
            ],
        },
    ],
    "quiz": [
        {"id": "der-q01", "type": "qcm",
         "question": "Lequel de ces produits est non linéaire ?",
         "choix": ["Un future sur indice", "Un swap de taux", "Une option d'achat", "Un forward de change"],
         "reponse": 2,
         "explication": "Le payoff d'une option est asymétrique ; forwards, futures et swaps sont linéaires."},
        {"id": "der-q02", "type": "qcm",
         "question": "Pourquoi un forward conclu au prix de marché ne coûte-t-il rien à la signature, alors qu'une option se paie ?",
         "choix": ["Parce que le forward est toujours listé", "Le forward engage les deux parties de façon symétrique ; l'option donne un droit à une seule",
                   "Parce que l'option a une maturité plus longue", "C'est une convention comptable"],
         "reponse": 1,
         "explication": "Le droit asymétrique de l'option a une valeur : la prime."},
        {"id": "der-q03", "type": "nombre",
         "question": r"Pétrole spot $80$, taux $4\,\%$, coût de stockage $2\,\%$, convenience yield $1\,\%$ (continus), 1 an. Prix forward ? (2 décimales)",
         "reponse": 84.10, "tolerance": 0.02,
         "explication": r"$80\, e^{(0{,}04 + 0{,}02 - 0{,}01)} = 80\, e^{0{,}05} \approx 84{,}10$."},
        {"id": "der-q04", "type": "nombre",
         "question": r"Vous avez acheté un forward au prix $K = 100$. Aujourd'hui le forward de même échéance vaut $106$, "
                     r"taux nul. Valeur de votre position ?",
         "reponse": 6, "tolerance": 0.001,
         "explication": r"$(F_t - K)\,e^{-r(T-t)} = 106 - 100 = 6$."},
        {"id": "der-q05", "type": "nombre",
         "question": r"Future : marge initiale $3\,000$ €, maintenance $2\,500$ €. Après pertes, le compte est à $2\,000$ €. "
                     r"Montant de l'appel de marge ?",
         "reponse": 1000, "tolerance": 0.001,
         "explication": "On revient à la marge initiale : 3 000 − 2 000 = 1 000 €."},
        {"id": "der-q06", "type": "nombre",
         "question": r"Ratio de couverture optimal : $\rho = 0{,}9$, $\sigma_S = 3\,\%$, $\sigma_F = 4\,\%$. Valeur de $h^*$ ? (3 décimales)",
         "reponse": 0.675, "tolerance": 0.001,
         "explication": r"$0{,}9 \times 3 / 4 = 0{,}675$."},
        {"id": "der-q07", "type": "nombre",
         "question": r"Avec $h^* = 0{,}675$, à couvrir $2\,000\,000$ gallons, contrat de $42\,000$ gallons. Nombre de contrats (arrondi) ?",
         "reponse": 32, "tolerance": 0.5,
         "explication": r"$0{,}675 \times 2\,000\,000 / 42\,000 \approx 32{,}1$."},
        {"id": "der-q08", "type": "nombre",
         "question": r"Swap de $100$ M€, vous recevez $4\,\%$ fixe, 3 ans restants, juste après un fixing ; taux zéro-coupon "
                     r"à $3\,\%$ partout (annuel). Valeur du swap en M€ (2 décimales) ?",
         "reponse": 2.83, "tolerance": 0.02,
         "explication": r"Jambe fixe $\approx 102{,}83$, jambe variable $= 100$ : $+2{,}83$ M€."},
        {"id": "der-q09", "type": "qcm",
         "question": "Quelle particularité distingue un cross-currency swap d'un swap de taux classique ?",
         "choix": ["Il n'a pas de jambe fixe", "Les nominaux, dans deux devises, sont échangés au début et à la fin",
                   "Il est toujours listé", "Il ne dépend pas des taux"],
         "reponse": 1,
         "explication": "Il transforme une dette dans une devise en dette synthétique dans une autre."},
        {"id": "der-q10", "type": "qcm",
         "question": "Pourquoi actualise-t-on les dérivés collatéralisés avec la courbe OIS ?",
         "choix": ["Par convention historique", "Parce que le collatéral est rémunéré au taux au jour le jour",
                   "Parce que l'OIS est le taux le plus élevé", "Pour réduire la CVA"],
         "reponse": 1,
         "explication": "Le coût de financement d'une position collatéralisée est le taux servi sur le collatéral."},
        {"id": "der-q11", "type": "qcm",
         "question": "Que mesure la CVA ?",
         "choix": ["Le coût du capital réglementaire", "Le coût du risque de défaut de la contrepartie",
                   "Le coût de financement de la marge initiale", "Le risque de modèle"],
         "reponse": 1,
         "explication": "KVA = capital, MVA = marge initiale, FVA = financement."},
        {"id": "der-q12", "type": "qcm",
         "question": "Quel règlement européen impose la compensation centrale des dérivés OTC standardisés ?",
         "choix": ["MiFID", "EMIR", "Bâle III", "Solvabilité II"],
         "reponse": 1,
         "explication": "EMIR (2012) en Europe, Dodd-Frank (2010) aux États-Unis."},
        {"id": "der-q13", "type": "qcm",
         "question": "Une entreprise endettée à taux variable veut se protéger d'une hausse des taux tout en profitant d'une baisse. Que lui proposer ?",
         "choix": ["Un swap payeur du fixe", "L'achat d'un cap", "La vente d'un floor", "Un swap receveur du fixe"],
         "reponse": 1,
         "explication": "Le cap plafonne le taux payé contre une prime ; le swap fige le taux et supprime le gain d'une baisse."},
        {"id": "der-q14", "type": "nombre",
         "question": r"Dette à €STR $+ 1\,\%$, couverte par un swap payeur du fixe à $2{,}5\,\%$. Si l'€STR monte à $5\,\%$, "
                     r"quel est le coût total de la dette en % ?",
         "reponse": 3.5, "tolerance": 0.001,
         "explication": r"Le swap transforme €STR en $2{,}5\,\%$ : coût $2{,}5 + 1 = 3{,}5\,\%$ quel que soit l'€STR."},
        {"id": "der-q15", "type": "qcm",
         "question": "Une compagnie aérienne achète un call à 90 $ et vend un put à 70 $ sur le pétrole. Que se passe-t-il si le baril tombe à 50 $ ?",
         "choix": ["Elle paie 50 $", "Elle paie 70 $ : le put vendu l'oblige à acheter à ce niveau",
                   "Elle paie 90 $", "Elle ne paie rien"],
         "reponse": 1,
         "explication": "Le collar fixe une fourchette : plafond 90 $ (call acheté), plancher 70 $ (put vendu)."},
        {"id": "der-q16", "type": "qcm",
         "question": "Le notionnel d'un swap de taux mesure…",
         "choix": ["sa valeur de marché", "le montant de référence servant à calculer les flux, pas le risque",
                   "la perte maximale", "la marge à déposer"],
         "reponse": 1,
         "explication": "La valeur de marché d'un swap n'est qu'une petite fraction du notionnel."},
    ],
    "flashcards": [
        {"id": "der-f01", "recto": "Les quatre familles de dérivés", "verso": "Forwards/futures, swaps, options, dérivés de crédit."},
        {"id": "der-f02", "recto": "Les trois usages des dérivés", "verso": "Couverture, spéculation (levier), arbitrage."},
        {"id": "der-f03", "recto": "Valorisation risque-neutre", "verso": r"$V_0 = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[\text{payoff}]$"},
        {"id": "der-f04", "recto": "Forward sur matière première", "verso": r"$F = S\,e^{(r + u - y)T}$ (stockage $u$, convenience yield $y$)"},
        {"id": "der-f05", "recto": "Valeur d'un forward existant", "verso": r"$(F_t - K)\,e^{-r(T - t)}$ pour l'acheteur"},
        {"id": "der-f06", "recto": "Appel de marge", "verso": "Sous la marge de maintenance, on reconstitue la marge initiale."},
        {"id": "der-f07", "recto": "Ratio de couverture de variance minimale", "verso": r"$h^* = \rho\,\sigma_S / \sigma_F$"},
        {"id": "der-f08", "recto": "Valeur d'un swap receveur", "verso": "Jambe fixe (obligation) − jambe variable (≈ pair juste après un fixing)."},
        {"id": "der-f09", "recto": "Cross-currency swap", "verso": "Échange d'intérêts et de nominaux dans deux devises (au début et à la fin)."},
        {"id": "der-f10", "recto": "Réforme post-2008 (G20 2009)", "verso": "Compensation centrale, déclaration des transactions, marges et capital : EMIR, Dodd-Frank."},
        {"id": "der-f11", "recto": "Les xVA", "verso": "CVA (contrepartie), DVA (propre défaut), FVA (financement), MVA (marge initiale), KVA (capital)."},
        {"id": "der-f12", "recto": "Ferme ou optionnel ?", "verso": "Ferme : prix figé, gratuit à l'origine. Optionnel : protection + potentiel, contre une prime."},
    ],
}
