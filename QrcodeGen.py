import qrcode

url = input("Enter The url: ").strip()
file_path = "/storage/emulated/0/MyGit/qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)