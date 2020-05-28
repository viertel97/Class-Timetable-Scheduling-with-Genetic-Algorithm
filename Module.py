class Module:
    def __init__(self, token, name, docents):
        self._token = token
        self._name = name
        self._docents = docents

    def get_number(self): return self._token

    def get_name(self): return self._name

    def get_docents(self): return self._docents

    def __str__(self): return self._name
