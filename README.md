# Mailings API

## Описание
Mailings API - это API позволяющий создать рассылку на почту.
В базу вносится имя и email клиента, и после можно создать моментальную или отложенную рассылку.

## Инструменты

Язык: Python

Фреймворк: FastApi

Брокер сообщений: Selery

База данных: Postgres

## Как развернуть
1. Разворачивание с помощью Docker
    - Скачиваете и устанавливаете Docker https://docs.docker.com/get-docker/.
    - Как только скачан Docker, запускаем
    - Клонируем репозиторий
        ```
        https://github.com/ded2322/mailigns_api.git
        ```
    - Перходим в его директорию
      ```
      cd mailigns_api
      ```
    - После прописываем в консоле команду
      ```
      docker-compose up --build
      ```
    - И переходим по адресу http://localhost:7777/docs
      
    ![изображение](https://github.com/ded2322/mailigns_api/assets/151318767/e73e7604-732b-492e-9b42-4e6565f4e175)
    Swagger Api
   
2. Чтобы развернуть проект без Docker
   - Установить Postgres
   - В pgAdmin создать сервер
   - В папке задать созданные вами параметры mailigns_api/.env
   - Установить Redis-server
   - Запустить Redis-server,Selery и FastApi
> [!Note]
> В случае, если вы хотетие создать рассыку со своего email, необходимо изменить переменные EMAIL_SENDER (ваш email) и PASSWORD (пароль) этом видео показывается как получить пароль: https://youtu.be/g_j6ILT-X0k?si=UI97wkkUqBCFBKQh
> 
> Файл с переменными находится mailigns_api/mailing/config_email.py
## Endpoint

##
