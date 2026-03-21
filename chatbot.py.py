print("UPSC Chatbot 🤖")
print("Type 'exit' to stop\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Good luck with your UPSC preparation! 🇮🇳")
        break

    elif "upsc" in user_input:
        print("UPSC is Union Public Service Commission, which conducts civil services exam.")

    elif "eligibility" in user_input or "age" in user_input or "qualification" in user_input:
        print("Age: 21-32 years, Degree required, Attempts vary by category.")

    elif "pattern" in user_input or "marks" in user_input or "exam" in user_input:
        print("Prelims: 400 marks, Mains: 1750 marks, Interview: 275 marks.")

    elif "syllabus" in user_input or "subjects" in user_input:
        print("Includes History, Polity, Economy, Geography, Environment, Science.")

    elif "roadmap" in user_input or "plan" in user_input or "strategy" in user_input:
        print("Read NCERTs, standard books, current affairs, practice tests and revision.")

    else:
        print("Sorry, I don't understand. Try asking about UPSC, eligibility, syllabus, etc.")