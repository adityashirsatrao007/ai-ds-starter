.PHONY: install lint typecheck test train clean setup

install:
	pip install --upgrade pip
	pip install -r requirements.txt

lint:
	ruff check src/ tests/

typecheck:
	mypy src/ --ignore-missing-imports

test:
	pytest tests/ -v --cov=src/

train:
	python src/train.py

dvc-pull:
	dvc pull

dvc-push:
	dvc push

dvc-repro:
	dvc repro

clean:
	rm -rf __pycache__ .pytest_cache .mypy_cache .ruff_cache
	find . -name "*.pyc" -delete

setup: install lint typecheck test
	@echo "All checks passed!"
