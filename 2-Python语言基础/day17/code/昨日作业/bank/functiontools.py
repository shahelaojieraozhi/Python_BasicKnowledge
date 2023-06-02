

def save(fn):
    def inner(self, *args, **kwargs):
        fn(self, *args, **kwargs)

        self.save_users()
        print('=>已同步到文件users.txt中！')
    return inner


