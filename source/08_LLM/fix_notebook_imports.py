#!/usr/bin/env python3
"""
노트북에서 직접 실행할 수 있는 패키지 설치 및 테스트 코드
이 코드를 노트북 셀에서 실행하여 langchain_community 문제를 해결합니다.
"""

def install_and_test_packages():
    """패키지를 설치하고 테스트합니다."""
    
    print("🚀 노트북에서 패키지 설치 및 테스트를 시작합니다...")
    
    # 1. 필요한 패키지들 설치
    packages_to_install = [
        "langchain-community==0.3.27",
        "langchain-text-splitters",
        "langchain-chroma",
        "langchain-openai",
        "langchain-upstage",
        "docx2txt",
        "langchain",
        "langchainhub",
        "chromadb",
        "sentence-transformers",
        "tiktoken"
    ]
    
    print("\n📦 패키지 설치 중...")
    for package in packages_to_install:
        try:
            import subprocess
            result = subprocess.run(
                f"pip install {package}", 
                shell=True, 
                capture_output=True, 
                text=True
            )
            if result.returncode == 0:
                print(f"✅ {package} 설치 성공")
            else:
                print(f"❌ {package} 설치 실패: {result.stderr}")
        except Exception as e:
            print(f"❌ {package} 설치 중 오류: {e}")
    
    print("\n🔍 설치 확인...")
    
    # 2. 설치된 패키지 확인
    try:
        result = subprocess.run(
            "pip list | grep langchain", 
            shell=True, 
            capture_output=True, 
            text=True
        )
        if result.returncode == 0:
            print("설치된 langchain 패키지들:")
            print(result.stdout)
        else:
            print("langchain 패키지 확인 실패")
    except Exception as e:
        print(f"패키지 확인 중 오류: {e}")
    
    # 3. 모듈 import 테스트
    print("\n🧪 모듈 import 테스트...")
    
    test_modules = [
        ("langchain_community", "문서 로더 등 커뮤니티 통합"),
        ("langchain_text_splitters", "텍스트 분할"),
        ("langchain_chroma", "Chroma 벡터 DB"),
        ("langchain_openai", "OpenAI 연동"),
        ("docx2txt", "Word 문서 읽기"),
    ]
    
    success_count = 0
    for module_name, description in test_modules:
        try:
            __import__(module_name)
            print(f"✅ {module_name} - {description}")
            success_count += 1
        except ImportError as e:
            print(f"❌ {module_name} - {description}")
            print(f"   오류: {e}")
        except Exception as e:
            print(f"⚠️  {module_name} - {description}")
            print(f"   예외: {e}")
    
    print(f"\n📊 테스트 결과: {success_count}/{len(test_modules)} 성공")
    
    if success_count == len(test_modules):
        print("🎉 모든 모듈이 정상적으로 설치되었습니다!")
        print("\n✅ 이제 노트북에서 다음 코드를 실행할 수 있습니다:")
        print("from langchain_community.document_loaders import Docx2txtLoader")
        print("from langchain_text_splitters import RecursiveCharacterTextSplitter")
        print("from langchain_chroma import Chroma")
        print("from langchain_openai import OpenAIEmbeddings")
    else:
        print("⚠️  일부 모듈 설치에 실패했습니다.")
        print("노트북을 재시작하고 다시 시도해보세요.")
    
    return success_count == len(test_modules)

def test_specific_imports():
    """구체적인 import를 테스트합니다."""
    
    print("\n🔍 구체적인 import 테스트...")
    
    # langchain_community.document_loaders 테스트
    try:
        from langchain_community.document_loaders import Docx2txtLoader
        print("✅ Docx2txtLoader import 성공!")
        
        # 실제 파일 로드 테스트
        try:
            loader = Docx2txtLoader("./tax_docs/소득세법(법률)(제20615호)(20250701).docx")
            documents = loader.load()
            print(f"✅ 문서 로드 성공! 문서 수: {len(documents)}")
        except Exception as e:
            print(f"⚠️  문서 로드 실패: {e}")
            
    except ImportError as e:
        print(f"❌ Docx2txtLoader import 실패: {e}")
    
    # langchain_text_splitters 테스트
    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        print("✅ RecursiveCharacterTextSplitter import 성공!")
    except ImportError as e:
        print(f"❌ RecursiveCharacterTextSplitter import 실패: {e}")
    
    # langchain_chroma 테스트
    try:
        from langchain_chroma import Chroma
        print("✅ Chroma import 성공!")
    except ImportError as e:
        print(f"❌ Chroma import 실패: {e}")
    
    # langchain_openai 테스트
    try:
        from langchain_openai import OpenAIEmbeddings
        print("✅ OpenAIEmbeddings import 성공!")
    except ImportError as e:
        print(f"❌ OpenAIEmbeddings import 실패: {e}")

if __name__ == "__main__":
    # 패키지 설치 및 기본 테스트
    success = install_and_test_packages()
    
    if success:
        # 구체적인 import 테스트
        test_specific_imports()
    else:
        print("\n❌ 기본 설치에 실패했습니다. 노트북을 재시작하고 다시 시도해주세요.") 