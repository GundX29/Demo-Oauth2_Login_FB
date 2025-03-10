from flask import Flask, render_template, request
import os

import requests

print("FB_APP_ID:", os.getenv("FB_APP_ID"))  # Đúng
print("FB_APP_SECRET:", os.getenv("FB_APP_SECRET"))  # Đúng

app = Flask(__name__)


@app.route("/")
def main(): 
    return render_template(
        "login_non_js_sdk.html",
        app_id=os.getenv("FB_APP_ID"),
        redirect_uri="https://localhost:5001/redirect",
    )


@app.route("/redirect")
def redirect():

    code = request.values.get("code")

    url = "https://graph.facebook.com/v6.0/oauth/access_token?client_id={app_id}&redirect_uri={redirect_uri}&client_secret={app_secret}&code={code_parameter}".format(
        app_id=os.getenv("FB_APP_ID"),
        redirect_uri="https://localhost:5001/redirect",
        app_secret=os.getenv("FB_APP_SECRET"),
        code_parameter=code,
    )
    r = requests.get(url)

    return r.json()

if __name__ == "__main__":
    app.run(ssl_context=("localhost.pem", "localhost-key.pem"), debug=True, port=5001)


