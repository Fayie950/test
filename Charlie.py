import tkinter as tk

# Updated knowledge base
knowledge_base = {
    "application process": "You can apply through our online admissions portal. Make sure to check the deadlines on our website.",
    "course catalog": "Our university offers over 200 courses across various disciplines. Visit our official website for a detailed course list.",
    "tuition fees": "Tuition fees vary depending on the program. Undergraduate programs start at $12,000 per year.",
    "scholarships available": "Yes, we offer merit-based and need-based scholarships. Visit the financial aid office for more details.",
    "campus facilities": "Our campus has libraries, labs, sports complexes, and student lounges to support your learning experience.",
    "student clubs": "We have over 50 student clubs including tech clubs, cultural societies, and sports teams.",
    "internship opportunities": "Our university partners with top companies to provide internship opportunities. Check with the career services department.",
    "graduation requirements": "To graduate, students must complete at least 120 credits, including major and elective courses.",
    "academic calendar": "The academic year is divided into two semesters: Fall (September - December) and Spring (January - May).",
    "contact support": "You can reach the university helpdesk at support@university.edu or call (123) 456-7890."
}

def get_response(user_input):
    # Convert the input to lowercase for case-insensitive matching.
    user_input = user_input.lower()

    # Check for specific keywords or phrases.
    if "apply" in user_input or "application" in user_input:
        return knowledge_base["application process"]
    elif "scholarship" in user_input:
        return knowledge_base["scholarships available"]
    elif "tuition" in user_input or "fees" in user_input:
        return knowledge_base["tuition fees"]
    # For campus facilities, require both "campus" and "facilities" to be mentioned.
    elif "campus" in user_input and "facilities" in user_input:
        return knowledge_base["campus facilities"]
    elif "course" in user_input or "catalog" in user_input:
        return knowledge_base["course catalog"]
    elif "internship" in user_input:
        return knowledge_base["internship opportunities"]
    elif "contact" in user_input or "support" in user_input or "helpdesk" in user_input:
        return knowledge_base["contact support"]
    # For the academic calendar, require both words for a clear match.
    elif "academic" in user_input and "calendar" in user_input:
        return knowledge_base["academic calendar"]
    elif "club" in user_input:
        return knowledge_base["student clubs"]
    else:
        return "I'm sorry, I don't have an answer for that. Please contact student support."

def chat():
    user_query = entry.get()  # Get user input
    response = get_response(user_query)  # Get chatbot response based on keyword matching
    chat_history.insert(tk.END, f"You: {user_query}\nBot: {response}\n\n")  # Display conversation
    entry.delete(0, tk.END)  # Clear input field

# GUI Setup
root = tk.Tk()
root.title("University Chatbot")
root.geometry("500x400")

# Chat history display
chat_history = tk.Text(root, height=15, width=60)
chat_history.pack(pady=10)

# User input field
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Send button to get chatbot response
send_button = tk.Button(root, text="Send", command=chat)
send_button.pack()

# Run the chatbot application
root.mainloop()