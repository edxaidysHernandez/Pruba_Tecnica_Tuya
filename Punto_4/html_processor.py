from pathlib import Path

from html_parser import ImageParser
from image_encoder import ImageEncoder


class HTMLProcessor:
    """
    Processes a single HTML file: extracts images, encodes them to Base64,
    replaces the src attributes and saves a new file.
    """

    def process(self, html_file):
        html_file = Path(html_file)
        results = {"success": {}, "fail": {}}

        with open(html_file, "r", encoding="utf-8") as f:
            html = f.read()

        parser = ImageParser()
        parser.feed(html)

        new_html = html

        for img_src in parser.images:
            image_path = html_file.parent / img_src

            try:
                base64_src = ImageEncoder.encode(image_path)
                new_html = new_html.replace(img_src, base64_src)
                results["success"][img_src] = str(image_path)

            except Exception as e:
                results["fail"][img_src] = str(e)

        output_file = html_file.with_name(html_file.stem + "_base64.html")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(new_html)

        return results
