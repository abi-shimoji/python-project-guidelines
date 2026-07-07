.PHONY: help format lint typecheck test check all

help:
	@printf "%s\n" \
	"make format     - run ruff format" \
	"make lint       - run ruff check" \
	"make typecheck  - run ty check" \
	"make test       - run pytest" \
	"make check      - run lint, typecheck, test" \
	"make all        - run format, lint, typecheck, test"

format:
	uv run ruff format

lint:
	uv run ruff check

typecheck:
	uv run ty check

test:
	uv run pytest

check: lint typecheck test

all: format lint typecheck test
