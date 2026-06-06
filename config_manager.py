# Task 6: JSON Config Manager

# json.dump() writes to a file directly
# json.dumps() converts to a string (not a file)

import json

def save_config(data: dict, filename: str):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Config saved to {filename}")

def load_config(filename: str) -> dict:
    with open(filename, "r") as f:
        return json.load(f)

def update_config(filename: str, key: str, value):
    data = load_config(filename)
    data[key] = value
    save_config(data, filename)
    print(f"Updated {key} = {value}")

config = {"model": "gpt-4", "learning_rate": 0.001, "epochs": 10}
save_config(config, "config.json")

update_config("config.json", "epochs", 20)

print(load_config("config.json"))