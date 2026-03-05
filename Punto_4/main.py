from file_finder import FileFinder
from html_processor import HTMLProcessor


def main(paths):
    finder = FileFinder(paths)
    html_files = finder.find_html_files()

    processor = HTMLProcessor()
    all_results = {"success": {}, "fail": {}}

    for html_file in html_files:
        result = processor.process(html_file)
        all_results["success"].update(result["success"])
        all_results["fail"].update(result["fail"])

    return all_results


if __name__ == "__main__":

    paths = [
        "html_folder",
        "example.html"
    ]

    results = main(paths)
    print(results)
