from pathlib import Path
import json
# from xml.parsers.expat import model
# from llm_sdk.llm_sdk import Small_LLM_Model

from src.parsing import Parser
from src.process import Process

import time
import sys


def main():
    try:
        args = Parser.parse_args(sys.argv)
    except ValueError as error:
        print(f"Argument error: {error}")
        return
    model = Small_LLM_Model()
    try:
        process = Process(
            model = model,
            args = args,
            functions = args.functions_definition,
            prompts = args.input,
            output = args.output
        )
    except Exception as error:
        print(f"Init error: {error}")
        return



    save_json(args.output, results)
   

if __name__ == "__main__":
    start = time.time()
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
    # checking compile time
    end = time.time()
    print(f"time to compile : {end - start:.2f}s")

