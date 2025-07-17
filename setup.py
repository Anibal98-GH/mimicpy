from setuptools import setup, find_packages

setup(
    name="mimicpy",
    version="0.1.0",
    packages=find_packages(),
    description="Python header generator inspired by mimic (Go)",
    author="TuNombre",
    author_email="tucorreo@example.com",
    url="https://github.com/tuusuario/mimicpy",  # reemplaza con tu repo real
    keywords=["mimic", "headers", "browser", "anti-bot", "fingerprint", "tls"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
    ],
    python_requires=">=3.6",
)
