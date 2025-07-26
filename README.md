# Smart_AI
A fully offline Smart Assistant built with Streamlit that responds to voice commands for system control, app launching, and multimedia tasks. It includes a sleek UI with real-time feedback for an interactive user experience.

**STEPS TO RUN THIS SMART ASSISTANT**

**STEP 1:**
--> Open the command prompt and check if python is installed or not.(**python --verison**)
--> If not install it by visiting this website.(**https://www.python.org/downloads/**)

**STEP 2:**
-->Run the following command:
    git clone https://github.com/JAGANADEEPAKKUMAR/Smart_AI.git
    cd Smart_AI
    
**STEP 3:**
--> Install the requirements.txt
    pip install -r requirements.txt
    
**STEP 4:**
-->Run the Application
    python -m streamlit run SmartAI.py


* Your app will start and open in the browser at **http://localhost:8501**
* There will be a list of voice commands:
  
🗣️ Supported Voice Commands (Smart AI)

## 🗣️ Supported Voice Commands (Smart AI)

Your Smart AI Assistant supports the following **offline voice commands**:

---

### 🕒 Date & Time
| Voice Command       | Action                        |
|---------------------|-------------------------------|
| `what's the time`   | Tells the current system time |
| `what's the date`   | Tells today's date            |

---

### 📸 Screenshot
| Voice Command       | Action                                  |
|---------------------|------------------------------------------|
| `take a screenshot` | Captures and saves a screenshot to desktop |

---

### 📝 Application Launchers
| Voice Command       | Action                    |
|---------------------|---------------------------|
| `open notepad`      | Launches Notepad          |
| `open file manager` | Opens File Explorer       |
| `open explorer`     | Also opens File Explorer  |
| `open calculator`   | Opens Calculator          |
| `open paint`        | Opens Microsoft Paint     |
| `open camera`       | Opens Camera application  |

---

### 🔉 Volume Control
| Voice Command       | Action                     |
|---------------------|----------------------------|
| `mute`              | Mutes system volume        |
| `unmute`            | Unmutes system volume      |
| `increase volume`   | Increases volume           |
| `decrease volume`   | Decreases volume           |

---

### 🔆 Brightness Control
| Voice Command         | Action                      |
|-----------------------|-----------------------------|
| `increase brightness` | Increases screen brightness |
| `decrease brightness` | Decreases screen brightness |

> **Note:** Brightness control may not be supported on all laptops.

---

### 🌐 Web Browsing
| Voice Command     | Action                       |
|-------------------|------------------------------|
| `open google`     | Opens Google in browser      |
| `open youtube`    | Opens YouTube in browser     |

---

### 🎵 Music Playback
| Voice Command     | Action                                          |
|-------------------|-------------------------------------------------|
| `play song`       | Plays a random song from your Music folder      |

> Default path: `C:/Users/admin/Music` (you can update it in the code)

---

### 🔐 System Controls
| Voice Command     | Action                 |
|-------------------|------------------------|
| `lock screen`     | Locks your computer    |

---

### ℹ️ Tips for Best Experience
- 🎙 Speak clearly and naturally.
- 🔇 Minimize background noise.
- 📶 No internet required (offline assistant).
- 💬 Uses Google Speech Recognition engine via mic.

---


