install: create-env
	venv/bin/pip install --no-cache-dir -r requirements.txt

create-env:
	python3 -m venv venv

lint:
	black .