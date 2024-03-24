<img src=https://img.shields.io/badge/python-3.9-violet>

> [!Note]
> Рабочая версия находится в ветке master: https://github.com/ded2322/mailigns_api/tree/master

# Mailings API

## Описание
Mailings API - это API позволяющий создать рассылку на почту.
В базу вносится имя и email клиента, и после можно создать моментальную или отложенную рассылку.

## Инструменты

Язык: Python

Фреймворк: FastApi

Брокер сообщений: Celery-beat

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
    - Все доступные методы находятся по адресу: http://localhost:7777/docs

> [!Note]
> Если вы хотите создать рассыку со своего email, необходимо изменить переменные EMAIL_SENDER (ваш email) и PASSWORD (пароль). Гайд: https://youtu.be/g_j6ILT-X0k?si=UI97wkkUqBCFBKQh .
> 
> Файл с переменными находится в .env файле

