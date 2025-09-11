import qrcode

data = input("Enter the text or URL: ").strip()
fileName = input("Enter the filename: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fil_color='black', back_color='white')
image.save(fileName)

print(f"QR saved as {fileName}")