import argparse
import os
from parser import parse_html_file
from stats import compute_statistics, generate_graphs
from advanced_stats import compute_advanced_statistics, generate_advanced_graphs
from export import export_to_excel, export_to_pdf

def process_survey(input_file, output_excel, output_pdf):
    """
    Exécute l'analyse complète du sondage : extraction, statistiques, visualisation, export.
    """
    if not os.path.exists(input_file):
        print(f" Erreur : Le fichier '{input_file}' n'existe pas.")
        return

    print("\n Chargement du fichier HTML...")
    df = parse_html_file(input_file)

    if df.empty:
        print(" Aucune réponse trouvée dans le fichier.")
        return

    print("\n Calcul des statistiques classiques...")
    stats_basic = compute_statistics(df)

    print("\n Calcul des statistiques avancées...")
    stats_advanced, df = compute_advanced_statistics(df)

    print("\n Génération des graphiques...")
    generate_graphs(df)
    generate_advanced_graphs(df)

    print("\n Export des résultats...")
    if not output_excel or not os.path.dirname(output_excel):
        output_excel = os.path.join("output", output_excel)
    if not output_pdf or not os.path.dirname(output_pdf):
        output_pdf = os.path.join("output", output_pdf)
    
    os.makedirs(os.path.dirname(output_excel), exist_ok=True)
    export_to_excel(df, stats_basic, stats_advanced, output_excel)
    
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)
    export_to_pdf(stats_basic, stats_advanced, output_file=output_pdf)

    print(f"\n Analyse terminée ! Résultats sauvegardés :\n  - 📊 Excel : {output_excel}\n  - 📄 PDF : {output_pdf}")

def main():
    """
    Fonction principale qui gère les arguments de ligne de commande et lance l'analyse.
    """
    parser = argparse.ArgumentParser(description="Analyse un fichier HTML et génère des statistiques détaillées.")
    parser.add_argument("input_file", help="Chemin vers le fichier HTML du sondage")
    parser.add_argument("output_excel", help="Chemin vers le fichier Excel généré")
    parser.add_argument("--output_pdf", default="output/report.pdf", help="Chemin du fichier PDF généré")

    args = parser.parse_args()
    process_survey(args.input_file, args.output_excel, args.output_pdf)

if __name__ == "__main__":
    main()
