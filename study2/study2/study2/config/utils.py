import json
import os
from pathlib import Path


def read_json(filePath):
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file at {filePath} does not exist.")
        raise
    except json.JSONDecodeError:
        print(f"Error: The file at {filePath} is not a valid JSON.")
        raise