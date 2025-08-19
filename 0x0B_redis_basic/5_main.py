#!/usr/bin/env python3
from web import get_page
import redis, time

r = redis.Redis()
url = "http://slowwly.robertomurray.co.uk/delay/2000/url/https://example.org/"

print("First call (should fetch)...")
html1 = get_page(url)
print("len(html1):", len(html1))
print("count:", r.get(f"count:{url}"))

print("Second call (should come from cache)...")
html2 = get_page(url)
print("len(html2):", len(html2))
print("count:", r.get(f"count:{url}"))
print("ttl now:", r.ttl(url))
