install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main 
	python -m pytest --nbval src/*.ipynb

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

deploy:
	# Deploy code goes here
		
all: install lint format test 

