import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="샘플교회 | 소개",
    page_icon="⛪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# SIMPLE THEME CSS
# -----------------------------
def inject_css():
    st.markdown(
        """
        <style>
        /* 전체 배경/폰트 */
        .stApp {
            background: radial-gradient(circle at 10% 10%, rgba(255,255,255,0.9), rgba(245,247,255,0.95) 45%, rgba(245,245,245,0.95));
            color: #111827;
        }

        /* 본문 폭 살짝 넓게 */
        .block-container {
            padding-top: 2.2rem;
            padding-bottom: 2.2rem;
            max-width: 1200px;
        }

        /* 섹션 타이틀 */
        .section-title {
            font-size: 1.55rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            margin: 0 0 0.75rem 0;
        }

        .muted {
            color: rgba(17,24,39,0.70);
            font-size: 0.98rem;
            line-height: 1.6;
        }

        /* 히어로 */
        .hero {
            border-radius: 22px;
            padding: 34px 34px 30px 34px;
            background: linear-gradient(135deg, rgba(99,102,241,0.18), rgba(59,130,246,0.12), rgba(255,255,255,0.70));
            border: 1px solid rgba(17,24,39,0.08);
            box-shadow: 0 12px 34px rgba(0,0,0,0.06);
        }
        .hero h1 {
            font-size: 2.35rem;
            line-height: 1.15;
            letter-spacing: -0.04em;
            margin: 0 0 0.6rem 0;
        }
        .hero-badges {
            display: flex;
            gap: 10px;
            margin: 16px 0 4px 0;
            flex-wrap: wrap;
        }
        .badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 12px;
            border-radius: 999px;
            background: rgba(255,255,255,0.75);
            border: 1px solid rgba(17,24,39,0.08);
            font-size: 0.92rem;
        }

        /* 카드 */
        .card {
            border-radius: 18px;
            padding: 18px 18px;
            background: rgba(255,255,255,0.74);
            border: 1px solid rgba(17,24,39,0.08);
            box-shadow: 0 10px 26px rgba(0,0,0,0.05);
            height: 100%;
        }
        .card h3 {
            margin: 0 0 0.35rem 0;
            font-size: 1.12rem;
            letter-spacing: -0.02em;
        }
        .card p {
            margin: 0.25rem 0 0 0;
            color: rgba(17,24,39,0.72);
            line-height: 1.55;
        }

        /* 구분선 */
        .soft-divider {
            height: 1px;
            background: rgba(17,24,39,0.08);
            margin: 26px 0;
        }

        /* CTA 영역 */
        .cta {
            border-radius: 22px;
            padding: 22px 22px;
            background: linear-gradient(135deg, rgba(16,185,129,0.13), rgba(59,130,246,0.10), rgba(255,255,255,0.72));
            border: 1px solid rgba(17,24,39,0.08);
            box-shadow: 0 10px 26px rgba(0,0,0,0.05);
        }

        /* 푸터 */
        .footer {
            margin-top: 26px;
            color: rgba(17,24,39,0.55);
            font-size: 0.92rem;
            text-align: center;
        }

        /* Streamlit 버튼 조금 더 "웹" 느낌 */
        div.stButton > button {
            border-radius: 12px !important;
            padding: 0.6rem 0.95rem !important;
            font-weight: 700 !important;
            border: 1px solid rgba(17,24,39,0.10) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

inject_css()

# -----------------------------
# DATA (여기만 바꿔도 전체가 바뀜)
# -----------------------------
CHURCH = {
    "name": "샘플교회",
    "tagline": "복음으로 살고, 사랑으로 섬기며, 소망을 전하는 공동체",
    "address": "서울특별시 ○○구 ○○로 123",
    "phone": "02-000-0000",
    "email": "contact@samplechurch.org",
    "kakao": "카카오채널: 샘플교회",
    "youtube": "YouTube: 샘플교회",
}

WORSHIP = [
    {"title": "주일예배", "time": "주일 11:00", "place": "본당 2F"},
    {"title": "청년예배", "time": "주일 14:00", "place": "비전홀 3F"},
    {"title": "수요예배", "time": "수요일 19:30", "place": "본당 2F"},
    {"title": "새벽기도", "time": "월-금 05:30", "place": "본당 2F"},
]

MINISTRIES = [
    {"title": "청년부", "desc": "말씀과 교제, 삶의 적용을 함께 세워가는 공동체"},
    {"title": "새가족", "desc": "처음 오신 분들이 편안히 정착할 수 있도록 안내합니다"},
    {"title": "교육부", "desc": "다음세대가 복음 위에 자라가도록 돕습니다"},
    {"title": "섬김/봉사", "desc": "예배, 안내, 미디어, 찬양 등 다양한 영역에서 섬깁니다"},
]

VALUES = [
    {"title": "말씀 중심", "desc": "성경을 통해 하나님을 알고 삶의 방향을 세웁니다"},
    {"title": "복음의 공동체", "desc": "서로를 세우며 함께 성장하는 교회"},
    {"title": "선교적 삶", "desc": "세상 가운데 빛과 소금으로 살아갑니다"},
]

# -----------------------------
# SIDEBAR NAV
# -----------------------------
st.sidebar.markdown(f"## ⛪ {CHURCH['name']}")
st.sidebar.caption(CHURCH["tagline"])
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "메뉴",
    ["홈", "교회 소개", "예배 안내", "섬김/사역", "오시는 길", "문의하기"],
    index=0,
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 빠른 연락")
st.sidebar.write(f"📍 {CHURCH['address']}")
st.sidebar.write(f"☎️ {CHURCH['phone']}")
st.sidebar.write(f"✉️ {CHURCH['email']}")
st.sidebar.write(f"💬 {CHURCH['kakao']}")
st.sidebar.write(f"▶️ {CHURCH['youtube']}")

# -----------------------------
# UI HELPERS
# -----------------------------
def section(title: str, desc: str = ""):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if desc:
        st.markdown(f'<div class="muted">{desc}</div>', unsafe_allow_html=True)

def card(title: str, desc: str):
    st.markdown(
        f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def divider():
    st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

# -----------------------------
# PAGES
# -----------------------------
if menu == "홈":
    st.markdown(
        f"""
        <div class="hero">
            <h1>{CHURCH['name']}</h1>
            <div class="muted" style="font-size:1.05rem;">
                {CHURCH['tagline']}
            </div>
            <div class="hero-badges">
                <div class="badge">📖 말씀 중심</div>
                <div class="badge">🤝 공동체</div>
                <div class="badge">🌍 선교적 삶</div>
                <div class="badge">☕ 새가족 환영</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    divider()

    c1, c2, c3 = st.columns(3, gap="large")
    with c1:
        card("처음 오셨나요?", "새가족 안내와 예배 동선을 친절히 도와드립니다.")
    with c2:
        card("예배 시간", "주일예배 11:00 | 청년예배 14:00 | 수요예배 19:30")
    with c3:
        card("함께하는 삶", "소그룹, 기도모임, 봉사로 믿음을 일상에서 이어갑니다.")

    divider()

    st.markdown('<div class="cta">', unsafe_allow_html=True)
    section("이번 주 함께 예배해요 🙌", "처음 오셔도 괜찮아요. 편하게 오시면 됩니다.")
    b1, b2, b3 = st.columns([1, 1, 2])
    with b1:
        if st.button("예배 안내 보기"):
            st.session_state["nav"] = "예배 안내"
            st.rerun()
    with b2:
        if st.button("문의하기"):
            st.session_state["nav"] = "문의하기"
            st.rerun()
    with b3:
        st.markdown(
            f'<div class="muted">📍 {CHURCH["address"]} | ☎️ {CHURCH["phone"]}</div>',
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "교회 소개":
    section("교회 소개", "우리는 예수 그리스도의 복음으로 모이고, 사랑으로 섬기며, 소망을 전합니다.")
    divider()

    section("핵심 가치", "교회의 방향을 잡아주는 세 가지 기둥")
    c1, c2, c3 = st.columns(3, gap="large")
    for col, item in zip([c1, c2, c3], VALUES):
        with col:
            card(item["title"], item["desc"])

    divider()

    section("담임목사 인사말 (예시)", "")
    st.markdown(
        """
        <div class="card">
            <h3>“하나님을 더 알고, 더 사랑하고, 더 닮아가길 소망합니다.”</h3>
            <p>
            샘플교회에 오신 여러분을 진심으로 환영합니다.  
            우리는 완벽한 사람들이 아니라, 은혜로 살아가는 사람들이 함께 모여
            말씀 안에서 회복과 성장을 경험하는 공동체입니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif menu == "예배 안내":
    section("예배 안내", "시간과 장소를 한눈에 확인하세요.")
    divider()

    cols = st.columns(4, gap="large")
    for i, w in enumerate(WORSHIP):
        with cols[i % 4]:
            st.markdown(
                f"""
                <div class="card">
                    <h3>{w['title']}</h3>
                    <p><b>시간</b> · {w['time']}</p>
                    <p><b>장소</b> · {w['place']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    divider()
    section("안내", "주차/유아실/새가족 안내 등")
    st.info("• 예배 15분 전 오시면 안내팀이 도와드립니다.\n• 유아실/수유실이 준비되어 있습니다.\n• 처음 오신 분은 로비 새가족 데스크로 와주세요 😊")

elif menu == "섬김/사역":
    section("섬김/사역", "각 사람의 은사로 교회를 세워갑니다.")
    divider()

    cols = st.columns(2, gap="large")
    for i, m in enumerate(MINISTRIES):
        with cols[i % 2]:
            card(m["title"], m["desc"])

    divider()
    section("봉사 지원", "섬김은 ‘교회 일을 더하는 것’이 아니라 ‘사랑을 나누는 방식’입니다.")
    st.success("원하시면 예배 후 안내팀에게 말씀해주세요. 지원서를 드립니다 🙏")

elif menu == "오시는 길":
    section("오시는 길", "지도/교통편 안내")
    divider()

    left, right = st.columns([1.1, 0.9], gap="large")
    with left:
        st.markdown(
            f"""
            <div class="card">
                <h3>주소</h3>
                <p>{CHURCH['address']}</p>
                <p><b>대중교통</b> · (예시) ○○역 3번 출구 도보 8분</p>
                <p><b>주차</b> · (예시) 지하 1-2층 주차장 이용</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        # Streamlit 기본 지도 (좌표는 예시: 서울시청)
        st.map([{"lat": 37.5665, "lon": 126.9780}])

    st.caption("※ 실제 교회 좌표로 바꾸려면 st.map의 lat/lon 값을 수정하세요.")

elif menu == "문의하기":
    section("문의하기", "연락 주시면 빠르게 답변드릴게요 🙂")
    divider()

    with st.form("contact_form"):
        name = st.text_input("이름")
        contact = st.text_input("연락처(전화/카톡/이메일 중 하나)")
        message = st.text_area("문의 내용", height=140)
        agree = st.checkbox("개인정보 수집 및 이용에 동의합니다.")
        submitted = st.form_submit_button("보내기")

    if submitted:
        if not (name and contact and message and agree):
            st.error("모든 항목을 입력하고 동의에 체크해주세요!")
        else:
            # 실제 저장/발송은 DB/이메일 연동 필요 (여기서는 UI만)
            st.success("접수되었습니다! 곧 연락드릴게요 🙌")
            st.write("입력 요약")
            st.code(f"이름: {name}\n연락처: {contact}\n문의: {message}")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
    f"""
    <div class="footer">
        © {CHURCH['name']} · {CHURCH['address']} · {CHURCH['phone']} · {CHURCH['email']}
    </div>
    """,
    unsafe_allow_html=True,
)

# Quick nav via session_state (for CTA buttons)
if "nav" in st.session_state:
    # Streamlit은 sidebar radio를 직접 강제 변경하기가 까다로워서
    # CTA는 rerun 트리거로만 두고, 실제 페이지 이동은 menu에서 선택하도록 안내
    st.session_state.pop("nav", None)
