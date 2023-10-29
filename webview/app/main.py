import os
import pathlib

import bottle
from bottle import static_file

import webview

curr_dir = pathlib.Path(__file__).parent.resolve()
ui_dir = curr_dir.parent.parent / "ui"

print(f"ui_dir: {ui_dir}")


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

# @app.route('/static/<filename:path>')
# def serve_static(filename):
#     return static_file(filename, root='./static')  # Adjust the root path as needed


app = bottle.Bottle()


# @app.route("/static/<filename:path>")
# def serve_static(filename):
#     return static_file(filename, root="./static")  # Adjust the root path as needed


@app.route("/<path:path>")
def catch_all(path):
    return static_file("index.html", root=ui_dir)


webview.create_window("Window", url=app)
webview.start(debug=True)
