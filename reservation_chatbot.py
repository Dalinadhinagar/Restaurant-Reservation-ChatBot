import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ------------------- MAIN WINDOW -------------------
root = tk.Tk()
root.title("Lavender Dine 🍽️")
root.geometry("650x500")
root.resizable(False, False)

LAVENDER = "#E6E6FA"
DARK_LAVENDER = "#B57EDC"
WHITE = "#FFFFFF"

root.configure(bg=LAVENDER)

# ------------------- DATA (COMPRESSED) -------------------
menu_data = {
    "starter": ["Soup", "Salad"],
    "main": ["Pasta", "Pizza", "Biryani"],
    "dessert": ["Ice Cream", "Brownie"]
}

availability = {
    "10:00 AM": 5,
    "1:00 PM": 3,
    "4:00 PM": 4,
    "7:00 PM": 2
}

# ------------------- GLOBAL VARS -------------------
user_name = tk.StringVar()

# ------------------- FRAMES -------------------
welcome_frame = tk.Frame(root, bg=LAVENDER)
chat_frame = tk.Frame(root, bg=LAVENDER)

for frame in (welcome_frame, chat_frame):
    frame.place(relwidth=1, relheight=1)

# ------------------- WELCOME PAGE -------------------
tk.Label(
    welcome_frame,
    text="🌸 Welcome to Lavender Dine 🌸",
    font=("Comic Sans MS", 24, "bold"),
    bg=LAVENDER,
    fg=DARK_LAVENDER
).pack(pady=40)

tk.Label(
    welcome_frame,
    text="Your smart dining reservation assistant",
    font=("Arial", 14),
    bg=LAVENDER
).pack(pady=10)

tk.Label(
    welcome_frame,
    text="Enter your name:",
    font=("Arial", 12),
    bg=LAVENDER
).pack(pady=10)

tk.Entry(
    welcome_frame,
    textvariable=user_name,
    font=("Arial", 12),
    width=30
).pack(pady=5)

def start_chat():
    if user_name.get().strip() == "":
        messagebox.showwarning("Oops!", "Please enter your name 🌼")
    else:
        welcome_frame.tkraise()
        chat_frame.tkraise()
        chat_display.insert(tk.END, f"🤖 Hello {user_name.get()}! Welcome to Lavender Dine 💜\n")
        chat_display.insert(tk.END, "🤖 Type: menu | availability | book | exit\n\n")

tk.Button(
    welcome_frame,
    text="Start Dining 🍽️",
    font=("Arial", 14, "bold"),
    bg=DARK_LAVENDER,
    fg=WHITE,
    command=start_chat
).pack(pady=30)

# ------------------- CHAT PAGE -------------------
tk.Label(
    chat_frame,
    text="💬 Lavender Dine Chatbot",
    font=("Arial", 18, "bold"),
    bg=LAVENDER,
    fg=DARK_LAVENDER
).pack(pady=10)

chat_display = tk.Text(
    chat_frame,
    height=18,
    width=75,
    bg=WHITE,
    font=("Arial", 11)
)
chat_display.pack(pady=10)
chat_display.config(state=tk.NORMAL)

user_input = tk.Entry(chat_frame, font=("Arial", 12), width=50)
user_input.pack(side=tk.LEFT, padx=10, pady=10)

def chatbot_response(msg):
    msg = msg.lower()

    if msg == "menu":
        response = "🍽️ Our Menu:\n"
        for category, items in menu_data.items():
            response += f"• {category.title()}: {', '.join(items)}\n"
        return response

    elif msg == "availability":
        response = "📅 Available Slots:\n"
        for time, seats in availability.items():
            response += f"• {time} → {seats} tables\n"
        return response

    elif msg == "book":
        return "📝 To book, type: book <time>\nExample: book 7:00 PM"

    elif msg.startswith("book"):
        parts = msg.split(" ", 1)
        if len(parts) < 2:
            return "⚠️ Please specify a time."
        time = parts[1].upper()
        if time in availability and availability[time] > 0:
            availability[time] -= 1
            return f"✅ Table booked at {time}! Enjoy your meal 💜"
        else:
            return "❌ Slot not available."

    elif msg == "exit":
        root.destroy()

    else:
        return "🤔 I didn’t understand. Try: menu | availability | book | exit"

def send_message():
    msg = user_input.get()
    if msg.strip() == "":
        return
    chat_display.insert(tk.END, f"🧑 You: {msg}\n")
    response = chatbot_response(msg)
    chat_display.insert(tk.END, f"🤖 {response}\n\n")
    user_input.delete(0, tk.END)
    chat_display.see(tk.END)

tk.Button(
    chat_frame,
    text="Send 💌",
    font=("Arial", 12, "bold"),
    bg=DARK_LAVENDER,
    fg=WHITE,
    command=send_message
).pack(side=tk.RIGHT, padx=10)

# ------------------- START -------------------
welcome_frame.tkraise()
root.mainloop()
