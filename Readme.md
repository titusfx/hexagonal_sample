virtualenv env
source env/local/bin/activate
pip install fastapi uvicorn
pip freeze > requirements.txt
uvicorn main:app --reload
