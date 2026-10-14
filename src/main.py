import json
from extract import extract_inventory
from transform import transform_inventory
from load import load_inventory

def main():
    with open("config/settings.json") as f:
        config = json.load(f)

    raw = extract_inventory(config)
    rows = transform_inventory(raw)
    load_inventory(rows, config["database_path"])

    print(f"Loaded {len(rows)} inventory rows into SQLite.")

if __name__ == "__main__":
    main()