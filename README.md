# 🛒 Yahoo Shopping API: Product Listings in Clean JSON

> The efficient, reliable, and developer-friendly way to use the Yahoo Shopping API.

**Actor page:** [apify.com/johnvc/Yahoo-Shopping-Search-Scraper](https://apify.com/johnvc/Yahoo-Shopping-Search-Scraper?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/Yahoo-Shopping-Search-Scraper/input-schema](https://apify.com/johnvc/Yahoo-Shopping-Search-Scraper/input-schema?fpr=9n7kx3)

The Yahoo Shopping API searches Yahoo Shopping and returns clean, structured JSON, one item per page of results. Each item carries the search parameters, search metadata (total results, pages processed), available filters, and a `shopping_results` array where every product includes title, seller, price, product ID, and a direct link. Supports price-range filtering, sorting, merchant and category filtering, and pagination.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Yahoo-Shopping-Scraper.git
   cd Apify-Yahoo-Shopping-Scraper
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
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

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python yahoo-shopping-scraper.py
```

## Why Use This Yahoo Shopping API?

**Structured product data on demand.** Pull titles, sellers, prices, product IDs, and direct links across any keyword in a single call, with no HTML parsing and no browser automation.

**Flexible price filtering.** Set `min_price` and `max_price` to target a price band, then combine with `sort_by` and `order_by` to retrieve the cheapest, the most expensive, or anything in between.

**Merchant and category filtering.** Restrict results to specific sellers with `merchants`, or narrow by category attributes with `category_attr_values`. Each page also returns the available `filters` (such as stores) so you can refine further.

**Configurable pagination.** Control depth with `max_pages`, offset with `start`, and page size with `limit` (up to 60 per page).

**Predictable, pay-per-use pricing.** A small per-run setup fee plus a per-page fee, with no subscription. You control cost with the page limit.

**Easy to automate.** Call it from Python in a few lines, or load it as an MCP tool so assistants like Claude and Cursor can search products for you on demand.

## Features

### Core Capabilities
- **Product search** across Yahoo Shopping by keyword
- **Price-range filtering** with `min_price` and `max_price`
- **Sort and order control** by price, relevancy, popularity, or discount
- **Merchant filtering** to restrict results to specific sellers
- **Category attribute filtering** with `category_attr_values`
- **Pagination control** with `max_pages`, `start`, `limit`, and `page`

### Data Quality
- **One item per page** with a stable structure
- **`shopping_results` array** with title, seller, price, product ID, and link per product
- **Search metadata** (total results, total pages, pages processed) on every item
- **Available filters** returned per page for refinement
- **Consistent JSON** shape across every query

## Usage Examples

### Basic search
```json
{
  "query": "coffee maker",
  "max_pages": 1
}
```

### Price-filtered and sorted
```json
{
  "query": "wireless headphones",
  "min_price": "50.00",
  "max_price": "200.00",
  "sort_by": "price",
  "order_by": "ASC",
  "max_pages": 1
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | `string` | Yes | - | Product search query, e.g. `coffee maker`, `laptop`. |
| `min_price` | `string` | No | `0.00` | Minimum price in USD; `0.00` removes the lower bound. |
| `max_price` | `string` | No | `0.00` | Maximum price in USD; `0.00` removes the upper bound. |
| `sort_by` | `string` | No | - | Sort field: `price`, `relevancy`, `popularity`, or `discountPercentage`. |
| `order_by` | `string` | No | - | Sort direction: `ASC` or `DESC`. |
| `category_attr_values` | `string` | No | - | Category attribute filters, comma-separated. |
| `merchants` | `string` | No | - | Restrict to specific merchant IDs, comma-separated. |
| `start` | `integer` | No | `0` | Offset-based pagination position; cannot combine with `page`. |
| `limit` | `integer` | No | `60` | Results per page (maximum 60). |
| `page` | `integer` | No | - | 1-indexed page number; cannot combine with `start`. |
| `max_pages` | `integer` | No | `1` | Maximum pages to fetch; `0` = unlimited. Each page is billed separately. |
| `output_file` | `string` | No | - | Optional filename to save results. |

## Output Format

A real result for `coffee maker` (one item per page; the `shopping_results` array is trimmed to a single product here, and `filters` lists the available facets).

```json
{
  "search_parameters": { "query": "coffee maker", "limit": 5, "start": 0 },
  "search_metadata": {
    "total_results": 14232,
    "total_pages": 2846,
    "shopping_results_count": 4,
    "pages_processed": 1,
    "max_pages_set": 1,
    "pagination_limit_reached": true
  },
  "search_timestamp": "2026-05-29T11:47:24",
  "page_number": 1,
  "shopping_results": [
    {
      "position": 1,
      "product_id": "00850039439001",
      "link": "https://shopping.yahoo.com/product/00850039439001",
      "title": "SimplyGoodCoffee Coffee Maker/Coffee Machine. 8 Cup Automatic Drip Pour Over Coffee Brewer. Easy To Use, Durable Stainless, Gold Cup Standard",
      "seller": "Amazon",
      "price": 199.95
    }
  ],
  "filters": [
    { "key": "stores", "values": [ { "id": "66ea567a-c987-4c2e-a2ff-02904efde6ea", "name": "Amazon" } ] }
  ]
}
```

Each page item echoes the `search_parameters` you sent, reports `search_metadata` (total results and pages processed), lists every product in `shopping_results` with its position, title, seller, price, product ID, and link, and returns the available `filters` (such as stores) for further refinement.

---

## Use as an MCP tool

You can load the Yahoo Shopping API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/Yahoo-Shopping-Search-Scraper
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Yahoo Shopping API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/Yahoo-Shopping-Search-Scraper"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Yahoo Shopping API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/Yahoo-Shopping-Search-Scraper"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/Yahoo-Shopping-Search-Scraper" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Yahoo Shopping API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/Yahoo-Shopping-Search-Scraper`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/Yahoo-Shopping-Search-Scraper`, using OAuth when prompted.
5. Ask Claude to run the Yahoo Shopping API.

Open Claude on the web: https://claude.ai

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/Yahoo-Shopping-Search-Scraper"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/Yahoo-Shopping-Search-Scraper",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Yahoo Shopping API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/Yahoo-Shopping-Search-Scraper`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Yahoo Shopping API to power price comparison, competitor research, and e-commerce market analysis with reliable, structured results.*

Last Updated: 2026.06.14
