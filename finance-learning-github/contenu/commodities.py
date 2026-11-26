"""Module : Matières premières (Commodities)."""

MODULE = {
    "id": "commodities",
    "titre": "Matières premières (Commodities)",
    "icone": "🛢️",
    "statut": "complet",
    "resume": "Énergie, métaux, agricoles : acteurs et places de marché, formation des prix, courbe des futures "
              "(contango, backwardation, roll yield), spreads (crack, spark, crush), couverture, or, investissement.",
    "chapitres": [
        # ------------------------------------------------------------------ 1
        {
            "id": "com-c1",
            "titre": "1. Panorama : les produits, les places, les acteurs",
            "contenu": r"""
### Les grandes familles

| Famille | Exemples | Places et contrats de référence | Unités |
|---|---|---|---|
| **Énergie** | Pétrole brut, produits raffinés (essence, diesel, kérosène), gaz naturel, électricité, charbon | Brent (ICE), WTI (NYMEX), gaz TTF (Europe), Henry Hub (États-Unis) | Baril ($\approx 159$ litres), MMBtu, MWh |
| **Métaux précieux** | Or, argent, platine, palladium | COMEX, marché de gré à gré de Londres | Once troy ($31{,}1$ g) |
| **Métaux industriels** | Cuivre, aluminium, nickel, zinc | **LME** (London Metal Exchange), COMEX | Tonne |
| **Agricoles : céréales et oléagineux** | Blé, maïs, soja, colza | CBOT (Chicago), Euronext (blé de meunerie) | Boisseau (*bushel*), tonne |
| **Agricoles : *softs*** | Café, cacao, sucre, coton | ICE | Livre, tonne |
| **Élevage** | Bovins, porcs | CME | Livre |
| **Émissions** | Quotas de CO₂ (système européen EU ETS) | ICE Endex | Tonne de CO₂ |

Les deux pétroles de référence : le **Brent** (mer du Nord, référence pour la majorité du pétrole
mondial) et le **WTI** (*West Texas Intermediate*, livré à Cushing, aux États-Unis).

### Physique contre financier

Les matières premières sont des biens **physiques** : il faut les produire, les transporter, les
stocker, les assurer. Beaucoup de futures prévoient une **livraison physique** ; les investisseurs
financiers doivent donc fermer ou rouler leurs positions avant l'échéance.

### Les acteurs

- **Producteurs** (compagnies pétrolières, mines, agriculteurs) : vendent à terme pour sécuriser leurs revenus.
- **Consommateurs** (compagnies aériennes, raffineurs, industriels, agroalimentaire) : achètent à terme
  pour sécuriser leurs coûts.
- **Négociants** (*trading houses* comme Vitol, Trafigura, Glencore, Gunvor, Cargill) : achètent,
  transportent, stockent et revendent ; ils gagnent sur les écarts de lieu, de temps et de qualité.
- **Banques** : couverture de leurs clients, financement du commerce, produits dérivés.
- **Investisseurs** : fonds indiciels, fonds de gestion systématique (CTA), hedge funds spécialisés.

### Les métiers en banque

Sales et traders commodities (souvent par énergie, métaux, agricoles), structureurs de solutions de
couverture pour les entreprises, financement du négoce (*trade finance*), analystes et stratégistes
matières premières.
""",
            "points_cles": [
                "Énergie, métaux précieux, métaux industriels, agricoles, élevage, émissions.",
                "Références : Brent et WTI (pétrole), TTF et Henry Hub (gaz), LME (métaux).",
                "Biens physiques : stockage, transport, livraison.",
                "Producteurs vendent à terme, consommateurs achètent à terme, négociants font le lien.",
            ],
        },
        # ------------------------------------------------------------------ 2
        {
            "id": "com-c2",
            "titre": "2. Ce qui fait bouger les prix",
            "contenu": r"""
Les prix des matières premières sont d'abord fixés par **l'offre et la demande physiques**, avec une
particularité : à court terme, l'une comme l'autre réagissent très peu au prix (on ne construit pas une
mine ni on ne change de chaudière en un mois). D'où des prix **très volatils**.

### Côté offre

- **Décisions des producteurs** : pour le pétrole, les quotas de l'**OPEP+** (OPEP et alliés, dont la Russie).
- **Géopolitique** : conflits, sanctions, routes maritimes (détroits, canaux).
- **Météo et climat** : récoltes, sécheresses, gel ; vagues de froid pour le gaz.
- **Coûts de production** : à long terme, le prix tend vers le **coût marginal** du producteur le plus cher
  dont on a besoin (la « courbe de coûts »).
- **Investissement passé** : des années de sous-investissement réduisent l'offre future.

### Côté demande

- **Croissance mondiale**, en particulier chinoise pour les métaux (la Chine consomme une part majeure du
  cuivre mondial).
- **Saisonnalité** : chauffage l'hiver (gaz), conduite l'été (essence), récoltes.
- **Transition énergétique** : demande croissante de cuivre, lithium, nickel ; incertitude sur le pétrole à long terme.
- **Substitutions** : passage du gaz au charbon quand le gaz est trop cher, par exemple.

### Les stocks, variable clé

Des stocks **bas** rendent le marché tendu : les prix comptant montent plus que les prix à terme (la
courbe passe en **backwardation**). Des stocks **élevés** pèsent sur les prix et mettent la courbe en
**contango**. Les traders suivent les publications hebdomadaires de stocks (par exemple les stocks de
pétrole américains).

### Le dollar et les taux

La plupart des matières premières se cotent en **dollars** : un dollar faible les rend moins chères pour
les autres pays et soutient la demande (relation inverse fréquente, pas systématique). Des taux réels
élevés augmentent le coût de détention des stocks, et pèsent particulièrement sur l'**or**.

### Scénarios

| Événement | Effet typique |
|---|---|
| L'OPEP+ annonce une baisse de production surprise | Pétrole ↑, courbe plus en backwardation |
| Ralentissement de l'économie chinoise | Cuivre et minerai de fer ↓ |
| Sécheresse dans une grande région productrice | Céréales concernées ↑ |
| Hiver doux en Europe | Gaz européen ↓, stocks élevés |
| Forte baisse du dollar | Soutien à la plupart des matières premières |
| Crise géopolitique sur une route maritime majeure | Pétrole et fret ↑, primes de risque |
""",
            "points_cles": [
                "Offre et demande peu réactives à court terme ⇒ forte volatilité.",
                "Stocks bas ⇒ backwardation ; stocks élevés ⇒ contango.",
                "Long terme : le prix tend vers le coût marginal de production.",
                "Dollar faible ⇒ soutien fréquent aux matières premières.",
            ],
        },
        # ------------------------------------------------------------------ 3
        {
            "id": "com-c3",
            "titre": "3. La courbe des futures : contango, backwardation et roll yield",
            "widget": "courbe_commodity",
            "contenu": r"""
### Le prix à terme

Détenir une matière première coûte du **financement** ($r$) et du **stockage** ($u$), mais rapporte un
**rendement d'opportunité** (*convenience yield*, $y$) : l'avantage d'avoir le bien physique sous la main
(éviter une rupture d'approvisionnement). D'où :

$$
F = S\, e^{(r + u - y)\,T}
$$

- **Contango** : $F > S$ ($r + u > y$). Marché bien approvisionné, stocks élevés.
- **Backwardation** : $F < S$ ($y > r + u$). Marché tendu, le physique immédiat vaut plus cher.

Exemple : pétrole à $80$ \$, $r = 4\,\%$, stockage $2\,\%$, convenience yield $1\,\%$ : future 1 an
$= 80\, e^{0{,}05} \approx 84{,}10$ \$ (contango).

### Le rendement d'un investisseur en futures

Un investisseur qui garde une position longue en **roulant** ses futures obtient :

$$
\text{Rendement total} \approx \text{variation du prix spot} + \text{roll yield} + \text{rendement du collatéral}
$$

- Le **roll yield** est **négatif en contango** (on revend le contrat proche moins cher qu'on n'achète le
  suivant) et **positif en backwardation**.
- Le **rendement du collatéral** : la trésorerie non utilisée (seule la marge est déposée) est placée au
  taux court.

Exemple : spot stable à $80$, future 1 mois à $81$. Chaque mois, l'investisseur long vend son contrat qui
converge vers $80$ et rachète le suivant à $81$ : il perd environ $1$ \$ par mois, soit plus de $14\,\%$
par an, **sans que le prix spot ait bougé**.

### Un cas extrême : le prix négatif du WTI (avril 2020)

Le 20 avril 2020, à la veille de son échéance, le contrat WTI de mai a clôturé à $-37{,}63$ \$ le baril.
Avec l'effondrement de la demande (pandémie) et des capacités de stockage à Cushing presque saturées,
les détenteurs de contrats longs qui ne pouvaient pas recevoir le pétrole ont dû payer pour s'en
débarrasser. Leçon : un future à livraison physique n'est **pas** un actif financier comme un autre,
et le stockage peut devenir la contrainte décisive (« super-contango »).

### Lire une courbe en entretien

- Pente positive forte : surabondance, stockage rentable (*cash-and-carry* : acheter comptant, stocker,
  vendre à terme).
- Pente négative : tension, le marché paie pour avoir le produit tout de suite.
- Les courbes de gaz et d'électricité ont en plus une forte **saisonnalité** (hiver plus cher).
""",
            "points_cles": [
                "F = S·e^((r + u − y)T) : financement + stockage − convenience yield.",
                "Contango : F > S, stocks élevés ; backwardation : F < S, marché tendu.",
                "Rendement = spot + roll yield + collatéral ; roll yield < 0 en contango.",
                "WTI à −37,63 $ le 20 avril 2020 : stockage saturé.",
            ],
        },
        # ------------------------------------------------------------------ 4
        {
            "id": "com-c4",
            "titre": "4. Les spreads : raffinage, électricité, trituration, lieu",
            "contenu": r"""
Beaucoup d'acteurs ne sont pas exposés à **un** prix, mais à un **écart** entre prix : un raffineur
achète du brut et vend des produits, une centrale achète du gaz et vend de l'électricité.

### Crack spread : la marge de raffinage

Le **crack spread 3:2:1** suppose qu'avec 3 barils de brut on produit 2 barils d'essence et 1 baril de
diesel :

$$
\text{Crack 3:2:1} = \frac{2 \times P_{essence} + 1 \times P_{diesel} - 3 \times P_{brut}}{3}
\quad \text{(en \$ par baril)}
$$

Exemple : brut $80$ \$, essence $100$ \$, diesel $110$ \$ (par baril) :
$(200 + 110 - 240) / 3 \approx 23{,}3$ \$ par baril de marge brute.

### Spark spread : la marge d'une centrale à gaz

$$
\text{Spark spread} = P_{électricité} - \text{heat rate} \times P_{gaz}
$$

Le *heat rate* est la quantité de gaz nécessaire pour produire 1 MWh d'électricité (2 pour un rendement
de $50\,\%$). Exemple : électricité $90$ €/MWh, gaz $35$ €/MWh, heat rate $2$ : $90 - 70 = 20$ €/MWh.

Le **clean spark spread** retranche aussi le coût du CO₂ : avec $0{,}37$ t de CO₂ émise par MWh et un
quota à $70$ €/t, le coût est d'environ $26$ €/MWh : la centrale **perd** alors environ $6$ €/MWh. Le
**dark spread** est l'équivalent pour une centrale à charbon.

### Crush spread : la trituration du soja

Écart entre la valeur des produits (tourteau et huile de soja) et celle des graines de soja : la marge
des usines de trituration.

### Spreads de lieu, de qualité et de temps

- **Lieu** : Brent contre WTI (coût du transport, contraintes d'export).
- **Qualité** : brut léger et peu soufré contre brut lourd et soufré.
- **Temps** (*calendar spread*) : écart entre deux échéances, pari sur la pente de la courbe ;
  par exemple long décembre, short juin sur le gaz pour parier sur un hiver tendu.

Les négociants et les traders vivent largement de ces spreads : ils arbitrent dans l'espace (transport),
dans le temps (stockage) et en qualité (mélange, transformation).
""",
            "points_cles": [
                "Crack 3:2:1 = (2·essence + diesel − 3·brut)/3.",
                "Spark spread = électricité − heat rate × gaz ; clean = − coût du CO₂.",
                "Spreads de lieu (Brent/WTI), de qualité, de temps (calendar).",
                "Raffineurs et centrales sont exposés à des écarts, pas à un seul prix.",
            ],
        },
        # ------------------------------------------------------------------ 5
        {
            "id": "com-c5",
            "titre": "5. Couvrir un risque de matière première",
            "contenu": r"""
### Les outils

| Outil | Principe | Particularité |
|---|---|---|
| **Futures** | Achat / vente à terme standardisée | Liquides, marges quotidiennes, risque de base si le produit diffère |
| **Swaps** | Prix fixe contre prix variable, réglés en cash | Sur mesure, souvent sur un **prix moyen** mensuel |
| **Options** | Calls (plafond), puts (plancher) | Souvent **asiatiques** (sur la moyenne du mois), moins chères |
| **Collars** | Achat d'une option financé par la vente d'une autre | Prime nette faible ou nulle |
| **Contrats physiques indexés** | Prix de livraison fixé selon une formule | Combinés avec des dérivés financiers |

Les options asiatiques dominent car les entreprises achètent ou vendent **en continu** : c'est le prix
moyen qui les concerne, pas le prix d'un jour.

### Exemple : un producteur de cuivre

Une mine produira $10\,000$ tonnes l'an prochain et craint une baisse des prix.
- **Vente à terme ou swap** à $9\,000$ \$ la tonne : revenu figé à $90$ M\$.
- **Achat de puts** de strike $8\,500$ \$ : plancher de revenu, le producteur garde la hausse, mais paie une prime.
- **Collar** : achat du put $8\,500$, vente du call $10\,000$ : prix effectif entre $8\,500$ et $10\,000$ \$.

| Prix moyen du cuivre | Sans couverture | Vente à terme à 9 000 | Collar 8 500 / 10 000 |
|---|---|---|---|
| 7 500 \$ | 75 M\$ | 90 M\$ | 85 M\$ |
| 9 000 \$ | 90 M\$ | 90 M\$ | 90 M\$ |
| 11 000 \$ | 110 M\$ | 90 M\$ | 100 M\$ |

### Exemple : une compagnie aérienne

Elle couvre souvent une partie de sa consommation de kérosène sur 12 à 24 mois avec des swaps et des
options sur le **brut** ou le **gasoil**, plus liquides que le kérosène : il reste un **risque de base**.
On ne couvre jamais 100 % : si les prix chutent, une couverture trop large fait payer le carburant plus
cher que les concurrents non couverts.

### Les pièges

- **Risque de base** : le produit couvert et l'instrument ne bougent pas exactement ensemble.
- **Liquidité** : une couverture en futures peut provoquer de gros appels de marge si les prix bougent
  contre la position, même si elle compense une exposition physique. Les cas célèbres de pertes viennent
  souvent d'un **décalage de trésorerie**, pas d'une mauvaise idée de couverture.
- **Volume incertain** : une récolte ratée laisse un agriculteur « sur-couvert ».
""",
            "points_cles": [
                "Futures, swaps (souvent sur prix moyen), options asiatiques, collars.",
                "Producteur : vend à terme ou achète des puts ; consommateur : achète à terme ou des calls.",
                "Risque de base, appels de marge, volume incertain.",
            ],
        },
        # ------------------------------------------------------------------ 6
        {
            "id": "com-c6",
            "titre": "6. L'or et les métaux précieux",
            "contenu": r"""
L'or est à part : il ne se consomme presque pas, et il est détenu surtout comme **réserve de valeur**
(banques centrales, investisseurs, bijouterie).

### Ce qui fait bouger l'or

- **Taux réels** : l'or ne verse ni coupon ni dividende. Quand les taux réels baissent, le coût
  d'opportunité de le détenir diminue : il tend à monter. Relation inverse historiquement forte, mais
  pas toujours vérifiée.
- **Dollar** : l'or étant coté en dollars, un dollar faible le soutient souvent.
- **Valeur refuge** : demande lors des crises géopolitiques et financières.
- **Achats des banques centrales** : de nombreuses banques centrales d'émergents diversifient leurs
  réserves hors du dollar en achetant de l'or.
- **Inflation** : couverture de long terme imparfaite.

### Particularités de marché

- Coté en dollars par **once troy** ($31{,}1035$ g).
- Marché de référence de gré à gré à **Londres** (prix de référence fixés deux fois par jour) et futures
  au COMEX.
- **ETF adossés à de l'or physique** : stockent des lingots pour leurs porteurs.
- Le **ratio or/argent** (combien d'onces d'argent pour une once d'or) est suivi par les traders.

### Les autres métaux précieux

- **Argent** : à la fois métal précieux et industriel (électronique, panneaux solaires), plus volatil que l'or.
- **Platine et palladium** : surtout industriels (pots catalytiques), dépendent de l'automobile et d'une
  offre très concentrée géographiquement.

### Question classique d'entretien

« Les taux réels américains montent fortement : que fait l'or ? » → Il tend à baisser (coût d'opportunité
plus élevé, dollar souvent plus fort), sauf si une crise déclenche une demande refuge qui l'emporte.
""",
            "points_cles": [
                "Or : réserve de valeur, sensible aux taux réels (relation inverse) et au dollar.",
                "Valeur refuge et achats des banques centrales.",
                "Once troy = 31,1 g ; marché de Londres et COMEX.",
                "Argent, platine, palladium : plus industriels et plus volatils.",
            ],
        },
        # ------------------------------------------------------------------ 7
        {
            "id": "com-c7",
            "titre": "7. Investir dans les matières premières et préparer l'entretien",
            "contenu": r"""
### Comment s'exposer

| Moyen | Avantage | Inconvénient |
|---|---|---|
| Futures | Liquides, levier | Roulement (roll yield), marges |
| ETF / ETC sur indices de futures | Simples d'accès | Subissent le roll yield en contango |
| ETC adossés au physique (or) | Pas de roulement | Coût de stockage, peu de métaux concernés |
| Actions de producteurs (pétrolières, minières) | Dividendes | Risque spécifique de l'entreprise, levier opérationnel |
| Fonds systématiques (CTA) | Suivent les tendances sur de nombreux marchés | Souffrent des marchés sans tendance |

### Les indices

- **S&P GSCI** : pondéré selon la **production mondiale**, donc très chargé en **énergie**.
- **Bloomberg Commodity Index** : pondérations plafonnées par secteur, plus diversifié.

### Pourquoi en détenir dans un portefeuille

- **Diversification** : corrélation souvent faible avec les actions et les obligations sur longue période.
- **Couverture contre l'inflation**, notamment lors des chocs d'offre (énergie).
- Mais pas de flux de trésorerie intrinsèque : le rendement de long terme vient surtout du roll yield
  et du collatéral, pas d'une « croissance » de la matière première.

### Les devises « matières premières »

Le **dollar australien** (métaux, minerai de fer), le **dollar canadien** et la **couronne norvégienne**
(pétrole) sont souvent corrélés aux prix des matières premières que leurs pays exportent.

### Questions fréquentes en entretien

1. *« Qu'est-ce que le contango ? Pourquoi un ETF pétrole peut-il perdre de l'argent même si le prix du
   pétrole ne baisse pas ? »* → Roll yield négatif.
2. *« L'OPEP+ annonce une coupe de production : effets sur le Brent, la courbe, le dollar canadien,
   les actions des compagnies aériennes ? »* → Brent ↑, backwardation ↑, CAD souvent ↑, compagnies aériennes ↓.
3. *« Comment une compagnie aérienne couvre-t-elle son carburant ? »* → Swaps et options sur brut ou
   gasoil, collars, couverture partielle, risque de base.
4. *« Qu'est-ce qu'un crack spread ? Un spark spread ? »*
5. *« Que s'est-il passé le 20 avril 2020 sur le WTI ? »*
6. *« Pourquoi l'or monte-t-il quand les taux réels baissent ? »*

Prépare aussi **un marché que tu suis** (pétrole, gaz européen, cuivre ou or) : les facteurs récents, la
forme de la courbe, et ton avis argumenté.
""",
            "points_cles": [
                "ETF sur futures : exposés au roll yield.",
                "S&P GSCI très énergie ; Bloomberg Commodity Index plus diversifié.",
                "Devises matières premières : AUD, CAD, NOK.",
                "Prépare un marché que tu suis, avec la forme de sa courbe.",
            ],
        },
    ],
    "quiz": [
        {"id": "com-q01", "type": "qcm",
         "question": "Sur quelle place se négocient principalement les métaux industriels comme le cuivre et l'aluminium ?",
         "choix": ["Le CBOT", "Le London Metal Exchange (LME)", "Euronext", "Le Nasdaq"],
         "reponse": 1,
         "explication": "Le LME est la référence mondiale des métaux industriels (le COMEX aussi pour le cuivre)."},
        {"id": "com-q02", "type": "qcm",
         "question": "Quelles sont les deux références mondiales du pétrole brut ?",
         "choix": ["TTF et Henry Hub", "Brent et WTI", "LME et COMEX", "GSCI et BCOM"],
         "reponse": 1,
         "explication": "TTF et Henry Hub sont des références de gaz ; GSCI et BCOM des indices."},
        {"id": "com-q03", "type": "nombre",
         "question": r"Pétrole spot $80$ \$, $r = 4\,\%$, stockage $2\,\%$, convenience yield $1\,\%$ (continus). Future 1 an (2 décimales) ?",
         "reponse": 84.10, "tolerance": 0.02,
         "explication": r"$80\, e^{0{,}05} \approx 84{,}10$ : contango."},
        {"id": "com-q04", "type": "qcm",
         "question": "Un marché pétrolier est en forte backwardation. Que cela indique-t-il le plus souvent ?",
         "choix": ["Des stocks élevés", "Un marché tendu, avec des stocks bas", "Des taux d'intérêt très élevés", "Un dollar faible"],
         "reponse": 1,
         "explication": "Le physique disponible tout de suite vaut plus que le physique livré plus tard : convenience yield élevé."},
        {"id": "com-q05", "type": "qcm",
         "question": "Un ETF qui roule des futures pétroliers perd de l'argent alors que le prix spot est stable. Pourquoi ?",
         "choix": ["Frais de gestion uniquement", "La courbe est en contango : le roll yield est négatif",
                   "La courbe est en backwardation", "Le dollar a monté"],
         "reponse": 1,
         "explication": "Il revend le contrat proche moins cher qu'il n'achète le suivant."},
        {"id": "com-q06", "type": "nombre",
         "question": r"Spot stable à $80$, le future à 1 mois cote toujours $81$. Perte de roulement approximative sur un an "
                     r"pour un investisseur long, en \$ par baril ?",
         "reponse": 12, "tolerance": 0.001,
         "explication": "Environ 1 $ par mois × 12 mois."},
        {"id": "com-q07", "type": "nombre",
         "question": r"Brut $80$ \$, essence $100$ \$, diesel $110$ \$ (par baril). Crack spread 3:2:1 en \$ par baril (1 décimale) ?",
         "reponse": 23.3, "tolerance": 0.05,
         "explication": r"$(2 \times 100 + 110 - 3 \times 80) / 3 = 70 / 3 \approx 23{,}3$."},
        {"id": "com-q08", "type": "nombre",
         "question": r"Électricité $90$ €/MWh, gaz $35$ €/MWh, heat rate $2$. Spark spread en €/MWh ?",
         "reponse": 20, "tolerance": 0.001,
         "explication": r"$90 - 2 \times 35 = 20$."},
        {"id": "com-q09", "type": "nombre",
         "question": r"Même centrale, avec $0{,}37$ t de CO₂ par MWh et un quota à $70$ €/t. Clean spark spread en €/MWh (1 décimale) ?",
         "reponse": -5.9, "tolerance": 0.05,
         "explication": r"$20 - 0{,}37 \times 70 = 20 - 25{,}9 = -5{,}9$ : la centrale perd de l'argent."},
        {"id": "com-q10", "type": "qcm",
         "question": "Pourquoi les couvertures de matières premières utilisent-elles souvent des options asiatiques ?",
         "choix": ["Elles se négocient en Asie", "Les entreprises achètent ou vendent en continu : c'est le prix moyen qui compte",
                   "Elles n'ont pas de prime", "Elles sont toujours à livraison physique"],
         "reponse": 1,
         "explication": "En plus, la moyenne étant moins volatile, l'option est moins chère."},
        {"id": "com-q11", "type": "nombre",
         "question": r"Une mine vend à terme $10\,000$ t de cuivre à $9\,000$ \$/t. Le prix moyen finit à $7\,500$ \$/t. "
                     r"Revenu total en M\$ (vente physique + couverture) ?",
         "reponse": 90, "tolerance": 0.001,
         "explication": "La couverture compense exactement la baisse : 10 000 × 9 000 = 90 M$."},
        {"id": "com-q12", "type": "nombre",
         "question": r"Même mine avec un collar put $8\,500$ / call $10\,000$ (prime nulle). Prix moyen final $11\,000$ \$/t. Revenu en M\$ ?",
         "reponse": 100, "tolerance": 0.001,
         "explication": "Le call vendu plafonne le prix à 10 000 $/t : 10 000 × 10 000 = 100 M$."},
        {"id": "com-q13", "type": "qcm",
         "question": "Les taux réels américains montent fortement. Effet le plus probable sur l'or ?",
         "choix": ["Hausse", "Baisse : le coût d'opportunité de détenir de l'or augmente", "Aucun effet", "Hausse uniquement en euros"],
         "reponse": 1,
         "explication": "L'or ne rapporte rien : des taux réels plus élevés le rendent moins attractif (sauf demande refuge)."},
        {"id": "com-q14", "type": "qcm",
         "question": "Que s'est-il passé le 20 avril 2020 sur le contrat WTI de mai ?",
         "choix": ["Il a atteint un record historique", "Il a clôturé en territoire négatif (−37,63 $)",
                   "Sa cotation a été suspendue un mois", "Il a été remplacé par le Brent"],
         "reponse": 1,
         "explication": "Demande effondrée et stockage saturé à Cushing : les longs ont payé pour sortir."},
        {"id": "com-q15", "type": "qcm",
         "question": "Quel indice de matières premières est le plus chargé en énergie ?",
         "choix": ["Le Bloomberg Commodity Index", "Le S&P GSCI, pondéré par la production mondiale", "Le CAC 40", "Le VIX"],
         "reponse": 1,
         "explication": "La pondération par la production donne un poids dominant au pétrole et au gaz."},
        {"id": "com-q16", "type": "qcm",
         "question": "L'OPEP+ annonce une coupe de production surprise. Quelle devise a tendance à s'apprécier ?",
         "choix": ["Le yen", "Le dollar canadien ou la couronne norvégienne", "Le franc suisse", "L'euro uniquement"],
         "reponse": 1,
         "explication": "Ce sont des devises de pays exportateurs de pétrole."},
        {"id": "com-q17", "type": "qcm",
         "question": "Qu'est-ce que le convenience yield ?",
         "choix": ["Le coût du stockage", "L'avantage de détenir le bien physique immédiatement", "Le taux sans risque",
                   "La prime d'une option"],
         "reponse": 1,
         "explication": "Il est élevé quand le marché est tendu, ce qui peut mettre la courbe en backwardation."},
    ],
    "flashcards": [
        {"id": "com-f01", "recto": "Prix à terme d'une matière première", "verso": r"$F = S\,e^{(r + u - y)T}$"},
        {"id": "com-f02", "recto": "Contango / backwardation", "verso": "Contango : F > S, stocks élevés. Backwardation : F < S, marché tendu."},
        {"id": "com-f03", "recto": "Décomposition du rendement d'une position en futures", "verso": "Variation du spot + roll yield + rendement du collatéral."},
        {"id": "com-f04", "recto": "Convenience yield", "verso": "Avantage de détenir le bien physique tout de suite ; élevé quand les stocks sont bas."},
        {"id": "com-f05", "recto": "Crack spread 3:2:1", "verso": "(2 × essence + 1 × diesel − 3 × brut) / 3 : marge de raffinage."},
        {"id": "com-f06", "recto": "Spark spread", "verso": "Électricité − heat rate × gaz ; clean spark spread : − coût du CO₂."},
        {"id": "com-f07", "recto": "Brent et WTI", "verso": "Brent : mer du Nord, référence mondiale (ICE). WTI : Texas, livré à Cushing (NYMEX)."},
        {"id": "com-f08", "recto": "LME", "verso": "London Metal Exchange : référence des métaux industriels (cuivre, aluminium, nickel, zinc)."},
        {"id": "com-f09", "recto": "Or et taux réels", "verso": "Relation inverse fréquente : l'or ne rapporte rien, son coût d'opportunité suit les taux réels."},
        {"id": "com-f10", "recto": "Once troy", "verso": "31,1035 grammes : unité de cotation des métaux précieux."},
        {"id": "com-f11", "recto": "WTI le 20 avril 2020", "verso": "Contrat de mai clôturé à −37,63 $ : demande effondrée, stockage saturé."},
        {"id": "com-f12", "recto": "Pourquoi des options asiatiques en commodities ?", "verso": "Les entreprises sont exposées au prix moyen ; la moyenne rend l'option moins chère."},
        {"id": "com-f13", "recto": "S&P GSCI vs Bloomberg Commodity Index", "verso": "GSCI : pondéré par la production, très énergie. BCOM : plafonds sectoriels, plus diversifié."},
        {"id": "com-f14", "recto": "Devises matières premières", "verso": "AUD (métaux), CAD et NOK (pétrole)."},
    ],
}
