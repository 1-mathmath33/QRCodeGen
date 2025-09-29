from qrmaker.orchestrator import generate_qr
# Input data
data = {"url": "chatgpt.com"}

# Generate PNG bytes
png_bytes = generate_qr("url", data, size=400, error="M")

# Save to file
with open("chatgpt.png", "wb") as f:
    f.write(png_bytes)

print("QR code written to chatgpt.png ({} bytes)".format(len(png_bytes)))
