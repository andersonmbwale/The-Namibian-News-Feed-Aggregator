import requests
from bs4 import BeautifulSoup

# Define the base url of the website
base_url = "https://www.namibian.com.na"

# Define an empty list to store the news articles
news_list = []

# Make a request to the website and get the html content
response = requests.get(base_url)
html = response.text

# Parse the html content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all the div elements that have the class "news-item"
news_items = soup.find_all("div", class_="news-item")

# Loop through each news item
for news_item in news_items:
    # Find the link, title and summary of the news article
    link = base_url + news_item.find("a")["href"]
    title = news_item.find("h2").text.strip()
    summary = news_item.find("p").text.strip()

    # Create a dictionary with the link, title and summary
    news_dict = {"link": link, "title": title, "summary": summary}

    # Append the dictionary to the news list
    news_list.append(news_dict)

# Print the news list
print(news_list)
