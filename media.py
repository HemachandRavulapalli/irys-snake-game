import urllib.request
import os
from PIL import Image


urls = [
    "https://irysarcade.xyz/assets/media-pack/snake/Bottom_Left.jpg",
    "https://irysarcade.xyz/assets/media-pack/snake/Down.jpg",
    "https://irysarcade.xyz/assets/media-pack/snake/Horizontal_.jpg",
    "https://irysarcade.xyz/assets/media-pack/snake/Left.jpg",
    "https://irysarcade.xyz/assets/media-pack/snake/Left_Top.jpg",
    "https://irysarcade.xyz/assets/media-pack/snake/Right.jpg",
    "https://irysarcade.xyz/assets/media-pack/snake/Right_Bottom_.jpg",
    "https://irysarcade.xyz/assets/media-pack/snake/Top_Right.jpg",
    "https://irysarcade.xyz/assets/media-pack/snake/Up.jpg",
    "https://irysarcade.xyz/assets/media-pack/snake/Vertical.jpg"
]


os.makedirs("media", exist_ok=True)

for url in urls:
    jpg_name = url.split("/")[-1]
    jpg_path = os.path.join("media", jpg_name)
    gif_path = jpg_path.replace(".jpg", ".gif")

    print(f"Downloading {jpg_name}...")
    urllib.request.urlretrieve(url, jpg_path)

    print(f"Converting {jpg_name} to GIF...")
    with Image.open(jpg_path) as img:
        img.convert("RGB").save(gif_path, "GIF")

print("✅ All images downloaded and converted in the 'media' folder.")
