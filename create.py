import os
from PIL import Image
import shutil

print("Delete target folder")
shutil.rmtree("icon.iconset")
print("Create target folder")
os.mkdir("icon.iconset")

targets = [
    ((1024, 1024), "icon_1024x1024.png"),
    ((128, 128), "icon_128x128@2x.png"),
    ((16, 16), "icon_16x16@2x.png"),
    ((256, 256), "icon_256x256.png"),
    ((256, 256), "icon_256x256@2x.png"),
    ((32, 32), "icon_32x32.png"),
    ((32, 32), "icon_32x32@2x.png"),
    ((512, 512), "icon_512x512.png"),
    ((512, 512), "icon_512x512@2x.png"),
    ((64, 64), "icon_64x64.png"),
]

for x in targets:
    print(f"Create {x[1]}")
    im = Image.open("logo.png")  # has to be a 1024x1024 PNG
    im.thumbnail(x[0], Image.ANTIALIAS)
    im.save(f"icon.iconset/{x[1]}", "PNG")

try:
    print("Remove icns")
    os.remove("icon.icns")
except:
    pass  # if icons.icns did not exist, an error is thrown. Ignore ita

print("Create icns")
os.system("iconutil -c icns icon.iconset")
