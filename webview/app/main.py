import os
import pathlib

import webview

curr_dir = pathlib.Path(__file__).parent.resolve()
ui_dir = curr_dir.parent.parent / "ui"


class Api:
    pass


def get_entrypoint():
    def exists(path: str):
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    if exists("./ui/index.html"):
        return "./ui/index.html"

    if exists("../ui/index.html"):
        return "../ui/index.html"

    if exists("../../ui/index.html"):
        return "../../ui/index.html"

    if exists("../../../ui/index.html"):
        return "../../../ui/index.html"

    if exists("../../../../ui/index.html"):
        return "../../../../ui/index.html"

    raise Exception("No index.html found")


entry = get_entrypoint()


if __name__ == "__main__":
    window = webview.create_window(
        "pywebview-vue",
        url=entry,
        # url="http://localhost:5173",
        js_api=Api(),
        frameless=True,
    )
    webview.start(debug=True)
