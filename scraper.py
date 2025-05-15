import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "http://quotes.toscrape.com"

def scrape():
    url = BASE_URL
    quotes = []
    authors_info = {}

    while url:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            break

        soup = BeautifulSoup(response.text, "lxml")
        quote_elements = soup.select(".quote")

        for quote_elem in quote_elements:
            text = quote_elem.select_one(".text").get_text()
            author = quote_elem.select_one(".author").get_text()
            tags = [tag.get_text() for tag in quote_elem.select(".tags .tag")]
            quotes.append({"tags": tags, "author": author, "quote": text})

            if author not in authors_info:
                author_link = quote_elem.select_one(".author + a")['href']
                try:
                    author_page = requests.get(f"{BASE_URL}{author_link}", timeout=10)
                    author_page.raise_for_status()
                    author_soup = BeautifulSoup(author_page.text, "html.parser")

                    fullname = author
                    born_date = author_soup.select_one(".author-born-date").get_text()
                    born_location = author_soup.select_one(".author-born-location").get_text()
                    description = author_soup.select_one(".author-description").get_text().strip()

                    authors_info[author] = {
                        "fullname": fullname,
                        "born_date": born_date,
                        "born_location": born_location,
                        "description": description,
                    }
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching author page for {author}: {e}")

        next_btn = soup.select_one(".next a")
        url = f"{BASE_URL}{next_btn['href']}" if next_btn else None

    # Save to JSON files
    with open("quotes.json", "w", encoding="utf-8") as fq:
        json.dump(quotes, fq, ensure_ascii=False, indent=2)

    with open("authors.json", "w", encoding="utf-8") as fa:
        json.dump(list(authors_info.values()), fa, ensure_ascii=False, indent=2)

    print("✅ Scraping completed. Files saved: quotes.json and authors.json")

if __name__ == "__main__":
    scrape()
