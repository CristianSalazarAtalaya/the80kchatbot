import os
from flask import Flask
import json

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

class ConfigFacebook:

    def __init__(self):
        json_url = os.path.join(SITE_ROOT, '', 'facebook.json')
        data = json.load(open(json_url))
        self.data = data
        self.page = data["page"]
        self.ACCESS_TOKEN = data["credentials"]["ACCESS_TOKEN"]
        self.VERIFY_TOKEN = data["credentials"]["VERIFY_TOKEN"]

class ConfigWatson:

    def __init__(self):
        json_url = os.path.join(SITE_ROOT, '', 'watson.json')
        data = json.load(open(json_url))
        self.data = data
        self.page = data["page"]
        self.autenticator = data["credentials"]["autenticator"]
        self.version = data["credentials"]["version"]
        self.workspaceid = data["credentials"]["workspaceid"]
        self.url = data["credentials"]["url"]


