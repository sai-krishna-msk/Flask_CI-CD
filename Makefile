install:
	pip install -r requirements.txt

test:
	set PYTHONPATH=./src
	pytest -v




	
all: install test