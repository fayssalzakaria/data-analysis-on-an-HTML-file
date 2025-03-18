# Analyse de Fichier HTML de Sondage et Exportation en Excel

Ce projet permet d'extraire des données à partir d'un fichier HTML contenant des résultats de sondage, d'effectuer une analyse statistique et de générer un fichier Excel contenant les données traitées ainsi que des graphiques.

##   Fonctionnalités

- Extraction des réponses du sondage à partir d'un fichier HTML
- Calcul de statistiques avancées sur les données
- Génération de graphiques pour une meilleure visualisation
- Exportation des résultats sous format Excel (`.xlsx`)

##   Structure du Projet

```
  data-analysis-on-an-HTML-file
├── 📄 main.py           # Script principal
├── 📄 parser.py         # Extraction des données HTML
├── 📄 stats.py          # Calcul des statistiques et génération de graphiques
├── 📄 export.py         # Exportation des données et statistiques en Excel
├── 📄 requirements.txt  # Dépendances du projet
├──   graphs/           # Dossier contenant les graphiques générés
│   ├── age_distribution.png
│   ├── gender_distribution.png
│   ├── academy_distribution.png
│   ├── status_distribution.png
│   └── ... (autres graphiques)
├──   data/             # Dossier contenant les fichiers de données
│   ├── fichierhtml.html  # Exemple de fichier HTML à analyser
│   ├── resultats.xlsx    # Fichier Excel généré après analyse
```

##    Installation

1. **Cloner le projet**
   ```bash
   git clone https://github.com/ton-repo/data-analysis-on-an-HTML-file.git
   cd data-analysis-on-an-HTML-file
   ```

2. **Installer les dépendances**
   Assurez-vous d'avoir Python installé, puis exécutez :
   ```bash
   pip install -r requirements.txt
   ```

##   Utilisation

Pour exécuter le script, utilisez la commande suivante :
```bash
python3 main.py fichierhtml.html resultats.xlsx
```

- `fichierhtml.html` : Le fichier HTML contenant les réponses du sondage
- `resultats.xlsx` : Le fichier Excel où seront exportés les résultats

## 📊 Statistiques Générées

Le programme analyse les données et génère les statistiques suivantes :
- Moyenne, médiane et écart-type de l'âge
- Temps moyen de réponse
- Répartition par genre, académie et statut professionnel

Des graphiques sont également générés dans le dossier `graphs/`.

##   Auteur

**Fayssal Zakaria**  
Email : [fayssal.132004@gmail.com](mailto:fayssal.132004@gmail.com)
