install:
	poetry install

build:
	poetry build

brain-even:
	poetry run brain-games -n 'brain-even'

brain-calc:
	poetry run brain-games -n 'brain-calc'

brain-gcd:
	poetry run brain-games -n 'brain-gcd'

package-install:
	pip3 install --user dist/*.whl

lint:
	poetry run flake8 brain_games
