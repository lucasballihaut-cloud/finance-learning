"""Module : Taux et obligations."""

MODULE = {
    "id": "taux",
    "titre": "Taux et obligations",
    "icone": "🏦",
    "statut": "complet",
    "resume": "Actualisation, prix et rendement d'une obligation, duration, convexité, DV01, "
              "courbe des taux et taux forward.",
    "chapitres": [
        {
            "id": "taux-c1",
            "titre": "1. Valeur temps de l'argent",
            "contenu": r"""
Un euro aujourd'hui vaut plus qu'un euro demain : on peut le placer. La **valeur actuelle**
d'un flux $F$ reçu dans $T$ années, au taux $r$, vaut :

$$
VA = \frac{F}{(1 + r)^T} \quad \text{(composition annuelle)}
\qquad
VA = F\, e^{-rT} \quad \text{(composition continue)}
$$

Avec $m$ capitalisations par an : $VA = F / (1 + r/m)^{mT}$. Quand $m \to \infty$, on retrouve
la composition continue. Pour passer d'une convention à l'autre à rendement égal :
$1 + r_{a} = e^{r_c}$, soit $r_c = \ln(1 + r_a)$.

Un **zéro-coupon** est un titre qui ne paie qu'un seul flux (le nominal) à maturité. Son prix
est simplement la valeur actuelle de ce nominal : c'est la brique de base de toute la
valorisation de taux. Le facteur $DF(T) = 1/(1 + r_T)^T$ s'appelle le **facteur d'actualisation**.

**Ordre de grandeur utile** (règle de 72) : un placement à $r\,\%$ double en environ $72/r$ ans.
""",
            "points_cles": [
                "VA = F/(1 + r)^T ou F·e^(−rT).",
                "Un zéro-coupon = un seul flux à maturité.",
                "Conversion : r_continu = ln(1 + r_annuel).",
            ],
        },
        {
            "id": "taux-c2",
            "titre": "2. Prix et rendement d'une obligation",
            "contenu": r"""
Une obligation à taux fixe de nominal $N$, coupon annuel $c$ (en % du nominal) et maturité $n$
ans paie $cN$ chaque année puis $N$ à la fin. Son prix, actualisé au **taux de rendement
actuariel** $y$ (*yield to maturity*), vaut :

$$
P = \sum_{t=1}^{n} \frac{cN}{(1 + y)^t} + \frac{N}{(1 + y)^n}
$$

Le rendement $y$ est le taux unique qui égalise ce calcul et le prix de marché.

**Propriétés essentielles** :
- **prix et taux varient en sens inverse** : si $y$ monte, $P$ baisse ;
- si $c = y$, l'obligation cote **au pair** ($P = N$) ; si $c > y$ elle cote au-dessus du pair,
  si $c < y$ en dessous ;
- à l'approche de la maturité, le prix converge vers le nominal (effet « pull to par »).

**Prix pied de coupon et coupon couru.** Entre deux dates de coupon, le prix payé (*dirty price*)
contient la part du prochain coupon déjà « gagnée » par le vendeur. Les marchés cotent le
*clean price* = dirty price − coupon couru, pour éviter que la cotation saute à chaque
détachement de coupon.

**Spread de crédit.** Une obligation d'entreprise rapporte en général plus qu'un emprunt d'État
de même maturité : l'écart de rendement (le *spread*) rémunère le risque de défaut et la
moindre liquidité.
""",
            "points_cles": [
                "Taux ↑ ⇒ prix ↓.",
                "Coupon = rendement ⇒ prix au pair.",
                "Clean price = dirty price − coupon couru.",
            ],
        },
        {
            "id": "taux-c3",
            "titre": "3. Duration, convexité et DV01",
            "contenu": r"""
La **duration de Macaulay** est la maturité moyenne des flux, pondérée par leur valeur actuelle :

$$
D_{mac} = \frac{1}{P} \sum_{t=1}^{n} t \cdot \frac{CF_t}{(1+y)^t}
$$

Pour un zéro-coupon, $D_{mac} = n$. Pour une obligation à coupons, $D_{mac} < n$, et elle est
d'autant plus faible que le coupon est élevé (on récupère son argent plus tôt).

La **duration modifiée** mesure la sensibilité du prix au rendement :

$$
D_{mod} = \frac{D_{mac}}{1 + y}
\qquad
\frac{\Delta P}{P} \approx -D_{mod}\, \Delta y + \tfrac{1}{2}\, \mathcal{C}\, (\Delta y)^2
$$

où $\mathcal{C} = \frac{1}{P} \frac{\partial^2 P}{\partial y^2}$ est la **convexité**. Pour une
obligation classique elle est positive : le prix monte plus quand les taux baissent qu'il ne
baisse quand les taux montent. À duration égale, un investisseur préfère plus de convexité.

**DV01** (ou PV01) : variation de valeur d'une position pour une hausse de 1 point de base
(0,01 %) du rendement :

$$
DV01 \approx D_{mod} \times \text{Valeur de la position} \times 0{,}0001
$$

Exemple : position de valeur $10$ M€ et duration modifiée $6$ : $DV01 \approx 6\,000$ € par bp.
Les traders taux raisonnent en DV01 pour comparer et couvrir des positions de maturités différentes.
""",
            "points_cles": [
                "Zéro-coupon : duration = maturité.",
                "ΔP/P ≈ −D_mod · Δy (+ terme de convexité).",
                "DV01 = perte pour +1 bp, en euros.",
            ],
        },
        {
            "id": "taux-c4",
            "titre": "4. Courbe des taux et taux forward",
            "contenu": r"""
La **courbe des taux** relie la maturité au taux zéro-coupon. Formes typiques :
- **croissante** (normale) : les taux longs dépassent les taux courts, prime de terme ;
- **plate** ;
- **inversée** : taux courts au-dessus des taux longs, souvent quand le marché anticipe des
  baisses de taux directeurs (elle est surveillée comme signal avancé de ralentissement).

**Taux forward.** Placer 2 ans au taux $r_2$ doit rapporter autant que placer 1 an au taux $r_1$
puis 1 an au taux forward $f_{1,2}$ fixé aujourd'hui (sinon il y aurait un arbitrage) :

$$
(1 + r_2)^2 = (1 + r_1)(1 + f_{1,2})
\qquad \Rightarrow \qquad
f_{1,2} = \frac{(1 + r_2)^2}{1 + r_1} - 1
$$

En continu : $f_{T_1, T_2} = \dfrac{r_2 T_2 - r_1 T_1}{T_2 - T_1}$.

Quand la courbe est croissante, les forwards sont au-dessus des taux zéro-coupon.

**Mouvements de courbe** utilisés par les desks : *parallel shift* (toute la courbe bouge
du même nombre de bp), *steepening* (la pente augmente), *flattening* (elle diminue). Une
position « 2s10s steepener » gagne si l'écart entre taux 10 ans et taux 2 ans s'élargit.
""",
            "points_cles": [
                "Forward implicite : (1 + r₂)² = (1 + r₁)(1 + f₁,₂).",
                "Courbe inversée : courts > longs.",
                "Steepener = pari sur une pente qui augmente.",
            ],
        },
        {
            "id": "taux-c5",
            "titre": "5. Les obligations en pratique : types, cotation, scénarios",
            "contenu": r"""
### Les grandes familles

| Type | Caractéristique | Point clé |
|---|---|---|
| **Emprunt d'État** (OAT, Bund, BTP, Treasury) | Référence sans risque (ou presque) de chaque pays | Sert de base au calcul des spreads |
| **Zéro-coupon** | Un seul flux à maturité | Duration = maturité |
| **Taux variable (FRN)** | Coupon indexé sur un taux court (€STR, Euribor) + marge | Duration très faible : environ le temps jusqu'au prochain fixing |
| **Indexée sur l'inflation** (OATi, OAT€i, TIPS) | Nominal revalorisé avec l'inflation | Rendement réel ; sert à mesurer le breakeven |
| **Callable** | L'émetteur peut rembourser par anticipation | Convexité **négative** quand les taux baissent : le prix est plafonné |
| **Perpétuelle / subordonnée** | Pas de maturité, ou rang inférieur en cas de défaut | Rendement plus élevé, risque plus élevé |
| **Convertible** | Convertible en actions | Obligation + call sur l'action |

### Cotation et coupon couru

Les obligations se cotent en **prix pied de coupon** (*clean*, en % du nominal) ou en **rendement**.
Le prix payé (*dirty*) ajoute le **coupon couru** :

$$
\text{coupon couru} = \text{coupon annuel} \times \frac{\text{jours depuis le dernier coupon}}{\text{jours de la période}}
$$

Exemple : OAT coupon $3\,\%$, 73 jours depuis le dernier coupon (base 365) : coupon couru
$= 3 \times 73/365 = 0{,}6$. Si le clean price vaut $98{,}5$, on paie $99{,}1$.

### Scénarios sur un portefeuille obligataire

Portefeuille de $100$ M€, duration modifiée $5$, convexité $40$ :

| Scénario | Calcul | Variation |
|---|---|---|
| Taux $+100$ bp | $-5 \times 1\,\% + \tfrac12 \times 40 \times (1\,\%)^2$ | $-4{,}8\,\%$, soit $-4{,}8$ M€ |
| Taux $-100$ bp | $+5 \times 1\,\% + \tfrac12 \times 40 \times (1\,\%)^2$ | $+5{,}2\,\%$ |
| Taux $+25$ bp | $\approx -5 \times 0{,}25\,\%$ | $\approx -1{,}25\,\%$ |
| Pentification (courts stables, longs $+50$ bp) | Dépend de la répartition par maturité | Les obligations longues perdent le plus |

La convexité positive fait gagner plus à la baisse qu'on ne perd à la hausse.

### Carry et roll-down

Même si les taux ne bougent pas, une obligation rapporte :
- le **carry** : coupon reçu moins coût de financement (par exemple taux du repo) ;
- le **roll-down** : en vieillissant, l'obligation « glisse » vers des maturités plus courtes ; si la
  courbe est croissante, son rendement baisse, donc son prix monte.

Exemple : obligation 5 ans à $3\,\%$, taux 4 ans à $2{,}8\,\%$. Dans un an, courbe inchangée, elle
rendra $2{,}8\,\%$ : gain de roll-down $\approx D_{mod}(4\text{ ans}) \times 0{,}20\,\% \approx 3{,}7 \times 0{,}20\,\%
\approx 0{,}74\,\%$, en plus du coupon.
""",
            "points_cles": [
                "Dirty = clean + coupon couru.",
                "FRN : duration très courte ; callable : convexité négative.",
                "ΔP/P ≈ −D·Δy + ½·C·(Δy)².",
                "Rendement à courbe inchangée = carry + roll-down.",
            ],
        },
        {
            "id": "taux-c6",
            "titre": "6. Dérivés de taux : swaps, FRA, caps, swaptions",
            "contenu": r"""
### FRA (Forward Rate Agreement)

Contrat qui fixe aujourd'hui le taux d'un emprunt ou d'un placement **futur** (par exemple un taux
3 mois dans 6 mois). À l'échéance, on règle en cash la différence entre le taux fixé et le taux
constaté, sur le nominal. Une entreprise qui empruntera dans 6 mois **achète** un FRA pour se protéger
d'une hausse.

### Swap de taux : rappel et usages

Payeur fixe : gagne si les taux montent. Receveur fixe : gagne s'ils baissent (position proche d'une
obligation). Le **swap spread** est l'écart entre le taux de swap et le rendement de l'emprunt d'État
de même maturité ; il reflète le risque bancaire, l'offre de titres d'État et la demande de couverture.

### Caps, floors et swaptions

- **Caplet** : option qui paie $\max(L - K, 0)$ sur une période (un call sur le taux $L$) ; un **cap**
  est une série de caplets. Un emprunteur à taux variable achète un cap pour plafonner son coût.
- **Floorlet / floor** : $\max(K - L, 0)$ (puts sur le taux). Un prêteur à taux variable s'assure un minimum.
- **Parité** : cap $-$ floor (même strike) $=$ swap payeur au taux $K$.
- **Collar de taux** : achat d'un cap financé par la vente d'un floor.
- **Swaption payeuse** : droit d'entrer dans un swap où l'on **paie** le fixe $K$ (gagne si les taux
  montent). **Swaption receveuse** : droit de recevoir le fixe (gagne si les taux baissent).

Les options de taux se cotent en volatilité **normale** (en points de base par an), car les taux
peuvent être proches de zéro, voire négatifs.

### Trades de courbe neutres en DV01

Un **steepener 2s10s** gagne si l'écart entre taux 10 ans et taux 2 ans s'élargit : on est **long du
2 ans** (receveur du fixe ou acheteur d'obligation) et **short du 10 ans**. Pour ne pas parier sur le
niveau des taux, on égalise les DV01 des deux jambes.

Exemple : DV01 pour 1 M€ de nominal $\approx 190$ € sur le 2 ans et $\approx 850$ € sur le 10 ans. Pour
10 M€ de 10 ans (DV01 $8\,500$ €), il faut $8\,500 / 190 \approx 44{,}7$ M€ de 2 ans.

| Mouvement de courbe | Steepener (long 2 ans, short 10 ans) | Flattener (inverse) |
|---|---|---|
| Hausse parallèle de 20 bp | ≈ 0 | ≈ 0 |
| 10 ans $+20$ bp, 2 ans stable | Gain $\approx 20 \times 8\,500 = 170\,000$ € | Perte |
| 2 ans $-20$ bp (baisse des taux directeurs anticipée) | Gain | Perte |

Le **butterfly** de courbe (par exemple 2s5s10s) parie sur la courbure : long des ailes, short du
centre, ou l'inverse.
""",
            "points_cles": [
                "FRA : fixe un taux futur ; acheteur protégé contre la hausse.",
                "Cap = calls sur taux ; floor = puts ; cap − floor = swap payeur.",
                "Swaption payeuse : gagne si les taux montent.",
                "Trades de courbe : neutres en DV01, pas en nominal.",
            ],
        },
        {
            "id": "taux-c7",
            "titre": "7. Le risque de crédit",
            "contenu": r"""
### Notation

Les agences (S&P, Moody's, Fitch) notent la solidité des émetteurs. L'échelle S&P/Fitch va de **AAA**
à **D** (défaut). La frontière essentielle :

- **Investment grade** : de AAA à **BBB−** (Baa3 chez Moody's) ;
- **High yield** (spéculatif) : **BB+** et en dessous.

Beaucoup d'investisseurs institutionnels ne peuvent détenir que de l'investment grade : un passage de
BBB− à BB+ (*fallen angel*) provoque souvent des ventes forcées.

### Spread de crédit et probabilité de défaut

Le spread rémunère la perte attendue (et des primes de risque et de liquidité). Avec une intensité de
défaut $\lambda$ (probabilité de défaut par an, approximativement) et un taux de recouvrement $R$ :

$$
s \approx \lambda\, (1 - R)
\qquad \Rightarrow \qquad
\lambda \approx \frac{s}{1 - R}
$$

C'est le **triangle du crédit**. Exemple : spread $120$ bp, recouvrement $40\,\%$ :
$\lambda \approx 1{,}2\,\% / 0{,}6 = 2\,\%$ par an. Probabilité de survie à 5 ans
$\approx e^{-5\lambda} = e^{-0{,}1} \approx 90{,}5\,\%$.

### Le CDS

Le **Credit Default Swap** est une assurance : l'acheteur de protection paie une prime périodique (le
spread du CDS) ; en cas de défaut de l'entité de référence, le vendeur lui paie la perte
$(1 - R) \times$ nominal. Acheter de la protection = être **short crédit** (on gagne si la qualité de
crédit se dégrade). Les indices de CDS (iTraxx en Europe, CDX aux États-Unis) permettent de couvrir ou
de prendre une vue sur tout un marché.

**Base CDS-obligation** : écart entre le spread du CDS et celui de l'obligation du même émetteur.

### Scénarios

| Événement | Effet sur l'obligation | Effet sur le CDS |
|---|---|---|
| Dégradation de note | Spread ↑, prix ↓ | Prime ↑ : l'acheteur de protection gagne |
| Résultats meilleurs que prévu | Spread ↓, prix ↑ | Prime ↓ |
| Risk-off généralisé | Spreads ↑ partout, surtout high yield | Indices iTraxx/CDX ↑ |
| Défaut | Prix ≈ taux de recouvrement | Paiement de $(1 - R)$ au porteur de protection |

### Spread duration

Sensibilité du prix au spread : pour une obligation à taux fixe, elle est proche de la duration
modifiée. Une obligation de spread duration 6 perd environ $6 \times 0{,}50\,\% = 3\,\%$ si son spread
s'écarte de 50 bp.
""",
            "points_cles": [
                "Investment grade jusqu'à BBB− ; high yield à partir de BB+.",
                "Triangle du crédit : s ≈ λ(1 − R).",
                "Acheter un CDS = acheter de la protection = short crédit.",
                "Spread duration ≈ duration modifiée pour un taux fixe.",
            ],
        },
    ],
    "quiz": [
        {"id": "taux-q01", "type": "nombre",
         "question": r"Prix d'un zéro-coupon de nominal $1\,000$ € à 2 ans, taux annuel $5\,\%$ ? (2 décimales)",
         "reponse": 907.03, "tolerance": 0.05,
         "explication": r"$1000 / 1{,}05^2 = 1000 / 1{,}1025 \approx 907{,}03$."},
        {"id": "taux-q02", "type": "nombre",
         "question": r"Obligation de nominal $100$, coupon annuel $4\,\%$, rendement actuariel $4\,\%$, 7 ans. Son prix ?",
         "reponse": 100, "tolerance": 0.01,
         "explication": "Coupon égal au rendement : l'obligation cote au pair."},
        {"id": "taux-q03", "type": "qcm",
         "question": "Les taux de marché montent. Le prix d'une obligation à taux fixe existante…",
         "choix": ["monte", "baisse", "ne bouge pas", "monte si le coupon est élevé"],
         "reponse": 1,
         "explication": "Les flux fixes sont actualisés à un taux plus élevé : leur valeur actuelle baisse."},
        {"id": "taux-q04", "type": "nombre",
         "question": "Duration de Macaulay d'un zéro-coupon à 7 ans (en années) ?",
         "reponse": 7, "tolerance": 0.001,
         "explication": "Un seul flux, à 7 ans : la moyenne pondérée vaut 7."},
        {"id": "taux-q05", "type": "nombre",
         "question": r"Duration modifiée $5$. Les taux montent de $50$ bp. Variation approximative du prix, en % ?",
         "reponse": -2.5, "tolerance": 0.01,
         "explication": r"$-5 \times 0{,}005 = -2{,}5\,\%$ (la convexité adoucirait un peu la baisse)."},
        {"id": "taux-q06", "type": "nombre",
         "question": r"Position d'une valeur de $10{,}2$ M€, duration modifiée $6$. DV01 en euros ?",
         "reponse": 6120, "tolerance": 1,
         "explication": r"$6 \times 10\,200\,000 \times 0{,}0001 = 6\,120$ €."},
        {"id": "taux-q07", "type": "nombre",
         "question": r"Taux 1 an $2\,\%$, taux 2 ans $3\,\%$ (annuels). Taux forward 1 an dans 1 an, en % ? (2 décimales)",
         "reponse": 4.01, "tolerance": 0.02,
         "explication": r"$1{,}03^2 / 1{,}02 - 1 = 1{,}0609/1{,}02 - 1 \approx 4{,}01\,\%$."},
        {"id": "taux-q08", "type": "qcm",
         "question": "Deux obligations de même maturité et même rendement : laquelle a la plus grande duration ?",
         "choix": ["Celle au coupon le plus élevé", "Celle au coupon le plus faible",
                   "Elles ont la même duration", "Impossible à dire"],
         "reponse": 1,
         "explication": "Un coupon faible place plus de poids sur le remboursement final, donc la duration est plus longue."},
        {"id": "taux-q09", "type": "qcm",
         "question": "À duration égale, pourquoi préférer l'obligation la plus convexe ?",
         "choix": ["Elle paie un coupon plus élevé",
                   "Elle gagne plus quand les taux baissent et perd moins quand ils montent",
                   "Elle a moins de risque de crédit", "Elle est plus liquide"],
         "reponse": 1,
         "explication": r"Le terme $\tfrac12 \mathcal{C} (\Delta y)^2$ est toujours positif : la convexité profite des deux sens."},
        {"id": "taux-q10", "type": "nombre",
         "question": r"OAT coupon $3\,\%$, 73 jours écoulés depuis le dernier coupon (base 365), clean price $98{,}5$. Dirty price ?",
         "reponse": 99.1, "tolerance": 0.005,
         "explication": r"Coupon couru $= 3 \times 73/365 = 0{,}6$ ; $98{,}5 + 0{,}6 = 99{,}1$."},
        {"id": "taux-q11", "type": "nombre",
         "question": r"Duration modifiée $5$, convexité $40$, taux $+100$ bp. Variation du prix en % (1 décimale) ?",
         "reponse": -4.8, "tolerance": 0.02,
         "explication": r"$-5 \times 0{,}01 + 0{,}5 \times 40 \times 0{,}0001 = -0{,}048$."},
        {"id": "taux-q12", "type": "nombre",
         "question": r"Steepener neutre en DV01 : 10 M€ de 10 ans (DV01 $850$ € par M€), DV01 du 2 ans $190$ € par M€. "
                     r"Nominal de 2 ans en M€ (1 décimale) ?",
         "reponse": 44.7, "tolerance": 0.2,
         "explication": r"$10 \times 850 / 190 \approx 44{,}7$ M€."},
        {"id": "taux-q13", "type": "qcm",
         "question": "Un steepener 2s10s consiste à…",
         "choix": ["être long du 10 ans et short du 2 ans", "être long du 2 ans et short du 10 ans",
                   "être long des deux", "acheter un cap"],
         "reponse": 1,
         "explication": "On gagne si le taux 10 ans monte par rapport au 2 ans : on vend le 10 ans, on achète le 2 ans."},
        {"id": "taux-q14", "type": "qcm",
         "question": "Cap moins floor, même strike et mêmes dates, vaut…",
         "choix": ["zéro", "un swap payeur au taux du strike", "un swap receveur", "une swaption"],
         "reponse": 1,
         "explication": r"$\max(L-K,0) - \max(K-L,0) = L - K$ à chaque période : on reçoit le variable, on paie le fixe."},
        {"id": "taux-q15", "type": "nombre",
         "question": r"Spread de crédit $120$ bp, taux de recouvrement $40\,\%$. Intensité de défaut annuelle en % ?",
         "reponse": 2, "tolerance": 0.01,
         "explication": r"$\lambda \approx s/(1-R) = 1{,}2\,\% / 0{,}6 = 2\,\%$."},
        {"id": "taux-q16", "type": "qcm",
         "question": "Quelle obligation a la duration la plus faible ?",
         "choix": ["Zéro-coupon 10 ans", "Obligation à taux fixe 10 ans", "Obligation à taux variable 10 ans (fixing trimestriel)",
                   "Obligation perpétuelle"],
         "reponse": 2,
         "explication": "Le coupon se réajuste au marché à chaque fixing : la sensibilité aux taux est celle d'un titre de 3 mois au plus."},
        {"id": "taux-q17", "type": "qcm",
         "question": "Pourquoi une obligation callable a-t-elle une convexité négative quand les taux baissent ?",
         "choix": ["Son coupon baisse", "L'émetteur la rembourse si les taux baissent : son prix est plafonné",
                   "Elle devient une obligation à taux variable", "Son spread de crédit augmente"],
         "reponse": 1,
         "explication": "L'investisseur a vendu un call à l'émetteur : la hausse de prix est limitée."},
        {"id": "taux-q18", "type": "qcm",
         "question": "Quelle est la note la plus basse de la catégorie investment grade (échelle S&P) ?",
         "choix": ["A−", "BBB−", "BB+", "BBB+"],
         "reponse": 1,
         "explication": "BBB− est le dernier cran investment grade ; BB+ est déjà high yield."},
        {"id": "taux-q19", "type": "qcm",
         "question": "Un investisseur achète de la protection CDS sur une entreprise. Il gagne si…",
         "choix": ["le spread de l'entreprise se resserre", "la qualité de crédit de l'entreprise se dégrade",
                   "les taux sans risque baissent", "l'action de l'entreprise monte"],
         "reponse": 1,
         "explication": "Acheter de la protection, c'est être short crédit."},
    ],
    "flashcards": [
        {"id": "taux-f01", "recto": "Prix d'une obligation à taux fixe",
         "verso": r"$P = \sum_t \dfrac{cN}{(1+y)^t} + \dfrac{N}{(1+y)^n}$"},
        {"id": "taux-f02", "recto": "Relation entre duration modifiée et Macaulay",
         "verso": r"$D_{mod} = D_{mac} / (1 + y)$"},
        {"id": "taux-f03", "recto": "Approximation de la variation de prix",
         "verso": r"$\Delta P / P \approx -D_{mod}\,\Delta y + \tfrac12 \mathcal{C} (\Delta y)^2$"},
        {"id": "taux-f04", "recto": "Définition du DV01",
         "verso": "Variation de valeur (en €) pour +1 point de base de rendement."},
        {"id": "taux-f05", "recto": "Taux forward entre 1 et 2 ans",
         "verso": r"$f_{1,2} = (1 + r_2)^2 / (1 + r_1) - 1$"},
        {"id": "taux-f06", "recto": "Quand une obligation cote-t-elle au pair ?",
         "verso": "Quand son coupon est égal à son rendement actuariel."},
        {"id": "taux-f07", "recto": "Clean price vs dirty price",
         "verso": "Dirty = clean + coupon couru ; le marché cote le clean."},
        {"id": "taux-f08", "recto": "Courbe inversée",
         "verso": "Taux courts au-dessus des taux longs ; souvent lue comme anticipation de baisses de taux."},
        {"id": "taux-f09", "recto": "Coupon couru", "verso": "Coupon annuel × jours écoulés / jours de la période ; dirty = clean + couru."},
        {"id": "taux-f10", "recto": "Carry et roll-down", "verso": "Carry : coupon − financement. Roll-down : gain de prix quand l'obligation vieillit sur une courbe croissante."},
        {"id": "taux-f11", "recto": "Parité cap-floor", "verso": "Cap − floor (même strike) = swap payeur au taux du strike."},
        {"id": "taux-f12", "recto": "Swaption payeuse / receveuse", "verso": "Payeuse : droit de payer le fixe (gagne si taux ↑). Receveuse : droit de recevoir le fixe (gagne si taux ↓)."},
        {"id": "taux-f13", "recto": "Steepener 2s10s", "verso": "Long 2 ans, short 10 ans, nominaux choisis pour être neutre en DV01."},
        {"id": "taux-f14", "recto": "Triangle du crédit", "verso": r"$s \approx \lambda(1 - R)$"},
        {"id": "taux-f15", "recto": "Investment grade / high yield", "verso": "IG : AAA à BBB− ; HY : BB+ et en dessous. Fallen angel : passage d'IG à HY."},
        {"id": "taux-f16", "recto": "Acheter un CDS", "verso": "Acheter une protection contre le défaut : short crédit."},
    ],
}
