
from agent import run_agent

def main():
    print("Research Agent Ready. Type 'exit' to quit.\n")
    
    while True:
        question = input("You: ").strip()
        
        if question.lower() == "exit":
            print("Goodbye!")
            break
            
        if question == "":
            continue
            
        run_agent(question)

if __name__ == "__main__":
    main()