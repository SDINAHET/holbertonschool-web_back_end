#!/usr/bin/env python3
"""Unit tests for Task 5 (web cache)."""

import threading
import time
import unittest
from http.server import HTTPServer, BaseHTTPRequestHandler

import redis
from web import get_page


class _SilentHandler(BaseHTTPRequestHandler):
    CONTENT = b"<html><body>Hello Cache</body></html>"

    def do_GET(self):  # noqa: N802 (keep standard name)
        body = self.CONTENT
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        # Silence the default logging
        return


class TestWebCache(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start a small HTTP server on a free port
        cls.httpd = HTTPServer(("127.0.0.1", 0), _SilentHandler)
        cls.port = cls.httpd.server_address[1]
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.thread.join()

    def setUp(self):
        self.r = redis.Redis()
        self.r.flushdb()
        self.url = f"http://127.0.0.1:{self.port}/"

    def test_cache_and_counter(self):
        # First call -> fetch and cache
        html1 = get_page(self.url)
        self.assertIn("Hello Cache", html1)
        self.assertEqual(self.r.get(f"count:{self.url}"), b"1")

        # Check TTL is set (0 < ttl <= 10)
        ttl1 = self.r.ttl(self.url)
        self.assertGreater(ttl1, 0)
        self.assertLessEqual(ttl1, 10)

        # Second call -> cache hit, counter increments
        html2 = get_page(self.url)
        self.assertEqual(html1, html2)
        self.assertEqual(self.r.get(f"count:{self.url}"), b"2")

        # TTL should remain > 0 (we do not refresh TTL on hits)
        ttl2 = self.r.ttl(self.url)
        self.assertGreater(ttl2, 0)

        # After expiration, cache miss occurs again
        time.sleep(11)
        html3 = get_page(self.url)
        self.assertIn("Hello Cache", html3)
        self.assertEqual(self.r.get(f"count:{self.url}"), b"3")  # counter increments every call


if __name__ == "__main__":
    unittest.main(verbosity=2)
