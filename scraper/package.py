from bs4 import BeautifulSoup
import requests
import pandas as pd

brand_list, price_list, km_list, kw_list, year_list, new_list, cc_list, fuel_list = ([] for i in range(8))


class MotorScraper:
    """
        A scraper class
        ...
        Attributes
        ----------
        Methods
        -------
        check_memory()
            checks the number in memory
        """

    @staticmethod
    def collect_urls(pages_number: int, keywords: list) -> list:
        """ Scrape url for number of pages and a keyword list
        and returns a list"""
        url_list = []
        possible_keywords = ['kawasaki', 'bmw', 'honda', 'yamaha', 'ktm', 'piaggio', 'harley-davidson', 'ducati']

        if pages_number <= 0:
            raise Exception("Should be more than 0")
        else:
            for page_no in range(1, pages_number + 1):
                for keyword in keywords:
                    if keyword not in possible_keywords:
                        raise Exception("Enter a keyword that's on the list")
                    else:
                        url = f"https://www.autoscout24.nl/lst-moto/{keyword}?sort=standard&desc=0&offer=N%2CU&ustate" \
                              f"=N%2CU&size=20&page={page_no}"

                        headers = {"User-Agent": "Mozilla/5.0"}
                        page = requests.get(url, headers=headers)
                        soup = BeautifulSoup(page.content, "html.parser")

                        url_list.extend(
                            [value["href"] for value in soup.find_all(attrs={"data-item-name": "detail-page-link"})])
            return url_list

    @staticmethod
    def __get_price(soup: BeautifulSoup, price_list: list) -> list:
        try:
            path = soup.find("div", class_="cldt-price")
            anchor = path.find("h2")
            price_list.extend([anchor.text])
        except:
            price_list.extend([None])
        return price_list

    @staticmethod
    def __get_km(soup: BeautifulSoup, km_list: list) -> list:
        try:
            path = soup.find("span", class_="cldt-stage-primary-keyfact")
            km_list.extend([path.text])
        except:
            km_list.extend([None])
        return km_list

    @staticmethod
    def __get_kw(soup: BeautifulSoup, kw_list: list) -> list:
        try:
            path = soup.find_all("span", class_="cldt-stage-primary-keyfact")
            kw_list.extend([path[2].text])
        except:
            kw_list.extend([None])
        return kw_list

    @staticmethod
    def __get_year(soup: BeautifulSoup, year_list: list) -> list:
        try:
            path = soup.find("dt", text="Bouwjaar")
            anchor = path.find_next_sibling("dd").text
            year_list.extend([anchor])
        except:
            year_list.extend([None])
        return year_list

    @staticmethod
    def __get_brand(soup: BeautifulSoup, brand_list: list) -> list:
        try:
            path = soup.find("dt", text="Merk")
            anchor = path.find_next_sibling("dd").text
            brand_list.extend([anchor])
        except:
            brand_list.extend([None])
        return brand_list

    @staticmethod
    def __get_new(soup: BeautifulSoup, new_list: list) -> list:
        try:
            path = soup.find("dt", text="Categorie")
            anchor = path.find_next_sibling("dd").text
            new_list.extend([anchor])
        except:
            new_list.extend([None])
        return new_list

    @staticmethod
    def __get_fuel(soup: BeautifulSoup, fuel_list: list) -> list:
        try:
            path = soup.find("dt", text="Brandstof")
            anchor = path.find_next_sibling("dd").text
            fuel_list.extend([anchor])
        except:
            fuel_list.extend([None])
        return fuel_list

    @staticmethod
    def __get_cc(soup: BeautifulSoup, cc_list: list) -> list:
        try:
            path = soup.find("dt", text="Cilinderinhoud")
            anchor = path.find_next_sibling("dd").text
            cc_list.extend([anchor])
        except:
            cc_list.extend([None])
        return cc_list

    @staticmethod
    def collect_info(search_list: list) -> pd.DataFrame:
        """ Scrape url for number of pages and a keyword
        and returns a pandas dataframe"""

        for urls in search_list:
            url = f"https://www.autoscout24.nl{urls}"

            headers = {"User-Agent": "Mozilla/5.0"}
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, "html.parser")

            price = MotorScraper.__get_price(soup, price_list)
            km = MotorScraper.__get_km(soup, km_list)
            kw = MotorScraper.__get_kw(soup, kw_list)
            year = MotorScraper.__get_year(soup, year_list)
            brand = MotorScraper.__get_brand(soup, brand_list)
            new = MotorScraper.__get_new(soup, new_list)
            fuel = MotorScraper.__get_fuel(soup, fuel_list)
            cc = MotorScraper.__get_cc(soup, cc_list)

        dict_ = {
            "brand": brand,
            "price": price,
            "mileage": km,
            "power": kw,
            "new": new,
            "year": year,
            "fuel": fuel,
            "cc": cc
        }

        df = pd.DataFrame.from_dict(dict_, orient='index')
        df = df.transpose()

        return df
