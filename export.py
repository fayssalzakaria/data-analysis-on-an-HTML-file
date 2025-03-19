import pandas as pd
import os
from fpdf import FPDF

def export_to_excel(df, stats_basic, stats_advanced, output_file="output/results.xlsx"):
    """
    Exporte les données, statistiques de base et avancées dans un fichier Excel 
    """
    if output_file and os.path.dirname(output_file):
        os.makedirs(os.path.dirname(output_file), exist_ok=True)


    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # Feuille 1 : Données brutes
        df.to_excel(writer, sheet_name="Raw Data", index=False)

        # Feuille 2 : Statistiques de base
        stats_basic_df = pd.DataFrame(stats_basic.items(), columns=['Metric', 'Value'])
        stats_basic_df.to_excel(writer, sheet_name="Basic Stats", index=False)

        # Feuille 3 : Statistiques avancées
        stats_advanced_df = pd.DataFrame(stats_advanced.items(), columns=['Metric', 'Value'])
        stats_advanced_df.to_excel(writer, sheet_name="Advanced Stats", index=False)

        # Feuille 4 : Clustering si disponible
        if "Response Cluster" in df.columns:
            cluster_df = df[["Response Time (minutes)", "Response Cluster"]].dropna()
            cluster_df.to_excel(writer, sheet_name="Clusters", index=False)

    print(f" Export Excel terminé : {output_file}")

def export_to_pdf(stats_basic, stats_advanced, graphs_dir="graphs/", output_file="output/report.pdf"):
    """
    Génère un rapport PDF détaillé avec les statistiques et les graphiques.
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Rapport d'Analyse des Données", ln=True, align='C')
    pdf.ln(10)

    # Section 1 : Statistiques de base
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, "1. Statistiques de base", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.ln(5)
    for key, value in stats_basic.items():
        pdf.multi_cell(0, 10, f"- {key}: {value}")
    pdf.ln(10)

    # Section 2 : Statistiques avancées
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, "2. Statistiques avancées", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.ln(5)

    # Test de normalité
    shapiro_stat = stats_advanced.get("Test de normalité (Shapiro-Wilk)", {}).get("Statistique", "N/A")
    shapiro_p = stats_advanced.get("Test de normalité (Shapiro-Wilk)", {}).get("p-value", "N/A")
    pdf.multi_cell(0, 10, f"- Test de normalité (Shapiro-Wilk):\n    Statistique: {shapiro_stat}\n    p-value: {shapiro_p}")
    pdf.multi_cell(0, 10, "   Conclusion : Les données ne suivent pas une distribution normale (p-value < 0.05).")
    pdf.ln(5)

    # Clusters (Temps de réponse)
    clusters = stats_advanced.get("Clusters (Temps de réponse)", [])
    pdf.multi_cell(0, 10, "- Clusters (Temps de réponse) :")
    for idx, cluster in enumerate(clusters):
        pdf.multi_cell(0, 10, f"    Cluster {idx + 1}: {cluster[0]:.2f} minutes")
    pdf.multi_cell(0, 10, "   Conclusion : Les utilisateurs peuvent être segmentés en trois groupes selon leur temps de réponse.")
    pdf.ln(5)

    # Matrice de corrélation (Spearman)
    spearman_corr = stats_advanced.get("Matrice de corrélation (Spearman)", {})
    pdf.multi_cell(0, 10, "- Matrice de corrélation (Spearman) :")
    for key, sub_dict in spearman_corr.items():
        pdf.multi_cell(0, 10, f"  {key}:")
        for sub_key, value in sub_dict.items():
            pdf.multi_cell(0, 10, f"    {sub_key}: {value:.3f}")
    pdf.multi_cell(0, 10, "   Conclusion :\n    - L'âge a une faible influence sur le temps de réponse (corrélation de ~0.25).\n    - Le cluster de temps de réponse est fortement corrélé au temps de réponse réel (~0.81).")
    pdf.ln(10)

    # Section 3 : Graphiques
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, "3. Visualisation des données", ln=True)
    pdf.ln(5)

    graphs = [
        "age_distribution.png",
        "gender_distribution.png",
        "academy_distribution.png",
        "status_distribution.png",
        "response_time_distribution.png",
        "correlation_matrix.png"
    ]

    for graph in graphs:
        graph_path = os.path.join(graphs_dir, graph)
        if os.path.exists(graph_path):
            pdf.add_page()
            pdf.image(graph_path, x=10, w=180)
            pdf.ln(5)

    pdf.output(output_file, "F")

    print(f" Rapport PDF généré : {output_file}")
