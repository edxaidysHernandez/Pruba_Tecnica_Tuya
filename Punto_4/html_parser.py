from html.parser import HTMLParser


class ImageParser(HTMLParser):
    """
    Extracts image sources from HTML <img> tags.
    """

    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            attrs_dict = dict(attrs)
            if "src" in attrs_dict:
                self.images.append(attrs_dict["src"])
