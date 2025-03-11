Analyse de données de sondage HTML et export vers Excel

Ce projet permet d'analyser les données d'un sondage au format HTML, de calculer des statistiques avancées, 
de générer des graphiques, puis d'exporter les résultats sous forme de fichier Excel. Le tout est automatisé
 grâce à un script Python utilisant des bibliothèques comme argparse, BeautifulSoup, pandas, matplotlib et seaborn.

Prérequis

Avant de commencer, assurez-vous d'avoir Python installé ainsi que les bibliothèques nécessaires. Vous pouvez installer les dépendances en utilisant pip :

pip install -r requirements.txt

Fonctionnalités

Analyse des données : Le script extrait les réponses du fichier HTML et les transforme en un tableau pandas DataFrame.
Calcul des statistiques : Le script calcule des statistiques telles que la moyenne, la médiane, l'écart-type pour les données d'âge, les temps de réponse, ainsi que des répartitions par genre, académie et statut professionnel.
Génération de graphiques : Le script génère plusieurs graphiques visuels pour mieux comprendre les données du sondage :
Répartition des âges (histogramme et boîte à moustaches).
Répartition des genres (graphique circulaire).
Répartition des académies (graphique à barres).
Répartition des statuts professionnels (graphique à barres).
Temps de réponse (histogramme).
Matrice de corrélation entre variables numériques.
Exportation vers Excel : Les résultats, y compris les statistiques et les graphiques, sont exportés dans un fichier Excel pour une analyse et un partage faciles.
Exemple de sortie
Le fichier Excel généré contiendra :

Un tableau avec les réponses du sondage.
Une feuille avec les statistiques calculées.
Les graphiques seront exportés dans un dossier graphs/.

Structure des fichiers

Voici la structure du projet :

bash
Copier
Modifier
/analyze_survey/
│
├── analyse_sondage.py         # Script principal pour l'analyse
├── parser.py                  # Code pour l'extraction des données HTML
├── stats.py                   # Code pour le calcul des statistiques et génération des graphiques
├── export.py                  # Code pour l'export vers Excel
├── graphs/                    # Dossier où les graphiques sont sauvegardés
│
└── README.md                  # Ce fichier

Auteurs
Fayssal Zakaria 
