"""
sample_pac/ab/__init__.py
from sample_pac.ab import * 수행할 경우
자동 import 될 모듈지정 할 수 있음 (__all__)

sample_pac/ab/a.py
sample_pac/ab/b.py
"""

__all__ = ["a"]
# __all__ = ["b"]

print("sample_pac패키지 안의 ab패키지 로드됩니다.")
