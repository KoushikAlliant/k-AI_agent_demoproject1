"""Command-line entry point: python main.py [path_to_file]"""

import sys

from agent import FileAgent


def main():
    # Use the file passed on the command line, or the bundled sample
    path = sys.argv[1] if len(sys.argv) > 1 else "sample_data.txt"
    agent = FileAgent(path)
    print(f"Loaded '{path}'. Ask questions about it (type 'exit' to quit).")

    while True:
        question = input("\nYou: ").strip()
        if question.lower() in ("exit", "quit"):   # Stop the loop
            break
        if not question:                            # Ignore empty input
            continue
        print("Agent:", agent.ask(question))


if __name__ == "__main__":
    main()
