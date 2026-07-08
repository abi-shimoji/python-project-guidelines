.PHONY: help install-mise format lint typecheck test check all

help:
	@printf "%s\n" \
	"make install-mise - install mise" \
	"make format     - run ruff format" \
	"make lint       - run ruff check" \
	"make typecheck  - run ty check" \
	"make test       - run pytest" \
	"make check      - run lint, typecheck, test" \
	"make all        - run format, lint, typecheck, test"

install-mise:
	curl https://mise.run | sh

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
