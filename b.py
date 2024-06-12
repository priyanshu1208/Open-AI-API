import requests
from bs4 import BeautifulSoup

# Specify the URL
url = "https://business.adobe.com/products/workfront/main.html"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title of the page
    title = soup.title.string
    print("Page Title:", title)

    # Extract other specific elements (e.g., all headings)
    headings = soup.find_all(['h1', 'h2', 'h3'])
    for heading in headings:
        print(heading.name + ': ' + heading.text.strip())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
