from __future__ import absolute_import, print_function, unicode_literals


class BaseSemrushError(Exception):
    def __str__(self):
        return self.text


class SemrushAPIError(BaseSemrushError):
    def __init__(self, error_payload: bytes):
        super().__init__(error_payload)
        text = error_payload.decode("UTF-8")
        phrases = text.split(" :: ")
        prefs = phrases[:-1]
        message = phrases[-1]
        codes = [int(pref.split(" ")[1]) for pref in prefs]
        self.text = text
        self.message = message
        self.codes = codes


class SemrushKeyError(BaseSemrushError):
    def __init__(self, error_text: str):
        super().__init__(error_text)
        self.text = error_text


class SemrushRegionalDatabaseError(BaseSemrushError):
    def __init__(self, error_text: str):
        super().__init__(error_text)
        self.text = error_text
