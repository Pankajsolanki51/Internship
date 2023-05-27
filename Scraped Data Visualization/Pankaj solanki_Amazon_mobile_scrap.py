import pandas as pd
import requests
from bs4 import BeautifulSoup

pages_to_scrape = 50  # specify the number of pages to scrape
url = 'https://www.amazon.in/s?k=mobiles&rh=p_36%3A-5000000&crid=VUIMNJPBJV5Z&qid=1683803996&rnid=1318502031&sprefix=mobile%2Caps%2C563&ref=sr_pg_1'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35', 'Accept-Language': 'en-US, en; q=0.5'}

product_name = []
price = []
rating = []
MRP=[]
Delivery_date = []

for page in range(1, pages_to_scrape + 1):
    page_url = url + '&page=' + str(page)  # add page number to the URL
    webpage = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    
    for product in soup.find_all('div', {'data-component-type': 's-search-result'}):
        try:
            product_name.append(product.find('h2', {'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}).text.strip())
        except:
            product_name.append(None)
        try:
            price.append(product.find('span', {'class': 'a-price-whole'}).text.strip())
        except:
            price.append(None)
        try:
            rating.append(product.find('span', {'class': 'a-icon-alt'}).text.strip())
        except:
            rating.append(None)
        try:
            MRP.append(product.find('span', {'class': 'a-offscreen'}).text.strip())
        except:
            MRP.append(None)
        try:
            Delivery_date.append(product.find('span', {'class': 'a-color-base a-text-bold'}).text.strip())
        except:
            Delivery_date.append(None)

df = pd.DataFrame({'Product Name': product_name, 'Price': price, 'Rating': rating, 'M.R.P': MRP, 'Expected Delivery':Delivery_date})
df.to_csv('Pankaj_solanki_Amazon_mobiles_17may23.csv', index=False)
print('Data saved to CSV successfully!')
