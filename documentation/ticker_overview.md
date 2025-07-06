# Ticker Overview

**Endpoint:** `GET /v3/reference/tickers/{ticker}`

Retrieve comprehensive details for a single ticker supported by Polygon.io. This endpoint provides an in-depth look into a company’s fundamental attributes:
- Primary exchange  
- Identifiers (CIK, Composite FIGI, Share Class FIGI)  
- Market capitalization  
- Industry classification  
- Key dates  
- Branding assets (e.g., logos, icons)

**Use Cases:**  
- Company research  
- Data integration  
- Application enhancement  
- Due diligence & compliance

---

## Path Parameters

| Name   | Type   | Required | Description                        |
|--------|--------|----------|------------------------------------|
| ticker | string | ✅        | The ticker symbol of the asset.    |

---

## Query Parameters

| Name | Type   | Required | Description |
|------|--------|----------|-------------|
| date | string | ❌        | Specify a date to retrieve ticker info valid at that time (e.g., for SEC filings). Defaults to the most recent available. |

📌 *Example:* For an SEC filing submitted by AAPL on `2019-07-31` (report date `2019-06-29`), querying with `date=2019-06-29` would include that filing.

---

## Response Attributes

### Top-Level

| Name        | Type    | Description                                      |
|-------------|---------|--------------------------------------------------|
| count       | integer | Total number of results.                         |
| request_id  | string  | Server-assigned request ID.                      |
| results     | object  | Ticker details object.                           |

---

### `results` Object Fields

#### General Info

| Name          | Type    | Description |
|---------------|---------|-------------|
| ticker        | string  | The trading symbol of the asset. |
| name          | string  | Asset/company name. |
| description   | string  | Company overview. |
| type          | string  | Type of asset (e.g., stock, ETF, crypto). |
| status        | string  | Status of the request/response. |
| active        | boolean | Whether the asset is actively traded. |
| locale        | enum    | `us`, `global` |
| market        | enum    | `stocks`, `crypto`, `fx`, `otc`, `indices` |
| market_cap    | number  | Market cap (price × weighted shares). |
| currency_name | string  | Trading currency name. |
| homepage_url  | string  | Company website URL. |
| phone_number  | string  | Company phone number. |
| list_date     | string  | First listing date (`YYYY-MM-DD`). |
| delisted_utc  | string  | Date of delisting (if any). |

#### Identifiers

| Name                            | Type    | Description |
|---------------------------------|---------|-------------|
| cik                             | string  | SEC Central Index Key. |
| composite_figi                  | string  | Composite FIGI. |
| share_class_figi                | string  | Share class FIGI. |
| share_class_shares_outstanding | number  | Shares outstanding for the share class. |
| weighted_shares_outstanding    | number  | Adjusted total outstanding shares. |
| ticker_root                    | string  | Root symbol (e.g., `BRK` for `BRK.A`). |
| ticker_suffix                  | string  | Suffix (e.g., `A` in `BRK.A`). |

#### Address

| Name        | Type   | Description |
|-------------|--------|-------------|
| address     | object | Company address object. |
| address1    | string | Street address line 1. |
| address2    | string | Street address line 2 (optional). |
| city        | string | City. |
| state       | string | State/province. |
| postal_code | string | ZIP/postal code. |

#### Branding

| Name      | Type   | Description |
|-----------|--------|-------------|
| branding  | object | Contains URLs for branding images. |
| icon_url  | string | URL to company's icon (small/square). |
| logo_url  | string | URL to company's full logo. |

🔐 *Note: Accessing branding URLs requires an API key. See the "Authentication" section.*

#### Classification

| Name            | Type   | Description |
|-----------------|--------|-------------|
| sic_code        | string | Standard Industrial Classification (SIC) code. |
| sic_description | string | Description of the SIC code. |
| total_employees | number | Approximate number of company employees. |
| primary_exchange | string | ISO code of the main exchange. |
| round_lot       | number | Round lot size (standard trading unit). |
