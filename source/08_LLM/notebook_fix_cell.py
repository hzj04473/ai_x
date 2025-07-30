# 노트북 셀에서 실행할 수 있는 해결 코드
# 이 코드를 노트북의 새로운 셀에 복사해서 실행하세요

import sys
import subprocess
import os

print("🔧 langchain_community 모듈 문제 해결을 시작합니다...")

# 1. 현재 환경 확인
print(f"Python 경로: {sys.executable}")
print(f"Python 버전: {sys.version}")
print(f"현재 환경: {os.environ.get('CONDA_DEFAULT_ENV', 'conda 환경 아님')}")

# 2. 필요한 패키지 설치
packages = [
    "langchain-community==0.3.27",
    "langchain-text-splitters",
    "langchain-chroma",
    "langchain-openai",
    "docx2txt",
]

print("\n📦 패키지 설치 중...")
for package in packages:
    try:
        result = subprocess.run(
            f"pip install {package}", shell=True, capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"✅ {package} 설치 성공")
        else:
            print(f"❌ {package} 설치 실패")
    except Exception as e:
        print(f"❌ {package} 설치 중 오류: {e}")

# 3. 설치 확인
print("\n🔍 설치된 langchain 패키지 확인...")
try:
    result = subprocess.run(
        "pip list | grep langchain", shell=True, capture_output=True, text=True
    )
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("langchain 패키지가 설치되지 않았습니다.")
except Exception as e:
    print(f"패키지 확인 중 오류: {e}")

# 4. 모듈 import 테스트
print("\n🧪 모듈 import 테스트...")

test_modules = [
    "langchain_community",
    "langchain_text_splitters",
    "langchain_chroma",
    "langchain_openai",
]

success_count = 0
for module in test_modules:
    try:
        __import__(module)
        print(f"✅ {module} import 성공")
        success_count += 1
    except ImportError as e:
        print(f"❌ {module} import 실패: {e}")

print(f"\n📊 테스트 결과: {success_count}/{len(test_modules)} 성공")

if success_count == len(test_modules):
    print("🎉 모든 모듈이 정상적으로 설치되었습니다!")
    print("\n✅ 이제 다음 코드를 실행할 수 있습니다:")
    print("from langchain_community.document_loaders import Docx2txtLoader")
    print("from langchain_text_splitters import RecursiveCharacterTextSplitter")
    print("from langchain_chroma import Chroma")
    print("from langchain_openai import OpenAIEmbeddings")
else:
    print("⚠️  일부 모듈 설치에 실패했습니다.")
    print("노트북을 재시작하고 다시 시도해주세요.")

print("\n💡 다음 단계:")
print("1. 이 셀 실행 후 Kernel → Restart 실행")
print("2. 다시 노트북을 실행해보세요")
