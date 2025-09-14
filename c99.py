import random
import sys
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
from time import time
import re

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
]

EXCLUDE_TEXTS = {"whois check", "download json", "download csv"}
ip_regex = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")

def get_urls(domain,max_minutes=4):
    print(f"[*] Running c99 for {domain} 🔍")
    today = datetime.now()
    start_time = time()
    results = []

    while True:
        if time() - start_time > max_minutes* 60:
            break
        date_str = today.strftime("%Y-%m-%d")
        url = f"https://subdomainfinder.c99.nl/scans/{date_str}/{domain}"
        headers = {"User-Agent": random.choice(USER_AGENTS)}

        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code != 200:
                today -= timedelta(days=1)
                continue
        except:
            today -= timedelta(days=1)
            continue

        soup = bs(res.content, "html.parser")
        found = False
        for div in soup.select("div.well.mt-5"):
            for a in div.select("a"):
                text = a.get_text(strip=True)
                if text.lower() not in EXCLUDE_TEXTS and text.lower() != "none" and not ip_regex.match(text):
                    results.append(text)
                    found = True

        if found:
            break
        else:
            today -= timedelta(days=1) 
    return list(set(results))

print(get_urls(sys.argv[1]))
