#!/usr/bin/env python
"""Test radium."""
import io
from time import time

import pytest

from radium.__main__ import (
    hashe,
    main,
    print_candidat_name,
    print_expected_salary,
    print_job_title,
    read_stdin,
    sleep_random,
)


@pytest.mark.asyncio
async def test_sleep_random():
    """Make sure `sleep_random()` sleeps expected time."""
    expeted_range = range(6)
    start = time()
    await sleep_random()
    duration = int(time() - start)
    assert duration in expeted_range


@pytest.mark.asyncio
async def test_print_candidat_name(capsys):
    """Make sure `print_candidat_name()` prints my name."""
    expected = "Vadim\n"
    await print_candidat_name()
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.asyncio
async def test_print_job_title(capsys):
    """Make sure `print_job_title()` prints your job title."""
    expected = "Стажёр-программист Python / Python Developer Trainee\n"
    await print_job_title()
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.asyncio
async def test_print_expected_salary(capsys):
    """Make sure `print_expected_salary()` prints expected salary in a year."""
    expected = "90_000\n"
    await print_expected_salary()
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.asyncio
async def test_main(capsys):
    """Make sure thе `main()` calls print_*() with expected strings.

    `main()` calls `print_candidat_name()`, `print_job_title()`
    and `print_expected_salary()` and expects an unambiguous print.
    """
    expected_strings = "Vadim\nСтажёр-программист Python / Python Developer Trainee\n90_000\n".split("\n")
    await main()
    captured = capsys.readouterr()
    for string in captured.out.split("\n"):
        assert string in expected_strings


def test_read_stdin(monkeypatch):
    """Make sure `read_stdin()` reads stdin and returns entered data."""
    monkeypatch.setattr("sys.stdin", io.StringIO("spam egg"))
    expected = "spam egg"
    result = read_stdin()
    assert result == expected


def test_hache():
    """Make sure `hache()` haches (sha256) data."""
    entered_data = "foo bar"
    expected = "fbc1a9f858ea9e177916964bd88c3d37b91a1e84412765e29950777f265c4b75"
    result = hashe(entered_data)
    assert result == expected
