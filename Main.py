from sentence_transformers import SentenceTransformer, util
import tkinter as tk
from tkinter import scrolledtext

model = SentenceTransformer('all-MiniLM-L6-v2')

qa_pairs = [
    ("hello hi hey greetings goodmorning goodafternoon goodevening yo sup", "Hi! How can I help with coding today?"),
    ("bye goodbye cya seeyou farewell later", "Goodbye! Happy coding!"),
    ("thanks thankyou appreciate helpful", "You're welcome! Let me know if you need more coding help."),
    ("python py programming coding developer", "Sure! What Python project are you working on?"),
    ("java javascript cpp csharp ruby php go rust swift kotlin", "Nice! What do you need help with in that language?"),
    ("error bug issue problem exception crash traceback", "Can you show me the error message or explain what happens?"),
    ("fix debug troubleshoot repair", "Send the code and I'll help you debug it."),
    ("optimize improve performance speed efficient", "I can help optimize your code. What feels slow?"),
    ("loop loops for while iteration repeat", "Loops repeat actions. Do you need a for-loop or while-loop?"),
    ("function functions def method methods", "Functions organize reusable code. Need help creating one?"),
    ("variable variables assign value values", "Variables store information. What are you trying to save?"),
    ("list lists array arrays collection collections", "Lists store multiple values. Need help adding or removing items?"),
    ("dictionary dictionaries dict hashmap key value", "Dictionaries connect keys to values. Want help accessing data?"),
    ("tuple tuples immutable", "Tuples are immutable collections. Need an example?"),
    ("set sets unique values", "Sets store unique items and support fast lookups."),
    ("string strings text manipulation format slice", "Working with strings? I can help with formatting or slicing."),
    ("input output print console", "Need help reading input or displaying output?"),
    ("file files read write open save load", "I can help with file handling. What file operation do you need?"),
    ("json csv xml yaml dataformat", "Need help parsing or saving structured data?"),
    ("class classes oop object objects inheritance encapsulation", "Object-oriented programming can organize your code. Need help with classes?"),
    ("library libraries import module modules package packages", "Which library are you trying to use?"),
    ("pip install dependency dependencies", "Are you having trouble installing a package?"),
    ("api request requests fetch endpoint", "Working with APIs? I can help send requests or parse responses."),
    ("web flask django fastapi backend server", "Building a web app? What framework are you using?"),
    ("html css frontend webpage website", "Need help designing or styling a webpage?"),
    ("database sql sqlite mysql postgres mongodb", "Need help storing or querying data?"),
    ("game pygame gamedev unity unreal", "Game development is fun! What are you building?"),
    ("ai machinelearning ml neuralnetwork tensorflow pytorch", "Interested in AI or machine learning?"),
    ("recursion recursive", "Recursion means a function calling itself. Need an example?"),
    ("algorithm algorithms logic", "I can help explain or improve algorithms."),
    ("sorting sort bubble quick merge", "Sorting algorithms organize data efficiently."),
    ("search binary linear searchalgorithm", "Need help finding values efficiently?"),
    ("stack queue linkedlist tree graph datastructure", "Data structures help organize information efficiently."),
    ("binary hexadecimal octal conversion", "Need help converting number systems?"),
    ("math calculation arithmetic", "Need help with calculations in code?"),
    ("random randint choice shuffle", "Working with randomness or probability?"),
    ("datetime time clock timer date", "Need help working with dates or time?"),
    ("thread threading multiprocessing async await", "Concurrency can improve performance. Need async help?"),
    ("socket networking tcp udp connection", "Working with networking or sockets?"),
    ("security encryption hash password auth", "Need help with cybersecurity or encryption concepts?"),
    ("regex regular expression pattern match", "Regular expressions are useful for matching text patterns."),
    ("gui tkinter pyqt interface window", "Building a desktop app interface?"),
    ("linux terminal bash shell commandline", "Need help with terminal commands or shell scripting?"),
    ("git github versioncontrol commit push pull", "Need help with Git or GitHub?"),
    ("deploy hosting server render vercel heroku", "Trying to deploy your project online?"),
    ("test testing unittest pytest", "Testing helps catch bugs early."),
    ("comment comments documentation docstring", "Good documentation makes code easier to understand."),
    ("beginner learn tutorial practice", "Everyone starts somewhere. What topic do you want to learn?"),
    ("advanced expert professional architecture", "What advanced concept are you exploring?"),
    ("memory ram storage cache", "Need help understanding memory usage?"),
    ("cpu gpu hardware acceleration", "Working on performance or hardware acceleration?"),
    ("compiler interpreter runtime", "Need help understanding how code executes?"),
    ("syntax indentation formatting", "Syntax issues are common. Show me the code."),
    ("logic logical thinking condition if else", "Conditional statements control program flow."),
    ("boolean bool true false", "Booleans represent true or false values."),
    ("exception exceptions try catch finally", "Exception handling prevents crashes."),
    ("numpy pandas matplotlib", "Working with data science tools?"),
    ("opencv image processing computervision", "Need help processing images or video?"),
    ("discord bot telegram bot chatbot", "Building a bot? What platform is it for?"),
    ("automation automate script scripting", "Automation can save lots of time."),
    ("scraping scrape selenium beautifulsoup", "Need help extracting data from websites?"),
    ("audio sound music pygame mixer", "Working with sound or music in your project?"),
    ("video webcam camera stream", "Need help with video processing?"),
    ("encryption decrypt cipher cryptography", "Cryptography can protect sensitive data."),
    ("firebase authentication cloud", "Need help with cloud services or authentication?"),
    ("mobile android ios app", "Building a mobile application?"),
    ("robotics arduino raspberrypi electronics", "Combining hardware and software?"),
    ("physics simulation engine", "Need help building simulations?"),
    ("school homework assignment", "I can help explain concepts step by step."),
    ("portfolio resume interview", "Preparing for a coding job or interview?"),
    ("leetcode hackerank codewars", "Practicing coding challenges?"),
    ("fps platformer puzzle survival roguelike", "What kind of game are you creating?"),
    ("enemy enemies ai npc", "Need help programming enemy behavior?"),
    ("player movement collision gravity", "Game physics and movement can be tricky."),
    ("score scoring leaderboard", "Need help tracking points or scores?"),
    ("save system savefile checkpoint", "Need help saving game progress?"),
    ("animation sprite spritesheet", "Working with animations or sprites?"),
    ("collision hitbox physics", "Need help detecting collisions?"),
    ("multiplayer online networking sync", "Multiplayer systems require synchronization."),
    ("database connection cursor query", "Need help connecting to a database?"),
    ("email smtp mail send", "Trying to send emails from code?"),
    ("pdf excel spreadsheet document", "Need help generating documents or spreadsheets?"),
    ("speech voice recognition tts", "Working with speech or voice systems?"),
    ("translation language multilingual", "Need help translating or processing languages?"),
    ("weather api forecast", "Using weather APIs or forecasts?"),
    ("map gps location geolocation", "Working with maps or location services?"),
    ("shopping ecommerce payment stripe paypal", "Building an online store or payment system?"),
    ("login register signup signin authentication", "Need help building user accounts?"),
    ("session cookie jwt token", "Working with authentication tokens or sessions?"),
    ("cache redis memcached", "Caching can speed up applications."),
    ("docker container kubernetes", "Need help with containers or deployment?"),
    ("aws azure gcp cloudcomputing", "Using cloud platforms?"),
    ("opensource contribution project", "Contributing to open source is great practice."),
    ("refactor cleanup organize structure", "Refactoring improves readability and maintenance."),
    ("portfolio showcase githubprofile", "Need help improving your coding portfolio?"),
    ("motivation burnout productivity", "Sometimes a small project helps regain motivation."),
    ("help assist support", "Tell me what you're working on and I'll help."),
]

question_texts = [q for q, a in qa_pairs]
question_embeddings = model.encode(question_texts, convert_to_tensor = True)

THRESHOLD = 0.3

def get_response(user_input):
    input_embedding = model.encode(user_input, convert_to_tensor = True)
    similarities = util.cos_sim(input_embedding, question_embeddings)[0]
    best_idx = similarities.argmax().item()
    best_score = similarities[best_idx].item()

    if best_score < THRESHOLD:
        return best_score, "Sorry, I don't understand. Please try something else."

    return best_score, qa_pairs[best_idx][1]




class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Coding Chatbot")
        self.root.geometry("500x600")
        self.root.configure(bg="#2E2E2E")

        tk.Label(root, text = "Coding Chatbot", font = ("Rubik Mono One", 16, "bold"),
                 fg = "#FFFFFF", bg = "#2E2E2E"
                 )

        self.chat_area = scrolledtext.ScrolledText(
            root, wrap = tk.WORD, height = 20, width = 50, font = ("Arial", 11),
            bg = "#3C3C3C", fg = "#E0E0E0", insertbackground = "white"
        )

        self.chat_area.pack(pady=10, padx=10)
        self.chat_area.insert(tk.END,
                              "Welcome to the Coding Chatbot!\n"
                              "Ask about coding tips (e.g., 'variable assign value' or 'python code programming').\n")

        self.chat_area.config(state='disabled')

        input_frame = tk.Frame(root, bg = "#2E2E2E")
        input_frame.pack(pady = 5)

        self.input_field = tk.Entry(
            input_frame, width = 40, font = ("Arial", 11), bg = "#4A4A4A", fg = "#FFFFFF",
            insertbackground = "white"
        )

        self.input_field.pack(side = tk.LEFT, padx = 5)
        self.input_field.bind("<Return>", self.send_message)

        tk.Button(
            input_frame, text = "Send!", command = self.send_message, font = ("Arial", 11),
            bg = "#4CAF50", fg = "#FFFFFF", activebackground = "#45A049"
        ).pack(side = tk.LEFT, padx = 5)

        tk.Button(
            root, text = "Clear Chat", command = self.clear_chat, font = ("Arial", 11),
            bg = "#F44336", fg = "#FFFFFF", activebackground = "#D32F2F"
        ).pack(pady = 5)

    def send_message(self, event = None):
        user_input = self.input_field.get().strip()
        if not user_input:
            return

        score, response = get_response(user_input)
        self.chat_area.config(state = "normal")
        self.chat_area.insert(tk.END, f"\nYou: {user_input}\n")
        self.chat_area.insert(tk.END, f"Match Confidence: {score:.2f}\n")
        self.chat_area.insert(tk.END, f"Bot: {response}\n")
        self.chat_area.config(state = "disabled")
        self.chat_area.see(tk.END)
        self.input_field.delete(0, tk.END)

    def clear_chat(self):
        self.chat_area.config(state = "normal")
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.insert(tk.END,
                              "Welcome to the Coding Chatbot!\n"
                              "Ask about coding tips!\n")
        self.chat_area.config(state = "disabled")



def main():
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()