import streamlit as st

# 🎤 오늘의 기분별 인디 노래 추천 리스트 (임의의 예시니까 dlals가 직접 채워야 하는 부분임! 개성 살리기 쌉가능)
# 유튜브 링크도 YOUR_VIDEO_ID_HERE 부분을 실제 유튜브 영상 ID로 바꾸면 됨!
mood_based_song_recommendations = {
    "신나고 싶음": [
        {"title": "혁오 - 위잉위잉", "artist": "혁오", "link": "https://m.youtube.com/watch?v=GIa80KLuDwc"},
        {"title": "보이넥스트도어 - Fadeaway", "artist": "보이넥스트도어", "link": "https://www.youtube.com/watch?v=AL5SkIfr26A"},
        {"title": "방탄소년단 - 진격의 방탄", "artist": "방탄소년", "link": "https://www.youtube.com/watch?v=7RsFNXsvusw"}
    ],
    "잔잔해지고 싶음": [
        {"title": "옥상달빛 - 수고했어 오늘도", "artist": "옥상달빛", "link": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_4"},
        {"title": "어쿠스틱 콜라보 - 그대와 나 설레임", "artist": "어쿠스틱 콜라보", "link": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_5"},
        {"title": "볼빨간사춘기 - 여행", "artist": "볼빨간사춘기", "link": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_6"} # 볼빨간도 인디는 아니지만, 잔잔하니 좋으니 넣어봄 ㅋㅋㅋ
    ],
    "우울함": [
        {"title": "짙은 - 백야", "artist": "짙은", "link": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_7"},
        {"title": "브로콜리 너마저 - 졸업", "artist": "브로콜리 너마저", "link": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_8"},
        {"title": "치즈 - 모두의 순간", "artist": "치즈", "link": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_9"}
    ],
    "몽환적": [
        {"title": "새소년 - 긴 꿈", "artist": "새소년", "link": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_10"},
        {"title": "ADOY - GRACE", "artist": "ADOY", "link": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_11"},
        {"title": "윤하 - 오르트구름", "artist": "윤하", "link": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_12"}
    ],
    "위로": [
        {"title": "스텔라장 - Colors", "artist": "스텔라장", "link": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_13"},
        {"title": "선우정아 - 도망가자", "artist": "선우정아", "link": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_14"},
        {"title": "소란 - Perfect Day", "artist": "소란", "link": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_15"}
    ],
    # 🤘 dlals가 추가하고 싶은 기분이나 장르가 있다면 여기에 더 넣어주면 됨!
    "기본": [ # 사용자가 선택한 기분이 리스트에 없을 때 추천
        {"title": "아무튼 음악", "artist": "노래 추천", "link": "https://www.youtube.com/watch?v=SOME_DEFAULT_VIDEO_ID"}
    ]
}

def get_song_recommendation_by_mood(mood):
    """
    기분 종류에 따라 노래 추천
    """
    return mood_based_song_recommendations.get(mood, mood_based_song_recommendations["기본"])

# Streamlit 앱 설정
st.set_page_config(
    page_title="🎧 기분별 인디 노래 추천 리스트",
    page_icon="🎶",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("🎧 기분별 인디 노래 추천 리스트")
st.markdown("---") # 구분선

st.subheader("😊 지금 어떤 기분이신가요?")

# 기분 선택 드롭다운 (선택지 dlals가 더 늘려도 됨!)
mood_options = ["신남", "잔잔함", "우울함", "몽환적", "위로"] # 나중에 여기에 원하는 기분 더 추가 ㄱㄱ
selected_mood = st.selectbox("기분을 선택해주세요:", mood_options)

if st.button("음악 추천받기!"):
    if selected_mood:
        st.success(f"✔️ **{selected_mood}** 기분에 맞춰 노래를 찾아볼게요!")
        
        st.markdown("---")
        st.subheader(f"✨ **{selected_mood}** 기분에 딱! 어울리는 인디 Pick!")
        
        recommended_songs = get_song_recommendation_by_mood(selected_mood)
        
        if recommended_songs:
            for i, song in enumerate(recommended_songs):
                st.write(f"**{i+1}. {song['title']}** - {song['artist']}")
                # 유튜브 링크는 걍 영상 ID만 넣어도 자동 연결됨! 개꿀팁 ㅋㅋㅋㅋ
                st.markdown(f"[노래 들으러 가기]({song['link']})") 
                st.markdown("---")
        else:
            st.info("죄송해요, 이 기분에 맞는 추천곡은 아직 없네요 ㅠㅠ") # 그럴 일은 없겠지만 ㅋㅋ
    else:
        st.warning("기분을 선택해주세요!")

st.markdown("---")

