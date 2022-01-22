Task
====

Cкрипт, запускающий асинхронные задачи, выводящие через случайное
количество времени (до 5 секунд) мое имя, название интересной вакансии,
ожидаемый уровень зарплаты через год.
После выполнения всех асинхронных задач скрипт должен прочитать stdin
и вывести sha256 хэш от прочитанных данных

Install
-------

::

    git clone https://github.com/fj-fj-fj/radium-trial-unit-task.git
    cd radium-trial-unit-task
    poetry install
    make check
    make test

Usage
-----

::

    $ ls | grep __main__
    __main__.py
    $ python3 .

Usage with Poetry
-----------------

::

    make run

Дождитесь завершения ``asyncio.gather()`` и введите данные в консоль.
Нажмите Cntrl+D, чтобы закрыть файловый дескриптор.
Вы увидете хеш введенных данных.
