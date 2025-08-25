import streamlit as st

def recommend_song(mood):
    #찐 취향 100% 반영된 플레이리스트 완성! ✨
    mood_songs = {
        '신남': [
            {"title": "진격의 방탄소년단", "artist": "방탄소년단", "youtube_link": "https://youtu.be/7RsFNXsvusw?si=6ouFa2WMrn7CKdBS"},
            {"title": "페더웨이", "artist": "보이넥스트도어", "youtube_link": "https://youtu.be/I6StVU3kABM?si=cPHdDdNcVKb1PxR_"},
            {"title": "아주 나이스", "artist": "세븐틴", "youtube_link": "https://youtu.be/pOA-XQsEG44?si=ZoIR7LP1Rsr2pQ2G"},
            {"title": "Super Shy", "artist": "NewJeans", "youtube_link": "https://youtu.be/k8yvl4911g8?si=lTskrX9B2Gz36x5K"}
        ],
        '잔잔한': [
            {"title": "돌고래", "artist": "Zion.T", "youtube_link": "https://youtu.be/O_XpD41tXjE?si=xXlyrluioLgoWWxT"},
            {"title": "for you", "artist": "이하이", "youtube_link": "https://youtu.be/fB3kTcfjybg?si=OUfsGcS_-Uzbvy8G"},
            {"title": "next mistake", "artist": "보이넥스트도어", "youtube_link": "https://youtu.be/PiaK5sgQSJM?si=1_D_qo7TFX8ibzqc"},
            {"title": "어떻게 이별까지 사랑하겠어, 널 사랑하는 거지", "artist": "악동뮤지션", "youtube_link": "https://youtu.be/RKUvG_bE_B8?si=YxR1V2vR2_n24p7I"}
        ],
        '위로': [
            {"title": "not ok", "artist": "로꼬", "youtube_link": "https://youtu.be/yKp_hKVsiEsE?si=HtlyXg4S5_LQhLm8r"},
            {"title": "도망가자", "artist": "선우정아", "youtube_link": "https://youtu.be/D0l1HdemykU?si=AKHI0gf2LHkzsRVP"},
            {"title": "나의 사춘기에게", "artist": "볼빨간사춘기", "youtube_link": "https://youtu.be/3gMAEZCOFtE?si=-gn4O5F9XtGXkzu0"},
            {"title": "별을 세는 밤", "artist": "스탠딩 에그", "youtube_link": "https://youtu.be/y9_Yq-N-Nn0?si=p837p1vC_-q_vT0K"}
        ],
        '사랑': [
            {"title": "선을 그어주던가", "artist": "1415", "youtube_link": "https://youtu.be/qky_GLtTy6I?si=McEIdth6cF6Fn2Cu"},
            {"title": "Drowning", "artist": "WOODZ", "youtube_link": "https://youtu.be/v39uoOIoOhI?si=MrTg4ANAOPnXvoN-"},
            {"title": "돌멩이", "artist": "보이넥스트도어", "youtube_link": "https://youtu.be/r-ODioF6rZc?si=jYgq2RQivuk_V0Ib"},
            {"title": "선물", "artist": "멜로망스", "youtube_link": "https://youtu.be/I9j4N6o16A8?si=fL5H-P4Kk6Qe0fFf"}
        ],
        '청춘': [ # <<< '여행'에서 '청춘'으로 이름 변경!
            {"title": "여행", "artist": "볼빨간사춘기", "youtube_link": "https://youtu.be/A9M_W8LwN0E?si=9o4T-P9xYl8kQ-T7"},
            {"title": "한 페이지가 될 수 있게", "artist": "DAY6", "youtube_link": "https://youtu.be/WjO1m4l_e24?si=Rj3kGZ_v1K2K8qPz"},
            {"title": "Lucky Charm", "artist": "보이넥스트도어", "youtube_link": "https://www.youtube.com/watch?v=MFL9_Y0-U_s"} # <<< '벚꽃 엔딩' 대신 'Lucky Charm' 추가!
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

# 분위기 선택 옵션에 '여행' 대신 '청춘' 추가!
mood_options = ['선택해주세요', '신남', '잔잔한', '위로', '사랑', '청춘'] # <<< '여행' 대신 '청춘'으로 변경!
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
