#!/usr/bin/env python3

import qrcode
from PIL import Image
from datetime import datetime

# Get input from user
input_URL = input("Enter the URL or text for the QR Code: ")
fill = input("Enter fill color (default: black): ") or "black"
back = input("Enter background color (default: white): ") or "white"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color=fill, back_color=back)

# Optional: Add a logo
add_logo = input("Do you want to add a logo in the center? (yes/no): ").lower()
if add_logo == "yes":
    try:
        logo = Image.open("logo.png")
        img = img.convert("RGBA")
        logo = logo.resize((60, 60))  # Resize logo if needed
        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos, mask=logo)
    except FileNotFoundError:
        print("Logo file not found. Skipping logo addition.")

# Save with timestamped filename
filename = f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
img.save(filename)
print(f"QR code saved as: {filename}")

# Display the image
img.show()
