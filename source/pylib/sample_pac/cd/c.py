# sample_pac/cd/c.py
# . : 현재폴더
# .. : 상위폴더

from ..ab import a

# from sample_pac.ab import a


def nice():
    print("smaple_pac/cd/c모듈안의 nice")
    a.hello()
