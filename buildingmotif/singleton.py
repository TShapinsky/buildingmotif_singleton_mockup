

class Singleton(type):
    def __new__(cls, name, bases, cls_dict):
        def make_global(self):
            klazz = self.__class__
            klazz.instance = self
        cls_dict['make_global'] = make_global
        return super().__new__(cls, name, bases, cls_dict)

    def __call__(cls, new_instance=False, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        if new_instance:
            return super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance

class SingletonNotInstantiatedException(Exception):
    """Raised when a singelton is accessed without being initialized"""