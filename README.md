**mimicpy** is a lightweight Python library that generates realistic HTTP headers to mimic Chrome-based browser behavior.

It is inspired by the `mimic` library in Go and is designed to help bypass bot detection systems such as Akamai, DataDome, and Cloudflare by emulating real-world browser fingerprinting techniques.

It includes accurate generation of:
- `User-Agent`
- `Sec-CH-UA` (brands)
- `Sec-CH-UA-Full-Version`, `Sec-CH-UA-Mobile`, etc.
- Chrome version randomization
- Greased brand positioning (per Chromium spec)

Ideal for use with `requests`, `tls_client`, or any HTTP client in Python.
