from flask import Blueprint

simple_templates = Blueprint('simple_templates', __name__)

@simple_templates.route("/faq")
def faq():
    return "Message Processed"