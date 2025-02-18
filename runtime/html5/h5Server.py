# -*- coding: utf-8 -*-
###
### Copyright FunASR (https://github.com/alibaba-damo-academy/FunASR). All Rights
### Reserved. MIT License  (https://opensource.org/licenses/MIT)
###
### 2022-2023 by zhaoming,mali aihealthx.com


from flask import Flask, render_template, request, send_from_directory, jsonify, redirect, url_for

# from gevent.pywsgi import WSGIServer

import datetime
import random
import string
import time
import argparse
import os


app = Flask(__name__, static_folder="static", static_url_path="/static")


@app.route("/")
def homePage():
    return redirect("/static/index.html")


parser = argparse.ArgumentParser()
parser.add_argument(
    "--host", type=str, default="0.0.0.0", required=False, help="host ip, localhost, 0.0.0.0"
)
parser.add_argument("--port", type=int, default=1337, required=False, help="html5 server port")

parser.add_argument(
    "--certfile", type=str, default="./ssl_key/server.crt", required=False, help="certfile for ssl"
)

parser.add_argument(
    "--keyfile", type=str, default="./ssl_key/server.key", required=False, help="keyfile for ssl"
)

if __name__ == "__main__":
    args = parser.parse_args()
    port = args.port

    # WSGIServer
    # ssl = {
    #    'certfile': 'server.crt',
    #    'keyfile': 'server.key'
    # }
    # httpsServer = WSGIServer(("0.0.0.0",port), app, **ssl)
    # httpsServer.serve_forever()

    # flask
    print("srv run on ", port)

    # 获取脚本所在目录的绝对路径
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

    # 修改证书文件路径为项目的 ssl_key 目录
    context = (
        os.path.join(os.path.dirname(SCRIPT_DIR), "ssl_key/server.crt"),
        os.path.join(os.path.dirname(SCRIPT_DIR), "ssl_key/server.key")
    )

    # 检查证书文件是否存在
    if not os.path.exists(context[0]) or not os.path.exists(context[1]):
        print("Warning: SSL certificate files not found. Running without SSL.")
        context = None

    app.run(
        host="0.0.0.0",
        port=port,
        ssl_context=context,
        threaded=True,
        debug=False
    )
