﻿# 06 web (Django)
Пример проекта на Django (c использованием REST API)

## Описание
Проект написан и тестировался под Python версии 3.6
Суперпользователь админской страницы: admin, пароль: admin987654 (появляется только если был выполнен импорт фикстур).

### Установка

Распаковать содержимое архива или залить из git-репозитория в выбранную корневую папку проекта.
Название корневой папки роли не играет и его можно поменять на любое.

### Структура проекта

credit - папка расположения приложения программы кредитования
credit/migrations - расположение миграций моделей базы данных
docs - документация
website - папка файлов ядра сервера
.gitignore - файл списка игнорирования git-репозитория
website/manage.py - скрипт стартующий сервер и выполняющий др. операции по управлению им

### Развертывание

1. Настройка (подробнее про настройки в пункте НАСТРОЙКИ)
  - Задайте настройки работы с БД в файле website/website/settings.py; можно оставить текущие
  !Для некоторых СУБД (например postgresql) указанная в настройках база данных АВТОМАТИЧЕСКИ НЕ СОЗДАЕТСЯ
    и должна быть создана самостоятельно перед запуском миграции!
  - Задать прочие настройки, по необходимости

2. Выполнить миграции
  Для применения миграций нужно перейти в корневую папку проекта и выполнить команду:

python manage.py migrate

3. Проимпортировать фикстуры

python manage.py loaddata credit/fixtures/credit.json

если фикстуры решили не импортировать, или в любом случае, можно добавить суперпользователя
python manage.py createsuperuser

4. Сервер готов к старту
  Для старта выполнить команду

python manage.py runserver

### Настройки

Настройки сайта расположены в файле

website/website/settings.py

1. Настройка базы данных
  Находятся в параметре DATABASES['default']
  По-умолчанию установлена БД sqlite, но можно сментить ее на другую.
  Для других типов СУБД могут потребоваться дополнительные параметры:
  HOST, USER, PASSWORD.

  После изменения БД нужно применить к ней миграции (описано в пункте РАЗВЕРТЫВАНИЕ).

2... описание остальных настроек...

### Запуск сервера

Проект содержит встроенный wsgi-сервер, достаточный для тестового запуска.
Для запуска сервервера нужно перейти в корневую папку проекта и выполнить в консоле команду

python manage.py runserver

web-интерфейс будет доступен по адресу
http://127.0.0.1:8000/

Чтобы изменить порт/хост сервера, нужно передать их остальными параметрами:
  - для прослушивания 80 порта

python manage.py runserver 80

  - чтобы сервер слушал публичные ip

python manage.py runserver 0.0.0.0:8080

### Использование

Для просмотра API перейти на страницу
http://127.0.0.1:8000/

Для перехода на админскую страницу
http://127.0.0.1:8000/admin

### Тестирование
