import os

# 1. content for requirements.txt
requirements_content = """streamlit
matplotlib
numpy
pandas
ollama
torch
transformers
"""

# 2. content for .gitignore (Cleaned up formatting)
gitignore_content = """# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.env
venv/
env/
.DS_Store

# Streamlit
.streamlit/

# Jupyter / logs
.ipynb_checkpoints/
logs/

# IDE settings
.vscode/
.idea/
"""

# 3. content for STREAMLIT_README.md
readme_content = """# Running the TheorySmith Streamlit App

## 📌 Requirements
Install dependencies:
pip install -r requirements.txt

## ▶️ Run the App Locally
streamlit run theorysmith_pro_advanced.py

Ensure the Python file is in the same directory.

## 🛠 Project Structure Example
theorysmith/
│── theorysmith_pro_advanced.py
│── requirements.txt
│── README.md
│── .gitignore
│── modules/
│   ├── physics_engine.py
│   ├── ai_reasoner.py
│   ├── visualizer.py

## 🌐 Deploying to Streamlit Cloud
1. Push your repo to GitHub
2. Go to https://streamlit.io/cloud
3. Click “Deploy App”
4. Select your repo
5. Done 🚀

## 🧠 Notes
This app uses:
- Streamlit for UI
- Ollama / LLaMA / Transformers for reasoning
- Matplotlib for visualization
- Custom physics modules for simulation
"""

def create_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created {filename}")

if __name__ == "__main__":
    create_file("requirements.txt", requirements_content)
    create_file(".gitignore", gitignore_content)
    create_file("STREAMLIT_README.md", readme_content)
    print("\nFiles are ready! You can now git add . and git push.")