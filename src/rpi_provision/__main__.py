from rpi_provision import (
    output_config_file,
    read_credentials,
    render_network_config,
)

credentials = read_credentials()
config_text = render_network_config(**credentials)
print(config_text)

output_config_file(config_text, output_path="./wpa_supplicant.output.conf")
