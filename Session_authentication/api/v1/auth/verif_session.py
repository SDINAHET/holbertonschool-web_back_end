#!/usr/bin/env python3
"""
Check active sessions stored in the database (UserSession).
Shows remaining time before expiration.
"""

import sys
import os
from datetime import datetime, timedelta
from os import getenv

# Ajouter la racine du projet au PYTHONPATH
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "../../../"))
sys.path.append(ROOT_DIR)

# Import maintenant possible
from models.user_session import UserSession

# Lire la durée de session
try:
    duration = int(getenv("SESSION_DURATION", "0"))
except Exception:
    duration = 0

now = datetime.now()
print(f"\n🟢 SESSION_DURATION = {duration} seconds\n")

for session in UserSession.all():
    created = session.created_at
    expire_at = created + timedelta(seconds=duration)
    remaining = (expire_at - now).total_seconds()
    if remaining > 0:
        print("✅ ACTIVE:")
    else:
        print("⛔ EXPIRED:")

    print(f" - session_id: {session.session_id}")
    print(f" - user_id:    {session.user_id}")
    print(f" - created:    {created}")
    print(f" - expires in: {int(remaining)}s\n")
