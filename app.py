import streamlit as st

def recommend_song(mood):
    #찐 취향만 남은 분위기들!
    mood_songs = {
        '신남': [
            {"title": "진격의 방탄소년단", "artist": "방탄소년단", "youtube_link": "https://youtu.be/7RsFNXsvusw?si=6ouFa2WMrn7CKdBS"},
            {"title": "페더웨이", "artist": "보이넥스트도어", "youtube_link": "https://youtu.be/I6StVU3kABM?si=cPHdDdNcVKb1PxR_"},
            {"title": "아주 나이스", "artist": "세븐틴", "youtube_link": "https://youtu.be/pOA-XQsEG44?si=ZoIR7LP1Rsr2pQ2G"}
        ],
        '잔잔한': [
            {"title": "돌고래", "artist": "Zion.T", "youtube_link": "https://youtu.be/O_XpD41tXjE?si=xXlyrluioLgoWWxT"},
            {"title": "for you", "artist": "이하이", "youtube_link": "https://youtu.be/fB3kTcfjybg?si=OUfsGcS_-Uzbvy8G"},
            {"title": "next mistake", "artist": "보이넥스트도어", "youtube_link": "https://youtu.be/PiaK5sgQSJM?si=1_D_qo7TFX8ibzqc"}
        ],
        '위로': [
            {"title": "not ok", "artist": "로꼬", "youtube_link": "https://youtu.be/yKp_hKVsiEsE?si=HtlyXg4S5_LQhLm8r"},
            {"title": "도망가자", "artist": "선우정아", "youtube_link": "https://youtu.be/D0l1HdemykU?si=AKHI0gf2LHkzsRVP"},
            {"title": "나의 사춘기에게", "artist": "볼빨간사춘기", "youtube_link": "https://youtu.be/3gMAEZCOFtE?si=-gn4O5F9XtGXkzu0"}
        ],
        '사랑': [ # <<< 여기 '사랑' 분위기 곡들 추가!
            {"title": "선을 그어주던가", "artist": "1415", "youtube_link": "https://youtu.be/qky_GLtTy6I?si=McEIdth6cF6Fn2Cu"},
            {"title": "Drowning", "artist": "WOODZ", "youtube_link": "https://youtu.be/v39uoOIoOhI?si=MrTg4ANAOPnXvoN-"},
            {"title": "돌멩이", "artist": "보이넥스트도어", "youtube_link": "https://youtu.be/r-ODioF6rZc?si=jYgq2RQivuk_V0Ib"}
        ]
    }
    return mood_songs.get(mood, [])


# 페이지 설정
st.set_page_config(
    page_title="분위기&장르 노래 추천 웹 앱🎶",
    page_icon="🎶"
)

# 웹 앱 메인 제목
st.title("🎶분위기&장르 노래 추천 웹 앱 🎶")

# 분위기 선택 옵션에 '사랑' 추가!
mood_options = ['선택해주세요', '신남', '잔잔한', '위로', '사랑'] # <<< '사랑' 추가!
selected_mood = st.selectbox("오늘의 분위기는?", mood_options)

# 유저가 분위기를 선택했을 때만 노래 추천 보여주기
if selected_mood != '선택해주세요':
    st.subheader(f"✨ {selected_mood} 분위기에 찰떡인 노래들! ✨")
    recommended_songs = recommend_song(selected_mood)

    if recommended_songs:
        for song in recommended_songs:
            st.markdown(f"- <a href='{song['youtube_link']}' target='_blank'><b>{song['title']}</b> by {song['artist']} (🎵 유튜브에서 듣기)</a>", unsafe_allow_html=True)
    else:
        st.write("아직 이 분위기에는 추천 곡이 없네 ㅠㅠ 다른 분위기를 선택해볼까?")
else:
    st.write("👆 위에서 분위기를 선택하면 노래가 짜잔~ 나타날 거야!")

st.markdown("---")
