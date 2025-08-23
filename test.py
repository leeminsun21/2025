import streamlit as st
import random # 노래 여러 개 추천할 때 쓰려고!

# 웹 앱 기본 설정
st.set_page_config(
    page_title="내 기분에 딱 맞는 노래 ✨",
    page_icon="EMOJI_1",
    layout="centered"
)

st.title("EMOJI_2 오늘 내 기분에 딱 맞는 노래 추천! EMOJI_3")
st.markdown("---")

# 기분 선택 옵션
mood_options = ["EMOJI_4 신남", "EMOJI_5 잔잔", "EMOJI_6 우울", "EMOJI_7 나른", "EMOJI_8 짜증", "EMOJI_9 생각 많음"]
selected_mood = st.selectbox("오늘 기분이 어때?", mood_options)

# 기분별 노래 추천 리스트 (노래 정보에 유튜브 링크 추가!)
songs_by_mood = {
    "EMOJI_10 신남": [ # dlals이 추천한 노래만 남겼어!
        {"title": "BTS (방탄소년단) - 진격의 방탄소년단", "youtube_url": "https://youtu.be/p6a2dM_MnyY"},
        {"title": "BOYNEXTDOOR (보이넥스트도어) - Feelin' Lucky (운수 좋은 날)", "youtube_url": "https://youtu.be/5dJ7d38zQUs"},
        {"title": "세븐틴 (SEVENTEEN) - 아주 NICE", "youtube_url": "https://youtu.be/OwN8jP0F_d4"},
        {"title": "DAY6 (데이식스) - 녹아내려요", "youtube_url": "https://youtu.be/lP2M_vC51tI"},
        {"title": "워너원 (Wanna One) - 에너제틱 (Energetic)", "youtube_url": "https://youtu.be/p0dF3m4Eawc"}
    ],
    "EMOJI_11 잔잔": [ # 평온 -> 잔잔으로 키 변경 및 노래 리스트 변경!
        {"title": "아이유 - 밤편지", "youtube_url": "https://youtu.be/BzYnjpgEDbY"},
        {"title": "폴킴 - 모든 날, 모든 순간", "youtube_url": "https://youtu.be/23uNqgR3Lkw"},
        {"title": "이하이 - For You", "youtube_url": "https://youtu.be/M_q628rE418"},
        {"title": "이하이 (with B.I) - 머리어깨무릎", "youtube_url": "https://youtu.be/mF8xHh5y1b4"},
        {"title": "이문세 - 소녀", "youtube_url": "https://youtu.be/lVvJ2uW8C6g"}
    ],
    "EMOJI_12 우울": [ # EMOJI_13 dlals이 새로 추가 요청한 노래들!
        {"title": "이하이 - 한숨", "youtube_url": "https://youtu.be/v-Y9v7VzOAY"},
        {"title": "줍에이 - 혼자여도 괜찮아", "youtube_url": "https://youtu.be/yW133S5rU1g"},
        {"title": "선우정아 - 도망가자", "youtube_url": "https://youtu.be/g3hW236JtHk"},
        {"title": "볼빨간사춘기 - 나의 사춘기에게", "youtube_url": "https://youtu.be/lM5_z0i9MGE"},
        {"title": "최유리 - 숲", "youtube_url": "https://youtu.be/wXo9B6m_n-I"}
    ],
    "EMOJI_14 나른": [
        {"title": "CHEESE (치즈) - Madeleine Love", "youtube_url": "https://youtu.be/E-Yp_tA22_A"},
        {"title": "DEAN - D (Half Moon)", "youtube_url": "https://youtu.be/jJ4k7N3sH64"},
        {"title": "백예린 - Square (2017)", "youtube_url": "https://youtu.be/u3W2E65IysY"},
        {"title": "윤하 - 오르트구름", "youtube_url": "https://youtu.be/s0aM7x7j7wU"}
    ],
    "EMOJI_15 짜증": [
        {"title": "NCT DREAM - Hot Sauce", "youtube_url": "https://youtu.be/f-fglM-c4Hw"},
        {"title": "ITZY - DALLA DALLA (달라달라)", "youtube_url": "https://youtu.be/pNfTK39k55U"},
        {"title": "블랙핑크 - DDU-DU DDU-DU (뚜두뚜두)", "youtube_url": "https://youtu.be/IHNzOHi8sJs"},
        {"title": "ATEEZ(에이티즈) - HALAZIA", "youtube_url": "https://youtu.be/F4d_hWlqC4c"}
    ],
    "EMOJI_16 생각 많음": [
        {"title": "김광석 - 서른 즈음에", "youtube_url": "https://youtu.be/qQ7g8xM8lVw"},
        {"title": "혁오 (HYUKOH) - TOMBOY", "youtube_url": "https://youtu.be/Qy-f06bYnJ4"},
        {"title": "에피톤 프로젝트 - 새는", "youtube_url": "https://youtu.be/n0N1N9R6iQ8"},
        {"title": "장기하와 얼굴들 - 풍문으로 들었소", "youtube_url": "https://youtu.be/1YJ4q3B3l3k"}
    ]
}

# 선택된 기분에 따라 노래 추천!
if st.button("오늘의 노래 추천받기 EMOJI_17"):
    if selected_mood in songs_by_mood:
        # 해당 기분에 맞는 노래 중 랜덤으로 하나 선택 (이제 노래 정보가 딕셔너리!)
        recommended_song = random.choice(songs_by_mood[selected_mood])

        st.success(f"### ✨ **{selected_mood}** 기분에 딱 맞는 노래는...")
        st.info(f"## EMOJI_18 `{recommended_song['title']}` EMOJI_19") # 노래 제목만 보여주고
        st.link_button("YouTube에서 듣기", recommended_song['youtube_url']) # 유튜브 링크 버튼 생성!
        st.markdown("이 노래로 기분 전환 (혹은 기분 몰입) 해보는 건 어때?")
    else:
        st.warning("선택된 기분에 대한 노래 데이터가 아직 없어! 다른 기분을 골라볼까?")

st.markdown("---")
st.caption("powered by 부힛 EMOJI_20")
