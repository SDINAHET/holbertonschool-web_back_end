#!/usr/bin/python3
from bs4 import BeautifulSoup
import os

def html_to_markdown(input_html, output_md):
    """Convertit un fichier HTML en Markdown."""
    with open(input_html, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    markdown = ""

    # Conversion HTML → Markdown
    for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'ul', 'ol', 'li', 'a']):
        if tag.name == 'h1':
            markdown += f"# {tag.get_text()}\n\n"
        elif tag.name == 'h2':
            markdown += f"## {tag.get_text()}\n\n"
        elif tag.name == 'h3':
            markdown += f"### {tag.get_text()}\n\n"
        elif tag.name == 'p':
            markdown += f"{tag.get_text()}\n\n"
        elif tag.name == 'ul':
            for li in tag.find_all('li'):
                markdown += f"- {li.get_text()}\n"
            markdown += "\n"
        elif tag.name == 'ol':
            for i, li in enumerate(tag.find_all('li'), 1):
                markdown += f"{i}. {li.get_text()}\n"
            markdown += "\n"
        elif tag.name == 'a':
            href = tag.get('href', '#')
            markdown += f"[{tag.get_text()}]({href})\n\n"

    # Écrire dans le fichier Markdown
    with open(output_md, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown)

    print(f"✅ Fichier converti : {output_md}")

# Entrée et sortie
input_html_file = "Project_ NoSQL _ Holberton Rennes, France Intranet.html"  # Nom de votre fichier
output_md_file = "README.md"  # Fichier Markdown généré

html_to_markdown(input_html_file, output_md_file)
