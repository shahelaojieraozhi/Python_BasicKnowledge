''''''
import os

'''
1. os模块
    # os.name
    # os.environ
    # os.getcwd()
    # os.curdir
    
    os.listdir() 
    os.mkdir()
    os.makedirs('a/b/c')
    os.rmdir()
    os.remove()
    os.rename()
    # os.stat()
    
    os.path.join()
    os.path.exists()
    os.path.isfile()
    os.path.isdir()
    os.path.getsize()
    os.path.split()
    os.path.splitext()
    os.path.abspath()
    # os.path.dirname()
    # os.path.basename()

2. 遍历目录

3. 包和模块
    1. 导入模块
        import
        from-import
        别名: as
    2. 安装第三方模块
        1. 使用pip
            pip install package
            pip uninstall package
            pip -V
            pip list
            pip freeze  (除了pip, setuptools)
            pip show package
            
            pip freeze > requirements.txt
            pip install -r requirements.txt
        2.使用快捷键: alt + enter
        3.使用pycharm的settings

4.__name__
    
    
'''

# path = 'aaa'
# if not os.path.exists(path):
#     os.mkdir(path)

import random as r
def fn():
    pass

def fn2():
    pass


if __name__ == '__main__':
    fn()
