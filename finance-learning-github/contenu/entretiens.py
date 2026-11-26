"""Questions d'entretien avec corrigés (techniques et comportementales).

Les corrigés donnent une structure de réponse : à adapter avec ton propre parcours.
"""

METIERS = ["Tous", "Sales", "Trading", "Structuration", "Quant", "Asset management"]

QUESTIONS = [
    # ---------- Comportemental ----------
    {"id": "ent-b01", "type": "Comportemental", "metiers": ["Tous"],
     "question": "Présentez-vous.",
     "corrige": r"""
Viser **1 min 30 à 2 min**, structure chronologique avec un fil rouge :
1. **Qui je suis** : formation actuelle, en une phrase.
2. **Ce qui m'a amené à la finance de marché** : un déclic concret (un cours, un projet, une lecture, une expérience).
3. **Ce que j'ai fait pour creuser** : projets personnels (par exemple un dashboard de pricing en Python), associations, stages.
4. **Pourquoi ce poste ici** : relier tes compétences au métier et à l'équipe.

Erreurs fréquentes : réciter le CV ligne par ligne, durer 5 minutes, ne pas conclure sur le poste.
"""},
    {"id": "ent-b02", "type": "Comportemental", "metiers": ["Tous"],
     "question": "Pourquoi la finance de marché ?",
     "corrige": r"""
Donner **2 ou 3 raisons personnelles et vérifiables**, pas « parce que ça paie bien » :
- goût pour un environnement rapide où l'information se traduit tout de suite en prix ;
- intérêt pour les mathématiques appliquées / la programmation au service d'une décision concrète ;
- envie de comprendre l'actualité économique et ses effets sur les actifs.

Appuie chaque raison sur **une preuve** : un projet, un suivi régulier des marchés, un cours que tu as approfondi.
"""},
    {"id": "ent-b03", "type": "Comportemental", "metiers": ["Tous"],
     "question": "Quelle est la différence entre sales, trading et structuration, et pourquoi ce métier pour vous ?",
     "corrige": r"""
Montrer que tu connais le métier **au quotidien** :
- **sales** : relation client, idées de marché, compréhension des besoins ;
- **trader** : prise et gestion du risque, cotation, couverture ;
- **structureur** : conception de produits qui répondent à une contrainte client (protection, rendement, vue de marché).

Puis relier **tes qualités** au métier choisi (exemple : « j'aime convaincre et vulgariser → sales ») et
expliquer pourquoi l'autre métier te correspond moins, sans le dénigrer.
"""},
    {"id": "ent-b04", "type": "Comportemental", "metiers": ["Tous"],
     "question": "Parlez-moi d'un échec ou d'une erreur.",
     "corrige": r"""
Méthode **STAR** (Situation, Tâche, Action, Résultat) + **ce que tu as appris**.
Choisis un échec réel mais pas rédhibitoire (un projet mal planifié, un examen raté puis rattrapé).
Passe 20 % du temps sur l'échec et 80 % sur ta réaction et la leçon, avec un exemple où tu l'as appliquée ensuite.
"""},
    {"id": "ent-b05", "type": "Comportemental", "metiers": ["Tous"],
     "question": "Parlez-moi d'une actualité de marché récente qui vous a marqué.",
     "corrige": r"""
Préparer **2 sujets** suivis depuis plusieurs semaines (banques centrales, inflation, un secteur, une devise…).
Structure : **le fait** → **pourquoi il compte** (mécanisme économique) → **l'effet sur les actifs**
(taux, actions, change, volatilité) → **ton avis** et ce qui le ferait changer.
Attends-toi à des relances (« et si l'inflation surprend à la hausse ? ») : connais les chiffres clés et les dates.
"""},
    {"id": "ent-b06", "type": "Comportemental", "metiers": ["Sales", "Trading", "Asset management"],
     "question": "Pitchez-moi une action (ou une idée de trade).",
     "corrige": r"""
Structure en **4 temps**, 2 minutes :
1. **La recommandation** d'emblée (achat / vente, horizon).
2. **La thèse** : 2 ou 3 arguments (croissance, valorisation relative, catalyseur à venir).
3. **Les risques** et ce qui invaliderait la thèse.
4. **Comment le mettre en place** : action, option (par exemple call spread pour limiter la prime), niveau de sortie.

Connaître quelques chiffres (secteur, concurrents, multiple de valorisation) rend le pitch crédible.
"""},
    {"id": "ent-b07", "type": "Comportemental", "metiers": ["Tous"],
     "question": "Comment gérez-vous la pression et un fort volume de travail ?",
     "corrige": r"""
Un **exemple concret** (période d'examens + projet, job à côté des études) avec la méthode employée :
priorisation, découpage, communication quand un délai est menacé. Montrer que tu restes précis sous pression :
en salle des marchés, une erreur de saisie coûte de l'argent.
"""},

    # ---------- Technique : produits et pricing ----------
    {"id": "ent-t01", "type": "Technique", "metiers": ["Trading", "Structuration", "Sales"],
     "question": "Comment price-t-on un forward sur action ?",
     "corrige": r"""
Par **cash-and-carry** : acheter l'action aujourd'hui en empruntant $S_0$ et la porter jusqu'à $T$
réplique le forward. Sans dividende, $F_0 = S_0 e^{rT}$ ; avec un rendement de dividende $q$,
$F_0 = S_0 e^{(r - q)T}$. Si le forward coté s'écarte de ce prix, un arbitrage existe.
Point bonus : le forward ne dépend **pas** des anticipations sur le prix futur.
"""},
    {"id": "ent-t02", "type": "Technique", "metiers": ["Trading", "Structuration", "Quant"],
     "question": "Pourquoi un call vaut-il plus cher quand la volatilité augmente ?",
     "corrige": r"""
Le payoff $(S_T - K)^+$ est **convexe** : les scénarios de forte hausse rapportent de plus en plus,
alors que les scénarios de baisse sont plafonnés à une perte nulle pour le détenteur. Plus de
volatilité élargit la distribution dans les deux sens, mais seul le côté favorable compte : la valeur
attendue du payoff augmente. Formellement, le vega $S\,n(d_1)\sqrt T$ est positif.
"""},
    {"id": "ent-t03", "type": "Technique", "metiers": ["Trading", "Quant"],
     "question": "Expliquez le delta hedging. Quel est le lien entre gamma et theta ?",
     "corrige": r"""
Le trader qui a vendu une option achète $\Delta$ unités du sous-jacent pour neutraliser les petits
mouvements. Le delta change avec le spot (gamma) : il faut rééquilibrer. Un vendeur d'option est
**short gamma** : il rachète après les hausses et revend après les baisses, ce qui lui coûte quand le
marché bouge beaucoup ; en échange il encaisse le **theta**. Sur $\Delta t$ :
$\text{PnL} \approx \tfrac12 \Gamma (\Delta S)^2 + \Theta \Delta t$. Le résultat dépend de la
volatilité réalisée face à la volatilité implicite.
"""},
    {"id": "ent-t04", "type": "Technique", "metiers": ["Tous"],
     "question": "Énoncez et démontrez la parité call-put.",
     "corrige": r"""
$C - P = S_0 - K e^{-rT}$ (européennes, sans dividende). Démonstration : le portefeuille
« call + zéro-coupon de nominal $K$ » et le portefeuille « put + action » valent tous deux
$\max(S_T, K)$ à maturité, donc ils ont la même valeur aujourd'hui par absence d'arbitrage.
"""},
    {"id": "ent-t05", "type": "Technique", "metiers": ["Structuration", "Sales"],
     "question": "Comment construire un produit à capital garanti à 100 % sur 5 ans indexé sur un indice actions ?",
     "corrige": r"""
Deux briques : un **zéro-coupon** qui garantit le remboursement du nominal à 5 ans, et des **calls**
sur l'indice achetés avec le reste. Exemple : avec un taux 5 ans de $3\,\%$, le zéro-coupon coûte
environ $100 / 1{,}03^5 \approx 86$ ; il reste environ $14$ (moins la marge) pour acheter des calls.
Le **taux de participation** = budget optionnel / prix du call ATM. Il augmente quand les taux montent
(zéro-coupon moins cher) et quand la volatilité baisse (calls moins chers). Leviers pour l'améliorer :
plafonner la hausse (call spread), moyenner le sous-jacent (option asiatique), allonger la maturité.
"""},
    {"id": "ent-t06", "type": "Technique", "metiers": ["Structuration", "Sales"],
     "question": "Qu'est-ce qu'un autocall et quels risques porte l'investisseur ?",
     "corrige": r"""
Produit structuré qui se **rembourse automatiquement par anticipation** avec un coupon si l'indice
est au-dessus d'un seuil (souvent son niveau initial) à une date d'observation. Sinon il continue.
À maturité, si l'indice est sous une **barrière de protection** (par exemple $-40\,\%$), l'investisseur
subit la baisse en capital. Il est en fait **vendeur d'un put à barrière** : il touche un coupon
élevé en échange d'un risque de perte en capital lors des fortes baisses. Risques : marché, émetteur
(crédit), durée incertaine.
"""},
    {"id": "ent-t07", "type": "Technique", "metiers": ["Trading", "Asset management", "Sales"],
     "question": "Qu'est-ce que la duration ? Que se passe-t-il pour une obligation si les taux montent de 1 % ?",
     "corrige": r"""
La duration de Macaulay est la maturité moyenne des flux pondérée par leur valeur actuelle. La
duration modifiée donne la sensibilité : $\Delta P / P \approx -D_{mod}\,\Delta y$. Avec $D_{mod} = 7$,
une hausse de $1\,\%$ fait perdre environ $7\,\%$, un peu moins grâce à la convexité positive.
"""},
    {"id": "ent-t08", "type": "Technique", "metiers": ["Trading", "Quant", "Asset management"],
     "question": "Qu'est-ce que la VaR ? Quelles sont ses limites ?",
     "corrige": r"""
La **Value at Risk** à $99\,\%$ sur 1 jour est la perte qui ne sera dépassée qu'avec une probabilité de $1\,\%$.
Pour une position gaussienne de volatilité journalière $\sigma$ et de valeur $V$ :
$VaR_{99} \approx 2{,}33\,\sigma V$. Limites : elle ne dit **rien sur l'ampleur** des pertes au-delà
du seuil, elle dépend des hypothèses (historique, normalité), et elle n'est pas toujours
sous-additive (la VaR d'un portefeuille peut dépasser la somme des VaR). L'**Expected Shortfall**
(perte moyenne au-delà de la VaR) corrige ce défaut et est utilisée par la réglementation actuelle.
"""},
    {"id": "ent-t09", "type": "Technique", "metiers": ["Asset management"],
     "question": "Qu'est-ce que le ratio de Sharpe et le bêta d'une action ?",
     "corrige": r"""
**Sharpe** $= \dfrac{\mathbb{E}[R_p] - r_f}{\sigma_p}$ : rendement en excès par unité de risque total.
**Bêta** $= \dfrac{\mathrm{Cov}(R_i, R_m)}{\mathrm{Var}(R_m)}$ : sensibilité au marché. Dans le CAPM,
$\mathbb{E}[R_i] = r_f + \beta_i (\mathbb{E}[R_m] - r_f)$ : seul le risque non diversifiable est rémunéré.
"""},
    {"id": "ent-t10", "type": "Technique", "metiers": ["Asset management", "Sales"],
     "question": "Comment la diversification réduit-elle le risque d'un portefeuille ?",
     "corrige": r"""
Pour deux actifs, $\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2 w_1 w_2 \rho\, \sigma_1 \sigma_2$.
Dès que $\rho < 1$, la volatilité du portefeuille est inférieure à la moyenne pondérée des volatilités.
Avec beaucoup d'actifs, le risque spécifique disparaît et il ne reste que le risque de marché (systématique).
"""},

    # ---------- Technique : macro ----------
    {"id": "ent-m01", "type": "Technique", "metiers": ["Tous"],
     "question": "La banque centrale monte ses taux plus qu'attendu. Que se passe-t-il sur les marchés ?",
     "corrige": r"""
Dérouler le mécanisme, classe d'actifs par classe d'actifs :
- **taux courts** en hausse (ils reflètent la politique monétaire attendue) ; **courbe** souvent plus plate ;
- **devise** qui s'apprécie (rendement plus attractif) ;
- **actions** en baisse (actualisation plus forte, croissance attendue plus faible), surtout les valeurs de croissance ;
- **crédit** : spreads qui s'écartent ; **volatilité** implicite en hausse.

Finir par la nuance : tout dépend de ce qui était **déjà anticipé** et du message sur la suite (*forward guidance*).
"""},
    {"id": "ent-m02", "type": "Technique", "metiers": ["Trading", "Asset management", "Sales"],
     "question": "Qu'est-ce que le point mort d'inflation (breakeven) et à quoi sert-il ?",
     "corrige": r"""
C'est l'écart entre le rendement d'une obligation d'État nominale et celui d'une obligation indexée sur
l'inflation de même maturité : $\text{breakeven} \approx y_{nominal} - y_{réel}$. C'est l'inflation moyenne
qui rendrait les deux placements équivalents, donc une mesure des **anticipations d'inflation du marché**
(avec des primes de risque et de liquidité). Un investisseur qui pense que l'inflation réalisée dépassera
le breakeven achète l'obligation indexée plutôt que la nominale.
"""},
    {"id": "ent-r01", "type": "Technique", "metiers": ["Trading", "Quant"],
     "question": "Comment backtester un modèle de VaR ?",
     "corrige": r"""
Comparer chaque jour la VaR de la veille au P&L réalisé et compter les **exceptions**. Pour une VaR 99 %
sur 250 jours, on en attend $2{,}5$. Le cadre bâlois : vert (0 à 4), orange (5 à 9), rouge (10 et plus).
Vérifier aussi que les exceptions sont **indépendantes** (pas regroupées pendant les crises), sinon le
modèle réagit trop lentement aux changements de volatilité.
"""},

    # ---------- Technique : quant ----------
    {"id": "ent-q01", "type": "Technique", "metiers": ["Quant"],
     "question": "Comment vérifier qu'une stratégie de trading n'est pas sur-optimisée (overfitting) ?",
     "corrige": r"""
- Séparer **in-sample / out-of-sample** (ou validation glissante, *walk-forward*) et ne regarder l'échantillon test qu'une fois.
- Limiter le nombre de paramètres et de variantes testées ; plus on teste, plus un bon résultat peut être dû au hasard.
- Intégrer **coûts de transaction**, glissement, contraintes de liquidité.
- Tester la **robustesse** : petites variations des paramètres, autres périodes, autres marchés.
- Se méfier d'un Sharpe très élevé sans explication économique.
"""},
    {"id": "ent-q02", "type": "Technique", "metiers": ["Quant"],
     "question": "Qu'est-ce qu'un mouvement brownien ? Que vaut E[W_t²] ?",
     "corrige": r"""
Processus $W$ avec $W_0 = 0$, trajectoires continues, accroissements **indépendants** et
**gaussiens** : $W_t - W_s \sim \mathcal{N}(0, t - s)$. Donc $\mathbb{E}[W_t] = 0$ et
$\mathbb{E}[W_t^2] = \mathrm{Var}(W_t) = t$. Par le lemme d'Itô, $d(W_t^2) = 2W_t\,dW_t + dt$ :
le terme $dt$ vient de la variation quadratique $(dW_t)^2 = dt$.
"""},
    {"id": "ent-q03", "type": "Technique", "metiers": ["Quant"],
     "question": "Comment pricer une option par Monte-Carlo, et comment réduire la variance de l'estimateur ?",
     "corrige": r"""
Simuler $N$ trajectoires du sous-jacent sous la probabilité **risque-neutre**
(par exemple $S_T = S_0 \exp\big((r - \tfrac12\sigma^2)T + \sigma\sqrt T\, Z\big)$), calculer le payoff
de chacune, faire la moyenne et actualiser. L'erreur standard décroît en $1/\sqrt N$. Réduction de
variance : **variables antithétiques** ($Z$ et $-Z$), **variable de contrôle** (un produit proche au
prix connu, par exemple le sous-jacent ou une option européenne), échantillonnage préférentiel.
"""},
]
