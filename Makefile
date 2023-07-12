start:
# poetry run flask --app flask_training.example run --port 8000

# poetry run flask --app flask_training.example:app run --port 8000

	poetry run flask --app flask_training.example:app run

start-debug:
	poetry run flask --app flask_training.example --debug run --port 8000
