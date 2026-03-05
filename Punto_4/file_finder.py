import os
from pathlib import Path


class FileFinder:
    """
    Finds HTML files from a list of files or directories (including subdirectories).
    """

    def __init__(self, paths):
        self.paths = paths

    def find_html_files(self):
        html_files = []

        for path in self.paths:
            p = Path(path)

            if p.is_file() and p.suffix.lower() == ".html":
                html_files.append(p)

            elif p.is_dir():
                for root, _, files in os.walk(p):
                    for file in files:
                        if file.lower().endswith(".html"):
                            html_files.append(Path(root) / file)

        return html_files
