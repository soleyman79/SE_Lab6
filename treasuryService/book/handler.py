from rest_framework.views import exception_handler
from rest_framework.response import Response

import sys
import os

borrow_service_dir = os.path.abspath('../.')
sys.path.append(borrow_service_dir)

from .Exceptions import NotAvailableBook


def customExceptionHandler(exc, context):
    response = exception_handler(exc, context)
    
    if isinstance(exc, NotAvailableBook):
        response = Response({'detail': exc.default_detail}, status=exc.status_code)
    
    return response 