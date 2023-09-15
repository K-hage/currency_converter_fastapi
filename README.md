# Конвертер валют

## Стек:

- FastAPI
- Docker

___

### Описание:

Сервис позволяет конвертировать валюту.
Внешний источник конвертации [exchangerate-api](https://www.exchangerate-api.com/docs/overview)

___

## Как запустить проект:

- Клонируйте репозиторий на свой компьютер
- Создайте .env файл по примеру env.example
- В терминале в папке с проектом использовать команду:

```shell
docker-compose up --build -d
```

Проект будет доступен по ссылке на [Swagger](http://localhost/)
___
Примеры запросов:

- [http://localhost/api/rates?from=USD&to=RUB&value=1](http://localhost/api/rates?from=USD&to=RUB&value=1)
- [http://localhost/api/rates?from=EUR&to=RUB&value=1](http://localhost/api/rates?from=EUR&to=RUB&value=1)
- [http://localhost/api/rates?from=RUB&to=USD&value=10000](http://localhost/api/rates?from=RUB&to=USD&value=10000)

___

## Как остановить проект:

- В терминале в папке с проектом использовать команду:

```shell
docker-compose down -v
```
