# Motor_scraper

Motor_scraper is a Python package to scrape [autoscout.nl](autoscout.nl) items and returns the brand, price, mileage, kw, cc, year, category and fuel in a DataFrame.


Table of content
* [Installation](#installation)
* [Getting Started](#getting-started)
* [Technologies Used](#technologies)
* [Contributing](#contributing)
* [License](#license)


### Installation

To run this calculator package please take a look at the following instructions

1. Install the package
```
pip install git+https://github.com/winckles/motor_scraper.git`
```
2. Import the class
```
from package import MotorScraper
```
3. Create an object and use the functions
```
scrape = MotorScraper()
test_list = scrape.collect_urls(5, ['kawasaki'])
```

### Getting Started
First, run `collect_urls()` with the required number of pages and a list with keywords and save it into a list. Then run `collect_info()` and input the list to get a dataframe.
See the list below for all the possible keywords: 
- kawasaki
  
- bmw
  
- honda
  
- yamaha 
  
- ktm 
  
- piaggio
  
- harley-davidson
  
- ducati

### Technologies
For the used packages and technologies view the [requirements.txt](requirements.txt) file.


### Contributing
Please let me know if you encounter a bug by filing an issue, all contributions are appreciated!

If you plan to contribute new features please send a PR.

### License
Calculator has a MIT-style license, as found in the [LICENSE](LICENSE) file.
