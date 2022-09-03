from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class DefaultAPIResponse(Response):
    def __init__(self, data=None, message="", success=None, http_status=HTTP_200_OK, other_data: dict = None):
        if data is None:
            data = {}
        if other_data is None:
            other_data = {}
        if success is None:
            success = False
            if not message:
                message = "Failed to perform task!"
            if 200 <= http_status < 300:
                success = True
                message = "Successfully performed task!"
        response_data = {**{
            "success": success,
            "message": message
        }, **other_data, 'data': data}
        super(DefaultAPIResponse, self).__init__(response_data, http_status)


class ErrorAPIResponse(DefaultAPIResponse):
    ERROR_CODE = "error_code"
    ERROR_MESSAGE = "error_message"
    ERROR_HTTP_STATUS = "error_http_status"

    def __init__(self, data=None, error_status_code_dict=None, custom_message="", append_message="",
                 errors: list or dict = None, other_data: dict = None, http_status=None):
        if other_data is None:
            other_data = {}
        if error_status_code_dict is None:
            error_status_code_dict = {}
        if data is None:
            data = {}
        custom_message = self.resolve_custom_message(error_status_code_dict, custom_message)
        if append_message:
            custom_message = f"{custom_message} :- {append_message}"
        errors_payload = {
            self.ERROR_CODE: error_status_code_dict.get(self.ERROR_CODE)
        }
        if errors:
            errors_payload['error_details'] = errors
        if not http_status:
            http_status = error_status_code_dict.get(self.ERROR_HTTP_STATUS)
            http_status = http_status if type(http_status) == int else HTTP_400_BAD_REQUEST
        super(ErrorAPIResponse, self).__init__(data=data, message=custom_message, http_status=http_status,
                                               other_data={**errors_payload, **other_data})

    def resolve_custom_message(self, error_code_dictionary, custom_message):
        """
        If custom message is present than override the default message set in the error_code_dictionary
        """
        if not custom_message:
            custom_message = error_code_dictionary.get(self.ERROR_MESSAGE)
        return custom_message
