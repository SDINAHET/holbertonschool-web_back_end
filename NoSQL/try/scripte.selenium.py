#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def url_to_markdown(url, output_md_file):
    """Utilise Selenium pour valider Cloudflare, récupère le contenu HTML et convertit en Markdown."""
    try:
        print("Démarrage du navigateur...")

        # Configuration de Selenium avec Chrome
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/google-chrome"  # Spécifiez le chemin complet
        chrome_options.add_argument("--headless")  # Mode sans interface graphique
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Installe automatiquement ChromeDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # Accéder à l'URL
        print(f"Connexion à {url}...")
        driver.get(url)

        # Attente pour que Cloudflare valide la session (ajustez si nécessaire)
        time.sleep(10)

        # Récupérer le contenu de la page après validation
        html_content = driver.page_source
        driver.quit()

        # Analyse du HTML avec BeautifulSoup
        print("Analyse du contenu HTML...")
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
            elif tag.name == 'a':
                href = tag.get('href', '#')
                markdown += f"[{tag.get_text()}]({href})\n\n"

        # Sauvegarder dans un fichier Markdown
        with open(output_md_file, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown)
        print(f"✅ Conversion réussie : {output_md_file}")

    except Exception as e:
        print(f"❌ Erreur : {e}")

# URL et fichier de sortie
url = "https://intranet.hbtn.io/projects/2234"
output_md_file = "README.md"

url_to_markdown(url, output_md_file)
