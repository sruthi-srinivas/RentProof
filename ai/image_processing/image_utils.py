from pathlib import Path

from PIL import Image

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
ALLOWED_FORMATS = {"JPEG", "PNG", "WEBP"}
MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB
MAX_IMAGE_WIDTH = 1920
MAX_IMAGE_HEIGHT = 1080
THUMBNAIL_WIDTH = 400
THUMBNAIL_HEIGHT = 400


def is_valid_image(file_path):
    path = Path(file_path)

    if not path.is_file():
        return False

    file_size = path.stat().st_size
    if file_size == 0 or file_size > MAX_FILE_SIZE_BYTES:
        return False

    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        return False

    try:
        with Image.open(path) as image:
            image.verify()

        # verify() closes the image, so we open it again to check the format
        with Image.open(path) as image:
            if image.format not in ALLOWED_FORMATS:
                return False

        return True
    except (OSError, ValueError):
        return False


def resize_image(file_path, output_path):
    if not is_valid_image(file_path):
        return False

    try:
        with Image.open(file_path) as image:
            image.thumbnail((MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT))
            image.save(output_path)
        return True
    except (OSError, ValueError):
        return False


def create_thumbnail(file_path, output_path):
    if not is_valid_image(file_path):
        return False

    try:
        with Image.open(file_path) as image:
            image.thumbnail((THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT))
            image.save(output_path)
        return True
    except (OSError, ValueError):
        return False
