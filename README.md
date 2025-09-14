# 🌐 Subdomain Finder (using c99)

This Python script scraps subdomains from [c99.nl subdomain finder](https://subdomainfinder.c99.nl/) for a given domain.  
It automatically checks scan pages (by date) until it finds results, filtering out irrelevant entries (like `whois check`, `download json`, `download csv`, IP addresses, etc.).

---

## 🚀 Features
- Rotates User-Agents for requests.
- Goes back in time (previous days) until subdomains are found.
- Filters out unwanted or invalid results.
- Returns unique subdomains for the target domain.

---

## 📦 Requirements

Install dependencies with pip:

```bash
pip install requests beautifulsoup4
```


## Usage

```bash
python3 c99.py example.com
```
