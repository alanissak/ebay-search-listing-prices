import requests
from bs4 import BeautifulSoup

# Replace the URL below with the eBay search result page you want to scrape
url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=AUX+CABLE+3.5MM+MALE+TO+MALE+MIC&_sacat=0'

# Send a GET request to the URL and parse the response with Beautiful Soup
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the HTML elements that contain the price values
price_elements = soup.find_all('span', class_='s-item__price')

# Extract the price values from the HTML elements and store them in a list
prices = [element.text for element in price_elements]

# Save the list of prices to a text file
with open('prices.txt', 'w') as f:
    for price in prices:
        f.write(price + '\n')

# Print a message to indicate that the prices have been saved
print(f'Successfully saved {len(prices)} prices to prices.txt')
