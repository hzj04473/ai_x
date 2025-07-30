#!/usr/bin/env python3
"""
모듈 import 테스트 스크립트
llm 환경에서 필요한 모든 모듈들이 정상적으로 import되는지 확인합니다.
"""

import sys
import os


def test_import(module_name, description=""):
    """모듈 import를 테스트합니다."""
    try:
        __import__(module_name)
        print(f"✅ {module_name} - {description}")
        return True
    except ImportError as e:
        print(f"❌ {module_name} - {description}")
        print(f"   오류: {e}")
        return False
    except Exception as e:
        print(f"⚠️  {module_name} - {description}")
        print(f"   예외: {e}")
        return False


def main():
    """모든 모듈 import를 테스트합니다."""

    print("🚀 llm 환경 모듈 import 테스트")
    print("=" * 50)

    # 환경 정보 출력
    print(f"Python 경로: {sys.executable}")
    print(f"Python 버전: {sys.version}")
    print(f"현재 환경: {os.environ.get('CONDA_DEFAULT_ENV', 'conda 환경 아님')}")
    print()

    # 테스트할 모듈들
    modules_to_test = [
        ("langchain_community", "문서 로더 등 커뮤니티 통합"),
        ("langchain_text_splitters", "텍스트 분할"),
        ("langchain_chroma", "Chroma 벡터 DB"),
        ("langchain_openai", "OpenAI 연동"),
        ("langchain_upstage", "Upstage 연동"),
        ("langchain_ollama", "Ollama 연동"),
        ("langchain_anthropic", "Anthropic 연동"),
        ("docx2txt", "Word 문서 읽기"),
        ("langchain", "핵심 라이브러리"),
        ("langchainhub", "LangChain Hub"),
        ("chromadb", "벡터 데이터베이스"),
        ("sentence_transformers", "임베딩 모델"),
        ("tiktoken", "토큰화"),
        ("openai", "OpenAI SDK"),
        ("dotenv", "환경변수 관리"),
    ]

    success_count = 0
    total_count = len(modules_to_test)

    for module_name, description in modules_to_test:
        if test_import(module_name, description):
            success_count += 1
        print()

    # 결과 요약
    print("=" * 50)
    print(f"📊 테스트 결과: {success_count}/{total_count} 성공")

    if success_count == total_count:
        print("🎉 모든 모듈이 정상적으로 import되었습니다!")
        print("\n✅ RAG 구현을 위한 모든 준비가 완료되었습니다!")
    else:
        print("⚠️  일부 모듈 import에 실패했습니다.")
        print("\n🔧 해결 방법:")
        print("1. install_llm_packages.py 스크립트를 실행하세요")
        print("2. setup_jupyter_kernel.py 스크립트를 실행하세요")
        print("3. Jupyter 노트북을 재시작하세요")

    # 추가 테스트
    print("\n🔍 추가 테스트...")

    # langchain_community의 구체적인 기능 테스트
    if test_import("langchain_community"):
        try:
            from langchain_community.document_loaders import Docx2txtLoader

            print("✅ Docx2txtLoader import 성공!")
        except ImportError as e:
            print(f"❌ Docx2txtLoader import 실패: {e}")

    # langchain_text_splitters의 구체적인 기능 테스트
    if test_import("langchain_text_splitters"):
        try:
            from langchain_text_splitters import RecursiveCharacterTextSplitter

            print("✅ RecursiveCharacterTextSplitter import 성공!")
        except ImportError as e:
            print(f"❌ RecursiveCharacterTextSplitter import 실패: {e}")

    # langchain_chroma의 구체적인 기능 테스트
    if test_import("langchain_chroma"):
        try:
            from langchain_chroma import Chroma

            print("✅ Chroma import 성공!")
        except ImportError as e:
            print(f"❌ Chroma import 실패: {e}")

    # langchain_openai의 구체적인 기능 테스트
    if test_import("langchain_openai"):
        try:
            from langchain_openai import OpenAIEmbeddings

            print("✅ OpenAIEmbeddings import 성공!")
        except ImportError as e:
            print(f"❌ OpenAIEmbeddings import 실패: {e}")


if __name__ == "__main__":
    main()
