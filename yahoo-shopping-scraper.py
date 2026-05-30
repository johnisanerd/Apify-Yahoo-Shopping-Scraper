"""
Example: call the Yahoo Shopping API Apify Actor from Python.

Get a free Apify API key at: https://apify.com?fpr=9n7kx3
Set it in a .env file (see .env.example) or export APIFY_API_TOKEN.

The example fetches a single page so the first run is inexpensive. Raise
max_pages when you want more results; each page is billed separately.
"""

import os

from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
if not APIFY_API_TOKEN:
    raise SystemExit(
        "APIFY_API_TOKEN is not set. Copy .env.example to .env and add your key, "
        "or run: export APIFY_API_TOKEN=your_api_key_here"
    )

client = ApifyClient(APIFY_API_TOKEN)

# Inputs are kept small so the first run is inexpensive: one page, 10 results.
run_input = {
    "query": "coffee maker",
    "limit": 10,
    "max_pages": 1,
}

print(f"Searching Yahoo Shopping for: {run_input['query']}")
run = client.actor("johnvc/Yahoo-Shopping-Search-Scraper").call(run_input=run_input)

if run is None:
    raise SystemExit("The Actor run did not start. Check your API token and inputs.")

# One dataset item is returned per page; each page holds a shopping_results list.
for page in client.dataset(run.default_dataset_id).iterate_items():
    metadata = page.get("search_metadata", {})
    products = page.get("shopping_results", [])
    print(
        f"\nPage {page.get('page_number', '?')}: "
        f"{len(products)} products (total found: {metadata.get('total_results', 'n/a')})\n"
    )

    for product in products:
        title = product.get("title", "")
        seller = product.get("seller", "")
        price = product.get("price", "")
        link = product.get("link", "")

        print(f"{product.get('position', '?')}. {title}")
        print(f"   Seller: {seller}")
        print(f"   Price:  {price}")
        print(f"   Link:   {link}")
        print()
