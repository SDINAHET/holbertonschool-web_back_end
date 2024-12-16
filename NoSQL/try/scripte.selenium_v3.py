#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth

def bypass_cloudflare_and_fetch(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Utilisez headless=True une fois confirmé
        page = browser.new_page()
        stealth(page)  # Activer le mode furtif pour masquer l'automatisation

        print(f"Connexion à {url}...")
        page.goto(url, timeout=60000)

        # Attente pour passer Cloudflare
        page.wait_for_timeout(15000)  # Ajustez selon le temps de validation

        # Récupérer le contenu HTML
        html_content = page.content()
        print("✅ Page récupérée avec succès.")
        browser.close()
        return html_content

# URL cible
url = "https://intranet.hbtn.io/projects/2234"
html_content = bypass_cloudflare_and_fetch(url)

# Sauvegarder le contenu
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("✅ Contenu sauvegardé dans output.html")
