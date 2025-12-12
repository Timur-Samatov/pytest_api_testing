from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "The API returned an unexpected status code."
    WRONG_CONTENT_TYPE = "The API returned an unexpected content type."