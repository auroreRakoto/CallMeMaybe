import sys

class Parser:
    def parse_args() -> None:
        i = 2
        arg = sys.argv[:i]
        if len(sys.argv) % 2 == 0:
            raise ValueError("lala 1")
        while arg:
            if arg in "--functions_definition":
                if sys.argv[:i+1]:
                    pass
                else:
                    raise ValueError("lala")
            i = i + 2
            arg = sys.argv[:i]
