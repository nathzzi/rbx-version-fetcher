# Created by Nathan on June 26, 2025
# Thanks to APKCombo for making this possible

import requests
from bs4 import BeautifulSoup
import re

def fetchRobloxVersion():
    url = "https://apkcombo.com/roblox/com.roblox.client/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    links = soup.find_all("a", href=True)
    for link in links:
        href = link["href"]
        if href.endswith("/roblox/com.roblox.client/download/apk"):
            text = link.get_text(strip=True)
            match = re.match(r"([\d\.]+)\s*\((\d+)\)", text)
            if match:
                ver, code = match.groups()
                return ver, code

    return None, None

if __name__ == "__main__":
    version, version_code = fetchRobloxVersion()
    print("Latest roblox version fetched:", version)
    print("Latest roblox version code fetched:", version_code)
