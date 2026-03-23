import tkinter as tk
import random
import urllib.request
import xml.etree.ElementTree as ET
import pyttsx3
import threading

# 🎤 Voice
engine = pyttsx3.init()

def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()

# 🎯 Quiz Data
quiz_questions = [
    {"q": "Who appoints the Chief Election Commissioner?",
     "options": ["President", "PM", "Parliament", "Supreme Court"],
     "ans": "President"},

    {"q": "Fundamental Rights are in which articles?",
     "options": ["12-35", "36-51", "51A", "370"],
     "ans": "12-35"},

    {"q": "Capital of India?",
     "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
     "ans": "Delhi"},
]

asked = []
score = 0
current_q = None

# 📰 News (fixed repetition)
def get_news():
    try:
        url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
        data = urllib.request.urlopen(url)
        root = ET.parse(data).getroot()

        items = root.findall(".//item")
        random.shuffle(items)

        news = "📰 Current Affairs:\n\n"
        for item in items[:5]:
            news += "👉 " + item.find("title").text + "\n"
        return news
    except:
        return "Unable to fetch news."

# 🎯 Quiz
def start_quiz():
    global current_q

    remaining = [q for q in quiz_questions if q not in asked]

    if not remaining:
        asked.clear()
        remaining = quiz_questions

    current_q = random.choice(remaining)
    asked.append(current_q)

    bot("🧠 Quiz Time!")
    bot(current_q["q"])

    for i, opt in enumerate(current_q["options"], 1):
        bot(f"{i}. {opt}")

def check(ans):
    global score
    if current_q:
        if ans.lower() in current_q["ans"].lower():
            score += 1
            return f"🔥 Correct! Score: {score}"
        else:
            return f"❌ Wrong! Answer: {current_q['ans']} | Score: {score}"
    return None

# 💬 Chat UI
def bot(msg):
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "🤖 " + msg + "\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)
    speak(msg)

def user(msg):
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "🧑 " + msg + "\n")
    chat_log.config(state=tk.DISABLED)

# 💬 Main Logic
def send():
    text = entry.get().strip()
    if not text:
        return

    entry.delete(0, tk.END)
    user(text)

    # quiz answer check
    ans = check(text)
    if ans:
        bot(ans)
        return

    t = text.lower()

    # ✅ FIXED MENU
    if "menu" in t:
        bot("""📚 MENU:
1. What is UPSC
2. Eligibility
3. Exam Pattern
4. Syllabus
5. Current Affairs
6. Quiz
""")

    elif "hi" in t or "hello" in t:
        bot("Hi champ 😎 Ready to crack UPSC?")

    elif "upsc" in t:
        bot("UPSC conducts Civil Services Exam for IAS, IPS, IFS.")

    elif "eligibility" in t:
        bot("Age: 21–32, Degree required, attempts vary by category.")

    elif "pattern" in t:
        bot("Prelims → Mains → Interview (Total 2025 marks).")

    # ✅ FULL SYLLABUS FIXED
    elif "syllabus" in t:
        bot("""📚 UPSC Syllabus:

1. History (Ancient, Medieval, Modern)
2. Polity (Constitution, Governance)
3. Geography (India & World)
4. Economy (Budget, Banking)
5. Environment (Ecology, Climate)
6. Science & Tech
7. Current Affairs
""")

    elif "news" in t or "current" in t:
        bot(get_news())

    elif "quiz" in t:
        start_quiz()

    else:
        bot("Try 'menu' champ 😉")

# 🎨 UI
root = tk.Tk()
root.title("UPSC JARVIS 🤖")
root.geometry("600x700")
root.configure(bg="#0f172a")

chat_log = tk.Text(root,
                   bg="#0f172a",
                   fg="#00f7ff",
                   font=("Segoe UI", 11))
chat_log.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
chat_log.config(state=tk.DISABLED)

entry = tk.Entry(root, font=("Segoe UI", 14))
entry.pack(fill=tk.X, padx=10, pady=5)
entry.bind("<Return>", lambda e: send())

# Buttons (NO LAG MENU)
frame = tk.Frame(root, bg="#0f172a")
frame.pack()

tk.Button(frame, text="Menu", command=lambda: bot("Type 'menu'")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Quiz", command=start_quiz).grid(row=0, column=1, padx=5)
tk.Button(frame, text="News", command=lambda: bot(get_news())).grid(row=0, column=2, padx=5)

tk.Button(root, text="Send", command=send).pack(pady=5)

root.mainloop()