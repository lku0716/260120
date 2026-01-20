
import streamlit as st
from streamlit_option_menu import option_menu

# 1. 페이지 설정
st.set_page_config(
    page_title="예수중심교회",
    page_icon="⛪",
    layout="wide"
)

# 2. 커스텀 CSS (모던 & 화려한 스타일)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;400;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stApp {
        color: #2C3E50;
    }
    .hero-text {
        text-align: center;
        padding: 50px;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 사이드바 내비게이션 (모던한 메뉴)
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1438232992991-995b7058bbb3?auto=format&fit=crop&q=80&w=300", caption="오직 예수 🕊️")
    selected = option_menu(
        "Menu", ["홈 (Home)", "교회소개", "예배안내", "청년부(팀)"],
        icons=['house', 'info-circle', 'clock', 'people'],
        menu_icon="cast", default_index=0,
        styles={
            "container": {"padding": "5px!", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#2C3E50"},
        }
    )

# 4. 페이지별 콘텐츠
if selected == "홈 (Home)":
    st.markdown("""
        <div class="hero-text">
            <h1 style='font-size: 3rem; color: #1A5276;'>🕆 예수중심교회</h1>
            <p style='font-size: 1.2rem;'>하나님의 말씀이 삶의 중심이 되는 공동체</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("##")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("### ✨ 오늘의 말씀")
        # 개역한글 번역본 적용
        st.write("*" + "태초에 하나님이 천지를 창조하시니라" + "*")
        st.caption("(창세기 1:1)")
    
    with col2:
        st.success("### 📢 공지사항")
        st.write("✔️ 이번 주 성경 공부 모임 안내")
        st.write("✔️ 새가족 환영회 (주일 오후 2시)")

elif selected == "교회소개":
    st.title("📖 교회 소개")
    st.markdown("---")
    st.write("#### 🔹 믿음의 고백")
    st.write("우리 예수중심교회는 **개혁주의 신학**에 기초하여 성경의 권위를 인정하며, 하나님 중심, 성경 중심, 교회 중심의 삶을 지향합니다.")
    st.image("https://images.unsplash.com/photo-1544427920-c49ccfb85579?auto=format&fit=crop&q=80&w=800", use_column_width=True)

elif selected == "예배안내":
    st.title("⏰ 예배 및 집회 안내")
    st.markdown("---")
    
    data = {
        "구분": ["주일 대예배", "청년부 예배", "수요 기도회", "새벽 기도회"],
        "시간": ["오전 11:00", "오후 02:00", "오후 07:30", "오전 05:30"],
        "장소": ["본당 2층", "소예배실", "본당 1층", "온라인/본당"]
    }
    st.table(data)

elif selected == "청년부(팀)":
    st.title("👥 청년부 공동체")
    st.write("현재 **15명의 소중한 팀원**들이 함께 모여 삶과 신앙을 나누고 있습니다.")
    
    # 팀 리더(사용자) 섹션
    st.markdown("""
        <div style="background-color: #EBF5FB; padding: 20px; border-left: 5px solid #2E86C1; border-radius: 10px;">
            <h4 style="margin:0;">🎖️ 팀장 메시지</h4>
            <p>"우리가 알거니와 하나님을 사랑하는 자 곧 그 뜻대로 부르심을 입은 자들에게는 모든 것이 합력하여 선을 이루느니라" (로마서 8:28)</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("##")
    st.subheader("📸 활동 갤러리")
    col1, col2, col3 = st.columns(3)
    col1.image("https://images.unsplash.com/photo-1529070538774-1843cb3265df?auto=format&fit=crop&q=80&w=200")
    col2.image("https://images.unsplash.com/photo-1511632765486-a01980e01a18?auto=format&fit=crop&q=80&w=200")
    col3.image("https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&q=80&w=200")

# 5. 푸터
st.divider()
st.center = st.markdown("<p style='text-align: center; color: gray;'>© 2026 예수중심교회 | God is always with you :) </p>", unsafe_allow_html=True)
