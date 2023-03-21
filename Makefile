up:
	docker-compose up --build --remove-orphans
req:
	pip freeze > backend/requirements.txt
down:
	docker-compose down -v
init:
	docker-compose exec -it web sh -c 'cd app && alembic revision --autogenerate -m "init"'
migrate:
	docker-compose exec -it web sh -c 'cd app && alembic revision --autogenerate -m "New"'
upgrade:
	docker-compose exec -it web sh -c 'cd app && alembic upgrade head'
downgrade:
	docker-compose exec -it web sh -c 'cd app && alembic downgrade base'
