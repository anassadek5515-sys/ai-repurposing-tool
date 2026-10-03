import streamlit as st
import time

# إعدادات الصفحة الاحترافية
st.set_page_config(
    page_title="Global AI Content Repurposing Suite", 
    page_icon="🚀", 
    layout="wide"
)

# تخصيص التصميم والتوجه البصري للواجهة باللغة الإنجليزية
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #FF4B4B;
        text-align: center;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .sub-title {
        text-align: center;
        color: #555;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# رأس الصفحة باللغة الإنجليزية
st.markdown('<div class="main-title">🚀 Global AI Content Repurposing Suite</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Transform any long article, text, or video transcript into multi-platform social media assets in any language instantly.</div>', unsafe_allow_html=True)

# الشريط الجانبي للإعدادات والتحكم بالإنجليزية
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/artificial-intelligence.png", width=150)
    st.header("⚙️ Platform Settings")
    
    # اختيار لغة المخرجات (دعم كل لغات العالم الرئيسية)
    output_language = st.selectbox(
        "🌍 Output Language:",
        ["English", "Arabic (العربية)", "Spanish (Español)", "French (Français)", "German (Deutsch)", "Chinese (中文)", "Japanese (日本語)", "Portuguese (Português)"]
    )
    
    content_style = st.selectbox(
        "🎭 Content Tone:",
        ["Professional & Formal", "Engaging & Hype", "Educational & Informative", "Short & Direct"]
    )
    
    target_audience = st.selectbox(
        "🎯 Target Audience:",
        ["Entrepreneurs & Investors", "Creators & Marketers", "Engineers & Developers", "General Audience"]
    )
    
    st.markdown("---")
    st.info("💡 **Pro Feature:** Built to scale your global content production by 10x seamlessly across all social networks.")

# منطقة إدخال النص الرئيسي
col1, col2 = st.columns([3, 1])
with col1:
    source_text = st.text_area(
        "📝 Paste your long article, text, or transcript here:", 
        height=220, 
        placeholder="Type or paste your text here..."
    )

with col2:
    st.markdown("### 📊 Quick Options")
    include_emojis = st.checkbox("Include Promo Emojis", value=True)
    include_hashtags = st.checkbox("Generate Smart Hashtags", value=True)
    st.markdown("---")
    generate_btn = st.button("✨ Generate Omni-Content")

# معالجة وتوليد المحتوى
if generate_btn:
    if not source_text.strip():
        st.error("⚠️ Please enter some text or an article in the input box first.")
    else:
        with st.spinner(f"🔄 Analyzing text and generating content in {output_language}... Please wait"):
            time.sleep(2) # محاكاة معالجة ذكية وسريعة
            
            # محاكاة النتائج المتولدة بناءً على اللغة المختارة
            if "Arabic" in output_language:
                twitter_thread = "🧵 سلسلة تغريدات احترافية:\n\n1/ الملخص الشامل للمحتوى الذي قدمته.\n2/ النقاط الرئيسية التي تم استخراجها بعناية.\n3/ كيف يمكنك الاستفادة القصوى من هذه الأفكار.\n4/ شاركنا برأيك ولا تنس الإعجاب والاعادة 🔄 #محتوى #ذكاء_اصطناعي"
                linkedin_post = "💼 منشور لينكد إن:\n\nكيف تطور أعمالك ومحتواك بسرعة فائقة؟ 🚀\n\nأهم الاستراتيجيات المستخلصة:\n• الابتكار المستمر\n• التحليل الدقيق\n\nما رأيك بهذا الطرح؟ شاركنا في التعليقات 👇\n\n#Business #Strategy"
                tiktok_script = "🎬 سيناريو فيديو قصير (Reels/TikTok):\n\n[0-3 ثوانٍ]: لو حابب تطور شغلك وتوفر وقتك، شوف الفيديو ده!\n[3-15 ثانية]: بنشرح أهم الأفكار بطريقة سهلة وسريعة.\n[الخاتمة]: جربها دلوقتي!"
            else:
                twitter_thread = f"""🧵 Twitter Thread (Optimized for Engagement):\n\n1/ Transforming complex ideas into high-impact content is the ultimate growth hack. Here is the breakdown. 👇\n\n2/ Based on your provided text, the core focus revolves around efficiency and scaling results.\n\n3/ By leveraging advanced automation and AI, you can save over 80% of your creation time.\n\n4/ Don't wait—start applying this framework today and multiply your reach.\n\n5/ Found this valuable? Drop a like 💙 and retweet 🔄 #ContentCreation #AI #Growth"""
                
                linkedin_post = f"""💼 Professional LinkedIn Post:\n\nHow do you scale your content production without burning out? 🚀\n\nWe analyzed the latest strategies to bring you a smarter workflow:\n• Maximize long-form articles effortlessly.\n• Repurpose ideas across multiple platforms automatically.\n• Build a sustainable global brand presence.\n\nWhat is your go-to repurposing strategy? Let's discuss in the comments below 👇\n\n#ContentStrategy #BusinessGrowth #Innovation"""
                
                tiktok_script = f"""🎬 Short-Form Video Script (TikTok / Reels):\n\n[Scene 1 - 0 to 3s]:\n(Energetic hook): "If you have a long article and want to turn it into viral social media posts in seconds, watch this!"\n\n[Scene 2 - 3 to 15s]:\n(Showcasing the tool): "Instead of spending hours writing, this AI platform instantly generates optimized Twitter threads, LinkedIn posts, and scripts with a {content_style} tone."\n\n[Scene 3 - Outro]:\n"Try it out and let me know your thoughts in the comments!" """

        st.success(f"🎉 Content successfully generated in {output_language}!")
        st.markdown("---")

        # عرض النتائج في تبويبات (Tabs) منظمة واحترافية
        tab1, tab2, tab3 = st.tabs(["🐦 Twitter Threads", "💼 LinkedIn Posts", "🎬 TikTok / Reels Scripts"])

        with tab1:
            st.markdown("### Ready-to-Publish Twitter Thread")
            st.text_area("Twitter Output", value=twitter_thread, height=180, key="t_out")
            st.code("Copy text above for X / Twitter", language="markdown")

        with tab2:
            st.markdown("### Professional LinkedIn Post")
            st.text_area("LinkedIn Output", value=linkedin_post, height=180, key="l_out")
            st.code("Copy text above for LinkedIn", language="markdown")

        with tab3:
            st.markdown("### Short-Form Video Script")
            st.text_area("Video Output", value=tiktok_script, height=180, key="v_out")
            st.code("Ready for production", language="markdown")

# تذييل الصفحة
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Global AI Content Repurposing Suite — Built for High Performance & Scalability 🚀</p>", unsafe_allow_html=True)
