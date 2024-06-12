from googlesearch import search
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Function to fetch and clean webpage content
def fetch_and_clean_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Retry mechanism
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))

    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        soup = BeautifulSoup(response.content, 'html.parser')
        clean_text = soup.get_text(separator='\n', strip=True)
        return clean_text
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

query = "Adobe Workfront"

# Fetch top search results from Google
search_results = search(query, num_results=1)  # Adjust num_results and pause as needed

# Print the search results
for i, result in enumerate(search_results, start=1):
    print(f"Result {i}: {result}")
    clean_text = fetch_and_clean_url(result)
    print(clean_text[:500])  # Print the first 500 characters for inspection

