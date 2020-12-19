install:
	poetry install

build:
	poetry build

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-games:
	poetry run brain-games

brain-prime:
	poetry run brain-prime

package-install:
	pip3 install --user dist/*.whl

lint:
	poetry run flake8 brain_games
