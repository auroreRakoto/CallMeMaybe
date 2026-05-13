from pathlib import Path
import json
# from xml.parsers.expat import model
from llm_sdk.llm_sdk import Small_LLM_Model

from typing import Any

from src.parsing import Parser
from src.process import Process

import time
import sys

def load_json(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a JSON array")

    return data

def save_json(path: Path, data: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def main():
    try:
        args = Parser.parse_args(sys.argv)
    except ValueError as error:
        raise ValueError(f"Argument error: {error}")

    try:
        functions = load_json()
        prompts = load_json()
    except OSError as error:
        raise OSError(f"File error: {error}")
    except Exception as error: # change to json error
        raise Exception(f"JSON error: {error}")

    try:
        model = Small_LLM_Model()
        process = Process(
            model=model,
            functions=functions,
            prompts=prompts
        )
        results = process.process_all()
    except Exception as error:
        raise Exception(f"Error {error}")

    try:
        save_json(args.output, results)
    except Exception as error:
        raise Exception(f"Output error: {error}")
   

if __name__ == "__main__":
    start = time.time()
    try:
        main()
    except Exception as error:
        print(error)
    # checking compile time
    end = time.time()
    print(f"time to compile : {end - start:.2f}s")

