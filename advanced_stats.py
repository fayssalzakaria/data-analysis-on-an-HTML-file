import pandas as pd
import numpy as np
import scipy.stats as stats
from sklearn.cluster import KMeans
import os
import plotly.express as px

def compute_advanced_statistics(df):
    """
    Calcule des statistiques avancées pour le dataset.
    """
    stats_results = {}

    # Analyse de la distribution des âges
    age_col = next((col for col in df.columns if "âge" in col.lower()), None)
    if age_col:
        df[age_col] = pd.to_numeric(df[age_col], errors='coerce')
        df = df.dropna(subset=[age_col]).copy()
        
        if not df.empty:
            stat, p = stats.shapiro(df[age_col])
            stats_results['Test de normalité (Shapiro-Wilk)'] = {

                "Statistique": round(stat, 3), "p-value": round(p, 3)
            }

            bins = [0, 20, 30, 40, 50, 60, 100]
            labels = ["<20", "20-30", "30-40", "40-50", "50-60", "60+"]
            df["Groupe d'âge"] = pd.cut(df[age_col], bins=bins, labels=labels)
    # Clustering sur les temps de réponse
    response_col = "Response Time (minutes)"
    if response_col in df.columns:
        df_cluster = df[[response_col]].dropna().copy()
        
        if not df_cluster.empty:
            kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
            df_cluster["Cluster"] = kmeans.fit_predict(df_cluster)
            df.loc[df_cluster.index, "Cluster Temps de Réponse"] = df_cluster["Cluster"]
            stats_results["Clusters (Temps de réponse)"] = [list(center) for center in kmeans.cluster_centers_]

    # Matrice de corrélation
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        stats_results["Matrice de corrélation (Spearman)"] = numeric_df.corr(method="spearman").round(3).to_dict()

    return stats_results, df

def generate_advanced_graphs(df, output_dir="graphs/"):
    """
    Génère les graphiques interactifs avancés.
    """
    os.makedirs(output_dir, exist_ok=True)

    age_col = next((col for col in df.columns if "âge" in col.lower()), None)
    if age_col:
        fig = px.histogram(df, x=age_col, title="Répartition des âges", nbins=10)
        fig.write_html(f"{output_dir}age_distribution.html")

    if "Response Cluster" in df.columns:
        fig = px.scatter(df, x="Response Time (minutes)", y=age_col, color="Response Cluster",
                         title="Clustering des temps de réponse")
        fig.write_html(f"{output_dir}response_time_clusters.html")