migrate:
	python manage.py makemigrations users projects
	python manage.py migrate
	python manage.py createsuperuser --username admin --email admin@admin.com
clear:
	rm -f db.sqlite3
	find . -name "__pycache__" -type d -exec /bin/rm -rf {} +
	find . -name "migrations" -type d -exec /bin/rm -rf {} +
lint:
	black .