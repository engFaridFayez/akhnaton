import os
import cloudinary.uploader
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = BASE_DIR / "media"

SUPPORTED_EXT = {".jpg", ".jpeg", ".png", ".gif", ".mp4", ".mov", ".webp"}

results = []

def upload_file(file_path):
    print(f"Uploading: {file_path}")

    response = cloudinary.uploader.upload(
        str(file_path),
        resource_type="auto"
    )

    return response.get("secure_url")


def walk_and_upload():
    if not MEDIA_ROOT.exists():
        print("❌ Media folder not found:", MEDIA_ROOT)
        return

    for root, dirs, files in os.walk(MEDIA_ROOT):
        for file in files:
            ext = Path(file).suffix.lower()

            if ext not in SUPPORTED_EXT:
                continue

            full_path = os.path.join(root, file)

            url = upload_file(full_path)

            results.append({
                "file": full_path,
                "url": url
            })

            print(f"✔ Uploaded: {file}")

    print("Done. Total:", len(results))

    with open("cloudinary_upload_map.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)


if __name__ == "__main__":
    walk_and_upload()