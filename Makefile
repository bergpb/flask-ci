install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

test:
	pytest -vv

coverage:
	coverage run -m pytest
	coverage report
	coverage xml

format:
	black app tests app.py setup.py

check:
	black app tests app.py setup.py --check

.PHONY: test coverage format check 