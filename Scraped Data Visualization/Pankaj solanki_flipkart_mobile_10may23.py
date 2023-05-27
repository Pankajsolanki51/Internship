import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Desscription = []
Rating = []
Reviews = []
Delivery = []
Discount=[]

for i in range(2, 52):
    url = (
        "https://www.flipkart.com/search?q=phone+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
        + str(i)
    )

    r = requests.get(url)
    print(r)

    soup = BeautifulSoup(r.text, "lxml")

    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_="_4rR01T")
    for i in names:
        name = i.text
        Product_name.append(name)

    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in prices:
        name = i.text
        Prices.append(name)

    desc = box.find_all("ul", class_="_1xgFaf")
    for i in desc:
        name = i.text
        Desscription.append(name)

    rating = box.find_all("div", class_="_3LWZlK")
    for i in rating:
        name = i.text
        Rating.append(name)

    reviews = box.find_all("span", class_="_13vcmD")
    for i in reviews:
        name = i.text
        Reviews.append(name)

    delivery = box.find_all("div", class_="_2Tpdn3")
    for i in delivery:
        name = i.text
        Delivery.append(name)

    discount = box.find_all("div",class_="_3Ay6Sb")
    for i in discount:
        name = i.text
        Discount.append(name)    


# Remove any elements causing the lists to have different lengths
min_length = min(
    len(Product_name),
    len(Prices),
    len(Desscription),
    len(Rating),
    len(Reviews),
    len(Delivery),
    len(Discount)
)
Product_name = Product_name[:min_length]
Prices = Prices[:min_length]
Desscription = Desscription[:min_length]
Rating = Rating[:min_length]
Reviews = Reviews[:min_length]
Delivery = Delivery[:min_length]
Discount = Discount[:min_length]
df = pd.DataFrame(
    {
        "Product Name": Product_name,
        "Prices": Prices,
        "Descriptio": Desscription,
        "Rating": Rating,
        "Reviews": Reviews,
        "Delivery": Delivery,
        "Discount": Discount,
    }
)

df.to_csv(
    "E:/data_analyst/flipkart_scrap_mobile/flipkart_mobile_under_50000_18may23.csv"
)
print('Data saved to CSV successfully!')