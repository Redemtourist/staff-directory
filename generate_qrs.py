import qrcode
import os

# Base URL for all staff pages
base_url = "https://redemptourist.github.io/staff-directory/staff/"

# Ensure assets/qr folder exists
os.makedirs("assets/qr", exist_ok=True)

# Loop through all staff markdown files
for file in os.listdir("_staff"):
    if file.endswith(".md"):
        slug = file.replace(".md", "")
        url = base_url + slug + "/"
        img = qrcode.make(url)
        img.save(f"assets/qr/{slug}.png")
        print(f"Generated QR for {slug}")

