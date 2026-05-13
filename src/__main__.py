from pathlib import Path
import json
# from xml.parsers.expat import model
from llm_sdk.llm_sdk import Small_LLM_Model

from src.parsing import Parser
from src.process import Process

import time
import sys

def load_json() -> list[dict[str,str]]:
    lst = []
    dico = {}
    lst.append(dico)
    return lst

def save_json():
    pass


def main():
    try:
        args = Parser.parse_args(sys.argv)
    except ValueError as error:
        raise f"Argument error: {error}"

    try:
        functions = load_json()
        prompts = load_json()
    except OSError as error:
        raise f"File error: {error}"
    except Exception as error: # change to json error
        raise f"JSON error: {error}"

    try:
        model = Small_LLM_Model()
        process = Process(
            model=model,
            functions=functions,
            prompts=prompts
        )
        results = process.process_all()
    except Exception as error:
        raise f"Error {error}"

    # try:
    #     save_json()
    # except Exception as error:
    #     raise f"Output error: {error}"
   

if __name__ == "__main__":
    start = time.time()
    try:
        main()
    except Exception as error:
        print(error)
    # checking compile time
    end = time.time()
    print(f"time to compile : {end - start:.2f}s")

