"""Module to test sw_file_fetch
"""

import os
from datetime import datetime, timedelta

import pytest
from polaris.swpc.space_weather.sw_file_fetch import fetch_indices


@pytest.mark.datafiles()
def test_fetch_indices_happy(datafiles):
    """Test happy case for fetch_indices"""
    os.chdir(datafiles)

    test_indices = ["DGD", "DpD", "dsd"]
    start_dates = [
        datetime(year=2018, month=3, day=12, hour=23, minute=22, second=47),
        None,
        datetime(year=2017, month=5, day=30, hour=15),
    ]
    end_dates = [
        datetime(year=2020, month=4, day=28),
        datetime(year=2019, month=10, day=12),
        None,
    ]

    for index, start, end in zip(test_indices, start_dates, end_dates):
        fetch_indices(
            index, start, end, directory=str(datafiles / "still_not_created")
        )


@pytest.mark.datafiles()
def test_fetch_indices_sad(datafiles):
    """Test sad case for fetch_indices"""
    os.chdir(datafiles)
    bad_start_date = "text_is_bad"
    bad_end_date = 12345  # Numbers are also bad
    start_date = datetime(year=2019, month=1, day=1)

    with pytest.raises(ValueError):
        fetch_indices("what_is_this")

    with pytest.raises(TypeError):
        fetch_indices("DGD", bad_start_date)

    with pytest.raises(TypeError):
        fetch_indices("DGD", bad_end_date)

    with pytest.raises(ValueError):
        fetch_indices("DGD", start_date, start_date - timedelta(days=10))
