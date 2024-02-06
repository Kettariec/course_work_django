
<h2 align="center">Курсовая работа Django</h2>

Веб-приложение сервиса управления рассылками, администрирования и получения статистики.


<!-- USAGE EXAMPLES -->
## Usage

Для запуска web-приложения используйте команду "python manage.py runserver" либо через конфигурационные настройки PyCharm.

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
    template/users - html шаблоны для приложения users
    admin.py - настройки админки
    forms.py - настройки форм
    models.py - модели приложения
    urls.py - файл маршрутизации приложения
    views.py - контроллеры

manage.py - точка входа веб-приложения

requirements.txt - список зависимостей для проекта.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

kettariec@gmail.com

https://github.com/Kettariec/course_work_django

<p align="right">(<a href="#readme-top">back to top</a>)</p>