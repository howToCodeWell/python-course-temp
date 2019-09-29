# Some special methods such as __del__ do not work in Micro Python
import gc


class Run:
    def __del__(self):
        print('__del__ was called')


runner = Run()
del runner

gc.collect()
