"""
Yahoo Shopping Scraper: A Quick Start Example
See more at: https://apify.com/johnvc/Yahoo-Shopping-Search-Scraper?fpr=9n7kx3
Input schema: https://apify.com/johnvc/Yahoo-Shopping-Search-Scraper/input-schema?fpr=9n7kx3

This script demonstrates how to scrape product listings from Yahoo Shopping
using the Yahoo Shopping Search Scraper on Apify. Returns product names,
prices, seller info, ratings, and descriptions as structured JSON.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input
run_input = {
    "query": "wireless headphones",
    "min_price": "50.00",
    "max_price": "200.00",
    "sort_by": "price",
    "max_pages": 2,
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/Yahoo-Shopping-Search-Scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
