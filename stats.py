import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def compute_statistics(df):
    """
    Calcule des statistiques avancées sur le dataset.
    Cette fonction génère des statistiques sur l'âge, le temps de réponse, 
    la répartition par genre, académie et statut professionnel.
    """
    stats = {}

    # Analyse de l'âge
    age_col = next((col for col in df.columns if "âge" in col.lower()), None)
    if age_col:
        # Conversion de la colonne en numérique (pour éviter les erreurs de type)
        df[age_col] = pd.to_numeric(df[age_col], errors='coerce')
        stats['Age Mean'] = df[age_col].mean()  # Moyenne de l'âge
        stats['Age Median'] = df[age_col].median()  # Médiane de l'âge
        stats['Age Std'] = df[age_col].std()  # Écart-type de l'âge
        stats['Age Min'] = df[age_col].min()  # Âge minimum
        stats['Age Max'] = df[age_col].max()  # Âge maximum

    # Analyse du temps de réponse (calcul du temps entre le lancement et la soumission)
    start_col = next((col for col in df.columns if "date de lancement" in col.lower()), None)
    end_col = next((col for col in df.columns if "date de soumission" in col.lower()), None)

    if start_col and end_col:
        # Conversion des colonnes de dates en format datetime
        df[start_col] = pd.to_datetime(df[start_col], errors='coerce')
        df[end_col] = pd.to_datetime(df[end_col], errors='coerce')
        # Calcul du temps de réponse en minutes
        df["Response Time (minutes)"] = (df[end_col] - df[start_col]).dt.total_seconds() / 60
        stats["Average Response Time"] = df["Response Time (minutes)"].mean()  # Temps de réponse moyen
        stats["Median Response Time"] = df["Response Time (minutes)"].median()  # Temps de réponse médian

    # Répartition par genre
    gender_col = next((col for col in df.columns if "vous vous identifiez" in col.lower()), None)
    if gender_col:
        stats['Gender Distribution'] = df[gender_col].value_counts().to_dict()  # Distribution des genres

    # Répartition par académie
    academy_col = next((col for col in df.columns if "académie" in col.lower()), None)
    if academy_col:
        stats['Academy Distribution'] = df[academy_col].value_counts().to_dict()  # Distribution par académie

    # Répartition des statuts professionnels
    status_col = next((col for col in df.columns if "statut actuel" in col.lower()), None)
    if status_col:
        stats['Status Distribution'] = df[status_col].value_counts().to_dict()  # Distribution des statuts professionnels

    return stats

def generate_graphs(df, output_dir="graphs/"):
    """
    Génère plusieurs graphiques statistiques à partir des données du sondage.
    Cette fonction génère des graphiques pour l'âge, le genre, l'académie, 
    le statut professionnel, le temps de réponse et une matrice de corrélation.
    """
    # Création du répertoire pour sauvegarder les graphiques (s'il n'existe pas)
    os.makedirs(output_dir, exist_ok=True)

    # Histogramme et KDE des âges
    age_col = next((col for col in df.columns if "âge" in col.lower()), None)
    if age_col:
        df[age_col] = pd.to_numeric(df[age_col], errors='coerce')

        # Histogramme avec estimation de la densité
        plt.figure(figsize=(8, 5))
        sns.histplot(df[age_col].dropna(), bins=10, kde=True, color='skyblue')
        plt.title("Répartition des âges")
        plt.xlabel("Âge")
        plt.ylabel("Nombre de répondants")
        plt.savefig(f"{output_dir}age_distribution.png")
        plt.close()

        # Boxplot des âges
        plt.figure(figsize=(6, 4))
        sns.boxplot(y=df[age_col], color="lightblue")
        plt.title("Boîte à moustaches des âges")
        plt.ylabel("Âge")
        plt.savefig(f"{output_dir}age_boxplot.png")
        plt.close()

    # Répartition des genres
    gender_col = next((col for col in df.columns if "vous vous identifiez" in col.lower()), None)
    if gender_col:
        plt.figure(figsize=(6, 6))
        df[gender_col].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])
        plt.title("Répartition des genres")
        plt.ylabel("")  # On enlève le label de l'axe des ordonnées
        plt.savefig(f"{output_dir}gender_distribution.png")
        plt.close()

    # Répartition des académies
    academy_col = next((col for col in df.columns if "académie" in col.lower()), None)
    if academy_col:
        plt.figure(figsize=(10, 5))
        df[academy_col].value_counts().plot(kind='bar', color='lightblue')
        plt.title("Répartition des enseignants par académie")
        plt.xlabel("Académie")
        plt.ylabel("Nombre de répondants")
        plt.xticks(rotation=45, ha="right")  # Rotation des labels pour plus de lisibilité
        plt.savefig(f"{output_dir}academy_distribution.png")
        plt.close()

    # Répartition des statuts professionnels
    status_col = next((col for col in df.columns if "statut actuel" in col.lower()), None)
    if status_col:
        plt.figure(figsize=(8, 5))
        df[status_col].value_counts().plot(kind='bar', color='orange')
        plt.title("Répartition des statuts des enseignants")
        plt.xlabel("Statut")
        plt.ylabel("Nombre de répondants")
        plt.xticks(rotation=45, ha="right")  # Rotation des labels
        plt.savefig(f"{output_dir}status_distribution.png")
        plt.close()

    # Temps de réponse
    if "Response Time (minutes)" in df.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(df["Response Time (minutes)"].dropna(), bins=10, kde=True, color='purple')
        plt.title("Distribution des temps de réponse")
        plt.xlabel("Temps de réponse (minutes)")
        plt.ylabel("Nombre de répondants")
        plt.savefig(f"{output_dir}response_time_distribution.png")
        plt.close()

    # Matrice de corrélation si plusieurs variables numériques
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        plt.figure(figsize=(10, 8))  # Augmenter la taille du graphique
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

        # Ajuster les étiquettes pour qu'elles soient lisibles
        plt.xticks(rotation=45, ha='right', fontsize=10)  
        plt.yticks(rotation=0, fontsize=10)  
        plt.title("Matrice de corrélation entre variables numériques", fontsize=12)
    
        # Sauvegarde du graphique avec ajustement des marges
        plt.savefig(f"{output_dir}correlation_matrix.png", bbox_inches="tight")  
        plt.close()
