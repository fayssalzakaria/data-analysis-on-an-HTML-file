import argparse
from parser import parse_html_file
from stats import compute_statistics, generate_graphs
from export import export_to_excel

def main():
    """
    Fonction principale qui analyse un fichier HTML de sondage, génère des statistiques,
    crée des graphiques, et exporte les résultats dans un fichier Excel.
    """
    # Initialisation du parser d'arguments pour lire les fichiers d'entrée et de sortie
    parser = argparse.ArgumentParser(description="Analyse et transformation d'un fichier HTML en tableau Excel avec statistiques.")
    # Ajout des arguments de ligne de commande : le fichier d'entrée et le fichier de sortie
    parser.add_argument("input_file", help="Chemin vers le fichier HTML de sondage")
    parser.add_argument("output_file", help="Chemin vers le fichier Excel généré")
    # Lecture des arguments passés via la ligne de commande
    args = parser.parse_args()

    # Affichage de l'état actuel du processus
    print("Chargement du fichier HTML...")
    # Appel de la fonction `parse_html_file` pour lire et analyser le fichier HTML
    df = parse_html_file(args.input_file)

    # Vérification si le DataFrame est vide (pas de réponses trouvées dans le fichier)
    if df.empty:
        print("Aucune réponse trouvée.")
        return

    # Affichage de l'état du calcul des statistiques
    print("Calcul des statistiques...")
    # Appel de la fonction `compute_statistics` pour calculer les statistiques du DataFrame
    stats = compute_statistics(df)

    # Affichage de l'état de la génération des graphiques
    print("Génération des graphiques...")
    # Appel de la fonction `generate_graphs` pour générer des graphiques basés sur les données
    generate_graphs(df)

    # Affichage de l'état de l'exportation des résultats
    print("Export des résultats vers Excel...")
    # Appel de la fonction `export_to_excel` pour exporter les données et les statistiques vers un fichier Excel
    export_to_excel(df, stats, args.output_file)

    # Message de confirmation indiquant que le processus est terminé et le fichier de sortie a été sauvegardé
    print(f"Analyse terminée. Résultats sauvegardés dans {args.output_file}")

# Vérification que ce script est exécuté directement (et non importé en tant que module)
if __name__ == "__main__":
    # Appel de la fonction principale pour démarrer l'analyse
    main()
