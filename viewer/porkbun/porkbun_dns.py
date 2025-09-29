#!/usr/bin/env python3
# file: porkbun_ddns.py
import os, sys, json, time
from typing import Optional, List
import requests

API_HOST = "https://api-ipv4.porkbun.com/api/json/v3"  # форсируем IPv4
TIMEOUT = 15

API_KEY = os.getenv("PORKBUN_API_KEY")
SECRET_KEY = os.getenv("PORKBUN_SECRET_KEY")
DOMAIN = os.getenv("PORKBUN_DOMAIN", "barsv.com")
SUBDOMAIN = os.getenv("PORKBUN_SUBDOMAIN", "").strip()  # "" => корневая запись
TTL = os.getenv("PORKBUN_TTL", "600")  # мин. и дефолт у Porkbun = 600

def check_env():
    missing = [k for k in ("PORKBUN_API_KEY", "PORKBUN_SECRET_KEY") if not os.getenv(k)]
    if missing:
        print(f"[ERR] Missing env vars: {', '.join(missing)}", file=sys.stderr)
        sys.exit(2)

def porkbun_post(path: str, payload: dict) -> dict:
    url = f"{API_HOST}{path}"
    print(f"[DEBUG] POST {url}")
    print(f"[DEBUG] Payload: {json.dumps({k: v if k not in ('apikey', 'secretapikey') else '***' for k, v in payload.items()})}")
    
    r = requests.post(url, json=payload, timeout=TIMEOUT)
    print(f"[DEBUG] Response status: {r.status_code}")
    print(f"[DEBUG] Response text: {r.text}")
    
    r.raise_for_status()
    data = r.json()
    if data.get("status") != "SUCCESS":
        raise RuntimeError(f"Porkbun API error: {data}")
    return data

def get_public_ipv4() -> str:
    # ping также возвращает ваш IP — удобно для DDNS
    data = porkbun_post("/ping", {"apikey": API_KEY, "secretapikey": SECRET_KEY})
    return data["yourIp"]

def retrieve_a_records(domain: str, subdomain: Optional[str]) -> List[dict]:
    # Try the simpler endpoint first - retrieve all DNS records for the domain
    try:
        data = porkbun_post(f"/dns/retrieve/{domain}", {"apikey": API_KEY, "secretapikey": SECRET_KEY})
        records = data.get("records", [])
        # Filter for A records and optionally by subdomain
        a_records = [r for r in records if r.get("type") == "A"]
        if subdomain:
            a_records = [r for r in a_records if r.get("name") == f"{subdomain}.{domain}"]
        else:
            # For root domain, name should equal domain
            a_records = [r for r in a_records if r.get("name") == domain]
        return a_records
    except Exception as e:
        print(f"[DEBUG] Failed with retrieve endpoint, trying retrieveByNameType: {e}")
        # Fallback to original method
        base = f"/dns/retrieveByNameType/{domain}/A"
        path = base if not subdomain else f"{base}/{subdomain}"
        data = porkbun_post(path, {"apikey": API_KEY, "secretapikey": SECRET_KEY})
        return data.get("records", [])

def edit_a_records(domain: str, subdomain: Optional[str], new_ip: str):
    base = f"/dns/editByNameType/{domain}/A"
    path = base if not subdomain else f"{base}/{subdomain}"
    porkbun_post(path, {
        "apikey": API_KEY,
        "secretapikey": SECRET_KEY,
        "content": new_ip,
        "ttl": TTL
    })

def main():
    check_env()
    
    # Test authentication first
    print(f"[INFO] Testing authentication...")
    try:
        current_ip = get_public_ipv4()
        print(f"[INFO] Authentication successful, public IP: {current_ip}")
    except Exception as e:
        print(f"[ERR] Authentication failed: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"[INFO] Retrieving DNS records for domain: {DOMAIN}, subdomain: '{SUBDOMAIN}'")
    try:
        records = retrieve_a_records(DOMAIN, SUBDOMAIN or None)
        print(f"[DEBUG] Found {len(records)} A records: {records}")
    except Exception as e:
        print(f"[ERR] failed to retrieve DNS records: {e}", file=sys.stderr)
        sys.exit(1)

    # сравним все A-записи (их может быть несколько)
    dns_ips = {rec.get("content") for rec in records} if records else set()

    if dns_ips == {current_ip}:
        print(f"[OK] No change ({DOMAIN} {'@' if SUBDOMAIN=='' else SUBDOMAIN}) stays {current_ip}")
        return

    try:
        edit_a_records(DOMAIN, SUBDOMAIN or None, current_ip)
        print(f"[OK] Updated {DOMAIN} {'@' if SUBDOMAIN=='' else SUBDOMAIN} -> {current_ip}")
    except Exception as e:
        print(f"[ERR] failed to update DNS: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()