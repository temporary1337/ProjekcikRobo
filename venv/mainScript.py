#potrzeba bilbioteki czy tam kompilatora PILLOW do obrazow
#https://pillow.readthedocs.io/en/5.1.x/ tu jest info
from PIL import Image, ImageFont, ImageDraw
snap = Image.open("Mox_Snapshot.png")
mox = Image.open("Mox_Baza.png")
karn = Image.open("Karn_baza.png")

snap_width, snap_height = snap.size
print ("snap width - ", snap_width, " and height - ", snap_height)

mox_width, mox_height = mox.size
print ("mox width - ", mox_width, " and height - ", mox_height)

karn_width, karn_height = karn.size
print ("karn width - ", karn_width, " and height - ", karn_height)

snap.show()
size = 223, 311
snap.thumbnail(size)
snap.show()