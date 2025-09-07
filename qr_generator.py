import qrcode

# 🔗 Replace this with your Streamlit Cloud link
url = "https://events-relational-algebra-app-4dhnan75tqisyvz4pzcizp.streamlit.app/"

# Generate QR code
qr = qrcode.make(url)

# Save as PNG
qr.save("Event1_app_qr.png")

print("✅ QR Code saved as Event1_app_qr.png")
print("Scan it with any device to open the app.")
