# pages/00_introduce.py
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="자기소개", page_icon="👋", layout="centered")

st.sidebar.title("⚙️ 설정")
photo_source = st.sidebar.radio(
    "사진 가져오기",
    ["업로드", "이미지 URL", "로컬 파일(Repo에 포함된 파일)"],
    index=0
)

img = None  # st.image에 넣을 대상

if photo_source == "업로드":
    uploaded = st.sidebar.file_uploader(
        "프로필 사진 업로드",
        type=["png", "jpg", "jpeg", "webp"]
    )
    if uploaded is not None:
        img = uploaded

elif photo_source == "이미지 URL":
    img_url = st.sidebar.text_input(
        "이미지 URL",
        value="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?w=900"
    )
    # URL은 문자열 그대로 st.image에 넣어도 OK
    if img_url.strip():
        img = img_url.strip()

else:  # 로컬 파일
    # Streamlit Cloud에서 쓰려면 repo에 실제로 파일이 있어야 함
    # 예: assets/profile.jpg 를 repo에 넣고 아래처럼 지정
    img_path_str = st.sidebar.text_input("로컬 이미지 경로", value="assets/profile.jpg")
    img_path = Path(img_path_str)
    if img_path.exists() and img_path.is_file():
        img = str(img_path)
    else:
        st.sidebar.warning(f"로컬 파일을 찾을 수 없어요: {img_path_str}")

name = st.sidebar.text_input("이름", value="이경업")
one_liner = st.sidebar.text_input("한 줄 소개", value="말씀과 공동체를 사랑하는 신학생입니다.")
greeting = st.sidebar.text_area("인사말", value="안녕하세요! 만나서 반갑습니다 👋")

st.title("👋 자기소개 웹 앱")
st.caption("Streamlit로 만든 간단한 소개 페이지")

col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    if img is not None:
        st.image(img, caption="My Photo", use_container_width=True)
    else:
        # 이미지가 없으면 기본 표시 (절대 안 터짐)
        st.info("📷 사진이 아직 없어요. 왼쪽에서 업로드하거나 URL을 넣어주세요!")
        st.image("https://placehold.co/600x600/png?text=Your+Photo", use_container_width=True)

with col2:
    st.header(name)
    st.write(f"**{one_liner}**")
    st.write(greeting)

st.divider()

st.subheader("🧾 About")
st.write(
    "저는 말씀을 더 잘 이해하고 전하기 위해 배우는 중입니다. "
    "꾸준함이 결국 사람을 만든다고 믿어요."
)

st.subheader("🧰 Skills / Interests")
st.write("- 설교/성경공부 준비 ✍️")
st.write("- 영어 말하기 연습 🇬🇧")
st.write("- 청년부 리딩 및 모임 기획 🧑‍🤝‍🧑")

st.subheader("📌 This week’s focus")
focus = st.text_input("이번 주 집중할 것", value="말씀 묵상 + 영어 10분 스피킹")
st.success(f"✅ 이번 주 목표: {focus}")

st.divider()

st.subheader("📮 Contact")
email = st.text_input("Email", value="your_email@example.com")
insta = st.text_input("Instagram", value="@your_id")
st.markdown(f"**Email:** {email}\n\n**Instagram:** {insta}")

st.caption("Made with Streamlit ✨")
