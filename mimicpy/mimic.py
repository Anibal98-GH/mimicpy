import random

greasyorders = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

greasy_chars = [" ", "(", ":", "-", ".", "/", ")", ";", "=", "?", ""]
greasy_versions = ["8", "99", "24"]
chrome_versions = [
    "120",
    "121",
    "122",
    "123",
    "124",
    "125",
    "126",
    "127",
    "128",
    "129",
    "130",
    "131",
    "132",
    "133",
    "134",
    "135",
    "136",
    "137",
    "138",
]


def formatBrand(brand, version):
    return f'"{brand}";v="{version}"'


def greasedBrand(seed):
    seedInt = int(seed)
    if seedInt >= 105:
        greasy1 = greasy_chars[seedInt % len(greasy_chars)]
        greasy2 = greasy_chars[(seedInt + 1) % len(greasy_chars)]
        brand = f"Not{greasy1}A{greasy2}Brand"
        version = greasy_versions[seedInt % len(greasy_versions)]
        return formatBrand(brand, version)
    return ""


def generateSecChUaFullVersionList(greased, majorVersion, fullVersion):
    seedInt = int(majorVersion)
    greasedVersion = f"{greasy_versions[seedInt % len(greasy_versions)]}.0.0.0"

    for i, b in enumerate(greased):
        if "Not" in b:
            greased[i] = b.replace(
                f'v="{greasy_versions[seedInt % len(greasy_versions)]}"',
                f'v="{greasedVersion}"',
            )
        else:
            greased[i] = b.replace(f'v="{majorVersion}"', f'v="{fullVersion}"')

    return ", ".join(greased)


class Mimic:
    def __init__(self, force_version=None):
        majorVersion = (
            force_version if force_version else random.choice(chrome_versions)
        )
        fullVersion = (
            f"{majorVersion}.0.{random.randrange(0, 9999)}.{random.randrange(0, 999)}"
        )
        order = random.choice(greasyorders)
        greased = [""] * 3

        greased[order[0]] = greasedBrand(majorVersion)
        greased[order[1]] = formatBrand("Chromium", majorVersion)
        greased[order[2]] = formatBrand("Google Chrome", majorVersion)

        self.UserAgent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{majorVersion}.0.0.0 Safari/537.36"
        self.SecChUa = ", ".join(greased)
        self.SecChUaFullVersionList = generateSecChUaFullVersionList(
            greased.copy(), majorVersion, fullVersion
        )
        self.SecChUaFullVersion = f'"{fullVersion}"'
        self.SecChUaMobile = "?0"
        self.SecChUaModel = ""
        self.SecChUaArch = "x86"
        self.SecChUaPlatform = "Windows"
        self.MajorVersion = f"{majorVersion}.0.0.0"
