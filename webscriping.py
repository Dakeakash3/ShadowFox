import requests
from bs4 import BeautifulSoup

url = "https://www.shadowfox.org.in/"

# Send request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# ---------------------------
# 1. Page Title
# ---------------------------
print("PAGE TITLE:")
print(soup.title.text)
print("-" * 50)

# ---------------------------
# 2. Extract All Headings
# ---------------------------
print("HEADINGS:")
for tag in soup.find_all(["h1", "h2", "h3", "h4"]):
    print(tag.text.strip())
print("-" * 50)

# ---------------------------
# 3. Extract About Section
# ---------------------------
print("ABOUT TEXT:")
about = soup.find_all("p")
for p in about:
    text = p.text.strip()
    if len(text) > 60:
        print(text)
print("-" * 50)

# ---------------------------
# 4. Extract Contact Info
# ---------------------------
print("CONTACT INFO:")
for text in soup.stripped_strings:
    if "@" in text or "+" in text or "Chennai" in text:
        print(text)

# ---------------------------
# 5. Save Full Website Text to File
# ---------------------------
with open("shadowfox_data.txt", "w", encoding="utf-8") as f:
    f.write(soup.get_text())

print("Data saved successfully to shadowfox_data.txt")