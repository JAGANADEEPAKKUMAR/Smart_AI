import streamlit as st
from gtts import gTTS
import tempfile
import playsound
import speech_recognition as sr
import datetime
import pyautogui
import os
import subprocess
import ctypes
import screen_brightness_control as sbc
import webbrowser
import random
import psutil  # For battery info

# Page config and styles
st.set_page_config(page_title="Offline Voice AI", layout="wide")
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        width: 100%;
        font-size: 18px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# TTS
def speak(text):
    try:
        temp_dir = tempfile.gettempdir()
        path = os.path.join(temp_dir, "voice.mp3")
        tts = gTTS(text)
        tts.save(path)
        playsound.playsound(path)
        os.remove(path)
    except Exception as e:
        st.error(f"TTS Error: {e}")

# Voice recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎧 Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            text = recognizer.recognize_google(audio)
            st.success(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            st.error("Could not understand audio.")
        except sr.RequestError as e:
            st.error(f"Recognition error: {e}")
    return ""

# Handle commands
def handle_voice_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        st.success(f"The time is: {current_time}")
        speak(f"The time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        st.success(f"Today's date is: {current_date}")
        speak(f"Today's date is {current_date}")

    elif "screenshot" in command:
        path = "C:/Users/admin/Desktop/New folder"
        os.makedirs(path, exist_ok=True)
        screenshot_path = f"{path}/screenshot.png"
        pyautogui.screenshot().save(screenshot_path)
        st.success(f"Screenshot saved to: {screenshot_path}")
        speak("Screenshot taken")

    elif "open notepad" in command:
        subprocess.Popen(["notepad.exe"])
        speak("Opening Notepad")

    elif "open explorer" in command or "open file manager" in command:
        subprocess.Popen("explorer")
        speak("Opening File Explorer")

    elif "lock screen" in command:
        ctypes.windll.user32.LockWorkStation()
        speak("Locking screen")

    elif "mute" in command:
        pyautogui.press("volumemute")
        speak("Volume muted")

    elif "unmute" in command:
        pyautogui.press("volumemute")
        speak("Volume unmuted")

    elif "increase volume" in command:
        pyautogui.press("volumeup")
        speak("Increasing volume")

    elif "decrease volume" in command:
        pyautogui.press("volumedown")
        speak("Decreasing volume")

    elif "increase brightness" in command:
        try:
            current = sbc.get_brightness()[0]
            sbc.set_brightness(min(current + 10, 100))
            speak("Increasing brightness")
        except:
            st.error("Brightness control not supported.")

    elif "decrease brightness" in command:
        try:
            current = sbc.get_brightness()[0]
            sbc.set_brightness(max(current - 10, 0))
            speak("Decreasing brightness")
        except:
            st.error("Brightness control not supported.")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "play song" in command:
        music_dir = "C:/Users/admin/Music"
        if os.path.exists(music_dir):
            songs = [song for song in os.listdir(music_dir) if song.endswith(('.mp3', '.wav'))]
            if songs:
                song_path = os.path.join(music_dir, random.choice(songs))
                os.startfile(song_path)
                speak("Playing a song")
            else:
                speak("No songs found in the music folder")
        else:
            speak("Music folder not found")

    elif "open camera" in command:
        subprocess.run("start microsoft.windows.camera:", shell=True)
        speak("Opening Camera")

    elif "open calculator" in command:
        subprocess.Popen("calc.exe")
        speak("Opening Calculator")

    elif "open paint" in command:
        subprocess.Popen("mspaint.exe")
        speak("Opening Paint")

    else:
        st.warning("❓ Command not recognized.")
        speak("I didn't understand the command.")

# Sidebar
with st.sidebar:
    st.header("🗣️ Voice Commands")
    st.markdown("""
- time  
- date  
- screenshot  
- open notepad  
- open explorer  
- lock screen  
- mute / unmute  
- increase volume / decrease volume  
- increase brightness / decrease brightness  
- open google / open youtube  
- play song  
- open camera  
- open calculator  
- open paint
""")

# Session state to store recent commands
if 'log' not in st.session_state:
    st.session_state.log = []

# Center layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="title">🎙️Smart Assistant</div>', unsafe_allow_html=True)
    if st.button("🎤 Start Listening"):
        spoken = recognize_speech()
        if spoken:
            st.session_state.log.append(spoken)
            handle_voice_command(spoken)

# Bottom Tabs (Assistant Info, Logs, Tips, System Info)
st.markdown("---")
tab1, tab2, tab3, tab4 = st.tabs(["🤖 Assistant Info", "📜 Recent Commands", "🎤 Voice Tips", "⚙️ System Info"])

with tab1:
    st.markdown("**Name:** Voice-AI")
    st.markdown("**Mode:** Offline")
    st.markdown("**Built by:** Jagana Deepak Kumar")
    st.markdown("**Version:** 1.0")

with tab2:
    if st.session_state.log:
        for cmd in st.session_state.log[-10:][::-1]:
            st.markdown(f"- {cmd}")
    else:
        st.markdown("No commands yet.")

with tab3:
    st.success("✔ Speak clearly and naturally.")
    st.success("✔ Try short, specific commands.")
    st.success("✔ Avoid background noise.")

with tab4:
    try:
        brightness = sbc.get_brightness()[0]
        st.markdown(f"**🔆 Brightness:** {brightness}%")
    except:
        st.markdown("**🔆 Brightness:** Not supported")

    try:
        battery = psutil.sensors_battery()
        if battery:
            plugged = "Charging 🔌" if battery.power_plugged else "On Battery 🔋"
            st.markdown(f"**🔋 Battery:** {battery.percent}% ({plugged})")
        else:
            st.markdown("**🔋 Battery:** Not available")
    except:
        st.markdown("**🔋 Battery:** Not supported")

    st.markdown(f"**🕒 Time:** {datetime.datetime.now().strftime('%H:%M:%S')}")
    st.markdown(f"**📅 Date:** {datetime.datetime.now().strftime('%Y-%m-%d')}")
