FROM python:3.10

RUN mkdir /src
WORKDIR /src

COPY requirements.txt .

RUN pip install install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "8000"]