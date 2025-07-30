#!/usr/bin/env python3
"""
llm 가상환경 패키지 설치 스크립트
이 스크립트는 llm 환경에서 필요한 모든 패키지들을 설치합니다.
"""

import subprocess
import sys
import os


def run_command(command, description):
    """명령어를 실행하고 결과를 출력합니다."""
    print(f"\n🔧 {description}")
    print(f"실행 명령어: {command}")

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ 성공!")
            if result.stdout:
                print("출력:", result.stdout)
        else:
            print("❌ 실패!")
            print("오류:", result.stderr)
            return False
    except Exception as e:
        print(f"❌ 예외 발생: {e}")
        return False

    return True


def check_conda_env():
    """conda 환경이 활성화되어 있는지 확인합니다."""
    env_name = os.environ.get("CONDA_DEFAULT_ENV")
    if env_name:
        print(f"📦 현재 활성화된 conda 환경: {env_name}")
        return env_name
    else:
        print("⚠️  conda 환경이 활성화되지 않았습니다.")
        return None


def install_packages():
    """필요한 패키지들을 설치합니다."""

    # 기본 패키지들
    packages = [
        "langchain-community==0.3.27",
        "langchain-text-splitters",
        "langchain-chroma",
        "langchain-openai",
        "langchain-upstage",
        "langchain-ollama",
        "langchain-anthropic",
        "docx2txt",
        "langchain",
        "langchainhub",
        "python-dotenv==1.1.0",
        "openai",
        "chromadb",
        "sentence-transformers",
        "tiktoken",
    ]

    print("🚀 llm 환경 패키지 설치를 시작합니다...")

    # conda 환경 확인
    env_name = check_conda_env()
    if not env_name:
        print("❌ conda 환경을 활성화한 후 다시 실행해주세요.")
        print("   conda activate llm")
        return False

    if env_name != "llm":
        print(f"⚠️  현재 환경이 'llm'이 아닙니다: {env_name}")
        response = input("계속 진행하시겠습니까? (y/N): ")
        if response.lower() != "y":
            return False

    # pip 업그레이드
    run_command("pip install --upgrade pip", "pip 업그레이드")

    # 각 패키지 설치
    for package in packages:
        success = run_command(f"pip install {package}", f"{package} 설치")
        if not success:
            print(f"⚠️  {package} 설치에 실패했습니다.")

    # 설치 확인
    print("\n🔍 설치된 패키지 확인...")
    run_command("pip list | grep langchain", "langchain 관련 패키지 확인")

    print("\n✅ 설치 완료!")
    print("\n📝 다음 단계:")
    print("1. Jupyter 노트북을 재시작하세요")
    print("2. Kernel → Restart & Clear Output 실행")
    print("3. 노트북에서 다음 코드로 테스트:")
    print("   import langchain_community")
    print("   print('✅ langchain_community 설치 완료!')")

    return True


if __name__ == "__main__":
    install_packages()
