import streamlit as st

def recommend_song(mood):
    # mood_songs에 youtube_link 키 추가했어!
    # dlals가 원하는 유튜브 링크로 바꿔주면 돼! (플레이리스트도 괜찮!)
    mood_songs = {
        '행복함': [
            {"title": "Happy", "artist": "Pharrell Williams", "youtube_link": "https://www.youtube.com/watch?v=y6Sxv-sUYtM"},
            {"title": "Sugar", "artist": "Maroon 5", "youtube_link": "https://www.youtube.com/watch?v=09R8_2nJhr4"}
        ],
        '슬픔': [
            {"title": "Someone Like You", "artist": "Adele", "youtube_link": "https://www.youtube.com/watch?v=hLQsP2N_g30"},
            {"title": "Stay With Me", "artist": "Sam Smith", "youtube_link": "https://www.youtube.com/watch?v=pB-5XG-DbCs"}
        ],
        '차분함': [
            {"title": "밤편지", "artist": "아이유", "youtube_link": "https://www.youtube.com/watch?v=F0z-9yq3qL8"},
            {"title": "늦은 밤 너의 집 앞 골목길에서", "artist": "노을", "youtube_link": "https://www.youtube.com/watch?v=0pL92v1m7D8"}
        ],
        '신남': [
            {"title": "Dynamite", "artist": "BTS", "youtube_link": "https://www.youtube.com/watch?v=gdZLi9oWNZg"},
            {"title": "DDU-DU DDU-DU", "artist": "BLACKPINK", "youtube_link": "https://www.youtube.com/watch?v=IHNzOHi8sJs"}
        ],
        '에너지 충전': [
            {"title": "Don't Stop Me Now", "artist": "Queen", "youtube_link": "https://www.youtube.com/watch?v=HgzGwKwLmgM"},
            {"title": "Dancing Queen", "artist": "ABBA", "youtube_link": "https://www.youtube.com/watch?v=xFrGuyw1V8s"}
        ]
    }
    return mood_songs.get(mood, [])


# 페이지 설정 (요건 똑같아!)
st.set_page_config(
    page_title="분위기별 노래 추천 웹 앱🎶",
    page_icon="🎶"
)

# 웹 앱 메인 제목
st.title("🎶 분위기별 노래 추천 웹 앱 🎶")
st.write("오늘 어떤 분위기인지 알려주면 부힛이 찰떡같은 노래 추천해줄게!")

# 분위기 선택 옵션
mood_options = ['선택해주세요', '행복함', '슬픔', '차분함', '신남', '에너지 충전']
selected_mood = st.selectbox("오늘의 분위기는?", mood_options)

# 유저가 분위기를 선택했을 때만 노래 추천 보여주기
if selected_mood != '선택해주세요':
    st.subheader(f"✨ {selected_mood} 분위기에 찰떡인 노래들! ✨")
    recommended_songs = recommend_song(selected_mood)

    if recommended_songs:
        for song in recommended_songs:
            # HTML 마크다운으로 유튜브 링크를 클릭 가능한 형태로 보여주기!
            # target='_blank' 이걸 넣어주면 새 탭으로 열려!
            st.markdown(f"- <a href='{song['youtube_link']}' target='_blank'><b>{song['title']}</b> by {song['artist']} (🎵 유튜브에서 듣기)</a>", unsafe_allow_html=True)
    else:
        st.write("아직 이 분위기에는 추천 곡이 없네 ㅠㅠ 다른 분위기를 선택해볼까?")
else:
    st.write("👆 위에서 분위기를 선택하면 노래가 짜잔~ 나타날 거야!")

st.markdown("---")
st.write("더 많은 기능 추가하고 싶으면 언제든지 물어봐, dlals! 같이 만들어보자 😉")
