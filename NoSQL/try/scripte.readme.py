#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def html_to_markdown(html_file, output_md):
    """Convertit un fichier HTML en un fichier Markdown."""
    try:
        # Vérifie si le fichier HTML existe
        if not os.path.exists(html_file):
            print(f"❌ Le fichier HTML spécifié n'existe pas : {html_file}")
            return

        # Lit le contenu du fichier HTML
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Utilisation de BeautifulSoup pour analyser le HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # Conversion du contenu HTML en Markdown
        markdown_content = md(str(soup), heading_style="ATX")

        # Écriture dans le fichier README.md
        with open(output_md, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        print(f"✅ Conversion réussie : {output_md}")

    except Exception as e:
        print(f"❌ Erreur lors de la conversion : {e}")

# Chemin vers le fichier HTML local
# html_file = r"C:\Users\steph\Documents\2ème trimestre holberton\web\site\holberton\v1_Project_ NoSQL _ Holberton Rennes, France Intranet.html"
html_file = r"/mnt/c/Users/steph/Documents/2ème trimestre holberton/web/site/holberton/v1_Project_ NoSQL _ Holberton Rennes, France Intranet.html"

# Nom du fichier de sortie en Markdown
output_md = "README.md"

# Conversion
html_to_markdown(html_file, output_md)
