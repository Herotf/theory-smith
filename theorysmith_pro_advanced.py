import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Simple test version without Ollama dependency
st.set_page_config(page_title="TheorySmith Test", page_icon="🧬")
st.title("🌱 TheorySmith Pro - Test Version")

st.markdown("**This is a test to make sure Streamlit is working correctly**")

# Simple interface
user_input = st.text_area("Enter your theory:", height=100)

if st.button("🧪 Test Analysis"):
    if user_input:
        st.success("✅ Interface working!")
        st.markdown(f"**Your input:** {user_input}")
        
        # Simple plot test
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title("Test Plot - Sine Wave")
        st.pyplot(fig)
        
        st.markdown("**Next step:** Make sure Ollama is running with `ollama serve`")
    else:
        st.warning("Please enter some text first")

# Status check
st.sidebar.header("System Check")
try:
    import ollama
    st.sidebar.success("✅ Ollama package installed")
    
    # Try to connect
    try:
        models = ollama.list()
        st.sidebar.success("✅ Ollama server reachable")
        if any('llama3' in model['name'] for model in models.get('models', [])):
            st.sidebar.success("✅ Llama3 model found")
        else:
            st.sidebar.warning("⚠️ Llama3 model not found. Run: `ollama pull llama3`")
    except Exception as e:
        st.sidebar.error(f"❌ Ollama server not running: {e}")
        st.sidebar.markdown("Run `ollama serve` in terminal")
        
except ImportError:
    st.sidebar.error("❌ Ollama not installed")
    st.sidebar.markdown("Install with: `pip install ollama`")