import os
from bottle import *

@route("/")
def home():
  return "Hello To Webiiiiite"

run(host="0.0.0.0", port=os.environ.get("PORT"))
