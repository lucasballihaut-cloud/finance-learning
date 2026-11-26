"""Culture générale pour les entretiens : capitalisations, banques centrales, indices, institutions.

⚠️ Ces données changent : capitalisations (chaque jour), dirigeants (au fil des nominations).
Mets à jour DATE_MAJ quand tu modifies ce fichier, et revérifie avant un entretien.
Capitalisations en milliards de dollars (Md$), arrondies, relevées sur companiesmarketcap.com.
"""

DATE_MAJ = "25 novembre 2026"

SOURCES = [
    ("Capitalisations boursières", "https://companiesmarketcap.com/"),
    ("Fed : Kevin Warsh président depuis le 22 mai 2026", "https://www.cbsnews.com/news/kevin-warsh-sworn-in-federal-reserve-chair/"),
    ("BCE : départ anticipé de Christine Lagarde le 7 février 2027", "https://www.cnbc.com/2026/10/29/lagarde-ecb-stand-down.html"),
    ("Banque de France : Emmanuel Moulin gouverneur depuis le 2 juin 2026",
     "https://www.banque-france.fr/fr/communiques-de-presse/emmanuel-moulin-est-nomme-gouverneur-de-la-banque-de-france"),
    ("Banque de Corée : Hyun Song Shin gouverneur depuis le 21 avril 2026", "https://www.bis.org/press/p260416a.htm"),
    ("Bank Indonesia : Destry Damayanti gouverneure depuis septembre 2026",
     "https://www.thejakartapost.com/business/2026/09/01/legislature-confirms-destry-as-new-central-bank-chief"),
    ("Dirigeants des banques centrales (présidences BIS, mai 2026)", "https://www.bis.org/press/p260512.htm"),
]

# ------------------------------------------------------------------ Capitalisations
# (rang, entreprise, pays, capitalisation en Md$, secteur)
MONDE = [
    (1, "Apple", "États-Unis", 5029, "Technologie"),
    (2, "Microsoft", "États-Unis", 3553, "Technologie"),
    (3, "Nvidia", "États-Unis", 3440, "Semi-conducteurs"),
    (4, "Alphabet (Google)", "États-Unis", 3227, "Technologie"),
    (5, "Amazon", "États-Unis", 2560, "Commerce en ligne, cloud"),
    (6, "Saudi Aramco", "Arabie saoudite", 1693, "Pétrole"),
    (7, "TSMC", "Taïwan", 1688, "Semi-conducteurs"),
    (8, "SpaceX", "États-Unis", 1580, "Spatial (non cotée)"),
    (9, "Meta Platforms", "États-Unis", 1471, "Réseaux sociaux"),
    (10, "Tesla", "États-Unis", 1435, "Automobile"),
    (11, "Broadcom", "États-Unis", 1349, "Semi-conducteurs"),
    (12, "Berkshire Hathaway", "États-Unis", 1227, "Holding, assurance"),
    (13, "Eli Lilly", "États-Unis", 1226, "Pharmacie"),
    (14, "Anthropic", "États-Unis", 1059, "IA (non cotée)"),
    (15, "Walmart", "États-Unis", 1046, "Distribution"),
]

# Par zone : liste de (pays, [(entreprise, Md$), ...]) – top 5 de chaque pays
PAR_ZONE = {
    "Amérique du Nord": [
        ("États-Unis", [("Apple", 5029), ("Microsoft", 3553), ("Nvidia", 3440), ("Alphabet", 3227), ("Amazon", 2560)]),
        ("Canada", [("Royal Bank of Canada", 258), ("Toronto-Dominion Bank", 187), ("Shopify", 161),
                    ("Bank of Montreal", 109), ("Enbridge", 104)]),
    ],
    "Europe": [
        ("Union européenne", [("ASML (Pays-Bas)", 478), ("L'Oréal (France)", 258), ("SAP (Allemagne)", 240),
                              ("LVMH (France)", 211), ("Siemens (Allemagne)", 207)]),
        ("France", [("L'Oréal", 258), ("LVMH", 211), ("TotalEnergies", 187), ("Hermès", 143), ("Schneider Electric", 139)]),
        ("Allemagne", [("SAP", 240), ("Siemens", 208), ("Allianz", 186), ("Deutsche Telekom", 141), ("Siemens Energy", 104)]),
        ("Royaume-Uni", [("AstraZeneca", 284), ("HSBC", 272), ("Shell", 264), ("Linde", 239), ("Arm Holdings", 158)]),
        ("Suisse", [("Roche", 395), ("Novartis", 291), ("Nestlé", 270), ("Chubb", 146), ("ABB", 138)]),
        ("Pays-Bas", [("ASML", 478), ("Airbus", 165), ("Prosus", 140), ("ING", 82), ("Argenx", 60)]),
    ],
    "Asie": [
        ("Chine", [("China Construction Bank", 494), ("Agricultural Bank of China", 418), ("Tencent", 378),
                   ("Bank of China", 363), ("CXMT", 357)]),
        ("Japon", [("Toyota", 249), ("Mitsubishi UFJ Financial", 215), ("Fast Retailing", 166), ("Sony", 164), ("Recruit", 148)]),
        ("Taïwan", [("TSMC", 1691), ("MediaTek", 175), ("Foxconn", 87), ("Delta Electronics", 82), ("ASE Group", 60)]),
        ("Corée du Sud", [("Samsung", 826), ("SK Hynix", 539), ("SK Square", 62), ("LG Energy Solution", 54), ("Hyundai", 53)]),
        ("Inde", [("Reliance Industries", 202), ("HDFC Bank", 145), ("Bharti Airtel", 143), ("Jio Platforms", 140), ("ICICI Bank", 130)]),
        ("Hong Kong", [("AIA", 96), ("Bank of China (Hong Kong)", 61), ("HKEX", 56), ("Swire Pacific", 49), ("Jardine Matheson", 43)]),
    ],
    "Moyen-Orient": [
        ("Arabie saoudite", [("Saudi Aramco", 1693), ("Al Rajhi Bank", 97), ("Saudi National Bank", 58), ("Ma'aden", 57),
                             ("Saudi Telecom", 54)]),
        ("Israël", [("Teva", 46), ("Bank Leumi", 31), ("Elbit Systems", 30), ("Bank Hapoalim", 27), ("Check Point", 16)]),
    ],
    "Amérique latine": [
        ("Brésil", [("Petrobras", 103), ("Itaú Unibanco", 74), ("Nu Holdings", 57), ("Ambev", 42), ("Vale", 41)]),
        ("Mexique", [("Grupo México", 75), ("América Movil", 74), ("Walmex", 47), ("FEMSA", 45), ("Banorte", 28)]),
    ],
    "Afrique": [
        ("Afrique du Sud", [("AngloGold Ashanti", 37), ("Capitec Bank", 30), ("Gold Fields", 28), ("FirstRand", 28),
                            ("Standard Bank", 27)]),
    ],
    "Océanie": [
        ("Australie", [("Commonwealth Bank", 187), ("BHP", 172), ("Westpac", 80), ("ANZ", 77), ("National Australia Bank", 75)]),
    ],
}

# ------------------------------------------------------------------ Banques centrales
# (continent, pays/zone, institution, dirigeant, titre, depuis, cible d'inflation, à savoir)
BANQUES_CENTRALES = [
    ("Amérique du Nord", "États-Unis", "Réserve fédérale (Fed)", "Kevin Warsh", "Président", "mai 2026", "2 %",
     "Double mandat : emploi et stabilité des prix. Décisions prises par le FOMC (8 réunions par an). A succédé à Jerome Powell."),
    ("Amérique du Nord", "Canada", "Banque du Canada", "Tiff Macklem", "Gouverneur", "2020", "2 % (fourchette 1-3 %)",
     "Taux directeur à 2,25 % en septembre 2026."),
    ("Amérique du Nord", "Mexique", "Banco de México (Banxico)", "Victoria Rodríguez Ceja", "Gouverneure", "2022", "3 % (± 1 point)",
     "Première femme à diriger Banxico."),
    ("Europe", "Zone euro", "Banque centrale européenne (BCE)", "Christine Lagarde", "Présidente", "2019", "2 % (symétrique)",
     "Départ anticipé annoncé pour le 7 février 2027 ; candidats cités : Pablo Hernández de Cos et Klaas Knot. Siège à Francfort."),
    ("Europe", "France", "Banque de France", "Emmanuel Moulin", "Gouverneur", "juin 2026", "— (membre de l'Eurosystème)",
     "A succédé à François Villeroy de Galhau. Siège au Conseil des gouverneurs de la BCE."),
    ("Europe", "Royaume-Uni", "Bank of England (BoE)", "Andrew Bailey", "Gouverneur", "2020", "2 %",
     "Mandat jusqu'en mars 2028. Décisions prises par le Monetary Policy Committee (MPC)."),
    ("Europe", "Suisse", "Banque nationale suisse (BNS)", "Martin Schlegel", "Président de la direction générale", "octobre 2024",
     "Moins de 2 %", "Intervient sur le change pour limiter l'appréciation du franc."),
    ("Europe", "Russie", "Banque de Russie", "Elvira Nabiullina", "Gouverneure", "2013", "4 %",
     "Mandat jusqu'en juin 2027."),
    ("Europe", "Turquie", "Banque centrale de Turquie", "Fatih Karahan", "Gouverneur", "février 2024", "5 % (cible officielle)",
     "Inflation encore très élevée : environ 31 % fin 2025."),
    ("Asie", "Chine", "Banque populaire de Chine (PBoC)", "Pan Gongsheng", "Gouverneur", "2023", "— (objectif annuel du gouvernement)",
     "Politique qualifiée de « modérément accommodante »."),
    ("Asie", "Japon", "Banque du Japon (BoJ)", "Kazuo Ueda", "Gouverneur", "2023", "2 %",
     "A mis fin aux taux négatifs et au contrôle de la courbe des taux."),
    ("Asie", "Inde", "Reserve Bank of India (RBI)", "Sanjay Malhotra", "Gouverneur", "décembre 2024", "4 % (± 2 points)",
     "A succédé à Shaktikanta Das."),
    ("Asie", "Corée du Sud", "Banque de Corée", "Hyun Song Shin", "Gouverneur", "avril 2026", "2 %",
     "Ancien conseiller économique de la BRI ; mandat jusqu'en 2030."),
    ("Asie", "Indonésie", "Bank Indonesia", "Destry Damayanti", "Gouverneure", "septembre 2026", "2,5 % (± 1 point)",
     "A succédé à Perry Warjiyo, démissionnaire en juillet 2026."),
    ("Amérique latine", "Brésil", "Banco Central do Brasil", "Gabriel Galípolo", "Gouverneur", "2025", "3 %",
     "Taux directeur : le Selic."),
    ("Afrique", "Afrique du Sud", "South African Reserve Bank (SARB)", "Lesetja Kganyago", "Gouverneur", "2014", "3 %",
     "Plus ancien gouverneur des grands émergents."),
    ("Afrique", "Nigeria", "Central Bank of Nigeria", "Olayemi Cardoso", "Gouverneur", "2023", "—",
     "A unifié les taux de change du naira."),
    ("Afrique", "Égypte", "Banque centrale d'Égypte", "Hassan Abdalla", "Gouverneur", "2022", "—", ""),
    ("Afrique", "Maroc", "Bank Al-Maghrib", "Abdellatif Jouahri", "Wali (gouverneur)", "2003", "—",
     "Plus de 20 ans à la tête de la banque centrale."),
    ("Océanie", "Australie", "Reserve Bank of Australia (RBA)", "Michele Bullock", "Gouverneure", "2023", "2-3 %",
     "Première femme à diriger la RBA."),
    ("Océanie", "Nouvelle-Zélande", "Reserve Bank of New Zealand", "Anna Breman", "Gouverneure", "décembre 2025", "1-3 % (milieu : 2 %)",
     "Ancienne première sous-gouverneure de la Riksbank (Suède)."),
]

# ------------------------------------------------------------------ Institutions internationales
INSTITUTIONS = [
    ("FMI (Fonds monétaire international)", "Washington", "Kristalina Georgieva",
     "Prête aux pays en difficulté de balance des paiements, surveille l'économie mondiale."),
    ("Banque mondiale", "Washington", "Ajay Banga", "Finance le développement des pays émergents et en développement."),
    ("BRI (Banque des règlements internationaux)", "Bâle", "Pablo Hernández de Cos (directeur général)",
     "« Banque des banques centrales » ; héberge le Comité de Bâle (règles prudentielles bancaires)."),
]

# ------------------------------------------------------------------ Indices boursiers (faits stables)
INDICES = [
    ("États-Unis", "S&P 500", "500 grandes entreprises américaines, pondéré par la capitalisation"),
    ("États-Unis", "Dow Jones Industrial Average", "30 valeurs, pondéré par les prix (méthode historique)"),
    ("États-Unis", "Nasdaq-100", "100 plus grandes valeurs non financières du Nasdaq, très technologique"),
    ("États-Unis", "VIX", "Indice de volatilité implicite à 30 jours du S&P 500"),
    ("Zone euro", "Euro Stoxx 50", "50 grandes valeurs de la zone euro"),
    ("France", "CAC 40", "40 valeurs, Euronext Paris"),
    ("Allemagne", "DAX", "40 valeurs (30 avant 2021), Francfort ; indice de rentabilité (dividendes réinvestis)"),
    ("Royaume-Uni", "FTSE 100", "100 plus grandes capitalisations de la Bourse de Londres"),
    ("Suisse", "SMI", "20 plus grandes valeurs suisses"),
    ("Espagne", "IBEX 35", "35 valeurs, Madrid"),
    ("Italie", "FTSE MIB", "40 valeurs, Milan"),
    ("Japon", "Nikkei 225", "225 valeurs, pondéré par les prix"),
    ("Japon", "TOPIX", "Ensemble large du marché japonais, pondéré par la capitalisation"),
    ("Chine", "CSI 300", "300 grandes valeurs de Shanghai et Shenzhen"),
    ("Hong Kong", "Hang Seng", "Principales valeurs cotées à Hong Kong"),
    ("Inde", "Nifty 50 / Sensex", "50 valeurs (NSE) / 30 valeurs (BSE)"),
    ("Corée du Sud", "KOSPI", "Ensemble des valeurs du marché principal coréen"),
    ("Australie", "S&P/ASX 200", "200 plus grandes valeurs australiennes"),
    ("Canada", "S&P/TSX Composite", "Principal indice de Toronto"),
    ("Brésil", "Ibovespa", "Principal indice de São Paulo (B3)"),
    ("Afrique du Sud", "JSE Top 40", "40 plus grandes valeurs de Johannesburg"),
]

# ------------------------------------------------------------------ Devises
DEVISES = [
    ("États-Unis", "Dollar américain", "USD"), ("Zone euro", "Euro", "EUR"), ("Royaume-Uni", "Livre sterling", "GBP"),
    ("Japon", "Yen", "JPY"), ("Suisse", "Franc suisse", "CHF"), ("Chine", "Yuan (renminbi)", "CNY"),
    ("Canada", "Dollar canadien", "CAD"), ("Australie", "Dollar australien", "AUD"), ("Nouvelle-Zélande", "Dollar néo-zélandais", "NZD"),
    ("Inde", "Roupie indienne", "INR"), ("Corée du Sud", "Won", "KRW"), ("Brésil", "Real", "BRL"), ("Mexique", "Peso mexicain", "MXN"),
    ("Afrique du Sud", "Rand", "ZAR"), ("Turquie", "Livre turque", "TRY"), ("Russie", "Rouble", "RUB"), ("Suède", "Couronne suédoise", "SEK"),
    ("Norvège", "Couronne norvégienne", "NOK"), ("Arabie saoudite", "Riyal", "SAR"), ("Maroc", "Dirham", "MAD"),
]
