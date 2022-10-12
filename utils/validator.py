import logging
from json import JSONDecodeError
from typing import Optional, Tuple

from pydantic import BaseModel, ValidationError
from requests import Response

logger = logging.getLogger("api")


class Validator:
    """Response json validator."""

    @staticmethod
    def structure(
        response: Response, type_response: Optional[BaseModel] = None
    ) -> Tuple[Response, Optional[Exception]]:
        """Transform response json to response.data field."""
        if type_response:
            try:
                response.data = type_response.parse_obj(  # type: ignore
                    response.json()
                )
            except (ValidationError, JSONDecodeError) as err:
                return response, err
        return response, None
