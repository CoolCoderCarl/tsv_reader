FROM python:3.9

WORKDIR /fastapi
COPY ./requirements.txt /fastapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt

COPY ./api.py /fastapi/api.py

CMD ["uvicorn", "api:api", "--host", "0.0.0.0", "--port", "8080"]