class NodeEvent:
    def __init__(self, value=None):
        self._value = value
        self._callbacks = []
        self._ls_name    = []

    @property
    def value(self):
        return self._value

    # def value(self, data):
    #     self._value = data
    #     self._notify()

    # @value.setter
    def active(self, data):
        self._value = data
        self._notify()

    def add_callback(self,name,callback):
        if callable(callback):
            self._callbacks.append(callback)
            self._ls_name.append(name)
        else:
            raise ValueError("Callback must be callable")
        
    def rm_callback(self,name):
        index = self._ls_name.index(name)
        self._ls_name.pop(index)
        self._callbacks.pop(index)

    def _notify(self):
        for callback in self._callbacks:
            callback(self._value)

    def list_callback(self):
        return self._ls_name
