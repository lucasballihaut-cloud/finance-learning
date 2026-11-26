"""Module complet : Options et Black-Scholes."""

MODULE = {
    "id": "options",
    "titre": "Options et Black-Scholes",
    "icone": "🧮",
    "statut": "complet",
    "resume": "Payoffs, parité call-put, arbre binomial, formule de Black-Scholes, grecques, "
              "volatilité implicite et stratégies classiques.",
    "chapitres": [
        {
            "id": "opt-c1",
            "titre": "1. Définitions et payoffs",
            "contenu": r"""
Une **option** est un contrat qui donne à son acheteur un **droit** (et non une obligation)
d'acheter ou de vendre un actif sous-jacent à un prix fixé à l'avance, le **strike** $K$,
à une date donnée ou jusqu'à cette date (la **maturité** $T$). En échange de ce droit,
l'acheteur paie une **prime** au vendeur dès la signature.

- **Call** : droit d'**acheter** le sous-jacent au prix $K$.
- **Put** : droit de **vendre** le sous-jacent au prix $K$.
- **Européenne** : exercice possible uniquement à la date $T$.
- **Américaine** : exercice possible à tout moment jusqu'à $T$.

À maturité, en notant $S_T$ le prix du sous-jacent, la valeur de l'option (son **payoff**) vaut :

$$
\text{Call : } (S_T - K)^+ = \max(S_T - K,\ 0)
\qquad
\text{Put : } (K - S_T)^+ = \max(K - S_T,\ 0)
$$

Le **P&L** de l'acheteur est le payoff moins la prime payée (on néglige ici l'actualisation
de la prime). Le vendeur a exactement le P&L opposé : il encaisse la prime mais porte un
risque qui peut être très grand (illimité pour un call vendu « à découvert »).

**Moneyness** (position du spot $S$ par rapport au strike) :

| | Call | Put |
|---|---|---|
| Dans la monnaie (ITM) | $S > K$ | $S < K$ |
| À la monnaie (ATM) | $S \approx K$ | $S \approx K$ |
| Hors de la monnaie (OTM) | $S < K$ | $S > K$ |

Le prix d'une option se décompose en **valeur intrinsèque** (ce que rapporterait un exercice
immédiat : $(S-K)^+$ pour un call) et **valeur temps** (le reste). La valeur temps rémunère la
possibilité que le sous-jacent bouge favorablement d'ici la maturité ; elle est maximale
autour de la monnaie et tend vers 0 à l'échéance.
""",
            "points_cles": [
                "Acheteur d'option : perte maximale = la prime.",
                "Prix = valeur intrinsèque + valeur temps.",
                "Un call vendu nu a une perte potentielle illimitée.",
            ],
        },
        {
            "id": "opt-c2",
            "titre": "2. Arbitrage et parité call-put",
            "contenu": r"""
Le pricing des dérivés repose sur l'**absence d'opportunité d'arbitrage (AOA)** : il est
impossible de construire un portefeuille qui ne coûte rien, ne peut jamais perdre et peut
gagner. Deux portefeuilles qui ont toujours la même valeur à $T$ doivent donc avoir la même
valeur aujourd'hui.

**Parité call-put** (options européennes, même strike et même maturité, sous-jacent sans dividende,
taux sans risque continu $r$) :

- portefeuille A : un call + un zéro-coupon qui paie $K$ en $T$ ;
- portefeuille B : un put + une action.

À maturité, A vaut $\max(S_T, K)$ et B vaut aussi $\max(S_T, K)$. Par AOA :

$$
C - P = S_0 - K e^{-rT}
$$

Avec un taux de dividende continu $q$ : $C - P = S_0 e^{-qT} - K e^{-rT}$.

**Bornes d'arbitrage** (sans dividende) :

$$
\max\left(S_0 - K e^{-rT},\ 0\right) \le C \le S_0
\qquad
\max\left(K e^{-rT} - S_0,\ 0\right) \le P \le K e^{-rT}
$$

**Conséquence importante** : pour un call américain sur une action *sans dividende*,
$C \ge S_0 - K e^{-rT} > S_0 - K$ dès que $r > 0$. L'option vaut plus « vivante » que
morte : l'exercice anticipé n'est jamais optimal, donc call américain = call européen.
Ce n'est plus vrai pour un put américain (il peut être optimal de l'exercer tôt quand il est
très dans la monnaie), ni pour un call si l'action verse un dividende important.
""",
            "points_cles": [
                "Parité : C − P = S₀ − K·e^(−rT) (sans dividende).",
                "Call américain sans dividende : jamais exercé avant T.",
                "Si la parité est violée, on achète le côté bon marché et on vend le côté cher.",
            ],
        },
        {
            "id": "opt-c3",
            "titre": "3. Arbre binomial et probabilité risque-neutre",
            "widget": "binomial",
            "contenu": r"""
Modèle le plus simple : sur une période $\Delta t$, le sous-jacent passe de $S_0$ à
$S_0 u$ (hausse) ou $S_0 d$ (baisse), avec $d < e^{r\Delta t} < u$ (sinon il y aurait
un arbitrage). L'option vaut $V_u$ ou $V_d$ selon le scénario.

**Réplication.** On cherche un portefeuille de $\Delta$ actions et d'un montant $B$ placé au taux
sans risque, qui vaut la même chose que l'option dans les deux états :

$$
\Delta = \frac{V_u - V_d}{S_0 (u - d)}
$$

Par AOA, le prix de l'option est le coût de ce portefeuille. En réarrangeant, on obtient :

$$
V_0 = e^{-r\Delta t}\left[\, p\, V_u + (1-p)\, V_d \,\right]
\qquad \text{avec} \qquad
p = \frac{e^{r\Delta t} - d}{u - d}
$$

$p$ est la **probabilité risque-neutre** : ce n'est pas la vraie probabilité de hausse,
c'est la pondération qui fait croître le sous-jacent au taux sans risque en espérance.
Point clé souvent demandé en entretien : **la vraie probabilité de hausse n'apparaît pas**
dans le prix. Le risque est neutralisé par la couverture, donc les préférences des
investisseurs n'interviennent pas.

**Exemple.** $S_0 = 100$, $u = 1{,}2$, $d = 0{,}8$, $r = 0$, call de strike $100$ :
$V_u = 20$, $V_d = 0$, $p = 0{,}5$, donc $V_0 = 10$ et $\Delta = 20/40 = 0{,}5$.

En multipliant les périodes (arbre à $n$ pas avec $u = e^{\sigma\sqrt{\Delta t}}$, $d = 1/u$),
le prix converge vers celui de Black-Scholes. L'arbre permet aussi de pricer des options
américaines : à chaque nœud, on compare la valeur de continuation et la valeur d'exercice.
""",
            "points_cles": [
                "p = (e^(rΔt) − d)/(u − d) : probabilité risque-neutre.",
                "Le prix ne dépend pas de la probabilité réelle de hausse.",
                "Δ = (V_u − V_d)/(S₀(u − d)) : nombre d'actions pour répliquer.",
            ],
        },
        {
            "id": "opt-c4",
            "titre": "4. La formule de Black-Scholes",
            "widget": "black_scholes",
            "contenu": r"""
**Hypothèses** : le sous-jacent suit un mouvement brownien géométrique de volatilité $\sigma$
constante, taux sans risque $r$ constant, pas de frais de transaction, trading continu,
vente à découvert possible, pas d'arbitrage.

Pour un call et un put européens (taux de dividende continu $q$, souvent $q = 0$) :

$$
C = S_0 e^{-qT} N(d_1) - K e^{-rT} N(d_2)
\qquad
P = K e^{-rT} N(-d_2) - S_0 e^{-qT} N(-d_1)
$$

$$
d_1 = \frac{\ln(S_0/K) + (r - q + \tfrac{1}{2}\sigma^2)\,T}{\sigma\sqrt{T}}
\qquad
d_2 = d_1 - \sigma\sqrt{T}
$$

où $N$ est la fonction de répartition de la loi normale centrée réduite.

**Interprétation** (avec $q = 0$) :
- $N(d_2)$ est la probabilité **risque-neutre** que le call finisse dans la monnaie ;
- $N(d_1)$ est le delta du call ;
- $K e^{-rT} N(d_2)$ est la valeur actuelle du strike payé « en cas d'exercice ».

**Approximation à la monnaie** (très utile en entretien, $S_0 = K$, $r \approx 0$) :

$$
C \approx P \approx \frac{1}{\sqrt{2\pi}}\, S_0\, \sigma \sqrt{T} \approx 0{,}4\, S_0\, \sigma\sqrt{T}
$$

Exemple : $S_0 = 100$, $\sigma = 20\,\%$, $T = 1$ an donne $C \approx 8$ (valeur exacte
avec $r = 0$ : environ $7{,}97$).

**Limites** : la volatilité n'est pas constante (smile), les rendements ont des queues plus
épaisses que la loi normale, les sauts existent. Le modèle reste la référence de marché :
on l'utilise surtout comme un « langage » pour coter les options en volatilité implicite.
""",
            "points_cles": [
                "Seul paramètre non observable : la volatilité σ.",
                "N(d₂) = probabilité risque-neutre d'exercice du call.",
                "ATM : C ≈ 0,4 · S · σ · √T.",
            ],
        },
        {
            "id": "opt-c5",
            "titre": "5. Les grecques et la couverture",
            "contenu": r"""
Les **grecques** mesurent la sensibilité du prix $V$ de l'option à chaque paramètre.
Formules Black-Scholes avec $q = 0$, où $n(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ est la
densité normale :

| Grecque | Définition | Call | Put |
|---|---|---|---|
| Delta $\Delta$ | $\partial V / \partial S$ | $N(d_1) \in [0,1]$ | $N(d_1) - 1 \in [-1,0]$ |
| Gamma $\Gamma$ | $\partial^2 V / \partial S^2$ | $\dfrac{n(d_1)}{S\sigma\sqrt T}$ | identique |
| Vega $\mathcal{V}$ | $\partial V / \partial \sigma$ | $S\, n(d_1) \sqrt T$ | identique |
| Theta $\Theta$ | $\partial V / \partial t$ | $< 0$ en général | souvent $< 0$ |
| Rho $\rho$ | $\partial V / \partial r$ | $K T e^{-rT} N(d_2) > 0$ | $-K T e^{-rT} N(-d_2) < 0$ |

**À retenir sur la forme** :
- le gamma et le vega d'une option vanille achetée sont **positifs** ;
- le gamma est maximal **à la monnaie et près de l'échéance** ;
- le vega est maximal à la monnaie et **augmente avec la maturité**.

**Delta hedging.** Un trader qui a vendu un call achète $\Delta$ actions par option pour être
insensible aux petits mouvements du spot. Comme le delta change quand le spot bouge (c'est le
gamma), il faut réajuster la couverture régulièrement.

**Gamma contre theta.** Sur une petite période $\Delta t$, une position **delta-neutre** gagne
à peu près :

$$
\text{PnL} \approx \tfrac{1}{2}\,\Gamma\,(\Delta S)^2 + \Theta\,\Delta t
$$

Être long gamma, c'est gagner quand le marché bouge beaucoup et payer du theta (le passage du
temps) quand il ne bouge pas. Dans Black-Scholes, ces deux termes s'équilibrent exactement
quand le sous-jacent réalise la volatilité $\sigma$ utilisée pour le pricing :

$$
\Theta + r S \Delta + \tfrac{1}{2}\sigma^2 S^2 \Gamma = r V
$$

C'est l'équation aux dérivées partielles de Black-Scholes. En pratique, un trader long gamma
gagne de l'argent si la **volatilité réalisée** dépasse la **volatilité implicite** payée.
""",
            "points_cles": [
                "Option achetée : gamma > 0, vega > 0, theta < 0 (en général).",
                "Gamma max à la monnaie près de l'échéance.",
                "Long gamma delta-neutre : gagne si vol réalisée > vol implicite.",
            ],
        },
        {
            "id": "opt-c6",
            "titre": "6. Volatilité implicite et stratégies",
            "contenu": r"""
**Volatilité implicite.** C'est la valeur de $\sigma$ qui, injectée dans Black-Scholes,
redonne le prix observé sur le marché. Le prix d'un call étant croissant en $\sigma$, cette
valeur est unique. Les traders cotent souvent les options directement en volatilité.

**Smile et skew.** Si Black-Scholes était parfait, la volatilité implicite serait la même pour
tous les strikes. En réalité, elle varie :
- sur les **indices actions**, la vol implicite est plus élevée pour les strikes bas
  (**skew** négatif) : les puts de protection sont très demandés et les fortes baisses sont plus
  fréquentes que ce que prévoit la loi normale ;
- sur le **change**, on observe plutôt un **smile** plus symétrique.

On appelle **surface de volatilité** la vol implicite en fonction du strike et de la maturité.

**Stratégies classiques** (toutes en options européennes de même maturité) :

| Stratégie | Construction | Vue de marché |
|---|---|---|
| Bull call spread | long call $K_1$, short call $K_2 > K_1$ | hausse modérée, prime réduite |
| Bear put spread | long put $K_2$, short put $K_1 < K_2$ | baisse modérée |
| Straddle (long) | long call $K$ + long put $K$ | gros mouvement, sens inconnu ; long vega |
| Strangle (long) | long put $K_1$ + long call $K_2 > K_1$ | idem, moins cher, mouvement plus fort nécessaire |
| Butterfly (long) | long $K_1$, short 2 × $K_2$, long $K_3$ (calls) | marché stable autour de $K_2$ |
| Risk reversal | long call OTM + short put OTM | haussier ; mesure le skew |
| Covered call | long action + short call | revenu de prime, hausse plafonnée |

**Points morts d'un straddle** : à maturité, le straddle est rentable si
$|S_T - K| >$ somme des deux primes.
""",
            "points_cles": [
                "Vol implicite = la σ qui redonne le prix de marché.",
                "Skew actions : puts OTM plus chers en vol que calls OTM.",
                "Straddle = pari sur l'amplitude du mouvement, pas sur son sens.",
            ],
        },
        {
            "id": "opt-c7",
            "titre": "7. Les stratégies en détail : payoffs et scénarios",
            "widget": "strategies",
            "contenu": r"""
Pour chaque stratégie, un trader ou un sales doit savoir dire en quelques secondes : **la vue de
marché**, **le gain maximal**, **la perte maximale**, **les points morts** et **le signe des
grecques**. Exemples avec un spot à $100$, taux nuls et ces primes (cohérentes avec la parité
call-put) :

| Option | Call | Put |
|---|---|---|
| Strike 90 | $12$ | $2$ |
| Strike 100 | $6$ | $6$ |
| Strike 110 | $2{,}5$ | $12{,}5$ |

### Spreads directionnels

**Bull call spread 100/110** : achat du call 100, vente du call 110. Coût $6 - 2{,}5 = 3{,}5$.
Gain maximal $10 - 3{,}5 = 6{,}5$ au-dessus de 110, perte maximale $3{,}5$ sous 100, point mort $103{,}5$.
On renonce à la hausse au-delà de 110 pour payer moins cher.

**Bear put spread 100/90** : achat du put 100, vente du put 90. Coût $6 - 2 = 4$, gain maximal $6$
sous 90, point mort $96$.

### Stratégies de volatilité

**Long straddle 100** : call 100 + put 100, coût $12$. Points morts $88$ et $112$. Perte maximale $12$
si le spot finit exactement à 100. Long gamma, long vega, theta négatif.

**Long strangle 90/110** : put 90 + call 110, coût $4{,}5$. Points morts $85{,}5$ et $114{,}5$. Moins cher,
mais il faut un mouvement plus fort.

**Short straddle / short strangle** : les positions inverses. Gain limité à la prime, perte
potentiellement illimitée : c'est **vendre de la volatilité**.

**Long butterfly 90/100/110 (calls)** : achat du call 90, vente de 2 calls 100, achat du call 110.
Coût $12 - 2 \times 6 + 2{,}5 = 2{,}5$. Gain maximal $10 - 2{,}5 = 7{,}5$ si le spot finit à 100, points
morts $92{,}5$ et $107{,}5$. Pari sur un marché **calme**, avec perte limitée. Short vega près du centre.

**Iron condor** : vente d'un strangle et achat d'un strangle plus large pour limiter la perte.
Pari sur un marché dans une fourchette.

### Stratégies avec le sous-jacent

**Protective put** : action + put 90 (coût 2). Perte maximale $10 + 2 = 12$, point mort $102$, gain
illimité. C'est une **assurance**.

**Covered call** : action + vente du call 110 (prime 2,5). Point mort $97{,}5$, gain maximal
$10 + 2{,}5 = 12{,}5$. On encaisse un revenu en renonçant à la forte hausse.

**Collar** : action + achat du put 90 + vente du call 110. Ici on encaisse $2{,}5 - 2 = 0{,}5$ : la
protection est financée par l'abandon de la hausse au-delà de 110. Résultat compris entre $-9{,}5$ et
$+10{,}5$. Un *zero-cost collar* choisit les strikes pour que les primes se compensent.

**Risk reversal** : achat d'un call OTM financé par la vente d'un put OTM. Exposition haussière
« bon marché », mais risque de baisse.

### Stratégies dans le temps

**Calendar spread** : vente d'une option courte et achat d'une option longue de même strike. Gagne
si le spot reste près du strike à l'échéance courte (la courte perd vite sa valeur temps) et si la
volatilité implicite longue monte : **long vega, short gamma**.

### Tableau de synthèse

| Stratégie | Vue | Delta | Gamma | Vega | Theta |
|---|---|---|---|---|---|
| Long call | Hausse | + | + | + | − |
| Long put | Baisse | − | + | + | − |
| Bull call spread | Hausse modérée | + | faible | faible | faible |
| Long straddle | Gros mouvement | ≈ 0 | + | + | − |
| Short strangle | Marché calme | ≈ 0 | − | − | + |
| Long butterfly | Spot au centre | ≈ 0 | − (au centre) | − (au centre) | + (au centre) |
| Covered call | Stable / légère hausse | + | − | − | + |
| Calendar | Spot stable, vol longue en hausse | ≈ 0 | − | + | + |
""",
            "points_cles": [
                "Toujours donner : vue, gain max, perte max, points morts, grecques.",
                "Straddle/strangle achetés : long gamma et long vega.",
                "Collar : protection financée par la vente de la hausse.",
                "Butterfly et condor : paris sur un marché calme, perte limitée.",
            ],
        },
        {
            "id": "opt-c8",
            "titre": "8. Gérer un book d'options : arbitrages, dividendes, exercice",
            "contenu": r"""
### Arbitrage de parité : conversion et reversal

Si la parité $C - P = S_0 - K e^{-rT}$ n'est pas respectée, on peut verrouiller un gain sans risque.

Exemple : $S_0 = 100$, $K = 100$, $T = 1$ an, $r = 5\,\%$. Alors $K e^{-rT} \approx 95{,}12$ et la
parité impose $C - P \approx 4{,}88$. Si le marché cote $C = 10$ et $P = 4$ (soit $C - P = 6$), le call
est trop cher :

- **conversion** : vendre le call ($+10$), acheter le put ($-4$), acheter l'action ($-100$), emprunter
  $95{,}12$ ;
- à maturité, quoi qu'il arrive, on livre l'action au prix $K = 100$ (par l'exercice du call vendu ou
  du put acheté), ce qui rembourse exactement l'emprunt ;
- gain verrouillé aujourd'hui : $10 - 4 - 100 + 95{,}12 = 1{,}12$.

Le **reversal** est l'opération inverse (quand le put est trop cher). En pratique, ces écarts sont
minuscules et reflètent souvent des coûts d'emprunt de titres ou des dividendes mal estimés.

### Dividendes

Le jour du détachement (*ex-date*), le cours baisse d'environ le montant du dividende. Les dividendes
attendus **baissent le forward**, donc **réduisent le prix des calls et augmentent celui des puts**.
Un trader d'options sur actions est donc exposé aux dividendes futurs : il peut les couvrir avec des
**futures sur dividendes**.

### Exercice anticipé des options américaines

- **Call américain** : sans dividende, jamais d'exercice anticipé. Avec dividende, il peut être optimal
  d'exercer **juste avant l'ex-date** si le call est très dans la monnaie et que le dividende dépasse la
  valeur temps restante.
- **Put américain** : l'exercice anticipé peut être optimal quand il est très dans la monnaie et que
  les taux sont élevés (on encaisse le strike plus tôt et on le place).

### Pin risk

À l'échéance, si le spot est **très proche du strike**, le vendeur ne sait pas si l'option sera exercée :
il ne sait pas quelle position il aura le lendemain. Le gamma devient énorme et la couverture délicate.

### Scénarios de P&L d'une journée

| Position (delta-neutre) | Le marché bouge de 3 % | Le marché ne bouge pas | La vol implicite monte de 5 points |
|---|---|---|---|
| Long straddle (long gamma, long vega) | Gain (gamma) | Perte (theta) | Gain (vega) |
| Short strangle (short gamma, short vega) | Perte | Gain (theta) | Perte |
| Long calendar (short gamma, long vega) | Perte | Gain modéré | Gain |

### Agréger les risques d'un book

Un trader ne regarde pas option par option : il suit le **delta total** (couvert avec le sous-jacent
ou des futures), le **gamma total**, le **vega par maturité** (les vols de maturités différentes ne
bougent pas ensemble), le theta et l'exposition au **skew**. Le **P&L explain** décompose chaque jour
le résultat : delta, gamma, vega, theta, résidu inexpliqué.
""",
            "points_cles": [
                "Conversion : short call + long put + long action quand C − P est trop élevé.",
                "Dividendes ↑ ⇒ calls ↓, puts ↑.",
                "Call américain : exercice anticipé possible juste avant un gros dividende.",
                "P&L explain : delta, gamma, vega, theta, résidu.",
            ],
        },
        {
            "id": "opt-c9",
            "titre": "9. Trader la volatilité",
            "contenu": r"""
### Volatilité implicite contre volatilité réalisée

Acheter une option et la couvrir en delta, c'est **acheter de la volatilité** au niveau implicite
$\sigma_{imp}$ et « encaisser » la volatilité réalisée $\sigma_{réal}$. Sur chaque petite période :

$$
\text{PnL} \approx \tfrac{1}{2}\, \Gamma\, S^2 \left( \sigma_{réal}^2 - \sigma_{imp}^2 \right) \Delta t
$$

- vol réalisée **au-dessus** de l'implicite : le long gamma gagne ;
- vol réalisée **en dessous** : le theta payé l'emporte, il perd.

Le résultat dépend aussi du **chemin** : le gain est plus fort quand le spot bouge près du strike (là
où le gamma est grand).

### Le variance swap

Contrat qui échange directement la **variance réalisée** contre une variance fixée à l'avance :

$$
\text{Payoff} = N_{var} \left( \sigma_{réal}^2 - K_{var}^2 \right)
\qquad
N_{var} = \frac{N_{vega}}{2\, K_{var}}
$$

(volatilités exprimées en points, par exemple 20 pour 20 %). Le *vega notional* $N_{vega}$ donne le
gain approximatif par point de vol : $\text{Payoff} \approx N_{vega}\,(\sigma_{réal} - K_{var})$ pour de
petits écarts.

Exemple : $N_{vega} = 100\,000$ €, strike $20$, vol réalisée $25$. Alors $N_{var} = 2\,500$ et le payoff
vaut $2\,500 \times (625 - 400) = 562\,500$ €, plus que l'approximation $500\,000$ € : le variance swap
est **convexe** en volatilité (il gagne plus qu'il ne perd pour un même écart). Il se réplique avec un
ensemble d'options de tous les strikes, pondérées en $1/K^2$, ce qui explique pourquoi son strike est
en général **au-dessus** de la vol ATM quand il y a du skew.

### Trades de skew et de structure par terme

- **Acheter le skew** (risk reversal acheté côté put) : on gagne si les puts OTM se renchérissent
  par rapport aux calls, typiquement lors d'une baisse brutale.
- **Calendar de vol** : acheter la vol longue et vendre la vol courte quand la structure par terme est
  inversée (stress), en pariant sur un retour à la normale.
- **Dispersion** : vendre la vol d'un indice et acheter la vol de ses composants. On gagne si les
  actions bougent beaucoup mais dans des sens différents (corrélation réalisée faible).

### Dynamique de la vol avec le marché

Sur les actions, la vol implicite **monte quand le marché baisse** (corrélation spot/vol négative) :
un portefeuille long actions et short vol perd deux fois lors d'un krach. C'est aussi pour cela que les
puts sont recherchés comme couverture.
""",
            "points_cles": [
                "Long gamma couvert : PnL ≈ ½ΓS²(σ²réal − σ²imp)Δt.",
                "Variance swap : N_var(σ²réal − K²), convexe en vol.",
                "Actions : vol ↑ quand spot ↓.",
                "Dispersion : short vol indice, long vol composants (pari sur corrélation faible).",
            ],
        },
    ],
    "quiz": [
        {
            "id": "opt-q01", "type": "nombre",
            "question": r"Vous achetez un put de strike $K = 50$ pour une prime de $3$. "
                        r"À maturité, $S_T = 42$. Quel est votre P&L ?",
            "reponse": 5, "tolerance": 0.001,
            "explication": r"Payoff $= \max(50 - 42, 0) = 8$, moins la prime $3$ : P&L $= 5$.",
        },
        {
            "id": "opt-q02", "type": "nombre",
            "question": r"$S_0 = 100$, $K = 105$, $T = 1$ an, $r = 5\,\%$ (continu), pas de dividende. "
                        r"Le call européen vaut $8$. Que vaut le put européen ? (2 décimales)",
            "reponse": 7.88, "tolerance": 0.05,
            "explication": r"Parité : $P = C - S_0 + K e^{-rT} = 8 - 100 + 105\,e^{-0{,}05} "
                           r"\approx 8 - 100 + 99{,}88 = 7{,}88$.",
        },
        {
            "id": "opt-q03", "type": "qcm",
            "question": "Dans quel intervalle se trouve le delta d'un call européen acheté (sans dividende) ?",
            "choix": ["Entre −1 et 0", "Entre 0 et 1", "Entre −1 et 1", "Il peut dépasser 1"],
            "reponse": 1,
            "explication": r"$\Delta_{call} = N(d_1)$, une probabilité normale, donc entre 0 et 1.",
        },
        {
            "id": "opt-q04", "type": "qcm",
            "question": "Où le gamma d'une option vanille est-il le plus élevé ?",
            "choix": ["Très dans la monnaie, longue maturité", "À la monnaie, proche de l'échéance",
                      "Très hors de la monnaie, proche de l'échéance", "À la monnaie, longue maturité"],
            "reponse": 1,
            "explication": r"$\Gamma = n(d_1)/(S\sigma\sqrt T)$ : $n(d_1)$ est maximal à la monnaie et "
                           r"$\sqrt T$ au dénominateur fait exploser le gamma ATM quand $T \to 0$.",
        },
        {
            "id": "opt-q05", "type": "qcm",
            "question": "Pourquoi n'exerce-t-on jamais par anticipation un call américain sur une action sans dividende ?",
            "choix": ["Parce que la prime est perdue à l'exercice",
                      "Parce que C ≥ S₀ − K·e^(−rT) > S₀ − K : l'option vaut plus que sa valeur d'exercice",
                      "Parce que le delta est inférieur à 1",
                      "C'est faux, on l'exerce dès qu'il est dans la monnaie"],
            "reponse": 1,
            "explication": "Garder l'option (ou la vendre) rapporte toujours plus que l'exercer : on "
                           "conserve la valeur temps et on paie le strike plus tard.",
        },
        {
            "id": "opt-q06", "type": "nombre",
            "question": r"Arbre à une période : $S_0 = 100$, $u = 1{,}1$, $d = 0{,}9$, $r = 0$. "
                        r"Quel est le prix du call de strike $100$ ?",
            "reponse": 5, "tolerance": 0.01,
            "explication": r"$p = (1 - 0{,}9)/(1{,}1 - 0{,}9) = 0{,}5$, $V_u = 10$, $V_d = 0$, "
                           r"donc $V_0 = 0{,}5 \times 10 = 5$.",
        },
        {
            "id": "opt-q07", "type": "nombre",
            "question": r"Même arbre ($S_0 = 100$, $u = 1{,}1$, $d = 0{,}9$, call $K = 100$) : "
                        r"combien d'actions faut-il détenir par option pour la répliquer ?",
            "reponse": 0.5, "tolerance": 0.001,
            "explication": r"$\Delta = (V_u - V_d)/(S_0(u - d)) = 10 / 20 = 0{,}5$.",
        },
        {
            "id": "opt-q08", "type": "qcm",
            "question": r"Dans Black-Scholes, que représente $N(d_2)$ ?",
            "choix": ["Le delta du call", "La probabilité réelle que le call finisse dans la monnaie",
                      "La probabilité risque-neutre que le call finisse dans la monnaie",
                      "Le gamma du call"],
            "reponse": 2,
            "explication": r"$N(d_2) = \mathbb{Q}(S_T > K)$ sous la probabilité risque-neutre. "
                           r"Le delta est $N(d_1)$.",
        },
        {
            "id": "opt-q09", "type": "nombre",
            "question": r"Approximation rapide : call à la monnaie, $S_0 = 200$, $\sigma = 25\,\%$, "
                        r"$T = 3$ mois, taux nuls. Prix approximatif ?",
            "reponse": 10, "tolerance": 0.3,
            "explication": r"$C \approx 0{,}4 \times 200 \times 0{,}25 \times \sqrt{0{,}25} = 10$ "
                           r"(valeur exacte $\approx 9{,}97$).",
        },
        {
            "id": "opt-q10", "type": "qcm",
            "question": "La volatilité implicite monte de 2 points, tout le reste égal. Le prix d'un put acheté…",
            "choix": ["baisse", "monte", "ne change pas", "dépend du signe du delta"],
            "reponse": 1,
            "explication": "Le vega d'un put est positif, comme celui d'un call : plus d'incertitude "
                           "rend le droit optionnel plus précieux.",
        },
        {
            "id": "opt-q11", "type": "nombre",
            "question": r"Position delta-neutre avec $\Gamma = 0{,}05$ (par action). Le spot monte de $2$. "
                        r"En ignorant le theta, quel P&L approximatif par action ?",
            "reponse": 0.1, "tolerance": 0.001,
            "explication": r"$\tfrac12 \Gamma (\Delta S)^2 = 0{,}5 \times 0{,}05 \times 4 = 0{,}10$.",
        },
        {
            "id": "opt-q12", "type": "nombre",
            "question": r"Vous êtes long 10 calls (chaque contrat porte sur 100 actions) de delta $0{,}6$. "
                        r"Combien d'actions vendre pour être delta-neutre ?",
            "reponse": 600, "tolerance": 0.001,
            "explication": r"Delta total $= 10 \times 100 \times 0{,}6 = 600$ actions : on en vend 600.",
        },
        {
            "id": "opt-q13", "type": "qcm",
            "question": "Straddle long de strike 100 : call payé 6 et put payé 5. Quels sont les points morts à maturité ?",
            "choix": ["94 et 106", "95 et 105", "89 et 111", "100 uniquement"],
            "reponse": 2,
            "explication": "Il faut que |S_T − 100| dépasse la prime totale 11 : S_T < 89 ou S_T > 111.",
        },
        {
            "id": "opt-q14", "type": "qcm",
            "question": "Sur les indices actions, le skew de volatilité implicite est en général…",
            "choix": ["plat", "plus élevé pour les strikes hauts (calls OTM)",
                      "plus élevé pour les strikes bas (puts OTM)", "nul à court terme"],
            "reponse": 2,
            "explication": "Forte demande de protection et risque de krach : les puts OTM se paient plus cher en vol.",
        },
        {
            "id": "opt-q15", "type": "nombre",
            "question": r"Une option a un vega de $0{,}25$ (pour 1 point de vol). La vol implicite passe de "
                        r"$20\,\%$ à $23\,\%$. Variation approximative du prix ?",
            "reponse": 0.75, "tolerance": 0.001,
            "explication": r"$3 \text{ points} \times 0{,}25 = +0{,}75$.",
        },
        {"id": "opt-q16", "type": "nombre",
         "question": r"Bull call spread 100/110 : call 100 acheté $6$, call 110 vendu $2{,}5$. Point mort à maturité ?",
         "reponse": 103.5, "tolerance": 0.001,
         "explication": r"Coût net $3{,}5$ : il faut $S_T = 100 + 3{,}5 = 103{,}5$."},
        {"id": "opt-q17", "type": "nombre",
         "question": r"Long straddle 100 : call et put à $6$ chacun. Point mort haut à maturité ?",
         "reponse": 112, "tolerance": 0.001,
         "explication": r"Prime totale $12$ : $100 + 12 = 112$ (et $88$ en bas)."},
        {"id": "opt-q18", "type": "nombre",
         "question": r"Butterfly 90/100/110 en calls : call 90 à $12$, call 100 à $6$, call 110 à $2{,}5$. Gain maximal ?",
         "reponse": 7.5, "tolerance": 0.001,
         "explication": r"Coût $12 - 12 + 2{,}5 = 2{,}5$ ; à $S_T = 100$ le payoff vaut $10$ : gain $7{,}5$."},
        {"id": "opt-q19", "type": "nombre",
         "question": r"Action à $100$ protégée par un put 90 payé $2$. Perte maximale à maturité ?",
         "reponse": 12, "tolerance": 0.001,
         "explication": r"Baisse jusqu'à 90 ($-10$) plus la prime ($-2$)."},
        {"id": "opt-q20", "type": "qcm",
         "question": "Un collar (action + put acheté + call vendu) sert à…",
         "choix": ["parier sur une hausse de la volatilité", "se protéger à la baisse en finançant le put par l'abandon de la hausse",
                   "doubler l'exposition à la hausse", "arbitrer la parité call-put"],
         "reponse": 1,
         "explication": "La prime du call vendu paie tout ou partie du put : protection bon marché, hausse plafonnée."},
        {"id": "opt-q21", "type": "nombre",
         "question": r"$S_0 = K = 100$, $T = 1$, $r = 5\,\%$ (continu). Le marché cote $C = 10$, $P = 4$. "
                     r"Gain d'arbitrage verrouillé aujourd'hui par une conversion ? (2 décimales)",
         "reponse": 1.12, "tolerance": 0.02,
         "explication": r"$10 - 4 - 100 + 100\,e^{-0{,}05} \approx 1{,}12$."},
        {"id": "opt-q22", "type": "nombre",
         "question": r"Variance swap : vega notional $100\,000$ €, strike $20$, vol réalisée $25$. Payoff en euros ?",
         "reponse": 562500, "tolerance": 100,
         "explication": r"$N_{var} = 100\,000 / 40 = 2\,500$ ; payoff $= 2\,500 \times (25^2 - 20^2) = 562\,500$ €."},
        {"id": "opt-q23", "type": "qcm",
         "question": "Un trader est long straddle couvert en delta. Quand gagne-t-il de l'argent sur la durée ?",
         "choix": ["Si la vol implicite reste stable", "Si la vol réalisée dépasse la vol implicite payée",
                   "Si le spot ne bouge pas", "Si les taux montent"],
         "reponse": 1,
         "explication": "Les gains de gamma doivent dépasser le theta payé, qui correspond à la vol implicite."},
        {"id": "opt-q24", "type": "qcm",
         "question": "Quand peut-il être optimal d'exercer un call américain avant l'échéance ?",
         "choix": ["Jamais", "Juste avant le détachement d'un dividende important, si le call est très dans la monnaie",
                   "Quand la volatilité monte", "Quand les taux baissent"],
         "reponse": 1,
         "explication": "En exerçant, on récupère l'action et son dividende ; c'est rentable si le dividende dépasse la valeur temps."},
        {"id": "opt-q25", "type": "qcm",
         "question": "Les dividendes attendus sur une action augmentent. Effet sur le call et le put ?",
         "choix": ["Call ↑, put ↓", "Call ↓, put ↑", "Les deux montent", "Aucun effet"],
         "reponse": 1,
         "explication": "Le forward baisse : le call vaut moins et le put plus."},
        {"id": "opt-q26", "type": "qcm",
         "question": "Exposition d'un calendar spread acheté (vente de l'option courte, achat de la longue, même strike) ?",
         "choix": ["Long gamma, short vega", "Short gamma, long vega", "Long gamma, long vega", "Aucune grecque"],
         "reponse": 1,
         "explication": "L'option courte domine le gamma (vendue), l'option longue domine le vega (achetée)."},
    ],
    "flashcards": [
        {"id": "opt-f01", "recto": "Payoff d'un call et d'un put à maturité",
         "verso": r"Call : $(S_T - K)^+$ ; put : $(K - S_T)^+$."},
        {"id": "opt-f02", "recto": "Parité call-put (sans dividende)",
         "verso": r"$C - P = S_0 - K e^{-rT}$"},
        {"id": "opt-f03", "recto": "Probabilité risque-neutre dans l'arbre binomial",
         "verso": r"$p = \dfrac{e^{r\Delta t} - d}{u - d}$"},
        {"id": "opt-f04", "recto": "Formule de Black-Scholes du call",
         "verso": r"$C = S_0 N(d_1) - K e^{-rT} N(d_2)$, $d_{1,2} = \dfrac{\ln(S_0/K) + (r \pm \sigma^2/2)T}{\sigma\sqrt T}$"},
        {"id": "opt-f05", "recto": "Approximation du prix d'un call ATM",
         "verso": r"$C \approx 0{,}4\, S\, \sigma \sqrt{T}$"},
        {"id": "opt-f06", "recto": "Delta d'un call et d'un put (BS, sans dividende)",
         "verso": r"Call : $N(d_1)$ ; put : $N(d_1) - 1$."},
        {"id": "opt-f07", "recto": "Où le gamma est-il maximal ?",
         "verso": "À la monnaie, et d'autant plus que l'échéance est proche."},
        {"id": "opt-f08", "recto": "P&L d'une position delta-neutre sur Δt",
         "verso": r"$\approx \tfrac12 \Gamma (\Delta S)^2 + \Theta \Delta t$"},
        {"id": "opt-f09", "recto": "Quand un long straddle gagne-t-il de l'argent (couvert en delta) ?",
         "verso": "Quand la volatilité réalisée dépasse la volatilité implicite payée."},
        {"id": "opt-f10", "recto": "Définition de la volatilité implicite",
         "verso": "La volatilité qui, dans Black-Scholes, redonne le prix de marché de l'option."},
        {"id": "opt-f11", "recto": "Signe du vega et du gamma d'une option vanille achetée",
         "verso": "Tous deux positifs, pour un call comme pour un put."},
        {"id": "opt-f12", "recto": "Composition d'un butterfly en calls",
         "verso": r"Long $K_1$, short $2 \times K_2$, long $K_3$ avec $K_2$ au milieu : pari sur un marché stable."},
        {"id": "opt-f13", "recto": "Bull call spread : coût, gain max, point mort",
         "verso": r"Coût $C(K_1) - C(K_2)$ ; gain max $K_2 - K_1 - \text{coût}$ ; point mort $K_1 + \text{coût}$."},
        {"id": "opt-f14", "recto": "Points morts d'un straddle", "verso": r"$K \pm$ (prime du call + prime du put)."},
        {"id": "opt-f15", "recto": "Collar", "verso": "Action + put acheté + call vendu : protection financée par l'abandon de la hausse."},
        {"id": "opt-f16", "recto": "Conversion", "verso": "Short call + long put + long action (+ emprunt) quand C − P est trop élevé par rapport à la parité."},
        {"id": "opt-f17", "recto": "Effet des dividendes sur les options", "verso": "Forward plus bas : calls moins chers, puts plus chers."},
        {"id": "opt-f18", "recto": "P&L d'un long gamma couvert",
         "verso": r"$\approx \tfrac12 \Gamma S^2 (\sigma_{réal}^2 - \sigma_{imp}^2)\Delta t$"},
        {"id": "opt-f19", "recto": "Payoff d'un variance swap",
         "verso": r"$N_{var}(\sigma_{réal}^2 - K_{var}^2)$ avec $N_{var} = N_{vega} / (2K_{var})$"},
        {"id": "opt-f20", "recto": "Pin risk", "verso": "Incertitude sur l'exercice quand le spot finit très près du strike à l'échéance."},
        {"id": "opt-f21", "recto": "Dispersion", "verso": "Vendre la vol d'un indice, acheter celle des composants : pari sur une corrélation réalisée faible."},
    ],
}
