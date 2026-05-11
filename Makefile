MANAGER	= uv
EXEC	= python3
PACKAGE	= src

install:
	UV_LINK_MODE=copy uv sync
	uv add torch transformers huggingface-hub pydantic numpy

run:
	$(MANAGER) run ${EXEC} -m ${PACKAGE}


.PHONY: install run debug clean lint