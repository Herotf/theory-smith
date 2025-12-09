Installation Guide — TheorySmith Pro

Requirements

-   Python 3.10+
-   Ollama installed
-   Local LLaMA model (llama3 recommended)

Install Ollama

Download: https://ollama.ai/download

Pull a model:

    ollama pull llama3

Clone Project

    git clone https://github.com/<your-username>/theorysmith_pro_advance.git
    cd theorysmith_pro_advance

Virtual Environment

    python -m venv venv
    venv\Scripts\activate

Install Dependencies

    pip install -r requirements.txt

Run App

    streamlit run theorysmith_pro_advanced.py
