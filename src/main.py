import sys
import os
from datetime import datetime
from src.search import web_search
from src.osint_checks import is_email, is_domain, check_email, whois_lookup, dns_records, username_search
from src.report import build_report

def determine_type(query: str) -> str:
    if is_email(query):
        return "email"
    elif is_domain(query):
        return "domain"
    else:
        return "username"

def run_osint(query: str) -> str:
    qtype = determine_type(query)
    print(f"🔍 Определён тип запроса: {qtype}")

    data = {}

    if qtype == "email":
        print("📧 Проверка email...")
        data = check_email(query)
        print("🌐 Поиск упоминаний email...")
        data['mentions'] = web_search(query, max_results=3)

    elif qtype == "domain":
        print("🌐 WHOIS-запрос...")
        data['whois'] = whois_lookup(query)
        print("📡 DNS-записи...")
        data['dns'] = dns_records(query)
        print("🔎 Поиск упоминаний домена...")
        data['mentions'] = web_search(query, max_results=3)

    elif qtype == "username":
        print("🔎 Поиск упоминаний никнейма...")
        data['mentions'] = username_search(query, max_results=6)

    report = build_report(query, qtype, data)

    safe_query = "".join(c if c.isalnum() or c in " _-" else "_" for c in query)[:50]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"osint_{safe_query}_{timestamp}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    return filename

def main():
    if len(sys.argv) < 2:
        print("Использование: osint-research <запрос>")
        print("Примеры:")
        print("  osint-research example@mail.com")
        print("  osint-research example.com")
        print("  osint-research username123")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    try:
        filename = run_osint(query)
        print(f" Отчёт сохранён: {filename}")
    except Exception as e:
        print(f" Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
