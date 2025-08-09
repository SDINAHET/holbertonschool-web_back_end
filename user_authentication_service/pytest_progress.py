#!/usr/bin/env python3
from tqdm import tqdm
import subprocess, re

ORDER = [
    "test_users_7.py", "test_valid_login_8.py", "test_generate_uuid_9.py",
    "test_auth_create_session_10.py", "test_app_login_11.py",
    "test_auth_get_user_from_session_id_12.py", "test_auth_destroy_session_13.py",
    "test_app_logout_14.py", "test_app_profile_15.py", "test_auth_reset_token_16.py",
    "test_app_reset_password_token_17.py", "test_auth_update_password_18.py",
    "test_app_update_password_19.py",
]

def count_total():
    p = subprocess.run(["pytest","--collect-only","-q"]+ORDER, capture_output=True, text=True)
    return sum(1 for l in p.stdout.splitlines() if "::" in l)

def main():
    total = count_total() or 31  # fallback
    bar = tqdm(total=total, desc="Pytest", ncols=80)
    proc = subprocess.Popen(["pytest","-q"]+ORDER, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in proc.stdout:
        line=line.rstrip("\n")
        if re.search(r"\bPASSED\b|\bFAILED\b|\bERROR\b|\bSKIPPED\b|[.FEsx]$", line):
            bar.update(1)
    proc.wait()
    bar.close()

if __name__=="__main__":
    main()
