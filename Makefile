MANAGER     = uv
EXEC        = python3
PACKAGE     = src

VENV_DIR    = .venv

UV_CACHE    = .cache/uv-cache

install:
	UV_PROJECT_ENVIRONMENT=$(VENV_DIR) \
	UV_CACHE_DIR=$(UV_CACHE) \
	UV_LINK_MODE=copy \
	$(MANAGER) sync

	UV_PROJECT_ENVIRONMENT=$(VENV_DIR) \
	UV_CACHE_DIR=$(UV_CACHE) \
	$(MANAGER) add torch transformers huggingface-hub pydantic numpy

run:
	UV_PROJECT_ENVIRONMENT=$(VENV_DIR) \
	UV_CACHE_DIR=$(UV_CACHE) \
	$(MANAGER) run $(EXEC) -m $(PACKAGE)

debug:
	UV_PROJECT_ENVIRONMENT=$(VENV_DIR) \
	UV_CACHE_DIR=$(UV_CACHE) \
	$(MANAGER) run $(EXEC) -m pdb -m $(PACKAGE)

clean:
	rm -rf $(VENV_DIR)
	rm -rf $(UV_CACHE)
	rm -rf .pytest_cache
	rm -rf __pycache__

lint:
	UV_PROJECT_ENVIRONMENT=$(VENV_DIR) \
	UV_CACHE_DIR=$(UV_CACHE) \
	$(MANAGER) run ruff check .

.PHONY: install run debug clean lint