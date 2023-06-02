
def save(self):

    def outer(fn):
        def inner(*args, **kwargs):
            fn(*args, **kwargs)
            self.__save_users()
        return inner

    return outer

