import requests
from bs4 import BeautifulSoup


url = 'https://example.com'


response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    page_title = soup.title.string if soup.title else 'No title found'
    print(f"Page Title: {page_title}")


    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    print("\nHeadings on the page:")
    for heading in headings:
        print(heading.get_text(strip=True))
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")



