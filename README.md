# DeOldify Image Colorization App

### Overview

This project is a web scraping application built with Python. It uses libraries and tools such as Streamlit, BeautifulSoup, pandas, requests,etc to scrape product data from an e-commerce website, Khelmart and display it in a web application.

It finds specific elements and attributes to extract the product data, such as the product name, old price, special price, and discount percentage.

The extracted data is stored in a pandas DataFrame, which is then displayed into a web application built with Streamlit. The application also provides a feature for users to sort the data on the basis of the numerical features such as Special price, old price, and discount, and also the facilityto download the dataset directly from the webpage is provided.

This project demonstrates the use of web scraping techniques to extract data from websites, and the use of web frameworks to build interactive web applications. It can be used as a starting point for more complex web scraping projects or data analysis tasks.
### Installation
Clone the repository and change path to Deoldify:
```bash
git clone https://github.com/SDeyGitHubber/Khelmart_Sports_Product_Scraper
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage
Run the application:

```bash
streamlit run app.py
```
This is a scraping tool that can be used to scrape any sports product from the Sports E-Commerce company, Khelmart, and the user may also download the dataset if required
### Tools and Technologies Used
- Python
- streamlit
- Beautiful Soup
- Pandas
- Jupyter Notebook

### Gallery

#### The input product is entered and the option to sort is provided accordingly
![Screenshot 2024-03-21 192241](https://github.com/SDeyGitHubber/Khelmart_Sports_Product_Scraper/assets/114286007/11a4d8d4-31e0-48df-a573-37bae9b6029a)

#### The scraped dataset is generated, which the user may also download
![Screenshot 2024-03-21 203106](https://github.com/SDeyGitHubber/Khelmart_Sports_Product_Scraper/assets/114286007/6a07c25d-e2d7-4e0d-9628-dfe3fadcd749)
