INI = ""

.PHONY: 
	clean
	install
	run
	test
	compile

install:
	poetry install --no-root

clean:
	@echo "Cleaning up Python directories..."
	find . -name "*.pyc" -delete
	find . -name "*.log" -delete
	find . -name "*.log.*" -delete
	find . -name "__pycache__" -type d -exec rm -r {} +
	find . -name ".ruff_cache" -type d -exec rm -r {} +
	find . -name ".mypy_cache" -type d -exec rm -r {} +
	find . -name ".pytest_cache" -type d -exec rm -r {} +

run:
	poetry run python app/main.py -f $(INI)

compile:
	poetry run pyinstaller --onefile src/app/main.py

test:
	poetry run python -m pytest
