INI = ""

.PHONY: 
	clean
	install
	run
	test
	compile

install:
	poetry install --no-root

install-prod
	poetry install --no-dev

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
	./dist/kaspersky_validator.exe -f $(INI)

compile:
	pyinstaller --onefile --add-data "../configs;configs" -p=".;../..;app" --name kaspersky_validator app/main.py

test:
	poetry run python -m pytest
