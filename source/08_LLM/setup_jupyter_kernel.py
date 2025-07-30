#!/usr/bin/env python3
"""
Jupyter 커널 설정 스크립트
llm 환경을 Jupyter 커널로 등록합니다.
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


def setup_jupyter_kernel():
    """Jupyter 커널을 설정합니다."""

    print("🚀 Jupyter 커널 설정을 시작합니다...")

    # conda 환경 확인
    env_name = os.environ.get("CONDA_DEFAULT_ENV")
    if not env_name:
        print("❌ conda 환경을 활성화한 후 다시 실행해주세요.")
        print("   conda activate llm")
        return False

    print(f"📦 현재 활성화된 conda 환경: {env_name}")

    # ipykernel 설치
    run_command("pip install ipykernel", "ipykernel 설치")

    # jupyter 설치
    run_command("pip install jupyter", "jupyter 설치")

    # llm 환경을 Jupyter 커널로 등록
    kernel_name = "llm"
    display_name = "llm(ipykernel)"

    print(f"\n📝 커널 등록: {kernel_name} -> {display_name}")

    # 기존 커널 제거 (있다면)
    run_command(f"jupyter kernelspec remove {kernel_name} --yes", "기존 커널 제거")

    # 새 커널 등록
    success = run_command(
        f"python -m ipykernel install --user --name {kernel_name} --display-name '{display_name}'",
        "새 커널 등록",
    )

    if success:
        print("\n✅ Jupyter 커널 설정 완료!")
        print(f"\n📝 등록된 커널 정보:")
        print(f"   - 커널 이름: {kernel_name}")
        print(f"   - 표시 이름: {display_name}")
        print(f"   - 환경: {env_name}")

        print("\n📝 다음 단계:")
        print("1. Jupyter 노트북을 재시작하세요")
        print("2. Kernel → Change kernel → llm(ipykernel) 선택")
        print("3. 또는 Kernel → Restart & Clear Output 실행")

        # 등록된 커널 목록 확인
        print("\n🔍 등록된 커널 목록:")
        run_command("jupyter kernelspec list", "커널 목록 확인")

    else:
        print("❌ 커널 등록에 실패했습니다.")
        return False

    return True


if __name__ == "__main__":
    setup_jupyter_kernel()
