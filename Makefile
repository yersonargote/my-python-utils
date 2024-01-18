args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`


ruff:
	pipenv run check .
	pipenv run ruff format .
black:
	pipenv run black .
check:
	make ruff
	make black

install:
	pipenv install --dev
help:
	pipenv run python3 main.py --help
run:
	pipenv run python3 main.py $(call args,--help)
	