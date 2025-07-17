# mimicpy

Mimic-style browser header generator in Python, inspired by [mimic (Go)](https://github.com/saucesteals/mimic).

Generates realistic HTTP headers (like `User-Agent`, `Sec-CH-UA`, etc.) to emulate Chrome-based browser behavior. Useful for creating consistent and randomized client fingerprint headers.

---

## 📦 Installation

```bash
pip install git+https://github.com/Anibal98-GH/mimicpy.git
```

---

## 🚀 Usage

```python
from mimicpy import Mimic

mimic = Mimic()

print(mimic.UserAgent)
print(mimic.SecChUa)
print(mimic.SecChUaFullVersionList)
print(mimic.SecChUaFullVersion)

```


