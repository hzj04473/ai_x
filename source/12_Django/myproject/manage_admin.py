#!/usr/bin/env python3
"""
Django Admin 계정 관리 스크립트
이 스크립트는 Django 프로젝트의 admin 계정을 관리하는 다양한 기능을 제공합니다.
"""

import os
import sys
import django

# Django 설정 초기화
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def show_all_users():
    """모든 사용자 목록을 출력합니다."""
    print("=== 현재 등록된 사용자 목록 ===")
    users = User.objects.all()

    if not users:
        print("등록된 사용자가 없습니다.")
        return

    for user in users:
        print(f"ID: {user.id}")
        print(f"  Username: {user.username}")
        print(f"  Email: {user.email or '이메일 없음'}")
        print(f"  First Name: {user.first_name or '이름 없음'}")
        print(f"  Last Name: {user.last_name or '성 없음'}")
        print(f"  Is Staff: {user.is_staff}")
        print(f"  Is Superuser: {user.is_superuser}")
        print(f"  Is Active: {user.is_active}")
        print(f"  Date Joined: {user.date_joined}")
        print("-" * 40)


def change_admin_password(username, new_password):
    """지정된 사용자의 비밀번호를 변경합니다."""
    try:
        user = User.objects.get(username=username)
        user.password = make_password(new_password)
        user.save()
        print(f"✅ '{username}' 사용자의 비밀번호가 성공적으로 변경되었습니다.")
        return True
    except User.DoesNotExist:
        print(f"❌ 사용자 '{username}'을 찾을 수 없습니다.")
        return False
    except Exception as e:
        print(f"❌ 비밀번호 변경 중 오류 발생: {e}")
        return False


def create_superuser(username, email, password, first_name="", last_name=""):
    """새로운 superuser를 생성합니다."""
    try:
        # 사용자가 이미 존재하는지 확인
        if User.objects.filter(username=username).exists():
            print(f"❌ 사용자명 '{username}'이 이미 존재합니다.")
            return False

        # 이메일이 이미 존재하는지 확인
        if email and User.objects.filter(email=email).exists():
            print(f"❌ 이메일 '{email}'이 이미 존재합니다.")
            return False

        # 새 superuser 생성
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=True,
            is_superuser=True,
        )

        print(f"✅ 새로운 superuser '{username}'이 성공적으로 생성되었습니다.")
        print(f"   이메일: {email}")
        print(f"   이름: {first_name} {last_name}")
        return True

    except Exception as e:
        print(f"❌ superuser 생성 중 오류 발생: {e}")
        return False


def deactivate_user(username):
    """지정된 사용자를 비활성화합니다."""
    try:
        user = User.objects.get(username=username)
        user.is_active = False
        user.save()
        print(f"✅ 사용자 '{username}'이 비활성화되었습니다.")
        return True
    except User.DoesNotExist:
        print(f"❌ 사용자 '{username}'을 찾을 수 없습니다.")
        return False
    except Exception as e:
        print(f"❌ 사용자 비활성화 중 오류 발생: {e}")
        return False


def activate_user(username):
    """지정된 사용자를 활성화합니다."""
    try:
        user = User.objects.get(username=username)
        user.is_active = True
        user.save()
        print(f"✅ 사용자 '{username}'이 활성화되었습니다.")
        return True
    except User.DoesNotExist:
        print(f"❌ 사용자 '{username}'을 찾을 수 없습니다.")
        return False
    except Exception as e:
        print(f"❌ 사용자 활성화 중 오류 발생: {e}")
        return False


def main():
    """메인 함수 - 사용자 인터페이스 제공"""
    print("=== Django Admin 계정 관리 도구 ===")
    print()

    while True:
        print("\n사용 가능한 작업:")
        print("1. 모든 사용자 목록 보기")
        print("2. admin 비밀번호 변경")
        print("3. 새로운 superuser 생성")
        print("4. 사용자 비활성화")
        print("5. 사용자 활성화")
        print("0. 종료")

        choice = input("\n원하는 작업을 선택하세요 (0-5): ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break

        elif choice == "1":
            show_all_users()

        elif choice == "2":
            username = input("비밀번호를 변경할 사용자명: ").strip()
            new_password = input("새 비밀번호: ").strip()
            if new_password:
                change_admin_password(username, new_password)
            else:
                print("❌ 비밀번호를 입력해주세요.")

        elif choice == "3":
            username = input("새 사용자명: ").strip()
            email = input("이메일 (선택사항): ").strip()
            password = input("비밀번호: ").strip()
            first_name = input("이름 (선택사항): ").strip()
            last_name = input("성 (선택사항): ").strip()

            if username and password:
                create_superuser(username, email, password, first_name, last_name)
            else:
                print("❌ 사용자명과 비밀번호는 필수입니다.")

        elif choice == "4":
            username = input("비활성화할 사용자명: ").strip()
            if username:
                deactivate_user(username)
            else:
                print("❌ 사용자명을 입력해주세요.")

        elif choice == "5":
            username = input("활성화할 사용자명: ").strip()
            if username:
                activate_user(username)
            else:
                print("❌ 사용자명을 입력해주세요.")

        else:
            print("❌ 잘못된 선택입니다. 0-5 사이의 숫자를 입력해주세요.")


if __name__ == "__main__":
    main()
