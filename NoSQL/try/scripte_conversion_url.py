#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

def url_to_markdown(url, output_md_file, cookies):
    """Accède à une URL avec authentification via cookies et convertit le contenu HTML en Markdown."""
    try:
        print(f"Connexion à {url}...")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Referer": "https://intranet.hbtn.io/"
        }

        # Faire la requête GET avec les cookies
        response = requests.get(url, headers=headers, cookies=cookies)
        response.raise_for_status()  # Vérifie si la requête a réussi

        # Analyser le contenu HTML avec BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
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

    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur : {e}")

# URL et cookies
url = "https://intranet.hbtn.io/projects/2234"  # URL du projet
output_md_file = "README.md"

# Cookies récupérés
cookies = {
    "_holberton_intranet_session": "x2XoAlqGigOG8N5AdRfcFUaxmhf2ObFqcjMk87A0c4iWnuBA26%2FPcv5q%2FQj%2B%2BwWo3W07%2Bs3B0oEbexhMafym3VT8hm96S02BYWXVW7ehpq78BcpP3TzW8upH7%2Ba90G6nNZaGTwHpvnbUQeDQ1d3JtfLkpP%2Btq%2B%2B2OHFEfb%2BTqrONWgLzwinaK8Vr%2FMzdyw%2FTggwyytyj8yvi%2BuaQhBdlj%2FbXPBJp6VEWogT7Lg5XbPTsmcYq%2BfutnArkNo2GiCuuukPdycWzb%2FeIkYZrL54sUw5uo1FbFv1uWCJjOeEfypN%2BtG7JdVJrJkEiFkHdxMMEngMiT4J4OWG0glmMNyD09s6RECaeHsZmGUu3Tdvt3uojyPdphv7yZU4FyKdAod3hiRiM4tp0X%2BQyVjQSeyOwF80jigYNu6RUB1%2Bk24AzVf8qtY5lwSyzFr1aDkVywze1GqkI5jMrr5EDwps2hvlomqt%2Btb%2FUiZY%3D--kMPCRulO21l1Jp%2Fy--dsygw3zEiVCFFKJPxWUphw%3D%3D",
    "cf_clearance": "49E8fm7D9q.UhtCNTvYTGYTk_t3H713fnT5Ak.OAFog-1734301466-1.2.1.1-7TiANIFvGO2O6Sa5UxCNooEEHb8za2X3TmsSjeyBtEe1ql8pjWAqNa01GtFwxFib_OHC8kAqs5QlrzF_bvj83ahxX3FWizKMO1Jn3ckkIIvoXvMqGtHomY0BAd7T10UQELqsvRTiW9HyAvw5qOA1tIVoSdoieZGh1A4_XrfcA5YvRCT6HGueFnIsC78BMPTVpfRoHxVKWGNy0xc2E7SSBqBXCD7kOaMQZMPWS6iE8nCBZ9fPON6ZKN_Q_wAaOCFkuJRRkCkTcByO8knbVs8XqShLgAyjzowxxkeIqjv2qoVyrsOl0Uxz11KhgJQRyQGIE3g5Y.O9Y.57xGwN7TbUvDBISmkpxV.kIBm2.BeGqeH5s4GqH2nX2yrpcAG7kIw7KnrlebRjAMEgoLUkJ9SZF9ozH6.ykhXJ9oPeL1027qdVhvbl9Q2_UGmOssGNuWmc"
}

# Appel de la fonction corrigé
url_to_markdown(url, output_md_file, cookies)
