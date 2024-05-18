
<h2 align="center">Курсовая работа Django</h2>

Веб-приложение сервиса управления рассылками, администрирования и получения статистики.


<!-- USAGE EXAMPLES -->
## Usage

Перед запуском web-приложения создайте базу данных, создайте и примените миграции, установите необходимые пакеты из файла requirements.txt и заполните файл .env по образцу env.sample. Используйте команду "python manage.py csu" для создания суперпользователя и "python manage.py manager" для создания группы с функционалом менеджера. Для запуска используйте команду "python manage.py runserver". Для запуска рассылок "python manage.py sm".

## Docker

Создать образы и контейнеры Docker с помощью команд: "docker-compose build" и "docker-compose up".

## Структура проекта

config/

    settings.py - настройки приложений
    urls.py - файл маршрутизации

blog/

    templates/blog - html шаблоны для приложения blog
    admin.py - настройки админки
    forms.py - настройки форм
    models.py - модели приложения
    urls.py - файл маршрутизации приложения
    views.py - контроллеры

newsletter/

    management/commands
        sm - кастомная команда начала рассылки
    static - директория с файлами для стилистического оформления сайта
    templates/newsletter - html шаблоны для приложения newsletter
    templatetags/
        my_tags - кастомные тэги
    admin.py - настройки админки
    forms.py - настройки форм
    models.py - модели приложения
    services.py - сервисные функции
    urls.py - файл маршрутизации приложения
    views.py - контроллеры

users/

    management/commands
        csu - кастомная команда создания суперпользователя
        manager - кастомная команда для создания группы с функционалом менеджера
    template/users - html шаблоны для приложения users
    admin.py - настройки админки
    forms.py - настройки форм
    models.py - модели приложения
    urls.py - файл маршрутизации приложения
    views.py - контроллеры

manage.py - точка входа веб-приложения.

requirements.txt - список зависимостей для проекта.

env.sample - пример заполнения переменных окружения.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

kettariec@gmail.com

https://github.com/Kettariec/course_work_django

<p align="right">(<a href="#readme-top">back to top</a>)</p>