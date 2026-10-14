
import requests

def extract_inventory(config):
    base = config["visco_base_url"]
    action = config["action"]
    function = config["function"]
    token = config["token"]

    url = f"{base}?action={action}&function={function}&token={token}"

    response = requests.get(url)
    response.raise_for_status()

    return response.json()
