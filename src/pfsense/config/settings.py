import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    print("[*] Loading environment variables from .env file")
    load_dotenv()

CONFIG_DIR = os.environ.get("CONFIG_DIR", "/conf/config.xml")
BACKUP_CONFIG_DIR = os.environ.get("BACKUP_CONFIG_DIR", "/conf/config.xml.bak")

PFSENSE_USERNAME = os.environ.get("PFSENSE_USERNAME", "admin")
PFSENSE_PASSWORD = os.environ.get("PFSENSE_PASSWORD", "pfsense")
PFSENSE_HOST = os.environ.get("PFSENSE_HOST", "pfsense.home.arpa")
