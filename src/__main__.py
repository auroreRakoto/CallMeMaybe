from pathlib import Path
import json
# from xml.parsers.expat import model
from llm_sdk.llm_sdk import Small_LLM_Model


def main():
    path = Path("data/input/function_calling_tests.json")
    path2 = Path("data/input/functions_definition.json")
    model = Small_LLM_Model()
    print("hello")
    print(model)
    path_to_vocab = model.get_path_to_vocab_file()
    test = model.encode("Spartiate quelle est votre metier?")
    test2 = model.encode("Ahoo! Ahoo! Ahoo!")
    logit = model.get_logits_from_input_ids(test[0])
    print(f"logit : {logit}")
    print(f"token : {test}")
    nat = model.decode(test)
    print(f"question : {nat}")
    nat = model.decode(test2)
    print(f"answer : {nat}")
    # with open(path, "r") as file:
    #     data = json.load(file)

    # with open(path2, "r") as file:
    #     data2 = json.load(file)

    # print(f"data: {data}")
    # print(f"\ndata2: {data2}")
    # print(f"\npath_to_vocab: {path_to_vocab}")


if __name__ == "__main__":
    main()
