#!/usr/bin/env python3
import undetected_chromedriver as uc
import time

def save_protected_page(url, output_file):
    """Utilise un navigateur furtif pour accéder à une page protégée par Cloudflare."""
    try:
        print("Démarrage du navigateur...")
        # Options pour Chrome
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

        # Lancer un navigateur furtif
        driver = uc.Chrome(options=options)

        print(f"Connexion à {url}...")
        driver.get(url)

        # Attente pour Cloudflare ou pour charger la page (augmenté ici)
        print("⏳ Attente pour passer la vérification Cloudflare et charger la page...")
        for i in range(30):  # Réessayer pendant 30 secondes
            time.sleep(1)
            if "challenge" not in driver.page_source.lower():
                print(f"✅ Page chargée après {i+1} secondes.")
                break
        else:
            print("⚠️ Le délai d'attente pour Cloudflare a été dépassé.")

        # Option pour gérer une page de connexion
        if "login" in driver.page_source.lower():
            print("🔑 Détection d'une page de connexion. Veuillez vous connecter manuellement.")
            time.sleep(30)  # Attendez que l'utilisateur se connecte manuellement

        # Sauvegarder le contenu HTML de la page
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print(f"✅ Page sauvegardée dans {output_file}")

    except Exception as e:
        print(f"❌ Erreur : {e}")
    finally:
        driver.quit()

# URL cible
url = "https://intranet.hbtn.io/projects/2234"
output_file = "output_protected_page.html"

save_protected_page(url, output_file)
