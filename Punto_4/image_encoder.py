import base64
from pathlib import Path


class ImageEncoder:
    """
    Encodes a local image file to a Base64 Data URI string.
    """

    @staticmethod
    def encode(image_path):
        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")

        ext = Path(image_path).suffix.replace(".", "")
        return f"data:image/{ext};base64,{encoded}"
