import pandas as pd

def export_to_excel(df, stats, output_file):
    """
    Exporte le DataFrame et les statistiques dans un fichier Excel.
    """
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Raw Data', index=False)

        # Export des statistiques
        stats_df = pd.DataFrame(stats.items(), columns=['Metric', 'Value'])
        stats_df.to_excel(writer, sheet_name='Statistics', index=False)
