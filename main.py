import streamlit as st

# 🎈 1. MBTI별 취미 데이터를 정의해요 (여기서 데이터는 예시입니다!)
# dlals님이 생각하시는 각 MBTI별 특징에 맞는 취미로 자유롭게 수정하시면 좋아요!
mbti_hobbies = {
    "ISTJ": ["꼼꼼한 자료 정리", "규칙적인 운동", "전통 공예"],
    "ISFJ": ["봉사 활동", "정원 가꾸기", "요리"],
    "INFJ": ["명상", "글쓰기", "심리학 책 읽기"],
    "INTJ": ["전략 게임", "코딩", "과학 다큐 시청"],
    "ISTP": ["캠핑", "목공", "DIY 프로젝트"],
    "ISFP": ["그림 그리기", "음악 연주", "산책"],
    "INFP": ["시 쓰기", "독서 클럽", "여행 계획"],
    "INTP": ["철학 토론", "새로운 기술 탐구", "퍼즐 맞추기"],
    "ESTP": ["스포츠 활동", "즉흥 여행", "새로운 맛집 탐방"],
    "ESFP": ["파티 기획", "댄스", "사교 모임"],
    "ENFP": ["버스킹", "새로운 동호회 가입", "아이디어 회의"],
    "ENTP": ["브레인스토밍", "논쟁", "창업 아이디어 구상"],
    "ESTJ": ["리더십 활동", "규칙적인 운동", "재테크 공부"],
    "ESFJ": ["단체 활동 기획", "친목 도모", "봉사 활동"],
    "ENFJ": ["멘토링", "인문학 스터디", "커뮤니티 운영"],
    "ENTJ": ["사업 계획", "자기계발 스터디", "문제 해결 토론"]
}

# 🌟 2. Streamlit 웹 페이지의 레이아웃과 요소를 구성해요.

st.set_page_config(page_title="MBTI 취미 추천기", page_icon="✨")

st.title("💖 나에게 딱 맞는 MBTI 취미 추천기 💫")
st.write("당신의 MBTI를 선택하고, 몰랐던 나만의 즐거운 취미를 찾아보세요!")

# MBTI 유형들을 정렬해서 드롭다운 메뉴에 보기 좋게 넣어줍니다.
mbti_types = sorted(list(mbti_hobbies.keys()))

# 사용자로부터 MBTI 선택을 받는 드롭다운 메뉴를 만들어요.
selected_mbti = st.selectbox(
    "🤔 당신의 MBTI는 무엇인가요?",
    options=["-- MBTI를 선택해주세요 --"] + mbti_types
)

# 🚀 3. 사용자가 MBTI를 선택했을 때 추천 취미를 보여주는 로직을 작성해요.
if selected_mbti != "-- MBTI를 선택해주세요 --":
    st.markdown(f"### 🎉 **{selected_mbti}** 유형을 위한 추천 취미는 다음과 같아요!")
    
    # 선택된 MBTI에 해당하는 취미 목록을 가져옵니다.
    hobbies = mbti_hobbies.get(selected_mbti, ["앗! 아쉽게도 추천 취미를 찾을 수 없어요. 😢"])
    
    # 각 취미를 목록 형태로 보여줍니다.
    for hobby in hobbies:
        st.write(f"- {hobby}")
        
    st.balloons() # 재미있는 풍선 효과를 추가해서 사용자 경험을 좋게 만들 수 있어요!
    
    st.markdown("---")
    st.caption("😊 본 추천은 일반적인 MBTI 특성을 기반으로 하며, 개인의 성향에 따라 다를 수 있습니다.")
    
else:
    st.info("⬆️ 위에 있는 드롭다운 메뉴에서 당신의 MBTI를 선택해주세요!")
