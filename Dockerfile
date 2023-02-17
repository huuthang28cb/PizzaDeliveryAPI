FROM python:3.9
WORKDIR /usr/src/personalised_nudges

RUN python -m venv venv
CMD ["source venv/Scripts/activate"]

RUN pip install --upgrade pip
COPY ./app ./app
COPY requirements.txt requirements.txt
# RUN pip install --root-user-action=ignore --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip3 install -r requirements.txt

CMD ['sudo chmod -R 777 venv/']
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]