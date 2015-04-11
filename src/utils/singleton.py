# singleton.py
# author: Josue Mendoza
# date: 4-5-2015


class Singleton(type):
    """Makes possible the creation of one and only one
    object of a particular type
    """
    def __init__(cls, name, bases, dic):
        super(Singleton, cls).__init__(name, bases, dic)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)

        return cls.instance