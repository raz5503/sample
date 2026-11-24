
import requests

SOURCE_URL = "https://raw.githubusercontent.com/ahan443/FreeHunter/refs/heads/main/Boss.m3u"

response = requests.get(SOURCE_URL, timeout=30)
response.raise_for_status()

lines = response.text.splitlines()

output = ["#EXTM3U"]

for line in lines:
    line = line.strip()

    if line and line != "#EXTM3U":
        output.append(line)

with open("1.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(output) + "\n")

print("1.m3u updated successfully!")
