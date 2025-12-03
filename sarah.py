import streamlit as st
import time

# Page config
st.set_page_config(
    page_title="Happy Birthday Siti Maisarah",
    page_icon="🎂",
    layout="centered"
)
st.write('tekan play dulu baru gempakk sikit hehe')
audio_file = open('hpy.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3', loop=True)


# Title
st.markdown(
    """
    <h1 style="text-align:center; color:#ff4b4b; font-size:55px;">
        🎉 Happy Birthday Siti Maisarah! 🎉
    </h1>
    """,
    unsafe_allow_html=True
)

# Subtext
st.markdown(
    """
    <p style="text-align:center; font-size:22px;">
        Born on <b>4 December 2000</b><br>
        From Faiz, with love ❤️
    </p>
    """,
    unsafe_allow_html=True
)

# Animation-like text reveal
message = [
    "Today is a special day...",
    "Because it's your day...",
    "The day an amazing person was born ❤️",
    "I just want to say...",
    "Happy Birthday, my love!",
]

for line in message:
    st.markdown(
        f"<p style='text-align:center; font-size:26px;'>{line}</p>",
        unsafe_allow_html=True
    )
    time.sleep(0.7)

# Final wish
st.markdown(
    """
    <h2 style="text-align:center; color:#ff7acb;">
        💕 May your day be filled with happiness, 
        laughter, and endless blessings 💕
    </h2>
    """,
    unsafe_allow_html=True

)
st.markdown(
    """
    <h2 style="text-align:center; color:#ff7acb;">
        btw jangan lupa diet hehe
    </h2>
    """,
    unsafe_allow_html=True
)
# Confetti effect (fun simple animation)
st.balloons()
