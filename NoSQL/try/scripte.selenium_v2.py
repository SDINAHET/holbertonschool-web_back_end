#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def bypass_cloudflare_and_fetch(url):
    print("Démarrage du navigateur Chrome...")
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Masquer Selenium

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print(f"Connexion à {url}...")
        driver.get(url)

        # Simuler des mouvements de souris
        actions = ActionChains(driver)
        actions.move_by_offset(100, 100).perform()
        time.sleep(2)

        # Faire défiler la page
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)

        # Attendre que Cloudflare valide
        print("Attente pour passer Cloudflare...")
        time.sleep(15)

        # Récupérer le HTML de la page
        page_source = driver.page_source

        # Convertir en Markdown avec BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        return soup.prettify()

    except Exception as e:
        print(f"❌ Erreur : {e}")
    finally:
        driver.quit()

# URL cible
url = "https://intranet.hbtn.io/projects/2234"
html_content = bypass_cloudflare_and_fetch(url)

# Sauvegarder le contenu dans un fichier
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("✅ Contenu sauvegardé dans output.html")
