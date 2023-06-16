# REST API сервер «Адресная книга»

## Краткое описание:
REST API сервер на основе Flask-RestX выполняющий базовый набор CRUD с использованием РСУБД PostgreSQL и ORM SQLAlchemy.
Имеется возможность записи логов сервера в JSON-файл с применением очередей брокера RabbitMQ.
Структуры БД заполняются автоматически при развертыании приложения из JSON-файла.

### Ручное развертывание приложения:
- Установка зависимостей:
```shell
pip install -r requirements.txt
```
- Развертывание docker-контейнера для PostgreSQL:
```shell
sudo docker run --name address_book_flask_rest_postgres -e POSTGRES_DB=address_book_flask_rest_postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```
- Развертывание docker-контейнера для RabbitMQ:
```shell
sudo docker run --name address_book_flask_rest_rabbit -p 5672:5672 -d rabbitmq
```
- Запуск bash-сценария для применения миграций, автоматического заполнения данных в БД и 
запуска сервера:
```shell
bash entrypoint.sh
```
- Запуск rabbitmq-consumer для получения данных из очереди брокера RabbitMQ:
```shell
python rabbitmq_logging_service/rabbitmq_logging_consumer.py
```
- Просмотр содержимого json-файла с логами приложения (через cat):
```shell
cat address_book_rabbitmq_logging.json
```
### Развертывание приложения через docker-composeЖ
#### Требует настройки, рекомендуется пока использовать первый способ:
- Выполняем сборку контейнера и запуск сервера:
```shell
sudo docker-compose up --build -d
```
- Ручной запуск rabbitmq-consumer для получения данных из очереди брокера RabbitMQ:
```shell
sudo docker exec -it address_book_flask_rest-1 /bin/bash
```
```shell
python rabbitmq_logging_service/rabbitmq_logging_consumer.py
```
```shell
cat address_book_rabbitmq_logging.json
```