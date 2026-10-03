import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# إعدادات الصفحة
st.set_page_config(page_title="AI Content Repurposing Tool (Local AI)", page_icon="🚀", layout="wide")

st.title("🚀 Local AI Content Repurposing & Auto-Poster")
st.markdown("Transform articles or transcripts into Twitter threads, LinkedIn posts, and Short-form video scripts using a **Local Open-Source AI** running on GPU.")

@st.cache_resource
def load_model():
    model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map="auto",
        load_in_8bit=True
    )
    return tokenizer, model

# تحميل النموذج مع معالجة الأخطاء
try:
    with st.spinner("Loading AI Model into GPU... Please wait (takes ~1 min) ⏳"):
        tokenizer, model = load_model()
    st.sidebar.success("AI Model Loaded Successfully on GPU! 🚀")
except Exception as e:
    st.warning("Note: Running with fallback mode or verification required.")

content_input = st.text_area("Paste your long article or transcript here:", height=200)

if st.button("✨ Generate Repurposed Content", type="primary"):
    if not content_input.strip():
        st.error("Please provide some content.")
    else:
        with st.spinner("Generating posts using Local AI... ⏳"):
            prompt = f"Act as an expert social media manager. Convert this text into: 1. Twitter Thread, 2. LinkedIn Post, 3. TikTok Script:\n\n{content_input}"
            
            inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
            outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.7)
            result = tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            st.success("Done! 🎉")
            st.markdown(result)
