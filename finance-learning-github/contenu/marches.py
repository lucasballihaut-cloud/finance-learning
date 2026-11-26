"""Module : Marchés, métiers et produits linéaires."""

MODULE = {
    "id": "marches",
    "titre": "Marchés, métiers et produits linéaires",
    "icone": "🌍",
    "statut": "complet",
    "resume": "Qui fait quoi en salle des marchés, classes d'actifs, marchés organisés et OTC, "
              "forwards, futures et swaps.",
    "chapitres": [
        {
            "id": "mar-c1",
            "titre": "1. Les acteurs et les métiers",
            "contenu": r"""
**Sell side et buy side.**
- Le **sell side** (banques d'investissement, brokers) fournit des services et de la liquidité :
  il cote des prix, exécute des ordres, crée des produits.
- Le **buy side** (sociétés de gestion, fonds de pension, assureurs, hedge funds) investit
  l'argent de ses clients ou le sien.

**Métiers du front office** (ceux visés par les stages et alternances) :

| Métier | Rôle | Qualités recherchées |
|---|---|---|
| **Sales** | Relation avec les clients institutionnels : comprendre leurs besoins, proposer des idées et des produits, remonter les demandes de prix aux traders | Communication, compréhension des marchés, sens commercial |
| **Trader** | Gérer un portefeuille de risque : coter des prix (*market making*), couvrir les positions, piloter le P&L | Rapidité, gestion du risque, calcul mental, sang-froid |
| **Structureur** | Concevoir des produits sur mesure (produits structurés, solutions de couverture) en combinant briques simples | Créativité, maîtrise des dérivés, rigueur |
| **Quant** | Modèles de pricing et de risque, outils de trading, recherche de stratégies | Mathématiques, probabilités, programmation |
| **Gérant / analyste (AM)** | Construire et piloter des portefeuilles pour des clients, analyser des titres | Analyse fondamentale, conviction, discipline |

On distingue souvent le trading **flow** (produits standards, gros volumes, marges faibles) du
trading **exotique** (produits complexes, risques plus difficiles à couvrir).

**Middle et back office** : contrôle des risques, calcul du P&L officiel, conformité,
règlement-livraison. Ils assurent que le front office prend des risques maîtrisés et que les
opérations sont correctement enregistrées.
""",
            "points_cles": [
                "Sell side = fournit la liquidité ; buy side = investit.",
                "Sales ↔ clients, trader ↔ risque, structureur ↔ produit, quant ↔ modèles.",
                "Flow : volumes et vitesse ; exotique : complexité des risques.",
            ],
        },
        {
            "id": "mar-c2",
            "titre": "2. Classes d'actifs et organisation des marchés",
            "contenu": r"""
**Grandes classes d'actifs** : actions, taux (dettes d'État, swaps), crédit (dettes
d'entreprises, CDS), change (FX), matières premières. Chacune a ses produits « cash »
(l'actif lui-même) et ses dérivés.

**Marché primaire / secondaire.** Sur le primaire, un émetteur lève de l'argent (introduction
en bourse, émission obligataire). Sur le secondaire, les investisseurs s'échangent ensuite
les titres existants ; c'est là que se forment les prix au jour le jour.

**Marché organisé ou OTC.**
- Sur un **marché organisé** (bourse), les contrats sont standardisés et une **chambre de
  compensation** s'interpose entre acheteur et vendeur : elle devient la contrepartie de
  chacun et exige des **dépôts de garantie**, ce qui réduit fortement le risque de contrepartie.
- De gré à gré (**OTC**), les contrats sont négociés bilatéralement et peuvent être
  personnalisés. Depuis la crise de 2008, une grande partie des dérivés OTC standards doit
  aussi passer par une chambre de compensation.

**Fourchette bid-ask.** Un teneur de marché cote un prix d'achat (*bid*) et un prix de vente
(*ask*). L'écart rémunère le service de liquidité et le risque pris ; il est faible pour les
actifs très liquides et large pour les produits complexes.

**Liquidité et volatilité** sont les deux mots qu'on vous demandera de définir clairement :
la liquidité est la capacité à traiter vite une taille importante sans trop bouger le prix ;
la volatilité mesure l'amplitude des variations de prix (écart-type des rendements, annualisé).
""",
            "points_cles": [
                "Chambre de compensation : contrepartie centrale + appels de marge.",
                "OTC = sur mesure, bilatéral.",
                "Bid-ask = rémunération du teneur de marché.",
            ],
        },
        {
            "id": "mar-c3",
            "titre": "3. Forwards et futures",
            "contenu": r"""
Un **forward** est un engagement ferme d'acheter (ou de vendre) un actif à une date future $T$
à un prix $F_0$ fixé aujourd'hui. Il ne coûte rien à la signature. Payoff de l'acheteur à
maturité : $S_T - F_0$.

**Prix forward par cash-and-carry.** Acheter l'actif aujourd'hui en empruntant au taux $r$ et
le porter jusqu'à $T$ réplique le forward. En notant $q$ le rendement de l'actif (dividendes) :

$$
F_0 = S_0\, e^{(r - q)T}
$$

Si $F_0$ était plus élevé, on vendrait le forward et on achèterait l'actif à crédit : gain sans
risque. S'il était plus bas, on ferait l'inverse.

**Change.** Pour une paire cotée en devise domestique par unité de devise étrangère
(par exemple EUR/USD en dollars par euro, domestique = USD) :

$$
F_0 = S_0\, e^{(r_{dom} - r_{etr})T}
$$

La devise au taux le plus élevé cote en « déport » à terme : c'est la **parité des taux
d'intérêt couverte**.

**Futures.** Même logique qu'un forward, mais contrat standardisé, coté en bourse, avec une
chambre de compensation et des **appels de marge quotidiens** : les gains et pertes sont
réglés chaque jour (*mark-to-market*). Le risque de contrepartie est donc très réduit.

**Contango / backwardation.** Un marché est en *contango* quand les futures cotent au-dessus du
spot (coût de portage positif : taux, stockage), en *backwardation* quand ils cotent en dessous
(par exemple quand détenir l'actif physique rapporte un avantage, le *convenience yield*).
""",
            "points_cles": [
                "F₀ = S₀·e^((r − q)T).",
                "Futures : standardisés + appels de marge quotidiens.",
                "Contango : futures > spot.",
            ],
        },
        {
            "id": "mar-c4",
            "titre": "4. Les swaps de taux",
            "contenu": r"""
Un **swap de taux d'intérêt** (IRS) est un échange de flux : une partie paie un **taux fixe**
$K$, l'autre paie un **taux variable** (par exemple €STR ou Euribor) sur un même nominal,
pendant une durée donnée. Le nominal n'est pas échangé.

- Le **payeur du fixe** gagne si les taux montent (il paie un fixe et reçoit un variable qui augmente).
- Le **receveur du fixe** gagne si les taux baissent ; sa position ressemble à celle d'un
  détenteur d'obligation à taux fixe.

**Taux de swap.** À la signature, on choisit $K$ pour que le swap vaille zéro : la valeur
actuelle de la jambe fixe égale celle de la jambe variable. Avec les facteurs d'actualisation
$DF(t_i)$ et des fractions d'année $\tau_i$ :

$$
K = \frac{1 - DF(t_n)}{\sum_{i=1}^{n} \tau_i\, DF(t_i)}
$$

(formule dans le cadre simple où la même courbe sert à projeter et à actualiser).

**À quoi ça sert ?** Une entreprise endettée à taux variable peut payer le fixe dans un swap
pour figer son coût de financement. Un investisseur peut ajuster la duration de son portefeuille
sans acheter ni vendre d'obligations. Le DV01 d'un swap est proche de celui d'une obligation de
même maturité.
""",
            "points_cles": [
                "Swap au pair : valeur nulle à la signature.",
                "Payeur fixe gagne quand les taux montent.",
                "Receveur fixe ≈ long obligation.",
            ],
        },
        {
            "id": "mar-c5",
            "titre": "5. Le marché actions",
            "contenu": r"""
### Émettre et échanger des actions

- **Introduction en bourse (IPO)** : l'entreprise vend des actions au public sur le marché primaire,
  accompagnée par des banques (activité d'*Equity Capital Markets*). Une **augmentation de capital**
  émet de nouvelles actions plus tard.
- **Indices** : panier représentatif (CAC 40, Euro Stoxx 50, S&P 500…), en général pondéré par la
  **capitalisation flottante** (seules les actions réellement échangeables comptent).
- **ETF** : fonds coté qui réplique un indice ; on l'achète comme une action.

### Les ordres

| Ordre | Principe | Risque |
|---|---|---|
| Au marché | Exécuté immédiatement au meilleur prix disponible | Prix d'exécution incertain si peu de liquidité |
| À cours limité | Exécuté seulement à un prix égal ou meilleur que la limite | Peut ne jamais être exécuté |
| Stop | Devient un ordre au marché si un seuil est franchi | Utilisé pour couper une perte, exécution parfois loin du seuil |

Les gros ordres institutionnels sont souvent découpés par des **algorithmes** (VWAP, TWAP…) pour
limiter leur **impact de marché**.

### Dividendes et opérations sur titres

Le jour du **détachement** (ex-date), le cours baisse d'environ le montant du dividende : une action à
$50$ € qui détache $2$ € ouvre autour de $48$ € (toutes choses égales par ailleurs). Une **division
d'action** (*split*) de 2 pour 1 divise le cours par deux sans changer la valeur de l'entreprise.

### La vente à découvert

Vendre une action qu'on ne possède pas, après l'avoir **empruntée** (prêt de titres, contre une
commission). On la rachète plus tard pour la rendre. Exemple : vente à $50$, rachat à $45$, frais
d'emprunt $0{,}5$ : gain $4{,}5$ par action. La perte est potentiellement illimitée si le cours monte.

### Valoriser une action (les bases)

- **PER** (*price earnings ratio*) $=$ cours / bénéfice par action : combien d'années de bénéfices on paie.
- **Rendement du dividende** $=$ dividende / cours.
- **VE/EBITDA** : valeur d'entreprise (capitalisation + dette nette) rapportée au résultat opérationnel
  avant amortissements ; permet de comparer des entreprises au niveau d'endettement différent.
- **Modèle de Gordon** : avec un dividende attendu $D_1$, une rentabilité exigée $r$ et une croissance
  perpétuelle $g < r$ :

$$
P_0 = \frac{D_1}{r - g}
$$

Exemple : $D_1 = 2$ €, $r = 8\,\%$, $g = 3\,\%$ : $P_0 = 2 / 0{,}05 = 40$ €. Le prix est très sensible
à $r - g$ : c'est pourquoi les actions de croissance réagissent fortement aux taux.
""",
            "points_cles": [
                "Ex-date : le cours baisse d'environ le dividende.",
                "Vente à découvert : emprunt de titres, perte potentiellement illimitée.",
                "Gordon : P = D₁/(r − g).",
                "Ordre limite : prix garanti, exécution non garantie.",
            ],
        },
        {
            "id": "mar-c6",
            "titre": "6. Le marché des changes",
            "contenu": r"""
### Lire une cotation

$\text{EUR/USD} = 1{,}1000$ signifie qu'**un euro vaut 1,10 dollar**. L'euro est la devise **de base**,
le dollar la devise **de cotation**. Si EUR/USD monte, l'euro s'apprécie face au dollar.

- **Pip** : quatrième décimale ($0{,}0001$) pour la plupart des paires, deuxième ($0{,}01$) pour les
  paires contre le yen.
- **Spot** : livraison à 2 jours ouvrés (T+2) pour la plupart des paires.
- **Taux croisé** : $\text{EUR/JPY} = \text{EUR/USD} \times \text{USD/JPY}$, par exemple
  $1{,}10 \times 150 = 165$.

### Forward et points de terme

Par la parité des taux couverte, $F = S\, e^{(r_{cot} - r_{base})T}$ (taux de la devise de cotation
moins taux de la devise de base). Les desks cotent les **points de terme** $F - S$, en pips.

Exemple : EUR/USD spot $1{,}1000$, $r_{USD} = 4\,\%$, $r_{EUR} = 2\,\%$, 1 an : $F \approx 1{,}1222$, soit
$+222$ pips. Ce n'est **pas** une prévision de hausse de l'euro : c'est le différentiel de taux.

### Les produits

- **Swap de change** (FX swap) : achat au comptant et revente à terme simultanés. Sert à gérer la
  trésorerie en devises ; c'est l'un des instruments les plus échangés au monde.
- **NDF** (*non-deliverable forward*) : forward réglé en cash (souvent en dollars) pour les devises
  dont la convertibilité est restreinte.
- **Options de change** : cotées en volatilité, avec des risk reversals et butterflies 25-delta.

### Scénario client : un exportateur

Une entreprise française recevra $10$ M USD dans 3 mois et craint une baisse du dollar (hausse
d'EUR/USD). Le sales lui propose de **vendre les dollars à terme** (acheter des euros à terme) au taux
forward, par exemple $1{,}1000$ :

| EUR/USD dans 3 mois | Sans couverture | Avec le forward |
|---|---|---|
| $1{,}05$ | $9{,}52$ M€ | $9{,}09$ M€ |
| $1{,}10$ | $9{,}09$ M€ | $9{,}09$ M€ |
| $1{,}20$ | $8{,}33$ M€ | $9{,}09$ M€ |

Le forward supprime le risque, mais aussi le gain possible. Une **option** (achat d'un call EUR/put
USD) protège tout en gardant le gain potentiel, contre une prime.
""",
            "points_cles": [
                "EUR/USD = 1,10 : 1 euro vaut 1,10 dollar.",
                "Points de terme = F − S, reflet du différentiel de taux.",
                "Taux croisé : EUR/JPY = EUR/USD × USD/JPY.",
                "Exportateur qui recevra des USD : vend les USD à terme.",
            ],
        },
        {
            "id": "mar-c7",
            "titre": "7. Matières premières et une journée en salle des marchés",
            "contenu": r"""
### Les spécificités des matières premières

- Les futures sont souvent à **livraison physique** : un investisseur financier doit **rouler** sa
  position (vendre le contrat qui arrive à échéance, acheter le suivant) avant la livraison.
- **Rendement de roulement** (*roll yield*) : en **contango** (futures plus chers que le spot), rouler
  une position longue coûte de l'argent à chaque échéance ; en **backwardation**, cela en rapporte.
  Exemple : pétrole à $80$, future 1 mois à $81$, 2 mois à $82$ : un acheteur qui roule tous les mois
  « perd » environ $1$ par mois si les prix ne bougent pas.
- Prix déterminés par l'offre et la demande physiques : stocks, météo, géopolitique, saisonnalité.

### Une journée type en salle des marchés

| Moment | Ce qui se passe |
|---|---|
| Avant l'ouverture | Lecture de l'actualité et des marchés asiatiques, **morning meeting** : vues des stratégistes, positions, axes de la journée |
| Ouverture | Les sales appellent leurs clients avec des idées ; les traders ajustent leurs couvertures |
| Journée | Demandes de prix des clients (**RFQ**), publications macro, gestion des risques en continu |
| Clôture | Calcul du **P&L**, contrôle des risques et des limites par le middle office, préparation du lendemain |

### Exemple de demande de prix

1. Un client appelle son sales : « Prix pour vendre 10 M USD contre EUR à 3 mois ? »
2. Le sales demande la cotation au trader FX forward.
3. Le trader cote un prix (spot + points de terme, avec une marge) en tenant compte de sa position et
   de la taille.
4. Le sales transmet ; le client accepte (« done ») ou refuse.
5. Le trader couvre son nouveau risque (par exemple en vendant des dollars au comptant et en faisant
   un swap de change).

Retiens que le **sales** est responsable de la relation et de l'information client, le **trader** du
prix et du risque : en entretien, montre que tu comprends cette collaboration.
""",
            "points_cles": [
                "Rouler un long en contango coûte, en backwardation rapporte.",
                "RFQ : client → sales → trader → prix → couverture.",
                "Morning meeting, flux de la journée, P&L et contrôle des risques le soir.",
            ],
        },
    ],
    "quiz": [
        {"id": "mar-q01", "type": "nombre",
         "question": r"$S_0 = 100$, $r = 3\,\%$, dividende continu $q = 1\,\%$, $T = 1$ an. Prix forward ? (2 décimales)",
         "reponse": 102.02, "tolerance": 0.05,
         "explication": r"$100\, e^{0{,}02} \approx 102{,}02$."},
        {"id": "mar-q02", "type": "nombre",
         "question": r"EUR/USD spot $1{,}10$ (dollars par euro), $r_{USD} = 4\,\%$, $r_{EUR} = 2\,\%$ (continus). "
                     r"Forward 1 an ? (4 décimales)",
         "reponse": 1.1222, "tolerance": 0.001,
         "explication": r"Domestique = USD : $F = 1{,}10\, e^{0{,}04 - 0{,}02} \approx 1{,}1222$."},
        {"id": "mar-q03", "type": "qcm",
         "question": "Quelle est la principale différence entre un future et un forward ?",
         "choix": ["Le future n'a pas de date de maturité",
                   "Le future est standardisé, coté et soumis à des appels de marge quotidiens",
                   "Le forward est toujours réglé en cash", "Le future coûte une prime à l'achat"],
         "reponse": 1,
         "explication": "Le future passe par une chambre de compensation et règle les gains et pertes chaque jour."},
        {"id": "mar-q04", "type": "qcm",
         "question": "Quel est le rôle d'une chambre de compensation ?",
         "choix": ["Fixer le prix des actifs", "Devenir la contrepartie de chaque acheteur et vendeur",
                   "Conseiller les investisseurs", "Émettre des obligations"],
         "reponse": 1,
         "explication": "En s'interposant et en exigeant des marges, elle réduit le risque de contrepartie."},
        {"id": "mar-q05", "type": "qcm",
         "question": "Que vaut un swap de taux au pair au moment de sa signature ?",
         "choix": ["Le nominal", "Zéro", "La somme des coupons fixes", "Le DV01"],
         "reponse": 1,
         "explication": "Le taux fixe est choisi pour égaliser la valeur des deux jambes."},
        {"id": "mar-q06", "type": "qcm",
         "question": "Un client pense que les taux vont monter. Quelle position de swap lui proposer ?",
         "choix": ["Recevoir le fixe", "Payer le fixe", "Aucune, un swap ne dépend pas des taux",
                   "Acheter un zéro-coupon long"],
         "reponse": 1,
         "explication": "Payer le fixe et recevoir le variable : le variable augmente avec les taux."},
        {"id": "mar-q07", "type": "qcm",
         "question": "Un marché est en contango quand…",
         "choix": ["les futures cotent au-dessus du spot", "les futures cotent en dessous du spot",
                   "la volatilité est négative", "la courbe des taux est inversée"],
         "reponse": 0,
         "explication": "Le coût de portage (financement, stockage) pousse les futures au-dessus du spot."},
        {"id": "mar-q08", "type": "qcm",
         "question": "Lequel de ces acteurs fait partie du buy side ?",
         "choix": ["Un market maker de banque", "Une société de gestion d'actifs",
                   "Un broker", "Une chambre de compensation"],
         "reponse": 1,
         "explication": "Le buy side investit pour ses clients ; le sell side leur fournit liquidité et services."},
        {"id": "mar-q09", "type": "nombre",
         "question": r"Une action cote $50$ € la veille du détachement d'un dividende de $2$ €. Cours d'ouverture théorique ?",
         "reponse": 48, "tolerance": 0.001,
         "explication": "Le dividende sort de la valeur de l'action : 50 − 2 = 48 (toutes choses égales par ailleurs)."},
        {"id": "mar-q10", "type": "nombre",
         "question": r"Modèle de Gordon : dividende attendu $2$ €, rentabilité exigée $8\,\%$, croissance $3\,\%$. Prix de l'action ?",
         "reponse": 40, "tolerance": 0.001,
         "explication": r"$2 / (0{,}08 - 0{,}03) = 40$ €."},
        {"id": "mar-q11", "type": "nombre",
         "question": r"Vente à découvert à $50$ €, rachat à $45$ €, frais d'emprunt $0{,}5$ € par action. Gain par action ?",
         "reponse": 4.5, "tolerance": 0.001,
         "explication": "50 − 45 − 0,5 = 4,5 €."},
        {"id": "mar-q12", "type": "nombre",
         "question": r"EUR/USD spot $1{,}1000$, $r_{USD} = 4\,\%$, $r_{EUR} = 2\,\%$ (continus), 1 an. Points de terme en pips ?",
         "reponse": 222, "tolerance": 2,
         "explication": r"$F = 1{,}1\,e^{0{,}02} \approx 1{,}1222$ : $+0{,}0222$, soit 222 pips."},
        {"id": "mar-q13", "type": "nombre",
         "question": r"EUR/USD $= 1{,}10$ et USD/JPY $= 150$. Combien vaut EUR/JPY ?",
         "reponse": 165, "tolerance": 0.01,
         "explication": r"$1{,}10 \times 150 = 165$."},
        {"id": "mar-q14", "type": "qcm",
         "question": "Un exportateur français recevra 10 M USD dans 3 mois. Comment couvrir son risque de change ?",
         "choix": ["Acheter des USD à terme", "Vendre les USD à terme contre des EUR", "Acheter un put EUR/USD", "Ne rien faire"],
         "reponse": 1,
         "explication": "Il est naturellement long USD : il les vend à terme pour fixer son montant en euros."},
        {"id": "mar-q15", "type": "nombre",
         "question": r"Le même exportateur a vendu 10 M USD à terme à $1{,}10$. Combien d'euros reçoit-il (en M€, 2 décimales) ?",
         "reponse": 9.09, "tolerance": 0.01,
         "explication": r"$10 / 1{,}10 \approx 9{,}09$ M€, quel que soit le change dans 3 mois."},
        {"id": "mar-q16", "type": "qcm",
         "question": "Un investisseur long de futures sur pétrole roule sa position chaque mois dans un marché en contango. Si les prix ne bougent pas…",
         "choix": ["il gagne de l'argent", "il perd de l'argent à chaque roulement", "il est neutre", "il reçoit le pétrole"],
         "reponse": 1,
         "explication": "Il revend le contrat proche moins cher qu'il n'achète le suivant : le roll yield est négatif."},
        {"id": "mar-q17", "type": "qcm",
         "question": "Qu'est-ce qu'un NDF ?",
         "choix": ["Une option de change", "Un forward de change réglé en cash, sans livraison des devises",
                   "Un future sur indice", "Un swap de taux"],
         "reponse": 1,
         "explication": "Utilisé pour les devises à convertibilité restreinte : on règle seulement la différence, souvent en USD."},
    ],
    "flashcards": [
        {"id": "mar-f01", "recto": "Prix forward d'une action à dividende continu q",
         "verso": r"$F_0 = S_0\, e^{(r - q)T}$"},
        {"id": "mar-f02", "recto": "Forward de change (parité couverte)",
         "verso": r"$F_0 = S_0\, e^{(r_{dom} - r_{etr})T}$"},
        {"id": "mar-f03", "recto": "Sell side vs buy side",
         "verso": "Sell side : banques et brokers qui fournissent liquidité et produits. Buy side : gérants qui investissent."},
        {"id": "mar-f04", "recto": "Contango et backwardation",
         "verso": "Contango : futures > spot. Backwardation : futures < spot."},
        {"id": "mar-f05", "recto": "Qui gagne dans un swap quand les taux montent ?",
         "verso": "Le payeur du taux fixe."},
        {"id": "mar-f06", "recto": "Définition de la liquidité",
         "verso": "Capacité à traiter rapidement une taille importante sans faire beaucoup bouger le prix."},
        {"id": "mar-f07", "recto": "Effet du détachement d'un dividende", "verso": "Le cours baisse d'environ le montant du dividende à l'ex-date."},
        {"id": "mar-f08", "recto": "Modèle de Gordon", "verso": r"$P_0 = D_1 / (r - g)$"},
        {"id": "mar-f09", "recto": "Ordre à cours limité", "verso": "Prix garanti (ou meilleur), exécution non garantie."},
        {"id": "mar-f10", "recto": "Lire EUR/USD = 1,10", "verso": "1 euro (devise de base) vaut 1,10 dollar (devise de cotation)."},
        {"id": "mar-f11", "recto": "Points de terme", "verso": "F − S en pips ; reflètent le différentiel de taux, pas une prévision."},
        {"id": "mar-f12", "recto": "Roll yield", "verso": "Coût (contango) ou gain (backwardation) du roulement d'une position longue en futures."},
        {"id": "mar-f13", "recto": "RFQ", "verso": "Request for quote : le client demande un prix, le sales le transmet au trader qui cote puis couvre."},
    ],
}
