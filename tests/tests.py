from scraper.package import MotorScraper
import pytest


def test_collect_urls_not_zero():
    scrape = MotorScraper()
    with pytest.raises(Exception):
        scrape.collect_urls(0, ['kawasaki'])


def test_collect_urls_different_keyword():
    scrape = MotorScraper()
    with pytest.raises(Exception):
        scrape.collect_urls(1, ['keyword'])


def test_collect_urls():
    scrape = MotorScraper()
    assert len(scrape.collect_urls(1, ['kawasaki'])) == 20


# def test_correct_division():
#     calc = Calculator(10)
#     assert calc.divide(2) == 5
#
#
# def test_divide_by_zero_error():
#     calc = Calculator()
#     with pytest.raises(ZeroDivisionError):
#         calc.divide(0)
#
#
# def test_take_root():
#     calc = Calculator(16)
#     assert calc.take_root(1) == 16
#
#
# def test_take_root_by_zero_error():
#     calc = Calculator()
#     with pytest.raises(ZeroDivisionError):
#         calc.take_root(0)
