#!/usr/bin/env python
"""Cкрипт, запускающий асинхронные задачи c рандомным асинхронным сном.

Асинхронные задачи, выводящие через случайное количество времени (до 5 секунд)
мое имя, название интересной вакансии, ожидаемый уровень зарплаты через год.
После выполнения всех асинхронных задач скрипт должен прочитать stdin
и вывести sha256 хэш от прочитанных данных

```
$ ls | grep __main__
__main__.py
$ python3 .
# Дождитесь завершения `asyncio.gather()` и введите данные в консоль.
# Нажмите Cntrl+D, чтобы закрыть файловый дескриптор.
# Вы увидете хеш введенных данных.
```

"""
import asyncio
import hashlib
import random
import sys


async def sleep_random() -> None:
    """Asynchronous sleep. By default 1-5 seconds."""
    await asyncio.sleep(random.randint(1, 5))  # noqa: S311


async def print_candidat_name() -> None:
    """Coroutine to print out a candidat name."""
    await sleep_random()
    print("Vadim")  # noqa: WPS421


async def print_job_title() -> None:
    """Coroutine to print out a job title."""
    await sleep_random()
    print("Стажёр-программист Python / Python Developer Trainee")  # noqa: WPS421


async def print_expected_salary() -> None:
    """Coroutine to print out an expected salary in a year."""
    await sleep_random()
    print("90_000")  # noqa: WPS421


async def main() -> None:
    """Pass coroutines to `asyncio.gather()`."""
    await asyncio.gather(
        print_candidat_name(),
        print_job_title(),
        print_expected_salary(),
    )


def read_stdin() -> str:
    """Return stdin data."""
    return sys.stdin.read()


def hashe(entered_data: str) -> str:
    """Return hashed (sha-256) stdin data."""
    return hashlib.sha256(entered_data.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    asyncio.run(main())
    HASHED = hashe(read_stdin())
    print(HASHED)  # noqa: WPS421
