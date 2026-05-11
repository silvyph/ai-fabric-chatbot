import streamlit as st
import google.generativeai as genai

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Chat Fabric Stylist",
    page_icon="🧵",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f8f5ff, #eef4ff);
}

.main-title {
    font-size: 48px;
    font-weight: 800;
    color: #2b2d42;
    text-align: center;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #555;
    font-size: 18px;
    margin-bottom: 30px;
}

.user-bubble {
    background: #6c63ff;
    color: white;
    padding: 14px;
    border-radius: 18px;
    margin: 10px 0;
    width: fit-content;
    margin-left: auto;
    max-width: 80%;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.bot-bubble {
    background: white;
    color: #222;
    padding: 16px;
    border-radius: 18px;
    margin: 10px 0;
    width: fit-content;
    max-width: 80%;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    border: 1px solid #ececec;
}

.category-card {
    background: white;
    padding: 18px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# GEMINI API
# =========================
genai.configure(api_key="AIzaSyCFmUsicq2O-R_gn35Ycgek3Ql7A-D_oIU")
model = genai.GenerativeModel("gemini-2.5-flash")

# =========================
# LOAD DATASET (RAG SEDERHANA)
# =========================
import pandas as pd

# Pastikan file fabric_dataset.csv ada di folder project
try:
    df = pd.read_csv("fabric_dataset.csv")
except:
    df = pd.DataFrame()

# Function retrieval sederhana
def search_fabric_data(user_question):

    if df.empty:
        return "Dataset kain tidak ditemukan."

    results = []

    for _, row in df.iterrows():

        fabric_name = str(row.iloc[0]).lower()

        if user_question and fabric_name in str(user_question).lower():
            results.append(str(row.to_dict()))

    if len(results) == 0:
        return "Tidak ada data spesifik yang cocok di dataset."

    return "\n".join(results)

# =========================
# HEADER
# =========================
st.markdown('<div class="main-title">🧵 AI Fabric Stylist</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI Fashion Assistant untuk rekomendasi bahan kain, outfit, dan fashion styling ✨</div>',
    unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.title("✨ Menu")

    style = st.selectbox(
        "Pilih Style Fashion",
        [
            "Casual",
            "Formal",
            "Streetwear",
            "Olahraga",
            "Hijab Fashion",
            "Vintage"
        ]
    )

    gender = st.radio(
        "Kategori",
        ["Pria", "Wanita", "Unisex"]
    )

    st.markdown("---")
    st.write("### 💡 Contoh Pertanyaan")

    st.write("- Bahan adem untuk kemeja kantor")
    st.write("- Kain terbaik untuk sport bra")
    st.write("- Outfit bahan linen cocok dipadukan dengan apa?")
    st.write("- Bahan premium untuk dress")

# =========================
# CATEGORY SECTION
# =========================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        '<div class="category-card">👔<br><b>Kemeja</b></div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="category-card">🏋️<br><b>Sportswear</b></div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div class="category-card">👗<br><b>Dress</b></div>',
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        '<div class="category-card">🧥<br><b>Outerwear</b></div>',
        unsafe_allow_html=True
    )

st.markdown("---")

# =========================
# SESSION STATE
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# DISPLAY CHAT HISTORY
# =========================
for message in st.session_state.messages:

    if message["role"] == "user":
        st.markdown(
            f'<div class="user-bubble">🧑 {message["content"]}</div>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f'<div class="bot-bubble">🤖 {message["content"]}</div>',
            unsafe_allow_html=True
        )

# =========================
# CHAT INPUT
# =========================
prompt = st.chat_input("Tanyakan tentang fashion dan bahan kain...")

if prompt:

    # Simpan pesan user
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Tampilkan bubble user
    st.markdown(
        f'<div class="user-bubble">🧑 {prompt}</div>',
        unsafe_allow_html=True
    )

    # =========================
    # RAG RETRIEVAL
    # =========================
    retrieved_data = search_fabric_data(prompt)

    # Gemini response
    response = model.generate_content(
        contents=f'''
        Kamu adalah AI fashion stylist dan ahli bahan kain.

        Style fashion user: {style}
        Preferensi fashion tambahan: {gender}

        Jawab berdasarkan konteks fashion dari pertanyaan user.
        Jangan mengubah konteks pertanyaan menjadi khusus pria atau wanita kecuali user meminta secara eksplisit.

        Data kain dari dataset internal:
        {retrieved_data}

        WAJIB gunakan data dataset internal sebagai sumber utama jawaban jika kain ditemukan.

        Tampilkan:
        - karakteristik
        - tekstur
        - ketebalan
        - range harga
        - tips perawatan

        Setelah itu baru boleh tambahkan penjelasan fashion tambahan.

        Tugas kamu:
        - Merekomendasikan bahan kain
        - Memberikan saran outfit
        - Menjelaskan karakteristik kain
        - Memberi tips fashion

        Jawab dengan santai, modern, dan friendly.

        Riwayat percakapan:
        {st.session_state.messages}

        Pertanyaan user:
        {prompt}
        '''
    )

    ai_reply = response.text

    # Simpan jawaban AI
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_reply
    })

    # Tampilkan bubble AI
    st.markdown(
        f'<div class="bot-bubble">🤖 {ai_reply}</div>',
        unsafe_allow_html=True
    )