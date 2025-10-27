# filename: build_qrcode_min.py
import sys
import urllib.request

from rjsmin import jsmin  # type: ignore[import]

SRC_URL = "https://raw.githubusercontent.com/davidshimjs/qrcodejs/master/qrcode.js"
OUT_FILE = "qrcode.min.js"


def main():
    print(f"Downloading {SRC_URL} ...")
    with urllib.request.urlopen(SRC_URL) as resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status}")
        src = resp.read().decode("utf-8")

    print("Minifying...")
    minified = jsmin(src)

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(minified)

    print(f"Wrote {OUT_FILE} ({len(minified) / 1024:.1f} KB)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
