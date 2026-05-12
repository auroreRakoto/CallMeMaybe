from pathlib import Path
import json
# from xml.parsers.expat import model
from llm_sdk.llm_sdk import Small_LLM_Model

from src.parsing import Parser

import time
import sys


def main():
    for arg in sys.argv[:2]:
        print(f"arg is {arg}\n")

    # if "--functions_definition" in sys.argv[:2]:
    #     print("\nchanging def\n")
    # else:
    #     print("\nnothing\n")
    try:
        Parser.parse_args()
    except Exception as error:
        print(f"derror: {error}")
        return
    path = Path("data/input/function_calling_tests.json")
    path2 = Path("data/input/functions_definition.json")
    model = Small_LLM_Model()
    print(f"model : {model}")
    test = model.encode("Spartiate quelle est votre metier?")
    test2 = model.encode("Ahoo! Ahoo! Ahoo!")
    ids = test.squeeze().tolist()
    logit = model.get_logits_from_input_ids(ids)
    print(f"logit : {logit[0]}")
    print(f"token : {type(test)}")
    nat = model.decode(test)
    print(f"question : {nat}")
    nat = model.decode(test2)
    print(f"answer : {nat}")
    with open(path, "r") as file:
        data = json.load(file)

    with open(path2, "r") as file:
        data2 = json.load(file)

    # print(f"data: {data}")
    # print(f"\ndata2: {data2}")

   

if __name__ == "__main__":
    start = time.time()
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
    # checking compile time
    end = time.time()
    print(f"time to compile : {end - start:.2f}s")

