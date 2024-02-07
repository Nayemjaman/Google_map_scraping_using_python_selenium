# Google_map_scraping_using_python_selenium

![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://github.dev/Nayemjaman/Google_map_scraping_using_python_selenium)

## Introduction
This project utilizes Python and Selenium to scrape business data from Google Maps. It collects information based on specific keywords and divisions in Bangladesh.


## Usage
1. Clone the repository:

   **bash**
   ```
   git clone https://github.com/Nayemjaman/Google_map_scraping_using_python_selenium.git
   cd Google_map_scraping_using_python_selenium
    ```
   **Install dependencies:**

```
pip install -r requirements.txt
```

  **Run the URL scraper:**
    
```
python url_scraper.py
```

  **Run the company details scraper:**
    
```
python company_details.py
```

  **Project Structure:**
    
**url_scraper.py:** Python script for scraping Google Maps URLs based on specified keywords and divisions.

**company_details.py:** Python script for scraping detailed information about businesses from the collected URLs.

**keywords.txt:** File containing keywords for search queries.

**division.txt:** File containing divisions in Bangladesh for search queries.

**company_urls.txt:** File to store unique URLs collected during the scraping process.

**data.csv:** CSV file to store the scraped business details.




## Built With
- **[Python](https://www.python.org/):** The elegant and versatile programming language used for scripting.
- **[Selenium](https://www.selenium.dev/):** A powerful web browser automation tool for effortless interaction with web pages.
- **[ChromeDriver](https://sites.google.com/chromium.org/driver/):** The WebDriver for Chrome, ensuring seamless integration and control.
- **[Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager):** A Python library that effortlessly manages web drivers, simplifying the setup process.

