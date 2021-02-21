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
    check = scrape.collect_urls(1, ['kawasaki'])
    assert len(check) == 20


def test_collect_info():
    scrape = MotorScraper()
    list_try = scrape.collect_urls(1, ['kawasaki'])
    df = scrape.collect_info(list_try)
    assert df.shape == (20, 8)
