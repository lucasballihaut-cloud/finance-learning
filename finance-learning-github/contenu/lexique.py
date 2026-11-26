"""Lexique de la finance de marché : définitions courtes avec exemple.

Chaque entrée : terme, catégorie, définition (Markdown + LaTeX), exemple (facultatif).
"""

CATEGORIES = [
    "Options : les bases", "Moneyness", "Grecques", "Volatilité", "Barrières et exotiques",
    "Produits structurés", "Actions (equity)", "Matières premières", "Taux et crédit", "Marchés et trading", "Risque", "Macro",
]


def _t(terme, categorie, definition, exemple=""):
    return {"terme": terme, "categorie": categorie, "definition": definition, "exemple": exemple}


B, M, G, V, X, S, EQ, CO, T, MT, R, MA = CATEGORIES

LEXIQUE = [
    # ---------------------------------------------------------------- Options : les bases
    _t("Option", B, "Contrat qui donne à son acheteur un **droit**, et non une obligation, d'acheter ou de vendre un "
       "actif à un prix fixé (le strike) à une date donnée ou jusqu'à cette date. L'acheteur paie une prime au vendeur."),
    _t("Call", B, r"Option d'**achat**. Payoff à maturité : $(S_T - K)^+ = \max(S_T - K, 0)$. On achète un call "
       "quand on anticipe une hausse.", "Call de strike 100 : si l'action finit à 112, il rapporte 12 ; à 95, il rapporte 0."),
    _t("Put", B, r"Option de **vente**. Payoff à maturité : $(K - S_T)^+$. On achète un put pour parier sur une baisse "
       "ou pour **se protéger** (assurance d'un portefeuille).",
       "Put de strike 100 : si l'action finit à 80, il rapporte 20 ; à 105, il rapporte 0."),
    _t("Strike (prix d'exercice)", B, r"Le prix $K$ auquel l'option permet d'acheter (call) ou de vendre (put) le sous-jacent. "
       "Il est souvent exprimé en % du spot initial (strike 100 % = à la monnaie)."),
    _t("Prime", B, "Prix payé par l'acheteur de l'option au vendeur, à la signature. Perte maximale de l'acheteur, "
       "gain maximal du vendeur."),
    _t("Sous-jacent", B, "L'actif sur lequel porte le dérivé : action, indice, taux, devise, matière première, panier…"),
    _t("Maturité (échéance)", B, r"Date $T$ à laquelle l'option expire. La **durée restante** $T - t$ influence fortement "
       "le prix (valeur temps)."),
    _t("Payoff", B, "Ce que rapporte un produit à maturité en fonction du prix final du sous-jacent, avant déduction de la prime."),
    _t("Option européenne / américaine / bermudéenne", B, "Européenne : exercice seulement à maturité. Américaine : à tout "
       "moment jusqu'à maturité. Bermudéenne : à certaines dates fixées."),
    _t("Valeur intrinsèque", B, r"Ce que rapporterait un exercice immédiat : $(S - K)^+$ pour un call, $(K - S)^+$ pour un put. "
       "Nulle pour une option hors de la monnaie.", "Call strike 100, spot 110 : valeur intrinsèque 10."),
    _t("Valeur temps", B, "Prix de l'option moins sa valeur intrinsèque. Rémunère la possibilité que le sous-jacent bouge "
       "favorablement d'ici la maturité. Maximale à la monnaie, nulle à l'échéance.",
       "Call strike 100, spot 110, prix 14 : valeur temps 4."),
    _t("Long / short", B, "Être **long**, c'est détenir (acheteur) : on gagne si la valeur monte. Être **short**, c'est avoir "
       "vendu : on gagne si la valeur baisse. On peut être long ou short d'une option, d'une action, de la volatilité…"),
    _t("Vente à nu (naked)", B, "Vendre une option sans détenir de couverture. Un call vendu à nu a une perte potentielle illimitée."),

    # ---------------------------------------------------------------- Moneyness
    _t("Moneyness", M, r"Position du strike par rapport au prix du sous-jacent, souvent mesurée par $K / S$ ou par le delta. "
       "Elle détermine si l'option a de la valeur intrinsèque."),
    _t("ITM — In the money (dans la monnaie)", M, r"Option qui a une **valeur intrinsèque positive** : call avec $S > K$, "
       "put avec $S < K$. Son delta est élevé en valeur absolue (proche de 1 pour un call très ITM).",
       "Spot 110 : le call 100 est ITM, le put 100 ne l'est pas."),
    _t("ATM — At the money (à la monnaie)", M, r"Strike égal (ou très proche) du spot : $K \approx S$. Valeur intrinsèque "
       "nulle, valeur temps maximale, delta proche de 0,5 pour un call. Gamma et vega y sont maximaux.",
       "Spot 100 : le call 100 et le put 100 sont ATM."),
    _t("OTM — Out of the money (hors de la monnaie)", M, r"Option sans valeur intrinsèque : call avec $S < K$, put avec $S > K$. "
       "Son prix n'est que de la valeur temps ; elle est bon marché mais a une faible probabilité de finir dans la monnaie.",
       "Spot 100 : un put 80 et un call 120 sont OTM."),
    _t("Deep ITM / deep OTM", M, "Très dans ou très hors de la monnaie. Une option deep ITM se comporte presque comme le "
       "sous-jacent (delta ≈ ±1) ; une option deep OTM vaut presque zéro (delta ≈ 0)."),
    _t("ATMF — à la monnaie forward", M, r"Strike égal au **prix forward** $F = S e^{(r-q)T}$ plutôt qu'au spot. Convention "
       "fréquente sur les desks car c'est le strike où call et put ont la même valeur (parité call-put)."),
    _t("Option 25-delta", M, "Option dont le delta vaut 0,25 (call) ou −0,25 (put) : une option OTM de référence. Les marchés "
       "de change cotent le smile avec les options 25-delta et 10-delta."),

    # ---------------------------------------------------------------- Grecques
    _t("Delta (Δ)", G, r"Sensibilité du prix de l'option au sous-jacent : $\partial V / \partial S$. Call : entre 0 et 1, "
       "put : entre −1 et 0. C'est aussi le nombre d'actions à détenir pour couvrir l'option.",
       "Delta 0,6 : si l'action monte de 1 €, l'option gagne environ 0,60 €."),
    _t("Gamma (Γ)", G, r"Variation du delta quand le sous-jacent bouge : $\partial^2 V / \partial S^2$. Positif pour une option "
       "achetée, maximal ATM près de l'échéance. Être long gamma : on gagne sur les grands mouvements."),
    _t("Vega", G, r"Sensibilité à la volatilité implicite : $\partial V / \partial \sigma$, en général pour +1 point de vol. "
       "Positive pour toute option vanille achetée, maximale ATM et croissante avec la maturité.",
       "Vega 0,25 : si la vol passe de 20 % à 21 %, l'option gagne 0,25."),
    _t("Theta (Θ)", G, r"Variation du prix avec le temps qui passe : $\partial V / \partial t$, souvent par jour. Généralement "
       "négatif pour une option achetée : c'est le coût du gamma."),
    _t("Rho (ρ)", G, r"Sensibilité au taux d'intérêt : $\partial V / \partial r$. Positif pour un call, négatif pour un put."),
    _t("Vanna", G, r"Sensibilité croisée : variation du delta quand la vol bouge, ou du vega quand le spot bouge "
       r"($\partial^2 V / \partial S \partial \sigma$). Importante pour gérer le skew."),
    _t("Volga (vomma)", G, r"Variation du vega quand la vol bouge : $\partial^2 V / \partial \sigma^2$. Une position longue "
       "volga gagne quand la volatilité de la volatilité est forte."),
    _t("Delta-neutre / delta hedging", G, "Position dont le delta total est nul : insensible aux petits mouvements du "
       "sous-jacent. Le delta hedging consiste à ajuster régulièrement la quantité de sous-jacent pour rester delta-neutre."),

    # ---------------------------------------------------------------- Volatilité
    _t("Volatilité réalisée (historique)", V, r"Écart-type des rendements observés sur une période, annualisé "
       r"($\sigma_{jour}\sqrt{252}$). Mesure ce qui s'est réellement passé.", "1 % par jour ≈ 16 % par an."),
    _t("Volatilité implicite", V, "La volatilité qui, mise dans Black-Scholes, redonne le prix de marché de l'option. Elle "
       "reflète l'anticipation et la demande du marché ; les options se cotent souvent directement en vol."),
    _t("Smile de volatilité", V, "Courbe de la volatilité implicite en fonction du strike en forme de sourire : les options "
       "OTM des deux côtés ont une vol plus élevée que l'ATM. Typique du change."),
    _t("Skew de volatilité", V, "Asymétrie du smile. Sur les actions, la vol implicite est **plus élevée pour les strikes bas** : "
       "les puts OTM sont chers, car les investisseurs achètent de la protection et les krachs sont plus fréquents que ne le "
       "prévoit la loi normale. On parle de skew négatif ou de *put skew*.",
       "Indice à 100 : vol du put 90 à 24 %, vol ATM à 18 %, vol du call 110 à 15 %."),
    _t("Structure par terme de la volatilité", V, "Volatilité implicite en fonction de la maturité. En général croissante en "
       "période calme, inversée (vol courte plus haute) en période de stress."),
    _t("Surface de volatilité", V, "Volatilité implicite en fonction du strike **et** de la maturité. C'est l'objet que "
       "gèrent les traders d'options et que calibrent les quants."),
    _t("Risk reversal (en vol)", V, "Écart de vol entre un call et un put OTM de même delta (par exemple 25-delta). Mesure le "
       "**skew** : négatif sur les actions. En stratégie, c'est aussi l'achat d'un call OTM financé par la vente d'un put OTM."),
    _t("Butterfly (en vol)", V, "Moyenne des vols des options 25-delta call et put moins la vol ATM. Mesure la **courbure** du "
       "smile (épaisseur des queues). En stratégie : long ailes, short 2 × le centre."),
    _t("Vol de vol", V, "Volatilité de la volatilité implicite elle-même. Les produits sensibles au volga (barrières, cliquets) en dépendent."),
    _t("VIX", V, "Indice de volatilité implicite à 30 jours du S&P 500, calculé à partir des prix d'options. Surnommé « indice "
       "de la peur » : il monte quand les marchés baissent."),

    # ---------------------------------------------------------------- Barrières et exotiques
    _t("Barrière", X, "Niveau du sous-jacent qui, s'il est touché, **active** (knock-in) ou **désactive** (knock-out) une "
       "option. Observée en continu (chaque instant), quotidiennement ou seulement à maturité selon le contrat."),
    _t("Knock-in (activante)", X, "Option qui n'existe que si la barrière est touchée. Moins chère que la vanille.",
       "Put 100 knock-in 70 : il ne devient un vrai put que si le spot passe sous 70."),
    _t("Knock-out (désactivante)", X, "Option qui disparaît si la barrière est touchée (avec parfois un rebate). Moins chère "
       "que la vanille. Relation : knock-in + knock-out = vanille."),
    _t("Up-and-in / up-and-out", X, "Barrière **au-dessus** du spot : l'option s'active (up-and-in) ou se désactive "
       "(up-and-out) si le sous-jacent **monte** jusqu'à la barrière.",
       "Call 100 up-and-out 130 : rapporte jusqu'à 30, mais vaut 0 (ou le rebate) si le spot touche 130. Brique du Shark."),
    _t("Down-and-in / down-and-out", X, "Barrière **en dessous** du spot : l'option s'active (down-and-in) ou se désactive "
       "(down-and-out) si le sous-jacent **baisse** jusqu'à la barrière."),
    _t("Put down-and-in", X, "Put qui ne s'active que si le sous-jacent baisse jusqu'à la barrière. Si la barrière n'est jamais "
       "touchée, il ne vaut rien ; si elle l'est, il devient un put normal (souvent de strike 100 %). C'est l'option "
       "**vendue par l'investisseur** dans un autocall ou un reverse convertible à barrière : elle explique la perte en "
       "capital sous la barrière et l'effet couperet.",
       "Put 100 down-and-in 60 : spot final 55 et barrière touchée → paie 45, soit toute la baisse depuis 100."),
    _t("Put down-and-out", X, "Put qui disparaît si le sous-jacent baisse jusqu'à la barrière. Brique du Twin Win et du Bonus : "
       "la protection fonctionne tant que la barrière n'est pas touchée."),
    _t("Rebate", X, "Montant fixe versé quand une option knock-out est désactivée (ou quand une knock-in ne s'active pas).",
       "Shark : rebate de 5 % si la barrière haute est touchée."),
    _t("Digitale (binaire)", X, r"Option qui paie un montant fixe si une condition est remplie à maturité (par exemple "
       r"$S_T > K$). Prix Black-Scholes : $Q\,e^{-rT}N(d_2)$. Les coupons conditionnels des autocalls sont des digitales."),
    _t("Option asiatique", X, "Payoff calculé sur la **moyenne** des cours. Moins chère qu'une vanille car la moyenne est moins volatile."),
    _t("Lookback", X, "Payoff calculé sur le maximum ou le minimum atteint. Toujours plus chère qu'une vanille."),
    _t("Worst-of / best-of", X, "Option sur plusieurs sous-jacents dont le payoff dépend du **moins** (worst-of) ou du **plus** "
       "(best-of) performant. Un put worst-of est d'autant plus cher que la corrélation est faible."),
    _t("Quanto", X, "Option sur un sous-jacent étranger payée dans une autre devise à un change fixé : supprime le risque de "
       "change, mais dépend de la corrélation sous-jacent/devise."),
    _t("Cliquet", X, "Somme de performances périodiques, chacune plafonnée et planchée, avec strike remis à jour à chaque période."),

    # ---------------------------------------------------------------- Produits structurés
    _t("Produit structuré", S, "Combinaison d'un placement de taux (zéro-coupon) et d'options, émise par une banque sous forme "
       "de dette (EMTN, certificat). Décomposition : zéro-coupon + options + marge."),
    _t("Émetteur et risque émetteur", S, "La banque qui émet le produit. Si elle fait défaut, l'investisseur peut perdre son "
       "capital, même sur un produit « garanti »."),
    _t("Term sheet", S, "Fiche technique d'un produit : sous-jacent, dates, seuils, barrières, coupons, formule de remboursement."),
    _t("DIC (KID)", S, "Document d'Informations Clés imposé par la réglementation PRIIPs : indicateur de risque de 1 à 7, "
       "scénarios de performance, coûts."),
    _t("Taux de participation", S, "Part de la hausse du sous-jacent reversée à l'investisseur dans un capital garanti.",
       "Participation 60 %, indice +30 % : gain de 18 %."),
    _t("Autocall", S, "Produit remboursé par anticipation (avec un coupon) dès que le sous-jacent est au-dessus d'un seuil de "
       "rappel à une date d'observation. Capital à risque sous une barrière à maturité."),
    _t("Seuil de rappel", S, "Niveau (souvent 100 % du niveau initial) au-dessus duquel un autocall est remboursé par anticipation."),
    _t("Barrière de protection", S, "Niveau sous lequel, à maturité, l'investisseur perd en capital (par exemple 60 %)."),
    _t("Barrière de coupon", S, "Niveau au-dessus duquel un Phoenix verse son coupon conditionnel (par exemple 70 %)."),
    _t("Effet couperet", S, "Sous la barrière de protection, l'investisseur subit toute la baisse depuis 100 %, pas seulement "
       "la partie sous la barrière.", "Barrière 60 %, indice final 55 % : remboursement 55, pas 95."),
    _t("Athena", S, "Autocall dont le coupon, cumulé, n'est payé qu'au rappel anticipé ou à maturité."),
    _t("Phoenix", S, "Autocall qui verse un coupon conditionnel à chaque date si le sous-jacent est au-dessus de la barrière de coupon."),
    _t("Effet mémoire", S, "Les coupons non versés sont rattrapés dès qu'une date d'observation remplit à nouveau la condition."),
    _t("Step-down", S, "Seuil de rappel qui baisse à chaque date d'observation : rappel plus probable, coupon plus faible."),
    _t("Airbag", S, "Mécanisme qui amortit la perte sous la barrière au lieu de l'effet couperet. Formule variable selon l'émetteur."),
    _t("Indice à décrément", S, "Indice qui retire chaque année un dividende fixe : forward plus bas, coupons plus élevés, "
       "mais indice structurellement pénalisé."),
    _t("Reverse convertible", S, "Zéro-coupon + coupons − put : coupon élevé garanti, capital à risque si l'action baisse."),
    _t("Twin Win", S, "Gain égal à la valeur absolue de la performance tant que la barrière basse n'est jamais touchée."),
    _t("Bonus", S, "Remboursement au moins égal au niveau du bonus tant que la barrière basse n'est jamais touchée."),
    _t("Shark (requin)", S, "Capital garanti avec participation à la hausse tant qu'une barrière haute n'est pas touchée, sinon rebate."),
    _t("Capital garanti / protégé", S, "Garanti : 100 % rendu à maturité (hors défaut de l'émetteur). Protégé : une partie "
       "seulement (par exemple 90 %)."),

    # ---------------------------------------------------------------- Actions (equity)
    _t("Capitalisation boursière", EQ, "Cours × nombre d'actions : valeur de marché des fonds propres."),
    _t("Valeur d'entreprise (VE)", EQ, "Capitalisation + dette nette (+ minoritaires…) : valeur de l'activité pour tous les financeurs.",
       "Capitalisation 800, dette nette 200 : VE 1 000."),
    _t("EBITDA", EQ, "Résultat avant intérêts, impôts, dépréciations et amortissements ; base du multiple VE/EBITDA."),
    _t("Free cash flow", EQ, "Cash réellement disponible : ≈ EBITDA − impôts − investissements − variation du BFR."),
    _t("BFR", EQ, "Besoin en fonds de roulement : stocks + créances clients − dettes fournisseurs."),
    _t("PER", EQ, "Price earnings ratio : cours / bénéfice par action. Son inverse est le rendement bénéficiaire.",
       "Cours 50 €, BPA 2,5 € : PER 20, rendement bénéficiaire 5 %."),
    _t("ROE / ROCE", EQ, "ROE : résultat net / capitaux propres. ROCE : résultat opérationnel après impôt / capitaux employés."),
    _t("DCF", EQ, "Discounted cash flows : valeur actuelle des free cash flows futurs, plus une valeur terminale, actualisés au WACC."),
    _t("WACC", EQ, r"Coût moyen pondéré du capital : $\frac{E}{E+D}k_e + \frac{D}{E+D}k_d(1-t)$."),
    _t("Valeur terminale", EQ, r"Valeur des flux au-delà de l'horizon explicite : $FCF_n(1+g)/(WACC-g)$."),
    _t("Comparables", EQ, "Valorisation par les multiples d'entreprises cotées similaires (ou de transactions récentes)."),
    _t("Alpha", EQ, "Rendement d'un portefeuille au-delà de ce qu'explique son exposition au marché (bêta)."),
    _t("Long/short, market neutral", EQ, "Acheter des actions sous-évaluées et vendre des surévaluées ; market neutral si l'exposition bêta nette est nulle."),
    _t("Merger arbitrage", EQ, "Acheter la cible d'un rachat sous le prix d'offre en pariant sur la réalisation de l'opération."),
    _t("Short squeeze", EQ, "Hausse brutale d'une action très vendue à découvert, qui force les vendeurs à racheter."),
    _t("Delta one", EQ, "Produits dont le delta vaut 1 : futures, TRS, ETF, prêt de titres."),
    _t("ECM", EQ, "Equity Capital Markets : introductions en bourse, augmentations de capital, placements de blocs."),
    _t("Catalyseur", EQ, "Événement qui doit faire converger le cours vers la valeur estimée (résultats, rachat, cession…)."),

    # ---------------------------------------------------------------- Matières premières
    _t("Brent / WTI", CO, "Les deux pétroles de référence : Brent (mer du Nord, ICE) et WTI (Texas, livré à Cushing, NYMEX)."),
    _t("Convenience yield", CO, "Avantage de détenir le bien physique immédiatement ; élevé quand les stocks sont bas."),
    _t("Roll yield", CO, "Gain ou perte en roulant une position en futures : négatif en contango, positif en backwardation."),
    _t("Crack spread", CO, "Marge de raffinage : valeur des produits raffinés moins coût du brut (souvent 3:2:1).",
       "Brut 80 $, essence 100 $, diesel 110 $ : crack 3:2:1 ≈ 23,3 $/baril."),
    _t("Spark spread / dark spread", CO, "Marge d'une centrale à gaz (spark) ou à charbon (dark) ; « clean » si l'on retire le coût du CO₂."),
    _t("Crush spread", CO, "Marge de trituration du soja : tourteau + huile − graines."),
    _t("Heat rate", CO, "Quantité de combustible nécessaire pour produire 1 MWh d'électricité."),
    _t("Once troy", CO, "31,1035 g : unité de cotation des métaux précieux."),
    _t("LME", CO, "London Metal Exchange : place de référence des métaux industriels."),
    _t("OPEP+", CO, "Organisation des pays exportateurs de pétrole et ses alliés (dont la Russie), qui fixent des quotas de production."),
    _t("Livraison physique / règlement en cash", CO, "Un future peut se dénouer par la livraison du bien ou par un simple paiement de la différence."),
    _t("Trading house", CO, "Négociant en matières premières (Vitol, Trafigura, Glencore…) qui achète, transporte, stocke et revend."),

    # ---------------------------------------------------------------- Taux et crédit
    _t("Point de base (bp)", T, "Un centième de pour cent : 0,01 %. 50 bp = 0,50 %."),
    _t("Rendement actuariel (yield)", T, "Taux unique qui égalise la valeur actuelle des flux d'une obligation et son prix."),
    _t("Duration", T, r"Maturité moyenne des flux pondérée par leur valeur actuelle. La duration modifiée donne la "
       r"sensibilité : $\Delta P / P \approx -D_{mod}\,\Delta y$.", "Duration 7 : +1 % de taux ≈ −7 % de prix."),
    _t("Convexité", T, "Courbure de la relation prix-taux. Positive pour une obligation classique : on gagne plus à la baisse "
       "des taux qu'on ne perd à la hausse."),
    _t("DV01", T, "Variation de valeur d'une position pour +1 bp de taux, en euros."),
    _t("Courbe des taux", T, "Taux en fonction de la maturité. Pentue, plate ou inversée."),
    _t("Taux forward", T, "Taux d'un emprunt futur fixé aujourd'hui, déduit de la courbe par absence d'arbitrage."),
    _t("Swap de taux", T, "Échange d'un taux fixe contre un taux variable sur un nominal, sans échange du nominal."),
    _t("Spread de crédit", T, "Écart de rendement entre une obligation d'entreprise et un emprunt d'État de même maturité : "
       "rémunère le risque de défaut et l'illiquidité."),
    _t("CDS", T, "Credit Default Swap : assurance contre le défaut d'un émetteur, payée par une prime périodique."),
    _t("€STR / SOFR", T, "Taux au jour le jour de référence de la zone euro (€STR) et des États-Unis (SOFR)."),
    _t("Repo", T, "Prêt garanti par des titres : on vend un titre et on s'engage à le racheter plus tard. Sert à financer des positions."),

    # ---------------------------------------------------------------- Marchés et trading
    _t("Bid / ask", MT, "Bid : prix auquel le teneur de marché achète. Ask (offer) : prix auquel il vend. L'écart est la "
       "fourchette (bid-ask spread)."),
    _t("Market making", MT, "Activité qui consiste à coter en permanence un prix d'achat et de vente pour fournir de la liquidité."),
    _t("Liquidité", MT, "Capacité à traiter rapidement une taille importante sans trop faire bouger le prix."),
    _t("Hedge (couverture)", MT, "Position prise pour réduire un risque existant."),
    _t("Book", MT, "Ensemble des positions d'un trader ou d'un desk, avec leurs risques (delta, vega, DV01…)."),
    _t("P&L", MT, "Profit and Loss : gain ou perte d'une position ou d'un desk."),
    _t("Carry", MT, "Gain (ou coût) obtenu en détenant une position si les prix ne bougent pas : coupons, différentiel de taux, theta…"),
    _t("Flow / exotique", MT, "Flow : produits standards, gros volumes. Exotique : produits complexes et sur mesure."),
    _t("OTC", MT, "De gré à gré : contrat négocié bilatéralement, hors bourse."),
    _t("Chambre de compensation", MT, "Contrepartie centrale entre acheteur et vendeur, qui exige des marges pour réduire le "
       "risque de contrepartie."),
    _t("Contango / backwardation", MT, "Contango : futures au-dessus du spot. Backwardation : futures en dessous."),

    # ---------------------------------------------------------------- Risque
    _t("VaR", R, "Value at Risk : perte qui ne sera dépassée qu'avec une probabilité donnée sur un horizon donné.",
       "VaR 99 % 1 jour de 1 M€ : on perd plus de 1 M€ environ un jour sur cent."),
    _t("Expected Shortfall", R, "Perte moyenne au-delà de la VaR. Mesure de risque cohérente, utilisée par la réglementation."),
    _t("Stress test", R, "Application au portefeuille d'un scénario extrême (historique ou hypothétique)."),
    _t("Corrélation", R, "Mesure, entre −1 et 1, de la tendance de deux actifs à évoluer ensemble."),
    _t("Bêta", R, "Sensibilité d'un actif au marché : bêta 1,2 signifie +1,2 % en moyenne quand le marché fait +1 %."),
    _t("Ratio de Sharpe", R, r"Rendement en excès du taux sans risque divisé par la volatilité : $(R_p - r_f)/\sigma_p$."),
    _t("Drawdown", R, "Baisse entre un plus haut et le plus bas suivant. Le maximum drawdown est la pire de ces baisses."),

    # ---------------------------------------------------------------- Macro
    _t("Hawkish / dovish", MA, "Hawkish : priorité à la lutte contre l'inflation (taux plus hauts). Dovish : soutien à "
       "l'activité (taux plus bas)."),
    _t("QE / QT", MA, "Quantitative easing : achats massifs de titres par la banque centrale pour faire baisser les taux longs. "
       "Quantitative tightening : réduction de ce bilan."),
    _t("Inflation sous-jacente (core)", MA, "Inflation hors énergie et alimentation."),
    _t("Breakeven d'inflation", MA, "Rendement nominal moins rendement réel d'une obligation indexée : inflation anticipée par le marché."),
    _t("PMI", MA, "Enquête auprès des directeurs d'achat : au-dessus de 50, expansion ; en dessous, contraction."),
    _t("Risk-on / risk-off", MA, "Risk-on : appétit pour le risque (actions, crédit). Risk-off : fuite vers les valeurs refuges."),
]
