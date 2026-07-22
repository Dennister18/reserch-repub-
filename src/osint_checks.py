import re
import socket
import whois
import dns.resolver
import requests
import validators
from typing import Optional, Dict, List

def is_email(value: str) -> bool:
    return validators.email(value)

def is_domain(value: str) -> bool:
    return validators.domain(value)

def check_email(email: str) -> Dict:
    result = {
        "email": email,
        "valid_syntax": validators.email(email),
        "domain": email.split("@")[1] if "@" in email else None,
        "mx_records": [],
        "mentions": []
    }
    if result["domain"]:
        try:
            answers = dns.resolver.resolve(result["domain"], 'MX')
            result["mx_records"] = [str(r.exchange) for r in answers]
        except Exception:
            pass
    return result

def whois_lookup(domain: str) -> Optional[Dict]:
    try:
        w = whois.whois(domain)
        return {
            "domain": domain,
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
            "name_servers": w.name_servers,
            "country": w.country,
            "org": w.org
        }
    except Exception:
        return {"domain": domain, "error": "Не удалось получить WHOIS"}

def dns_records(domain: str) -> Dict[str, List[str]]:
    records = {}
    for rtype in ['A', 'AAAA', 'MX', 'NS', 'TXT']:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            records[rtype] = [str(a) for a in answers]
        except Exception:
            records[rtype] = []
    return records

def username_search(username: str, max_results: int = 5) -> List[Dict]:
    queries = [
        f'"{username}"',
        f'site:github.com {username}',
        f'site:twitter.com {username}',
        f'site:instagram.com {username}',
        f'site:reddit.com {username}',
    ]
    results = []
    for q in queries:
        results.extend(web_search(q, max_results=2))
    seen = set()
    unique = []
    for r in results:
        if r['url'] not in seen:
            seen.add(r['url'])
            unique.append(r)
    return unique[:max_results]
