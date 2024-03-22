import qrcode
import os

if not os.path.exists("qr_codes"):
    os.makedirs("qr_codes")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data("Hello, world!")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

img.save("hello_world.png")
