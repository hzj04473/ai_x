# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Korean AI+X education course repository containing comprehensive learning materials and source code for AI, web development, databases, and frameworks. It's organized by subject areas with both lecture notes (`lecNote/`) and practical source code (`source/`).

## Development Environment Setup

### Python Virtual Environments

This repository uses multiple conda environments for different subject areas:

#### LLM Environment (for Large Language Models)
```bash
conda activate llm
cd source/08_LLM
python install_llm_packages.py  # Install required packages
python setup_jupyter_kernel.py  # Setup Jupyter kernel
```

Key packages in LLM environment:
- `langchain-community`, `langchain-chroma`, `langchain-openai`
- `openai`, `transformers`, `sentence-transformers`
- `chromadb`, `tiktoken`

#### Natural Language Processing
```bash
# Requirements in source/07_자연어처리/requirements.txt
pip install -r source/07_자연어처리/requirements.txt
```

Key packages include: `konlpy`, `nltk`, `tensorflow`, `transformers`

#### RPA (Robotic Process Automation)
```bash
# Requirements in source/09_generativeAI_RPA/requirements.txt  
pip install -r source/09_generativeAI_RPA/requirements.txt
```

Key packages: `xlwings`, `openai`, `pandas`, `pyinstaller`

## Project Structure

### Main Directories

- **`source/`** - All practical source code organized by topic:
  - `01_python/` - Python fundamentals, data analysis (pandas, numpy, matplotlib)
  - `02_HTML_CSS/` - Web frontend basics
  - `03_javascript/` - JavaScript programming
  - `04_DBMS/` - Database operations (Oracle, MySQL, SQLite)
  - `05_DeepLearning/` - TensorFlow/Keras deep learning projects
  - `06_이미지처리/` - Computer vision with CNN
  - `07_자연어처리/` - NLP with NLTK, KoNLPy, transformers
  - `08_LLM/` - Large Language Models, RAG, OpenAI API
  - `09_generativeAI_RPA/` - Excel automation with AI
  - `10_MachineLearning/` - Scikit-learn ML projects
  - `11_Flask/` - Flask web applications
  - `12_Django/` - Django web framework projects

- **`lecNote/`** - Course materials and documentation
- **`note/`** - Study notes and summaries

### Key Projects

#### Django Web Applications (`source/12_Django/`)
- **myproject/**: Full-featured Django application with:
  - User authentication (`accounts/`)
  - Article management with file uploads (`article/`)
  - Blog functionality (`blog/`)
  - Book management (`book/`)

Run Django projects:
```bash
cd source/12_Django/myproject
python manage.py runserver
```

#### Flask Applications (`source/11_Flask/`)
- Multiple chapters covering routing, templates, file uploads, database integration
- Todo list application with database connectivity

#### LLM/RAG Applications (`source/08_LLM/`)
- OpenAI API integrations (Chat, DALL-E, TTS, Whisper)
- RAG implementations using LangChain and vector databases
- Performance optimization with metadata

## Common Development Tasks

### Running Jupyter Notebooks
```bash
jupyter notebook  # From any source directory
# Ensure correct kernel is selected (e.g., 'llm' for LLM projects)
```

### Django Development
```bash
cd source/12_Django/myproject
python manage.py migrate       # Apply database migrations
python manage.py runserver     # Start development server
python manage.py createsuperuser  # Create admin user
```

### Flask Development
```bash
cd source/11_Flask/[chapter_directory]
python app.py  # Most Flask apps use app.py as entry point
```

### Database Operations
- Oracle and MySQL connection examples in `source/04_DBMS/`
- SQLite databases included in Django projects
- Database repository patterns in Flask projects

## Environment Variables

### LLM Projects
Create `.env` files in LLM project directories:
```
OPENAI_API_KEY=your_api_key_here
LANGCHAIN_API_KEY=your_langchain_key  # Optional
```

### Django Projects
Configure in Django settings or use python-decouple for environment variables

## Troubleshooting

### LLM Environment Issues
If encountering `ModuleNotFoundError: No module named 'langchain_community'`:
1. Activate llm environment: `conda activate llm`
2. Run setup scripts in `source/08_LLM/`
3. Restart Jupyter and select correct kernel

See `source/08_LLM/README_문제해결.md` for detailed troubleshooting.

### Package Installation
Each major directory has its own `requirements.txt` where applicable. Install dependencies specific to the project you're working on.

## Architecture Notes

- **Web Projects**: Use both Flask (simpler) and Django (full-featured) frameworks
- **AI/ML Projects**: Jupyter notebooks for experimentation, Python scripts for production
- **Database**: SQLite for development, examples for Oracle/MySQL integration
- **Frontend**: HTML/CSS/JavaScript fundamentals, some Bootstrap usage
- **File Structure**: Korean directory names used throughout, maintain existing naming conventions