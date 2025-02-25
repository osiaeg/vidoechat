### Self-hosted
```bash
pip install django-generate-secret-key

python manage.py generate_secret_key
```
Результат работы последней команды сохранить в файл *.env* в корневой директории проекта.
Пример содержания *.env*
```
SECRET_KEY=output_from_previous_command
```

### Requirements

Если после установки модуля *psycopg* в момент выполнения команды появляются ошибки,
то необходимо выполниться следующую команду:
```bash 
sudo pacman -Syu postgresql-libs
```


