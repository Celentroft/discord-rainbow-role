import json
from typing import Dict, Any

def load_json() -> Dict[str, Any]:
    config = json.load(open("config.json", 'r'))
    return config

def embed_color() -> int:
    config = load_json()
    return int(config['color'], 16)
