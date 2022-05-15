import copy


class Something:
    def __init__(self, some_int, some_list, some_ref):
        self.i_int = some_int
        self.i_list = some_list
        self.i_ref = some_ref
    def __copy__(self):
        some_list = copy.copy(self.i_list)
        some_ref = copy.copy(self.i_ref)
        new = self.__class__(
            self.i_int, some_list, some_ref
        )
        new.__dict__.update(self.__dict__)
        return new
    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}
        some_list = copy.deepcopy(self.i_list, memo)
        some_ref = copy.deepcopy(self.i_ref, memo)
        new = self.__class__(
            self.i_int, some_list, some_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new