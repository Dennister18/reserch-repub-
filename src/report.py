from datetime import datetime
from typing import Dict, Any

def build_report(query: str, query_type: str, data: Dict[str, Any]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"# OSINT-отчёт: {query}\n"
    report += f"*Сгенерирован: {timestamp}*\n"
    report += f"*Тип запроса: {query_type}*\n\n"

    if query_type == "email":
        report += "## 📧 Email\n"
        report += f"- Синтаксис корректен: {'✅' if data['valid_syntax'] else '❌'}\n"
        report += f"- Домен: {data['domain']}\n"
        if data.get('mx_records'):
            report += f"- MX-записи: {', '.join(data['mx_records'])}\n"
        if data.get('mentions'):
            report += "\n### search в интернете\n"
            for m in data['mentions']:
                report += f"- [{m['title']}]({m['url']})\n"

    elif query_type == "domain":
        report += "## 🌐 Домен\n"
        whois_data = data.get('whois', {})
        dns_data = data.get('dns', {})
        report += "### WHOIS\n"
        for key, val in whois_data.items():
            report += f"- {key}: {val}\n"
        report += "\n### DNS-записи\n"
        for rtype, values in dns_data.items():
            if values:
                report += f"- {rtype}: {', '.join(values)}\n"

    elif query_type == "username":
        report += "## 👤 Никнейм / Имя\n"
        if data.get('mentions'):
            report += f"Найдено {len(data['mentions'])} упоминаний:\n"
            for m in data['mentions']:
                report += f"- [{m['title']}]({m['url']}) — {m['snippet']}\n"
        else:
            report += "Упоминаний не найдено.\n"

    report += f"\n---\n*Отчёт создан инструментом OSINT Research*"
    return report
