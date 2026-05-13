from pathlib import Path
from pydantic import BaseModel

# functions = load_json(args.functions_definition)
# prompts = load_json(args.input)



class ProgramArgs(BaseModel):
    """Stores paths received from command-line arguments."""

    functions_definition: Path = Path("data/input/functions_definition.json")
    input: Path = Path("data/input/function_calling_tests.json")
    output: Path = Path("data/output/function_calling_results.json")


class Parser:
    """Parses command-line arguments for the function calling project."""

    VALID_OPTIONS = {
        "--functions_definition": "functions_definition",
        "--input": "input",
        "--output": "output",
    }

    @staticmethod
    def parse_args(argv: list[str]) -> ProgramArgs:
        """Parse command-line arguments.

        Args:
            argv: Arguments received from sys.argv.

        Returns:
            ProgramArgs: Parsed paths.

        Raises:
            ValueError: If an option is unknown or missing its value.
        """
        parsed_args: dict[str, Path] = {}

        index = 1
        while index < len(argv):
            option = argv[index]

            if option not in Parser.VALID_OPTIONS:
                raise ValueError(f"Unknown option: {option}")

            if index + 1 >= len(argv):
                raise ValueError(f"Missing value after {option}")

            value = argv[index + 1]

            if value.startswith("--"):
                raise ValueError(f"Missing value after {option}")

            field_name = Parser.VALID_OPTIONS[option]
            parsed_args[field_name] = Path(value)

            index += 2

        return ProgramArgs(**parsed_args)
