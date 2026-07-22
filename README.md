# OSINT Research

Консольный инструмент для автоматического сбора информации из открытых источников (OSINT)

Поддерживает поиск по:
- **email** – проверка синтаксиса, MX-запись, упоминания в интернете;
- **домену** – WHOIS, DNS-записи, поисковые упоминания;
- **никнейму / имени** – поиск профилей на GitHub, Twitter, Reddit и других сайтах.

Никаких API-ключей не требуется.

## Установка

   bash
   git clone https://github.com/yourname/osint-research.git
   cd osint-research
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install .
python -m src.main <запрос>
