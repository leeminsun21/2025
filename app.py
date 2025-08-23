import streamlit as st
import random # 노래 여러 개 추천할 때 쓰려고!

# 웹 앱 기본 설정
st.set_page_config(
    page_title="내 기분에 딱 맞는 노래 ✨", # 웹페이지 제목
    page_icon="EMOJI_2", # 브라우저 탭 아이콘
    layout="centered" # 페이지 중앙 정렬
)

st.title("오늘 내 분위기에 딱 맞는 노래 추천!") # 앱의 메인 제목
st.markdown("---") # 구분선

# --- 기분 선택 옵션 정의 ---
# dlals이 요청한 '평온' 대신 '잔잔'으로 변경된 상태
mood_options = ["신남", "잔잔", "우울", "나른", "짜증", "생각 많음"]
selected_mood = st.selectbox("오늘 기분이 어때?", mood_options)

# --- 기분별 노래 추천 리스트 (유튜브 링크 포함) ---
# 각 노래는 'title'과 'youtube_url'을 가진 딕셔너리 형태로 저장
songs_by_mood = {
    # dlals이 추천한 '신남' 노래들만 포함!
    "신남": [
        {"title": "BTS (방탄소년단) - 진격의 방탄소년단", "youtube_url": "https://youtu.be/p6a2dM_MnyY"},
        {"title": "BOYNEXTDOOR (보이넥스트도어) - Feelin' Lucky (운수 좋은 날)", "youtube_url": "https://youtu.be/5dJ7d38zQUs"},
        {"title": "세븐틴 (SEVENTEEN) - 아주 NICE", "youtube_url": "https://youtu.be/OwN8jP0F_d4"},
        {"title": "DAY6 (데이식스) - 녹아내려요", "youtube_url": "https://youtu.be/lP2M_vC51tI"},
        {"title": "워너원 (Wanna One) - 에너제틱 (Energetic)", "youtube_url": "https://youtu.be/p0dF3m4Eawc"}
    ],
    # dlals이 추천한 '잔잔' 노래들만 포함!
    "잔잔": [
        {"title": "아이유 - 밤편지", "youtube_url": "https://youtu.be/BzYnjpgEDbY"},
        {"title": "폴킴 - 모든 날, 모든 순간", "youtube_url": "https://youtu.be/23uNqgR3Lkw"},
        {"title": "이하이 - For You", "youtube_url": "https://youtu.be/M_q628rE418"},
        {"title": "이하이 (with B.I) - 머리어깨무릎", "youtube_url": "https://youtu.be/mF8xHh5y1b4"}, # (with B.I) 붙여놨어!
        {"title": "이문세 - 소녀", "youtube_url": "https://youtu.be/lVvJ2uW8C6g"}
    ],
    # dlals이 추천한 '우울' 노래들만 포함!
    "우울": [
        {"title": "이하이 - 한숨", "youtube_url": "https://youtu.be/v-Y9v7VzOAY"},
        {"title": "줍에이 - 혼자여도 괜찮아", "youtube_url": "https://youtu.be/yW133S5rU1g"},
        {"title": "선우정아 - 도망가자", "youtube_url": "https://youtu.be/g3hW236JtHk"},
        {"title": "볼빨간사춘기 - 나의 사춘기에게", "youtube_url": "https://youtu.be/lM5_z0i9MGE"},
        {"title": "최유리 - 숲", "youtube_url": "https://youtu.be/wXo9B6m_n-I"}
    ],
    # 나른, 짜증, 생각 많음은 예시 노래들이 그대로 유지됨
    "나른": [
        {"title": "CHEESE (치즈) - Madeleine Love", "youtube_url": "https://youtu.be/E-Yp_tA22_A"},
        {"title": "DEAN - D (Half Moon)", "youtube_url": "https://youtu.be/jJ4k7N3sH64"},
        {"title": "백예린 - Square (2017)", "youtube_url": "https://youtu.be/u3W2E65IysY"},
        {"title": "윤하 - 오르트구름", "youtube_url": "https://youtu.be/s0aM7x7j7wU"}
    ],
    "짜증": [
        {"title": "NCT DREAM - Hot Sauce", "youtube_url": "https://youtu.be/f-fglM-c4Hw"},
        {"title": "ITZY - DALLA DALLA (달라달라)", "youtube_url": "https://youtu.be/pNfTK39k55U"},
        {"title": "블랙핑크 - DDU-DU DDU-DU (뚜두뚜두)", "youtube_url": "https://youtu.be/IHNzOHi8sJs"},
        {"title": "ATEEZ(에이티즈) - HALAZIA", "youtube_url": "https://youtu.be/F4d_hWlqC4c"}
    ],
    "생각 많음": [
        {"title": "김광석 - 서른 즈음에", "youtube_url": "https://youtu.be/qQ7g8xM8lVw"},
        {"title": "혁오 (HYUKOH) - TOMBOY", "youtube_url": "https://youtu.be/Qy-f06bYnJ4"},
        {"title": "에피톤 프로젝트 - 새는", "youtube_url": "https://youtu.be/n0N1N9R6iQ8"},
        {"title": "장기하와 얼굴들 - 풍문으로 들었소", "youtube_url": "https://youtu.be/1YJ4q3B3l3k"}
    ]
}

# --- 노래 추천 실행 버튼 ---
if st.button("오늘의 노래 추천받기"):
    # 선택된 기분이 songs_by_mood 딕셔너리에 있는지 확인
    if selected_mood in songs_by_mood:
        # 해당 기분에 맞는 노래 리스트에서 랜덤으로 한 곡 선택
        recommended_song = random.choice(songs_by_mood[selected_mood])

        # --- 추천 결과 출력 ---
        st.success(f"### ✨ **{selected_mood}** 기분에 딱 맞는 노래는...")
        st.info(f"## EMOJI_18 `{recommended_song['title']}` EMOJI_19") # 노래 제목 표시
        
        # 유튜브 링크 버튼 생성
        st.link_button("YouTube에서 듣기", recommended_song['youtube_url'])
        
        st.markdown("이 노래로 기분 전환 (혹은 기분 몰입) 해보는 건 어때?")
    else:
        # 만약 선택된 기분에 해당하는 노래 데이터가 없으면 경고 메시지 출력
        st.warning("선택된 기분에 대한 노래 데이터가 아직 없어! 다른 기분을 골라볼까?")

st.markdown("---") # 하단 구분선
st.caption("powered by 부힛 EMOJI_20") # 풋터
