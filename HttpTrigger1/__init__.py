import logging

import azure.functions as func


# note that the package is "azf-wsgi" but the import is "azf_wsgi"
from azf_wsgi import AzureFunctionsWsgi
# Django, for example, but works with any WSGI app
from django_azure.wsgi import application


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AzureFunctionsWsgi(application).main(req, context)
