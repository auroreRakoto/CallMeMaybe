from typing import Any

from pydantic import BaseModel, ConfigDict

from llm_sdk.llm_sdk import Small_LLM_Model

class Process(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    model: Small_LLM_Model
    functions: list[dict[str, Any]]
    prompts: list[dict[str, str]]

    def process_prompt(self, prompt: str) -> dict[str, Any]:
        return {
            "prompt": prompt,
            "name": self.functions[0]["name"],
            "parameters": {}
        }

    def build_prompt(self, user_prompt: str) -> str:
        return (
            "Choose the correct function for this user request.\n"
            f"User request: {user_prompt}\n"
            f"Available functions: {self.functions}\n"
            "Return only the function name."
        )

    def process_all(self) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []

        for item in self.prompts:
            results.append(self.process_prompt(item["prompt"]))

        return results
