from bing_image_downloader import downloader
import os
from all_categories import return_categories

base_dir = "downloaded_images"
os.makedirs(base_dir, exist_ok=True)

names = return_categories()

for name in names:
    safe_name = name.replace(" ", "_")
    print(f"Downloading images for: {name} -> Folder: {safe_name}")

    downloader.download(
        query=name,
        limit=5,
        output_dir=base_dir,
        adult_filter_off=True,
        force_replace=False,
        timeout=60,
        verbose=True
    )

print("All images of those categories downloaded.")
