# 🚀 llm 환경 langchain_community 문제 해결 가이드

## 문제 상황

```
ModuleNotFoundError: No module named 'langchain_community'
```

## 🔧 해결 방법

### 1단계: llm 환경 활성화

```bash
conda activate llm
```

### 2단계: 패키지 설치 스크립트 실행

```bash
cd source/08_LLM
python install_llm_packages.py
```

### 3단계: Jupyter 커널 설정

```bash
python setup_jupyter_kernel.py
```

### 4단계: Jupyter 노트북 재시작

1. Jupyter 노트북을 완전히 종료
2. 다시 시작
3. Kernel → Change kernel → llm(ipykernel) 선택
4. Kernel → Restart & Clear Output 실행

### 5단계: 테스트

노트북에서 다음 코드 실행:

```python
import langchain_community
print("✅ langchain_community 설치 완료!")

# 추가 테스트
from langchain_community.document_loaders import Docx2txtLoader
print("✅ Docx2txtLoader import 성공!")
```

## 📦 설치되는 패키지 목록

- `langchain-community==0.3.27` - 문서 로더 등 커뮤니티 통합
- `langchain-text-splitters` - 텍스트 분할
- `langchain-chroma` - Chroma 벡터 DB
- `langchain-openai` - OpenAI 연동
- `langchain-upstage` - Upstage 연동
- `langchain-ollama` - Ollama 연동
- `langchain-anthropic` - Anthropic 연동
- `docx2txt` - Word 문서 읽기
- `langchain` - 핵심 라이브러리
- `langchainhub` - LangChain Hub
- `chromadb` - 벡터 데이터베이스
- `sentence-transformers` - 임베딩 모델
- `tiktoken` - 토큰화

## 🔍 문제 진단

만약 여전히 문제가 있다면:

### 환경 확인

```python
import sys
print("Python 경로:", sys.executable)
print("Python 버전:", sys.version)

import os
print("현재 환경:", os.environ.get('CONDA_DEFAULT_ENV', 'conda 환경 아님'))
```

### 패키지 설치 확인

```bash
pip list | grep langchain
```

### 커널 목록 확인

```bash
jupyter kernelspec list
```

## 🆘 추가 문제 해결

### 방법 1: 수동 설치

```bash
conda activate llm
pip install langchain-community==0.3.27
pip install langchain-text-splitters
pip install langchain-chroma
pip install langchain-openai
pip install docx2txt
```

### 방법 2: 노트북에서 직접 설치

```python
# 노트북 셀에서 실행
!pip install langchain-community==0.3.27
!pip install langchain-text-splitters
!pip install langchain-chroma
```

설치 후 **Kernel → Restart** 실행

### 방법 3: 환경 재생성

```bash
conda deactivate
conda remove -n llm --all
conda create -n llm python=3.10
conda activate llm
# 위의 설치 스크립트 다시 실행
```

## ✅ 성공 확인

모든 단계가 완료되면 다음 코드가 오류 없이 실행됩니다:

```python
from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

print("🎉 모든 모듈이 정상적으로 import되었습니다!")
```

## 📞 문제가 지속되는 경우

1. 터미널에서 `conda list`로 설치된 패키지 확인
2. `jupyter kernelspec list`로 등록된 커널 확인
3. Jupyter 노트북의 Kernel 메뉴에서 올바른 커널 선택 확인
4. 노트북 재시작 후 다시 시도

---

**💡 팁**: 환경 변수 설정도 확인해주세요!

- `.env` 파일에 `OPENAI_API_KEY` 설정
- 필요시 `LANGCHAIN_API_KEY` 설정
