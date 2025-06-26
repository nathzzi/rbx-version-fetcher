# Created by Nathan on June 26, 2025
# Thanks to APKCombo for making this possible

# Changelogs 06/27/25
# - Added VNG version support

import requests
from bs4 import BeautifulSoup
import re

def fetchRobloxVersion(url_suffix):
    url = f"https://apkcombo.com/{url_suffix}/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    links = soup.find_all("a", href=True)
    for link in links:
        href = link["href"]
        if href.endswith("/download/apk"):
            text = link.get_text(strip=True)
            match = re.match(r"([\d\.]+)\s*\((\d+)\)", text)
            if match:
                ver, code = match.groups()
                return ver, code

    return None, None

if __name__ == "__main__":
    global_version, global_code = fetchRobloxVersion("roblox/com.roblox.client")
    print(f"{'Latest Roblox Global version fetched:'} {global_version}")
    print(f"{'Latest Roblox Global version code fetched:'} {global_code}")

    print(f"{'-' * 50}")

    vn_version, vn_code = fetchRobloxVersion("roblox-vn/com.roblox.client.vnggames")
    print(f"{'Latest Roblox VNG version fetched:'} {vn_version}")
    print(f"{'Latest Roblox VNG version code fetched:'} {vn_code}")
