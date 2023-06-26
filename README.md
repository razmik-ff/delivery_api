# delivery_api

python -m venv venv
. venv/bin/activate
pip isntall -r requirements.txt
alembic upgrade head
uvicorn main:app --reload