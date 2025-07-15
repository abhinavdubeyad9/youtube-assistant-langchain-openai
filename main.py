import streamlit as st
from langchain_helper import create_vector_db_from_youtube_url, get_response_from_query
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="YouTube Assistant", layout="wide", page_icon="🎬")

# --- HEADER ---
st.markdown(
    """
    <h1 style='text-align: center; color: #F63366;'>🎬 YouTube Assistant</h1>
    <p style='text-align: center; font-size: 18px; color: #AAAAAA;'>Ask questions about any YouTube video using its transcript</p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- INPUT SECTION ---
with st.container():
    left, right = st.columns([1, 3])
    
    with left:
        st.markdown("### Paste YouTube Video URL")
    with right:
        youtube_url = st.text_area("", placeholder="https://youtu.be/xyz...", height=70)

    st.markdown("### What is your question?")
    query = st.text_area("", placeholder="e.g., What are the key takeaways?", height=70)

    submit = st.button("💬 Submit", use_container_width=True)

# --- PROCESSING ---
if submit and youtube_url and query:
    with st.spinner("🔍 Processing video transcript and finding the answer..."):
        db = create_vector_db_from_youtube_url(youtube_url)
        response = get_response_from_query(db, query)

    st.markdown("---")

    # --- ANSWER SECTION ---
    st.markdown(
        """
        <div style="padding: 20px; background-color: #1E1E1E; border-radius: 12px;">
            <h2 style='color: #FAD02C;'>🧠 Answer</h2>
            <p style='font-size: 17px; color: #DDDDDD; line-height: 1.6;'>{}</p>
        </div>
        """.format(response),
        unsafe_allow_html=True
    )

# --- FOOTER ---
st.markdown(
    """
    <hr style="margin-top: 3rem; margin-bottom: 1rem;">
    <p style="text-align: center; font-size: 14px; color: #666;">
    Made with ❤️ using LangChain, OpenAI, and Streamlit
    </p>
    """,
    unsafe_allow_html=True
)
