install:
	poetry install

build:
	poetry build

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

package-install:
	pip3 install --user dist/*.whl

lint:
	poetry run flake8 brain_games
