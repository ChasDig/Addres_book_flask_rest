export FLASK_APP=app.py
export FLASK_DEV=develop
flask db upgrade
python load_data_for_database.py
flask run -h 0.0.0.0 -p 80