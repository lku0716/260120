# app.py
import streamlit as st

st.set_page_config(
    page_title="자기소개",
    page_icon="👋",
    layout="centered"
)

# ====== 사이드바 ======
st.sidebar.title("⚙️ 설정")
photo_source = st.sidebar.radio("사진 가져오기", ["로컬 이미지 사용", "이미지 URL 사용"])

# 로컬 이미지를 쓸 경우: 같은 폴더에 profile.jpg 를 두세요.
# URL을 쓸 경우: 아래 입력칸에 이미지 링크를 넣으세요.
img = None
if photo_source == "로컬 이미지 사용":
    img_path = st.sidebar.text_input("로컬 이미지 파일명", value="profile.jpg")
    try:
        img = img_path
    except:
        img = None
else:
    img_url = st.sidebar.text_input(
        "이미지 URL",
        value="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?w=900"
    )
    img = img_url

name = st.sidebar.text_input("이름", value="이경업")
one_liner = st.sidebar.text_input("한 줄 소개", value="신학생으로서 말씀과 공동체를 사랑합니다.")
greeting = st.sidebar.text_area("인사말", value="안녕하세요! 만나서 반갑습니다 👋")

# ====== 메인 ======
st.title("👋 자기소개 웹 앱")
st.caption("Streamlit로 만든 간단한 소개 페이지")

col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    # 이미지 표시
    st.image(img, caption="My Photo", use_container_width=True)

with col2:
    st.header(f"{name}")
    st.write(f"**{one_liner}**")
    st.write(greeting)

st.divider()

# 소개 섹션들
st.subheader("🧾 About")
st.write(
    "저는 사람들을 세우고, 말씀을 더 잘 이해하고 전하기 위해 배우는 중입니다. "
    "작은 습관과 꾸준한 훈련이 큰 변화를 만든다고 믿어요."
)

st.subheader("🧰 Skills / Interests")
st.write("- 설교/성경공부 준비 ✍️")
st.write("- 영어 말하기 연습 🇬🇧")
st.write("- 청년부 리딩 및 모임 기획 🧑‍🤝‍🧑")

st.subheader("📌 This week’s focus")
focus = st.text_input("이번 주 집중할 것", value="말씀 묵상 + 영어 10분 스피킹")
st.success(f"✅ 이번 주 목표: {focus}")

st.divider()

# 연락처
st.subheader("📮 Contact")
st.write("원하시면 아래에 연락처를 추가해 꾸밀 수 있어요.")
email = st.text_input("Email", value="your_email@example.com")
insta = st.text_input("Instagram", value="@your_id")

st.markdown(
    f"""
**Email:** {email}  
**Instagram:** {insta}
"""
)

# 푸터
st.caption("Made with Streamlit ✨")
