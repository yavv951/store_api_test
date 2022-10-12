import requests
from requests import Response


class Client:
    """Клиент для отправки запросов."""

    @staticmethod
    def request(method: str, url: str, **kwargs) -> Response:
        """
        Request method: method for the new Request object: get, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
        url – URL for the new Request object.
        **kwargs:
            params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request.
        """
        return requests.request(method, url, **kwargs)
