# 🛒 Yahoo Shopping Scraper: Scrape Yahoo Shopping Product Listings with Python

> **The most efficient, reliable, and developer-friendly Yahoo Shopping scraper**

**Actor page:** [apify.com/johnvc/Yahoo-Shopping-Search-Scraper](https://apify.com/johnvc/Yahoo-Shopping-Search-Scraper?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/Yahoo-Shopping-Search-Scraper/input-schema](https://apify.com/johnvc/Yahoo-Shopping-Search-Scraper/input-schema?fpr=9n7kx3)

Scrape Yahoo Shopping product listings with Python using the [Yahoo Shopping Search Scraper on Apify](https://apify.com/johnvc/Yahoo-Shopping-Search-Scraper?fpr=9n7kx3). Returns structured JSON with product names, prices, seller info, ratings, and descriptions - with support for price range filters, sort options, merchant filtering, and pagination.

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Yahoo-Shopping-Scraper.git
   cd Apify-Yahoo-Shopping-Scraper
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you don't have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python yahoo-shopping-scraper.py
   ```

### Alternative: Set API Key Directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python yahoo-shopping-scraper.py
```

## 🌟 Why Use This Yahoo Shopping Scraper?

The [Yahoo Shopping scraper on Apify](https://apify.com/johnvc/Yahoo-Shopping-Search-Scraper?fpr=9n7kx3) delivers structured product data directly from Yahoo Shopping search results - a large and often-overlooked product index with strong coverage of independent merchants, competitive pricing, and product categories not always prominent on other platforms.

**Price Intelligence at Scale**: Pull prices, seller names, and product details across any category or keyword in a single API call. Whether you are building a price comparison tool, monitoring competitor listings, or researching market rates, the scraper returns exactly the fields you need - no HTML parsing, no browser automation required.

**Flexible Price Filtering**: Set `min_price` and `max_price` to narrow results to a specific price band. Combined with `sort_by` and `order_by`, you can retrieve the cheapest listings, the most expensive, or anything in between - making it easy to segment product data by tier for analysis or display.

**Merchant and Category Filtering**: Use the `merchants` parameter to restrict results to specific sellers, or `category_attr_values` to narrow by product category attributes. This makes the scraper useful for vendor-specific research, niche category analysis, and building curated product datasets.

**Configurable Pagination**: Set `max_pages` to control how deeply you scrape. The `start` and `limit` parameters give additional control over result offsets and page size, useful when integrating results into a paginated display or resuming an interrupted run.

**Pay-Per-Event, No Subscriptions**: Pricing is $0.01 per run plus $0.02 per page scraped. You pay only for what you use - no monthly minimums, no seat licenses. Scale up for large catalog sweeps and back down for spot checks.

**Production-Ready JSON Output**: Every product result includes a consistent set of fields across all merchants and categories. Load directly into a database, feed into a price tracking pipeline, or pass to an LLM for product comparison and summarization - no transformation layer needed.

## 🎯 Common Use Cases for Yahoo Shopping Data

**Price Comparison**: Collect product prices across sellers on Yahoo Shopping and compare against other platforms to identify the best deals or monitor market pricing trends.

**Competitor Research**: Track what products competitors are listing, at what prices, and with what descriptions - updated on demand without manual browsing.

**Product Catalog Enrichment**: Source product names, descriptions, images, and pricing data to enrich an internal catalog or populate a comparison site.

**E-commerce Market Research**: Analyze product availability, pricing distributions, and merchant concentration in any niche or category.

**Deal Monitoring**: Set up periodic scrapes for specific keywords with price filters to catch deals as they appear on Yahoo Shopping.

**LLM Product Analysis**: Feed structured product listings into a language model for automated summarization, comparison, or recommendation generation.

## ⚡ Features

### Core Capabilities
- **Yahoo Shopping Index**: Queries Yahoo Shopping's full product index across all merchants
- **Price Range Filtering**: Set `min_price` and `max_price` to target a specific price band
- **Sort and Order Control**: Sort by price, relevance, or other fields in ascending or descending order
- **Merchant Filtering**: Restrict results to specific sellers using the `merchants` parameter
- **Category Attribute Filtering**: Narrow by product category attributes with `category_attr_values`
- **Configurable Pagination**: Control depth with `max_pages`, offset with `start`, and page size with `limit`

### Data Quality
- **Consistent JSON Schema**: Every product result shares the same field structure regardless of merchant
- **Seller Attribution**: Merchant name and seller info included on every result
- **Ratings and Reviews**: Product rating data where available
- **Full Descriptions**: Complete product description text, not just titles
- **Per-Page Dataset Items**: Results pushed as discrete items for accurate billing and easy processing

## 📖 Usage Examples

### Basic Search: Scrape Yahoo Shopping for Any Product

```json
{
  "query": "wireless headphones",
  "max_pages": 1
}
```

### Advanced Search: Price-Filtered and Sorted Results

Retrieve wireless headphones priced between $50 and $200, sorted by price ascending, across 2 pages.

```json
{
  "query": "wireless headphones",
  "min_price": "50.00",
  "max_price": "200.00",
  "sort_by": "price",
  "order_by": "asc",
  "max_pages": 2
}
```

## 🔍 Input Parameters

Full input schema reference: [apify.com/johnvc/Yahoo-Shopping-Search-Scraper/input-schema](https://apify.com/johnvc/Yahoo-Shopping-Search-Scraper/input-schema?fpr=9n7kx3)

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | `str` | YES | - | Product search query |
| `min_price` | `str` | no | `"0.00"` | Minimum price filter |
| `max_price` | `str` | no | `"0.00"` | Maximum price (0 = no limit) |
| `sort_by` | `str` | no | - | Sort field (e.g. `"price"`) |
| `order_by` | `str` | no | - | Sort direction (e.g. `"asc"`, `"desc"`) |
| `category_attr_values` | `str` | no | - | Category attribute filters |
| `merchants` | `str` | no | - | Filter by merchant names |
| `start` | `int` | no | `0` | Result offset |
| `limit` | `int` | no | `60` | Results per page |
| `page` | `int` | no | - | Page number |
| `max_pages` | `int` | no | `1` | Maximum pages to scrape |
| `output_file` | `str` | no | - | Optional output filename |

## 📊 Output Format

Each run returns a dataset of structured JSON objects. Sample output:

```json
{
  "query": "wireless headphones",
  "min_price": "50.00",
  "max_price": "200.00",
  "max_pages": 2,
  "pages_processed": 2,
  "products": [
    {
      "position": 1,
      "title": "Sony WH-1000XM5 Wireless Noise Canceling Headphones",
      "link": "https://shopping.yahoo.com/product/example-1",
      "price": "$279.99",
      "price_raw": 279.99,
      "merchant": "Best Buy",
      "rating": 4.8,
      "review_count": 2341,
      "description": "Industry-leading noise cancellation with 30-hour battery life and multipoint connection for pairing with two devices simultaneously.",
      "image": "https://example.com/image1.jpg",
      "brand": "Sony"
    },
    {
      "position": 2,
      "title": "Bose QuietComfort 45 Bluetooth Wireless Headphones",
      "link": "https://shopping.yahoo.com/product/example-2",
      "price": "$229.00",
      "price_raw": 229.00,
      "merchant": "Amazon",
      "rating": 4.6,
      "review_count": 1876,
      "description": "High-fidelity audio with world-class noise cancellation. Up to 24 hours of battery life with 2.5 hour charge time.",
      "image": "https://example.com/image2.jpg",
      "brand": "Bose"
    }
  ],
  "search_metadata": {
    "total_results_found": 312,
    "pages_processed": 2
  }
}
```

---

[**Made with love**](https://apify.com/johnvc?fpr=9n7kx3)

*Transform your data collection with the most reliable and efficient scraper on the market.*

Last Updated: 2026.05.29
