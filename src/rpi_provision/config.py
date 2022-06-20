from pathlib import Path

HERE = Path(__file__).parent
CONFIG_TEMPLATE_FILE = HERE / "wpa_supplicant.conf"

DEFAULT_OUTPUT_PATH = Path("/etc/wpa_supplicant/wpa_supplicant.conf")

DEFAULT_COUNTRY_CODE = "de"

CREDENTIALS_FILE = Path("wifi_credentials.yml")
