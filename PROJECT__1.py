
__all__ = ['TRANSFORM']


class TRANSFORM(object):
    __slots__ = ['__VALUE_KILOGRAM__']

    def __init__(self, KILOGRAM=None):
        self.__VALUE_KILOGRAM__ = KILOGRAM

    def __mul__(self):
        VAR = 'G'
        return self.__VALUE_KILOGRAM__ * 10 ** 3, VAR

    def __pow__(self):
        VAR = 'KG'
        return self.__VALUE_KILOGRAM__ * 10 ** (-3), VAR





