"""Module : Produits structurés (produits, décompositions, scénarios)."""

MODULE = {
    "id": "structures",
    "titre": "Produits structurés",
    "icone": "🧩",
    "statut": "complet",
    "resume": "Briques de base, term sheet, capital garanti, reverse convertibles, autocalls (Athena, Phoenix, "
              "mémoire, step-down), Twin Win, Bonus, Shark, options exotiques et scénarios à présenter au client.",
    "chapitres": [
        # ------------------------------------------------------------------ 1
        {
            "id": "str-c1",
            "titre": "1. Le principe : assembler des briques",
            "contenu": r"""
Un **produit structuré** combine un placement de taux (le plus souvent un **zéro-coupon**) et une ou
plusieurs **options**, pour fabriquer un profil de gain sur mesure : protéger le capital, viser un
rendement élevé, exprimer une vue de marché précise.

### Qui intervient ?

- l'**émetteur** (une banque) : le produit est juridiquement une **dette** de l'émetteur, sous forme
  d'EMTN (*Euro Medium Term Note*), de certificat ou de fonds à formule ;
- le **structureur** conçoit le payoff, choisit les paramètres et le price ;
- le **sales** le présente aux clients (banques privées, conseillers en gestion de patrimoine,
  assureurs pour l'assurance-vie, institutionnels) ;
- le **trader exotique** gère ensuite les risques de l'option incluse dans le produit ;
- le **distributeur** le commercialise auprès des clients finaux.

### La règle de construction

Le prix d'émission (souvent $100\,\%$ du nominal) se décompose en :

$$
100\,\% = \underbrace{\text{zéro-coupon}}_{\text{partie taux}} + \underbrace{\text{options}}_{\text{partie risquée}} + \underbrace{\text{marge}}_{\text{émetteur et distribution}}
$$

Le zéro-coupon est actualisé au taux de financement de l'émetteur (taux sans risque + son **spread de
crédit**) : un émetteur au spread plus élevé dispose d'un budget optionnel plus grand, mais fait porter
un risque de crédit plus élevé à l'investisseur.

**Deux leviers** pour rendre un produit plus attractif :
1. **un budget plus grand** : taux plus élevés, maturité plus longue, protection du capital moindre ;
2. **des options moins chères** : plafonner la hausse, faire vendre une option à l'investisseur (il
   devient vendeur de volatilité), utiliser une moyenne, un panier, un worst-of ou une barrière.

### Lire une term sheet

La *term sheet* (fiche technique) résume les caractéristiques. Les champs à repérer :

| Champ | Exemple | À vérifier |
|---|---|---|
| Émetteur / garant | Banque X, notation A | Risque de crédit |
| Sous-jacent | Indice actions, action, panier, worst-of | Volatilité, dividendes, décrément éventuel |
| Devise, nominal | EUR, 1 000 € | Risque de change |
| Dates | Émission, observations, maturité | Durée maximale |
| Seuils et barrières | Rappel 100 %, coupon 70 %, protection 60 % | Observation à maturité ou en continu |
| Coupon | 8 % par an, conditionnel, mémoire | Quand et à quelle condition il est payé |
| Formule de remboursement | Selon les scénarios | Le pire scénario |
| Frais, prix secondaire | Marge, fourchette de rachat | Coût réel, liquidité |

### Les risques à expliquer au client

- **risque de marché** sur le sous-jacent ;
- **risque de crédit de l'émetteur** : même un capital « garanti » ne l'est que si l'émetteur ne fait
  pas défaut ;
- **liquidité** : revente avant maturité possible en général, mais au prix proposé par l'émetteur
  (marché secondaire), qui peut être très inférieur au nominal ;
- **durée incertaine** pour les produits à rappel anticipé ;
- **complexité** : le client doit comprendre le scénario défavorable.

En Europe, ces produits sont accompagnés d'un **DIC** (Document d'Informations Clés, réglementation
PRIIPs) avec un indicateur de risque de 1 à 7 et quatre scénarios de performance (tensions,
défavorable, intermédiaire, favorable).
""",
            "points_cles": [
                "Structuré = zéro-coupon + options + marge.",
                "Le produit est une dette de l'émetteur : risque de crédit.",
                "Pour enrichir : plus de budget ou des options moins chères.",
                "Term sheet : sous-jacent, seuils, barrière, coupon, formule, frais.",
            ],
        },
        # ------------------------------------------------------------------ 2
        {
            "id": "str-c2",
            "titre": "2. Le capital garanti",
            "widget": "capital_garanti",
            "contenu": r"""
**Objectif** : rendre $100\,\%$ du capital à maturité et faire profiter l'investisseur d'une partie
de la hausse d'un indice.

**Construction** : un zéro-coupon de nominal 100 à maturité $T$, plus des calls à la monnaie achetés
avec le reste du budget. À maturité, l'investisseur reçoit :

$$
100 \times \left[\, 1 + p \times \max\left(\frac{S_T}{S_0} - 1,\ 0\right) \right]
$$

où $p$ est le **taux de participation** :

$$
p = \frac{\text{budget optionnel}}{\text{prix du call ATM (en \% du nominal)}}
= \frac{100 - ZC - \text{marge}}{C_{ATM}}
$$

**Exemple.** Taux 5 ans $3\,\%$ : $ZC = 100 / 1{,}03^5 \approx 86{,}3$. Avec une marge de $1$, le
budget vaut $12{,}7$. Si le call ATM 5 ans coûte $20$, la participation est d'environ $64\,\%$.

### Scénarios à maturité (participation 60 %, 5 ans)

| Scénario | Indice à maturité | Remboursement | Rendement annuel |
|---|---|---|---|
| Favorable | $+30\,\%$ | $100 \times (1 + 0{,}6 \times 0{,}30) = 118$ | $\approx 3{,}4\,\%$ |
| Neutre | $0\,\%$ | $100$ | $0\,\%$ |
| Défavorable | $-30\,\%$ | $100$ | $0\,\%$ (mais perte de pouvoir d'achat et coût d'opportunité) |
| Défaut de l'émetteur | quel que soit l'indice | perte possible | — |

### Sensibilités

- **taux en hausse** → zéro-coupon moins cher → budget plus grand → participation **plus élevée** ;
- **volatilité en hausse** → calls plus chers → participation **plus faible** ;
- **dividendes élevés** sur l'indice → forward plus bas → calls moins chers → participation plus élevée ;
- **spread de crédit de l'émetteur** plus élevé → zéro-coupon moins cher → participation plus élevée.

C'est pourquoi les capitaux garantis étaient rares quand les taux étaient proches de zéro : le
zéro-coupon coûtait presque 100 et il ne restait presque rien pour les options.

### Variantes pour augmenter la participation

- **capital protégé à 90 %** : le zéro-coupon ne rembourse que 90, le budget augmente ;
- **gain plafonné** : call spread au lieu d'un call (par exemple participation 100 % jusqu'à +40 %) ;
- **moyenne** du sous-jacent (option asiatique), moins chère ;
- **barrière haute** désactivante : c'est le **Shark** (chapitre 5) ;
- **cliquet** : gains annuels plafonnés et cumulés (chapitre 6).
""",
            "points_cles": [
                "Participation = (100 − ZC − marge) / prix du call.",
                "Taux ↑ ⇒ participation ↑ ; vol ↑ ⇒ participation ↓.",
                "Pire scénario de marché : 100 (hors défaut de l'émetteur).",
            ],
        },
        # ------------------------------------------------------------------ 3
        {
            "id": "str-c3",
            "titre": "3. Produits de rendement : reverse convertible et discount",
            "contenu": r"""
Ici, l'investisseur **vend** une option et touche sa prime sous forme de coupon ou de décote. Derrière
un rendement élevé se cache presque toujours une option vendue : il faut savoir dire **laquelle** et
**dans quel scénario elle coûte**.

### Reverse convertible

Coupon élevé **garanti**. À maturité, l'investisseur récupère son nominal si l'action est au-dessus du
strike (souvent $100\,\%$), sinon il reçoit des actions (ou leur valeur), donc il subit la baisse :

$$
\text{Reverse convertible} = \text{zéro-coupon} + \text{coupons} - \text{put}(K)
$$

Scénarios (1 an, coupon $9\,\%$, strike $100\,\%$) :

| Action à maturité | Remboursement | Coupon | Total |
|---|---|---|---|
| $+10\,\%$ | $100$ | $9$ | $109$ (la hausse au-delà du coupon est perdue) |
| $-5\,\%$ | $95$ | $9$ | $104$ |
| $-30\,\%$ | $70$ | $9$ | $79$ |

### Reverse convertible à barrière (BRC)

Le put vendu est un **put down-and-in** : il n'est activé que si l'action passe sous une barrière
(par exemple $70\,\%$, observée à maturité ou en continu). Coupon plus faible, protection meilleure.

| Action à maturité (barrière 70 %, coupon 6 %) | Total |
|---|---|
| $-5\,\%$ | $106$ |
| $-25\,\%$ | $106$ (barrière non franchie) |
| $-35\,\%$ | $65 + 6 = 71$ (barrière franchie : toute la baisse est subie) |

### Certificat discount

On achète l'action avec une décote, mais le gain est plafonné à un niveau $K$ (le *cap*) :

$$
\text{Discount} = \text{action} - \text{call}(K) = \text{zéro-coupon}(K) - \text{put}(K)
$$

(la seconde égalité vient de la parité call-put, sans dividende).

Scénarios : action à $50$, cap $55$, prix du certificat $47$.

| Action à maturité | Remboursement | Performance |
|---|---|---|
| $60$ | $55$ (plafonné) | $+17{,}0\,\%$ (l'action fait $+20\,\%$) |
| $50$ | $50$ | $+6{,}4\,\%$ (l'action fait $0\,\%$) |
| $40$ | $40$ | $-14{,}9\,\%$ (l'action fait $-20\,\%$) |

Le discount surperforme l'action dans les marchés stables ou en légère baisse, et la sous-performe
en cas de forte hausse.

### Le point commun

Reverse convertible, BRC et discount ont le même profil : **gain limité, perte potentiellement
importante**. L'investisseur est **vendeur de volatilité** : plus la volatilité est élevée au moment de
l'émission, plus le coupon ou la décote sont attractifs, mais plus le risque de baisse est grand.
""",
            "points_cles": [
                "Reverse convertible = ZC + coupons − put.",
                "BRC : put down-and-in, protégé tant que la barrière tient.",
                "Discount = action − call = ZC(K) − put.",
                "Gain plafonné, perte possible : profil vendeur de vol.",
            ],
        },
        # ------------------------------------------------------------------ 4
        {
            "id": "str-c4",
            "titre": "4. Les autocalls : Athena, Phoenix et variantes",
            "widget": "autocall",
            "contenu": r"""
Les autocalls sont parmi les produits structurés les plus vendus en Europe, en France notamment. Tous
reposent sur la même mécanique, mais le **versement des coupons** change d'un produit à l'autre.

### Le mécanisme commun

À chaque **date d'observation** (annuelle, semestrielle ou trimestrielle), on compare le niveau du
sous-jacent $S_t$ à son niveau initial $S_0$ :

- si $S_t / S_0 \ge$ **seuil de rappel** (souvent $100\,\%$), le produit est **remboursé par
  anticipation** : l'investisseur récupère 100 % plus le coupon prévu, et le produit s'arrête ;
- sinon, il continue jusqu'à la date suivante.

À la **maturité** (souvent 8 à 12 ans au maximum), s'il n'a jamais été rappelé :

$$
\text{Remboursement} =
\begin{cases}
100 \ (+\ \text{coupon éventuel}) & \text{si } S_T / S_0 \ge \text{seuil final} \\
100 & \text{si barrière} \le S_T / S_0 < \text{seuil final} \\
100 \times S_T / S_0 & \text{si } S_T / S_0 < \text{barrière de protection}
\end{cases}
$$

Sous la barrière (par exemple $60\,\%$), l'investisseur subit **toute** la baisse, pas seulement la
partie sous la barrière : à $55\,\%$, il récupère $55$. C'est l'**effet couperet**.

### Athena : le coupon payé au rappel

Le coupon n'est versé **qu'en cas de remboursement**, anticipé ou final, et il est **cumulé** sur toutes
les périodes écoulées (effet mémoire intégré). Profil : coupon potentiel élevé, mais **aucun revenu**
tant que le marché reste sous le seuil de rappel.

### Phoenix : un coupon même sans rappel

Le Phoenix verse un **coupon conditionnel** à chaque date d'observation si le sous-jacent est au-dessus
d'une **barrière de coupon** (par exemple $70\,\%$), plus basse que le seuil de rappel. Le rappel
anticipé rembourse 100 % (plus le coupon de la période), les coupons ayant déjà été versés au fil de
l'eau.

- Avantage : un revenu régulier même dans un marché stable ou en légère baisse.
- Contrepartie : à paramètres égaux, le coupon annuel est **plus faible** que celui d'un Athena, car
  il est payé dans beaucoup plus de scénarios.

### Phoenix mémoire

Un coupon non versé (sous-jacent sous la barrière de coupon) est mis **en mémoire** : à la prochaine
date où le sous-jacent repasse au-dessus, l'investisseur touche le coupon de la période **et** les
coupons manqués. Cette option a un coût : le coupon est un peu plus faible que celui d'un Phoenix sans
mémoire.

### Scénarios chiffrés

**Athena** : coupon $8\,\%$ par an, rappel à $100\,\%$, barrière de protection $60\,\%$ à maturité, 8 ans.

| Scénario | Trajectoire (niveau aux dates annuelles) | Résultat |
|---|---|---|
| Favorable | $105\,\%$ dès l'année 1 | Rappel : $108$ après 1 an |
| Rappel tardif | $90, 85, 95$ puis $102\,\%$ en année 4 | Rappel : $100 + 4 \times 8 = 132$ |
| Neutre | Autour de $80\,\%$ pendant 8 ans | $100$ après 8 ans, aucun coupon |
| Défavorable | Finit à $50\,\%$ | $50$ : perte de $50\,\%$ |

**Phoenix** : coupon $6\,\%$ par an, barrière de coupon $70\,\%$, rappel $100\,\%$, protection $60\,\%$.

| Scénario | Trajectoire | Sans mémoire | Avec mémoire |
|---|---|---|---|
| Favorable | $105\,\%$ en année 1 | $106$ | $106$ |
| Chahuté | $90, 75, 65, 98, 101\,\%$ | coupons $6+6+0+6+6$, puis rappel : total $124$ | coupon manqué de l'année 3 rattrapé en année 4 : total $130$ |
| Neutre | Autour de $80\,\%$ pendant 8 ans | $8 \times 6 + 100 = 148$ | $148$ |
| Défavorable | $90, 75$ puis sous $70\,\%$, finit à $50\,\%$ | $6 + 6 + 50 = 62$ | $62$ |

Le scénario « neutre » montre la différence clé : un Phoenix **rapporte** dans un marché qui stagne
sous son niveau initial, un Athena non.

### Les variantes courantes

| Variante | Principe | Effet |
|---|---|---|
| **Step-down (dégressif)** | Le seuil de rappel baisse à chaque date (100 %, 95 %, 90 %…) | Rappel plus probable, coupon plus faible |
| **Barrière à maturité ou en continu** | Protection observée seulement à $T$, ou chaque jour | En continu : plus risqué, donc coupon plus élevé |
| **Airbag** | Sous la barrière, la perte est amortie (par exemple $100 \times (S_T/S_0) / \text{barrière}$) | Pas d'effet couperet, coupon plus faible |
| **Worst-of** | Le produit suit la plus mauvaise de plusieurs actions | Coupon plus élevé, risque plus élevé |
| **Indice à décrément** | Indice qui retire chaque année un dividende fixe (en points ou en %) | Coupon plus élevé, mais l'indice monte structurellement moins vite |
| **Coupon fixe + autocall** | Coupon garanti la première année, puis Phoenix | Rassure le client, coût pris sur les coupons suivants |

Les formules exactes **varient selon les émetteurs** : il faut toujours lire la term sheet avant
d'expliquer un produit.

### Ce qui fait monter le coupon

L'investisseur est **vendeur d'un put down-and-in** (le risque sous la barrière) et reçoit des coupons
conditionnels (des options digitales). Le coupon est donc d'autant plus élevé que ce put vaut cher et
que le budget de taux est grand :

- **volatilité** élevée (le put vendu vaut plus) ;
- **taux** élevés (le zéro-coupon coûte moins cher) ;
- **dividendes** élevés ou indice à décrément (forward plus bas, put plus cher) ;
- **corrélation** faible dans un worst-of ;
- **barrière** plus haute, **seuil de rappel** plus haut, **maturité** plus longue.

Côté banque : la position inverse, **longue de volatilité et courte de corrélation**. Juste avant une
date d'observation ou près de la barrière, le gamma devient très grand et difficile à couvrir.
""",
            "points_cles": [
                "Athena : coupon cumulé payé seulement au rappel ou à maturité.",
                "Phoenix : coupon conditionnel versé si S ≥ barrière de coupon, même sans rappel.",
                "Mémoire : les coupons manqués sont rattrapés.",
                "Sous la barrière à maturité : toute la baisse est subie (effet couperet).",
            ],
        },
        # ------------------------------------------------------------------ 5
        {
            "id": "str-c6",
            "titre": "5. Produits à barrière : Twin Win, Bonus, Shark",
            "widget": "barrieres",
            "contenu": r"""
Ces produits n'ont pas de rappel anticipé : tout se joue à **maturité**, selon la performance finale
$x = S_T / S_0$ et selon que la **barrière** a été touchée ou non pendant la vie du produit (en
continu, ou seulement à certaines dates selon la documentation).

### Twin Win : gagner à la hausse comme à la baisse

Tant que la **barrière basse** (par exemple $60\,\%$) n'a jamais été touchée, l'investisseur gagne la
**valeur absolue** de la performance :

$$
\text{Twin Win} =
\begin{cases}
100 \times \big(1 + |x - 1|\big) & \text{barrière jamais touchée} \\
100 \times x & \text{barrière touchée}
\end{cases}
$$

| Scénario (barrière 60 %) | Remboursement |
|---|---|
| Action à $120\,\%$, barrière jamais touchée | $120$ |
| Action à $80\,\%$, barrière jamais touchée | $120$ : la baisse devient un gain |
| Action passée par $58\,\%$, finit à $75\,\%$ | $75$ |
| Action à $50\,\%$ | $50$ |

**Décomposition** : action (ou call de strike nul) $+\ 2$ puts **down-and-out** à la monnaie. Les deux
puts transforment la baisse en gain, la barrière désactivante les rend moins chers. Souvent, une partie
des dividendes sert à acheter des calls pour obtenir une participation à la hausse supérieure à
$100\,\%$. Vue de marché : **le marché bougera, mais sans krach**.

### Bonus : un gain minimum si la barrière tient

$$
\text{Bonus} =
\begin{cases}
100 \times \max(\text{bonus},\ x) & \text{barrière jamais touchée} \\
100 \times x & \text{barrière touchée}
\end{cases}
$$

| Scénario (bonus 120 %, barrière 70 %) | Remboursement |
|---|---|
| Action à $130\,\%$ | $130$ |
| Action à $90\,\%$, barrière jamais touchée | $120$ |
| Action passée par $68\,\%$, finit à $85\,\%$ | $85$ |

**Décomposition** : action $+$ put down-and-out de strike égal au niveau du bonus, financé par les
dividendes que l'investisseur abandonne. Les versions plafonnées (*capped bonus*) offrent un bonus plus
élevé en échange d'un gain maximal.

### Shark (requin) : capital garanti avec barrière haute

Le capital est garanti. L'investisseur participe à la hausse **tant qu'une barrière haute** (par
exemple $130\,\%$) n'a jamais été touchée ; sinon il ne reçoit qu'un **coupon fixe** (le *rebate*).

$$
\text{Shark} =
\begin{cases}
100 \times \big(1 + p \times \max(x - 1,\ 0)\big) & \text{barrière haute jamais touchée} \\
100 \times (1 + \text{rebate}) & \text{barrière touchée}
\end{cases}
$$

| Scénario (barrière 130 %, participation 100 %, rebate 5 %) | Remboursement |
|---|---|
| Action à $120\,\%$, barrière jamais touchée | $120$ |
| Action passée par $135\,\%$, finit à $125\,\%$ | $105$ |
| Action à $80\,\%$ | $100$ |

**Décomposition** : zéro-coupon $+$ call **up-and-out** avec rebate. La barrière rend le call bien moins
cher, ce qui permet une participation élevée. Vue de marché : **hausse modérée**. Le profil a la forme
d'un aileron de requin, d'où son nom.

### Récapitulatif des produits du module

| Produit | Vue de marché | Capital | Option clé pour l'investisseur |
|---|---|---|---|
| Capital garanti | Hausse | Garanti | Call acheté |
| Shark | Hausse modérée | Garanti | Call up-and-out acheté |
| Reverse convertible | Stable | À risque | Put vendu |
| Reverse convertible à barrière | Stable, baisse limitée | À risque sous la barrière | Put down-and-in vendu |
| Discount | Stable | À risque | Call vendu (sur l'action détenue) |
| Athena / Phoenix | Stable ou hausse modérée | À risque sous la barrière | Put down-and-in vendu + digitales |
| Twin Win | Mouvement fort, sans krach | À risque si barrière touchée | 2 puts down-and-out achetés |
| Bonus | Stable ou hausse, sans krach | À risque si barrière touchée | Put down-and-out acheté |
""",
            "points_cles": [
                "Twin Win : 100·(1 + |x − 1|) si la barrière basse n'est jamais touchée.",
                "Bonus : 100·max(bonus, x) si la barrière basse n'est jamais touchée.",
                "Shark : capital garanti, participation tant que la barrière haute tient, sinon rebate.",
                "Barrière touchée (Twin Win, Bonus) : on finit comme l'action.",
            ],
        },
        # ------------------------------------------------------------------ 6
        {
            "id": "str-c5",
            "titre": "6. Options exotiques",
            "contenu": r"""
Les produits structurés sont fabriqués avec ces briques. En entretien de structuration, on attend que
tu saches dire **pourquoi** chacune est moins chère ou plus chère qu'une vanille.

### Options à barrière

Elles sont activées (*knock-in*) ou désactivées (*knock-out*) si le sous-jacent touche un niveau $B$
pendant leur vie. Quatre familles : up-and-in, up-and-out, down-and-in, down-and-out. Relation
fondamentale (même strike, même barrière, même maturité, sans rebate) :

$$
\text{knock-in} + \text{knock-out} = \text{vanille}
$$

Une barrière rend donc l'option **moins chère** que la vanille. Près de la barrière, delta et gamma
peuvent devenir très importants, et une option knock-out peut avoir un **vega négatif** (plus de vol
augmente la probabilité de toucher la barrière).

### Options digitales (binaires)

Une digitale *cash-or-nothing* paie un montant fixe $Q$ si $S_T > K$. En Black-Scholes :

$$
\text{Digitale call} = Q\, e^{-rT} N(d_2)
$$

En pratique, on la réplique par un **call spread** très serré, ce qui fait apparaître la sensibilité
au **skew** de volatilité. Les coupons conditionnels des autocalls sont des digitales.

### Options asiatiques

Le payoff porte sur la **moyenne** des cours sur une période. La moyenne varie moins que le cours
final : l'option est en général **moins chère** qu'une vanille de même strike, et moins exposée à un
pic de prix le dernier jour. Usage courant en matières premières et dans les capitaux garantis.

### Cliquets

Le gain est la somme (ou le produit) de performances **périodiques**, chacune éventuellement
plafonnée et planchée, par exemple :
$\sum_{i} \min\big(\max(S_{t_i}/S_{t_{i-1}} - 1,\ \text{plancher}),\ \text{cap}\big)$.
Le strike est remis à jour à chaque période : l'investisseur « verrouille » ses gains. Ces produits
sont très sensibles à la **volatilité future** (forward volatility).

### Lookback

Le payoff dépend du **maximum** (ou du minimum) atteint par le sous-jacent, par exemple
$\max_t S_t - K$ : on achète « au plus bas » ou on vend « au plus haut ». Toujours plus cher qu'une
vanille.

### Range accrual

Le coupon s'accumule pour chaque jour où un taux ou un indice reste **dans une fourchette** :
$\text{coupon} \times \frac{\text{jours dans la fourchette}}{\text{jours totaux}}$. Équivalent à une
série de digitales journalières. Vue de marché : marché calme.

### Panier, worst-of, best-of

- un call sur **panier** est moins cher qu'un panier de calls (la diversification réduit la
  volatilité du panier) ;
- un put **worst-of** est plus cher qu'un put sur un seul sous-jacent, et d'autant plus que la
  corrélation est faible ;
- un call **best-of** est plus cher qu'un call sur un seul sous-jacent.

### Quanto

Option sur un sous-jacent étranger payée dans une autre devise à un taux de change fixé d'avance :
l'investisseur n'a pas de risque de change, mais le prix dépend de la **corrélation** entre le
sous-jacent et la devise.
""",
            "points_cles": [
                "Knock-in + knock-out = vanille.",
                "Digitale = Q · e^(−rT) · N(d₂), répliquée par un call spread serré.",
                "Asiatique : moyenne ⇒ moins volatile ⇒ moins chère.",
                "Cliquet : sensible à la volatilité future ; lookback : toujours plus cher.",
            ],
        },
        # ------------------------------------------------------------------ 7
        {
            "id": "str-c7",
            "titre": "7. Présenter un produit : scénarios et méthode",
            "contenu": r"""
En entretien de **sales** ou de **structuration**, on te demandera souvent : « Un client veut… que
lui proposez-vous ? » ou « Pitchez-moi ce produit. » Voici une méthode.

### 1. Partir du besoin du client

| Besoin du client | Produit naturel |
|---|---|
| Ne rien perdre, profiter de la hausse | Capital garanti, Shark |
| Un revenu régulier, accepte un risque en capital | Phoenix (mémoire), reverse convertible à barrière |
| Un rendement élevé, peut attendre | Athena |
| Pense que le marché va bouger fortement | Twin Win |
| Marché stable, veut mieux qu'une action | Bonus, discount |
| Couvrir un portefeuille d'actions | Achat de puts, put spread, collar |

### 2. Présenter le produit en trois phrases

1. **Ce que le client gagne** et dans quel scénario.
2. **Ce qu'il risque** et dans quel scénario (le pire cas, chiffré).
3. **Ce qu'il abandonne** pour obtenir ce profil (dividendes, hausse au-delà d'un niveau, liquidité).

Exemple pour un Phoenix mémoire 8 ans sur indice, coupon $6\,\%$, barrière de coupon $70\,\%$,
protection $60\,\%$ : « Vous recevez $6\,\%$ par an tant que l'indice ne perd pas plus de $30\,\%$,
et les coupons manqués sont rattrapés. Le produit s'arrête dès que l'indice repasse au-dessus de son
niveau initial à une date annuelle. Si, après 8 ans, l'indice a perdu plus de $40\,\%$, vous subissez
toute la baisse. Vous renoncez aux dividendes et à la hausse au-delà des coupons. »

### 3. Dérouler les scénarios

Toujours au moins trois : **favorable**, **médian**, **défavorable**, chiffrés et avec la **durée**
(un rappel rapide et un remboursement à 100 % après 10 ans n'ont pas du tout la même valeur). Ajouter le
**défaut de l'émetteur** pour tout produit.

### 4. Justifier les paramètres par le marché

« Le coupon est attractif aujourd'hui parce que la volatilité implicite est élevée et que les taux
permettent un zéro-coupon moins cher. » Montrer que tu relies le produit aux **conditions de marché** :
taux, volatilité, dividendes, corrélation, spread de l'émetteur.

### 5. Anticiper les objections

- « Et si le marché baisse de 50 % ? » → le scénario défavorable, sans détour.
- « Pourquoi ne pas acheter l'indice directement ? » → la protection conditionnelle et le coupon
  dans les marchés stables, contre l'abandon des dividendes et de la forte hausse.
- « Puis-je sortir avant ? » → marché secondaire assuré par l'émetteur, prix fonction du marché.

### Erreurs à éviter

- dire « capital garanti » sans mentionner le **risque émetteur** ;
- présenter un coupon conditionnel comme un coupon **garanti** ;
- oublier l'**effet couperet** sous la barrière ;
- ignorer la **durée** dans le calcul du rendement.
""",
            "points_cles": [
                "Partir du besoin du client, pas du produit.",
                "Gain, risque, renoncement : trois phrases.",
                "Scénarios favorable / médian / défavorable chiffrés, durée incluse.",
                "Toujours citer le risque émetteur et l'effet couperet.",
            ],
        },
    ],
    "quiz": [
        {"id": "str-q01", "type": "nombre",
         "question": r"Prix d'un zéro-coupon 5 ans de nominal $100$, taux annuel $3\,\%$ ? (2 décimales)",
         "reponse": 86.26, "tolerance": 0.05,
         "explication": r"$100 / 1{,}03^5 \approx 86{,}26$."},
        {"id": "str-q02", "type": "nombre",
         "question": r"Capital garanti : zéro-coupon à $87$, marge $1$, call ATM à $20$ (en % du nominal). "
                     r"Taux de participation en % ?",
         "reponse": 60, "tolerance": 0.5,
         "explication": r"Budget $= 100 - 87 - 1 = 12$, participation $= 12 / 20 = 60\,\%$."},
        {"id": "str-q03", "type": "qcm",
         "question": "Les taux d'intérêt montent, toutes choses égales par ailleurs. La participation d'un capital garanti…",
         "choix": ["baisse", "augmente", "ne change pas", "devient négative"],
         "reponse": 1,
         "explication": "Le zéro-coupon coûte moins cher : il reste plus de budget pour les options."},
        {"id": "str-q04", "type": "qcm",
         "question": "La volatilité implicite monte. Effet sur la participation d'un capital garanti ?",
         "choix": ["Elle augmente", "Elle baisse", "Aucun effet", "Elle dépend uniquement des taux"],
         "reponse": 1,
         "explication": "Les calls achetés sont plus chers : le même budget en achète moins."},
        {"id": "str-q05", "type": "qcm",
         "question": "Quelle décomposition correspond à un reverse convertible ?",
         "choix": ["Zéro-coupon + call acheté", "Zéro-coupon + coupons − put vendu",
                   "Action + put acheté", "Deux calls de strikes différents"],
         "reponse": 1,
         "explication": "Le coupon élevé est financé par le put que l'investisseur vend implicitement."},
        {"id": "str-q06", "type": "nombre",
         "question": r"Certificat discount sur une action à $50$, cap à $55$. Le call de strike $55$ vaut $3$. "
                     r"Prix du certificat ?",
         "reponse": 47, "tolerance": 0.001,
         "explication": r"Discount $=$ action $-$ call $= 50 - 3 = 47$."},
        {"id": "str-q07", "type": "qcm",
         "question": "Même strike, même barrière, même maturité, sans rabais : un call knock-in plus un call knock-out valent…",
         "choix": ["zéro", "un call vanille", "deux calls vanille", "une digitale"],
         "reponse": 1,
         "explication": "Dans chaque scénario, exactement l'une des deux options est vivante à maturité."},
        {"id": "str-q08", "type": "nombre",
         "question": r"Digitale cash-or-nothing qui paie $100$ si $S_T > K$, taux nuls, $N(d_2) = 0{,}45$. Prix ?",
         "reponse": 45, "tolerance": 0.001,
         "explication": r"$100 \times e^{0} \times 0{,}45 = 45$."},
        {"id": "str-q09", "type": "qcm",
         "question": "Pourquoi une option asiatique est-elle en général moins chère qu'une vanille de même strike ?",
         "choix": ["Elle a une maturité plus courte", "La moyenne des cours est moins volatile que le cours final",
                   "Elle ne peut pas finir dans la monnaie", "Elle n'a pas de vega"],
         "reponse": 1,
         "explication": "Moyenner lisse les variations : la distribution du sous-jacent effectif est plus resserrée."},
        {"id": "str-q10", "type": "qcm",
         "question": "Dans un autocall classique avec barrière de protection, l'investisseur est principalement…",
         "choix": ["acheteur d'un call", "vendeur d'un put down-and-in", "acheteur d'un put", "vendeur d'un call up-and-out"],
         "reponse": 1,
         "explication": "Il perd en capital seulement si le sous-jacent finit sous la barrière : c'est un put down-and-in vendu."},
        {"id": "str-q11", "type": "qcm",
         "question": "Autocall worst-of sur trois actions : quelle est l'exposition de l'investisseur à la corrélation ?",
         "choix": ["Short corrélation", "Long corrélation", "Aucune", "Long uniquement si la vol baisse"],
         "reponse": 1,
         "explication": "Une corrélation faible augmente la chance qu'une des actions chute : l'investisseur préfère une corrélation élevée."},
        {"id": "str-q12", "type": "nombre",
         "question": r"Athena, coupon $8\,\%$ par an, rappel à $100\,\%$. L'indice est sous son niveau initial les années "
                     r"1 et 2, à $103\,\%$ en année 3. Montant reçu (pour 100) ?",
         "reponse": 124, "tolerance": 0.001,
         "explication": r"Rappel en année 3 avec coupons cumulés : $100 + 3 \times 8 = 124$."},
        {"id": "str-q13", "type": "qcm",
         "question": "Quelle est la différence principale entre un Athena et un Phoenix ?",
         "choix": ["L'Athena a une barrière de protection, pas le Phoenix",
                   "Le Phoenix verse un coupon conditionnel même sans rappel ; l'Athena ne paie qu'au rappel ou à maturité",
                   "Le Phoenix est toujours à capital garanti",
                   "L'Athena n'a pas de rappel anticipé"],
         "reponse": 1,
         "explication": "Les deux ont un rappel et une barrière ; seul le mode de versement des coupons change."},
        {"id": "str-q14", "type": "nombre",
         "question": r"Phoenix mémoire, coupon $7\,\%$ par an, barrière de coupon $70\,\%$, rappel $100\,\%$. "
                     r"Année 1 : $65\,\%$. Année 2 : $80\,\%$. Montant versé en année 2 (pour 100) ?",
         "reponse": 14, "tolerance": 0.001,
         "explication": r"Coupon de l'année 2 plus coupon manqué de l'année 1 : $2 \times 7 = 14$ ; pas de rappel ($80\,\% < 100\,\%$)."},
        {"id": "str-q15", "type": "nombre",
         "question": r"Athena, barrière de protection $60\,\%$ à maturité, seuil final $100\,\%$, jamais rappelé. "
                     r"L'indice finit à $80\,\%$. Remboursement (pour 100) ?",
         "reponse": 100, "tolerance": 0.001,
         "explication": "Entre la barrière et le seuil : capital remboursé, mais aucun coupon."},
        {"id": "str-q16", "type": "nombre",
         "question": r"Même Athena, l'indice finit à $55\,\%$. Remboursement (pour 100) ?",
         "reponse": 55, "tolerance": 0.001,
         "explication": "Sous la barrière, toute la baisse est subie (effet couperet) : 55."},
        {"id": "str-q17", "type": "qcm",
         "question": "Un autocall step-down par rapport à un autocall à seuil fixe…",
         "choix": ["a un coupon plus élevé et un rappel moins probable",
                   "a un rappel plus probable et un coupon plus faible",
                   "n'a plus de barrière de protection",
                   "est à capital garanti"],
         "reponse": 1,
         "explication": "Le seuil de rappel baisse avec le temps : plus de chances d'être rappelé, ce qui se paie par un coupon plus bas."},
        {"id": "str-q18", "type": "nombre",
         "question": r"Twin Win, barrière basse $60\,\%$ jamais touchée. L'action finit à $75\,\%$. Remboursement (pour 100) ?",
         "reponse": 125, "tolerance": 0.001,
         "explication": r"$100 \times (1 + |0{,}75 - 1|) = 125$ : la baisse devient un gain."},
        {"id": "str-q19", "type": "nombre",
         "question": r"Même Twin Win, mais l'action est passée par $55\,\%$ et finit à $75\,\%$. Remboursement ?",
         "reponse": 75, "tolerance": 0.001,
         "explication": "Barrière touchée : les puts down-and-out sont désactivés, on finit comme l'action."},
        {"id": "str-q20", "type": "qcm",
         "question": "Quelle est la décomposition d'un Twin Win ?",
         "choix": ["Zéro-coupon + call", "Action + 2 puts down-and-out à la monnaie",
                   "Action − call", "Zéro-coupon − put down-and-in"],
         "reponse": 1,
         "explication": "Sans activation de la barrière, les deux puts rendent 2 × la baisse, ce qui transforme −x en +x."},
        {"id": "str-q21", "type": "nombre",
         "question": r"Bonus $120\,\%$, barrière $70\,\%$ jamais touchée, l'action finit à $110\,\%$. Remboursement ?",
         "reponse": 120, "tolerance": 0.001,
         "explication": r"$100 \times \max(1{,}20 ; 1{,}10) = 120$."},
        {"id": "str-q22", "type": "nombre",
         "question": r"Shark : barrière haute $130\,\%$, participation $100\,\%$, rebate $5\,\%$. "
                     r"L'action monte à $135\,\%$ puis finit à $125\,\%$. Remboursement ?",
         "reponse": 105, "tolerance": 0.001,
         "explication": "La barrière haute a été touchée : seul le rebate est versé, 100 + 5."},
        {"id": "str-q23", "type": "qcm",
         "question": "Quel produit rapporte dans un marché qui stagne à 85 % de son niveau initial pendant 8 ans ?",
         "choix": ["Un Athena (rappel à 100 %)", "Un Phoenix (barrière de coupon 70 %)",
                   "Un capital garanti", "Un Shark"],
         "reponse": 1,
         "explication": "Le Phoenix verse son coupon tant que l'indice est au-dessus de 70 % ; l'Athena ne paie rien sans rappel."},
        {"id": "str-q24", "type": "qcm",
         "question": "Un client présente un « capital garanti ». Quel risque devez-vous toujours mentionner ?",
         "choix": ["Le risque de change uniquement", "Le risque de crédit de l'émetteur",
                   "Aucun, le capital est garanti", "Le risque de taux à maturité"],
         "reponse": 1,
         "explication": "Le produit est une dette de l'émetteur : la garantie dépend de sa solvabilité."},
    ],
    "flashcards": [
        {"id": "str-f01", "recto": "Décomposition d'un produit structuré",
         "verso": "Zéro-coupon + options + marge de l'émetteur."},
        {"id": "str-f02", "recto": "Taux de participation d'un capital garanti",
         "verso": r"$p = (100 - ZC - \text{marge}) / C_{ATM}$"},
        {"id": "str-f03", "recto": "Reverse convertible", "verso": "Zéro-coupon + coupons − put : l'investisseur est vendeur de volatilité."},
        {"id": "str-f04", "recto": "Certificat discount", "verso": r"Action − call($K$) $=$ zéro-coupon($K$) − put($K$)."},
        {"id": "str-f05", "recto": "Parité des barrières", "verso": "Knock-in + knock-out = vanille (même strike, barrière, maturité)."},
        {"id": "str-f06", "recto": "Prix Black-Scholes d'une digitale cash-or-nothing",
         "verso": r"$Q\, e^{-rT} N(d_2)$"},
        {"id": "str-f07", "recto": "Expositions de la banque qui vend des autocalls worst-of",
         "verso": "Longue de volatilité, courte de corrélation."},
        {"id": "str-f08", "recto": "Pourquoi les capitaux garantis sont-ils rares quand les taux sont nuls ?",
         "verso": "Le zéro-coupon coûte presque 100 : il ne reste presque pas de budget pour les options."},
        {"id": "str-f09", "recto": "Athena", "verso": "Autocall dont le coupon, cumulé, n'est payé qu'au rappel anticipé ou à maturité."},
        {"id": "str-f10", "recto": "Phoenix",
         "verso": "Autocall qui verse un coupon conditionnel à chaque date si le sous-jacent est au-dessus de la barrière de coupon, même sans rappel."},
        {"id": "str-f11", "recto": "Effet mémoire", "verso": "Les coupons non versés sont rattrapés à la prochaine date où la condition est remplie."},
        {"id": "str-f12", "recto": "Effet couperet",
         "verso": "Sous la barrière de protection à maturité, l'investisseur subit toute la baisse depuis 100 %, pas seulement sous la barrière."},
        {"id": "str-f13", "recto": "Step-down", "verso": "Seuil de rappel dégressif : rappel plus probable, coupon plus faible."},
        {"id": "str-f14", "recto": "Twin Win",
         "verso": r"$100 (1 + |x - 1|)$ si la barrière basse n'est jamais touchée, sinon $100\,x$ ; action + 2 puts down-and-out."},
        {"id": "str-f15", "recto": "Bonus",
         "verso": r"$100 \max(\text{bonus}, x)$ si la barrière n'est jamais touchée, sinon $100\,x$ ; action + put down-and-out."},
        {"id": "str-f16", "recto": "Shark (requin)",
         "verso": "Capital garanti + call up-and-out : participation tant que la barrière haute tient, sinon rebate fixe."},
        {"id": "str-f17", "recto": "Indice à décrément",
         "verso": "Indice qui retire un dividende fixe chaque année : forward plus bas, coupon plus élevé, indice structurellement pénalisé."},
        {"id": "str-f18", "recto": "Cliquet", "verso": "Somme de performances périodiques plafonnées/planchées ; sensible à la volatilité future."},
        {"id": "str-f19", "recto": "Range accrual", "verso": "Coupon × proportion des jours où le sous-jacent reste dans une fourchette."},
        {"id": "str-f20", "recto": "Présenter un produit en 3 phrases",
         "verso": "Ce que le client gagne, ce qu'il risque (chiffré), ce à quoi il renonce."},
    ],
}
