from bs4 import BeautifulSoup
import pandas as pd

def parse_html_file(file_path):
    """
    Analyse le fichier HTML et extrait les réponses du questionnaire sous forme de DataFrame Pandas.
    
    Paramètres:
    file_path (str): Le chemin du fichier HTML à analyser.
    
    Retourne:
    pandas.DataFrame: Un DataFrame contenant les réponses du questionnaire.
    """
    # Liste pour stocker les réponses extraites du fichier HTML
    responses = []

    # Ouverture du fichier HTML en mode lecture avec encodage UTF-8
    with open(file_path, encoding='utf-8') as f:
        # Utilisation de BeautifulSoup pour analyser le contenu du fichier HTML
        soup = BeautifulSoup(f, 'html.parser')

    # Parcours de tous les éléments div ayant la classe "response" qui contient les réponses
    for response_div in soup.find_all("div", class_="response"):
        # Dictionnaire pour stocker les données d'une seule réponse
        response_data = {}
        
        # Variable pour stocker le groupe actuel des questions (peut être vide si aucune catégorie de groupe n'est spécifiée)
        current_group = ""

        # Parcours des enfants de chaque div de réponse
        for child in response_div.children:
            # Si l'enfant est un titre de groupe (h1 ou h2), on met à jour le groupe actuel
            if child.name in ["h2", "h1"]:
                current_group = child.get_text(strip=True)
            # Si l'enfant est une table avec la classe "group" (indiquant que cette table contient un groupe de questions)
            elif child.name == "table" and "group" in child.get("class", []):
                # Parcours des lignes de la table qui contiennent les questions
                for row in child.find_all("tr", class_="question"):
                    # On récupère toutes les cellules de la ligne (td)
                    cells = row.find_all("td")
                    # Si la ligne contient au moins deux cellules (question et réponse)
                    if len(cells) >= 2:
                        # Récupération du texte de la question et de la réponse
                        question = cells[0].get_text(strip=True)
                        answer = cells[1].get_text(strip=True)
                        
                        # Construction de la clé pour cette question (incluant le groupe si disponible)
                        key = f"{current_group} - {question}" if current_group else question
                        # Ajout de la question et de la réponse au dictionnaire
                        response_data[key] = answer

        # Ajout des données de réponse (sous forme de dictionnaire) à la liste des réponses
        responses.append(response_data)

    # Conversion de la liste de réponses en DataFrame Pandas pour une manipulation facile
    return pd.DataFrame(responses)
