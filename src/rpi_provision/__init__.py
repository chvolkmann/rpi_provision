from pathlib import Path
from typing import Union
import jinja2
import yaml
from rpi_provision.config import CREDENTIALS_FILE

from rpi_provision.config import (
    CONFIG_TEMPLATE_FILE,
    DEFAULT_COUNTRY_CODE,
    DEFAULT_OUTPUT_PATH,
)


def render_network_config(
    ssid: str,
    psk: str,
    country_code: str = DEFAULT_COUNTRY_CODE,
    template_path: Union[str, Path] = CONFIG_TEMPLATE_FILE,
) -> str:
    """Renders a template configuration file with variables inserted."""
    config_template = jinja2.Template(Path(template_path).read_text("utf8"))
    return config_template.render(
        ssid=ssid,
        psk=psk,
        country_code=country_code,
    )


def output_config_file(
    content: str,
    output_path: Union[str, Path] = DEFAULT_OUTPUT_PATH,
) -> None:
    """Writes the content to file."""
    Path(output_path).write_text(content, encoding="utf8")


def read_credentials(
    credentials_path: Union[str, Path] = CREDENTIALS_FILE,
) -> dict:
    """Reads credentials from a YAML file."""
    txt = Path(credentials_path).read_text("utf8")
    return yaml.safe_load(txt)
