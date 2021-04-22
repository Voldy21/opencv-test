from flask import Flask
import cv2

application = Flask(__name__)


@application.route("/")
def index():
    return "Hello World!"


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
