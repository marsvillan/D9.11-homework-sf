# D9.11-homework-sf

## Установка и запуск (все действия через коммандную строку)
  - скачать проект и перейти в директорию проекта
```
$ git clone https://github.com/marsvillan/D9.11-homework-sf.git
$ cd D9.11-homework-sf
```

  - создать виртуальное окружение
```
$ python -m venv env
```

  - применить виртуальное окружение
```
### Если у вас Linux:
$ source env/bin/activate
### Если у вас Windows:
$ env\Scripts\activate.bat
```

 - установить зависимости
```
$ pip install -r requirements.txt
```

  - загрузить фикстуры в качестве примеров
```
$ python manage.py loaddata data.json
```

  - запустить сервер
```
$ python manage.py runserver
```
