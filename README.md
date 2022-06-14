# api_final

## Что это такое 

Это REST API для учебного проекта соцсети Yatube. Через него сможет работать,например, мобильное приложение. Из мобильного приложения можно будет написать пост, почитать посты в определенной группе или оставить комментарий. При этом будут отслеживаться права на редактирование или удаление поста или комментария. 

## Как его запустить

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/AleksandraRum/api_final_yatube.git
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

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

