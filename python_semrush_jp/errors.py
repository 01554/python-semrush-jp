from __future__ import absolute_import, print_function, unicode_literals


class BaseSemrushError(Exception):
    def __str__(self):
        return self.text


class SemrushAPIError(BaseSemrushError):
    def __init__(self, error_payload: bytes):
        super().__init__(error_payload)
        text = error_payload.decode("UTF-8")
        pref, message = text.split(" :: ")
        code = int(pref.split(" ")[1])
        self.text = text
        self.message = message
        self.code = code


class SemrushKeyError(BaseSemrushError):
    def __init__(self, error_text: str):
        super().__init__(error_text)
        self.text = error_text


class SemrushRegionalDatabaseError(BaseSemrushError):
    def __init__(self, error_text: str):
        super().__init__(error_text)
        self.text = error_text
