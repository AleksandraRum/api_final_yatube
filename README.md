# api_final

## Что это такое 

Данный API разработан для использования функционала социальной сети Yatube с помощью запросов.
(в рамкахучебного проекта в Яндекс.Практикум)
В приложении можно создавать, удалять, просматривать и редактировать посты, подписываться на пользователей, добавлять авторов в избранное, комментировать посты, фильтровать записи.

## Используемые технологии

Python 3.7
Django==2.2.16
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AleksandraRum/api_final_yatube.git
```

```
cd api_final_yatube 
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Для работы с JWT установить и подключить библиотеки Djoser и Simple JWT:

```
pip install djoser djangorestframework-simplejwt==4.7.2 
```
```
cd yatube_api
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```



