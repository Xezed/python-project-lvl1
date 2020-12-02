install:
	poetry install

build:
	poetry build

make brain-games:
	poetry run brain-games

package-install:
	pip3 install --user dist/*.whl

lint:
	poetry run flake8 brain_games
