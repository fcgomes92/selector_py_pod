from json import dumps
from pprint import PrettyPrinter

from selector_py_pod.models.selection import Selection


class SerialAdapter:
    def __init__(self, config) -> None:
        self.pretty = config.get('OUTPUT_PRETTY')
        self.json = bool(config.get('OUTPUT_JSON'))

    def post(self, selection: Selection) -> None:
        s = selection.serialize()
        text = dumps(s) if self.json else s
        printer = PrettyPrinter().pprint if self.pretty else print
        printer(text)
        return True, text
