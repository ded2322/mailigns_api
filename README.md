<img src=https://img.shields.io/badge/python-3.9-violet> <img src=https://img.shields.io/badge/linter-black-green>
# Mailings API

## Описание
Mailings API - это API позволяющий создать рассылку на почту.
В базу вносится имя и email клиента, и после можно создать моментальную или отложенную рассылку.

## Инструменты

Язык: Python

Фреймворк: FastApi

Брокер сообщений: Celery

База данных: Postgres

## Как развернуть
1. Разворачивание с помощью Docker
    - Устанавливаем Docker https://docs.docker.com/get-docker/.
    - Клонируем репозиторий
        ```
        https://github.com/ded2322/mailigns_api.git
        ```
    - Перходим в директорию
      ```
      cd mailigns_api
      ```
    - После прописываем в консоле команду
      ```
      docker-compose up --build
      ```
    - Все доступные методы находятся по адресу http://localhost:7777/docs
      
    ![изображение](https://github.com/ded2322/mailigns_api/assets/151318767/e73e7604-732b-492e-9b42-4e6565f4e175)
    Демонстрация работы в Swagger Api
   
2. Разварачивание проекта без Docker
   - Установить Postgres
   - В pgAdmin или другой субд создаете сервер
   - В папке задать созданные вами параметры mailigns_api/.env
   - Установить Redis-server
   - Запустить Redis-server,Сelery и FastApi
> [!Note]
> Если вы хотите создать рассыку со своего email, необходимо изменить переменные EMAIL_SENDER (ваш email) и PASSWORD (пароль), гайд: https://youtu.be/g_j6ILT-X0k?si=UI97wkkUqBCFBKQh
> 
> Файл с переменными находится mailigns_api/mailing/config_email.py

## Запросы

### Http метод- Get
1.
  ```http
  GET /clients/all_client
  ```
Response
```json
[
  {
    "Clients": {
      "email": "user@example.com",
      "username": "string",
      "id": 1
    }
  }
]
```
2.
```http
GET /mailings/all
```
Response
```json
 {
    "Mailings": {
      "email_client": "user@example.com",
      "subject_mailing": "string",
      "date": "2024-01-29 02:20:17.528674",
      "id": 1
    }
  },
  {
    "Mailings": {
      "email_client": "user@example.com",
      "subject_mailing": "string",
      "date": "2024-01-29 02:21:23.708353",
      "id": 2
    }
  }
```
---

### Http метод - Post
1.
```http
POST /clients/add_client
```
Request
```json
{
  "name": "string",
  "email": "user@example.com"
}
```

2.
```http
POST /mailings/create_queue_mailings
```
Request
```json
{
  "subject": "string",
  "text_message": "string",
  "scheduled_date": "DD-MM-YYYY HH:MM"
}
```

3.
```http
POST /mailings/create_and_start_mailings
```
Request
```json
{
  "subject": "string",
  "text_message": "string"
}
```
---

### Остальные Http методы
1. Метод для удаления клиента по id
```http
DELETE /clients/delete_clients
```
Request
```json
{
  "id": 0
}
```
2. Метод для обнавления email клиента
```http
PATCH /clients/update_data
```
Request
```json
{
  "id": 0,
  "name": "string",
  "new_email": "user@example.com"
}
```
   