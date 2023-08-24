from rest_framework.exceptions import APIException


class NotAvailableBook(APIException):
    status_code = 409
    default_detail = 'Book is not available'