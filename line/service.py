import ast
from django.contrib.messages import get_messages


def session_delete(request, data: list):
    """
    :セッション削除用
    """
    for i in data:
        try:
            del request.session[i]
        except KeyError:
            pass


def get_error_message(request: object) -> dict or None:
    """
    :Get Flash Error Message
    """
    error_message = None
    if get_messages(request):
        message_storage = get_messages(request)
        for message in message_storage:
            error_message = str(message)
        error_message = ast.literal_eval(error_message)
    return error_message
