.PHONY: help install format lint test check clean run-config run-logger

help:
	@echo ""
	@echo "Available commands:"
	@echo "  make install      - Install project dependencies"
	@echo "  make format       - Format code using Ruff"
	@echo "  make lint         - Run Ruff lint checks"
	@echo "  make test         - Run pytest"
	@echo "  make check        - Run format + lint + tests"
	@echo "  make run-config   - Test configuration"
	@echo "  make run-logger   - Test logger"
	@echo "  make clean        - Remove cache files"

install:
	poetry install

format:
	poetry run ruff format .

lint:
	poetry run ruff check .

test:
	poetry run pytest

check:
	poetry run ruff format .
	poetry run ruff check .
	poetry run pytest

run-config:
	poetry run python scripts/test_config.py

run-logger:
	poetry run python scripts/test_logger.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
