"""Core of the agent: loads a text file and answers questions using only that file."""

import os

from anthropic import Anthropic          # Official Anthropic SDK
from dotenv import load_dotenv           # Reads variables from the .env file

load_dotenv()  # Load ANTHROPIC_API_KEY from .env into environment variables

MODEL = "claude-sonnet-5-5"  # Model used to answer questions


def load_file(path: str) -> str:
    """Read the input file and return its text."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


class FileAgent:
    """A tiny agent that answers questions based only on a given file."""

    def __init__(self, file_path: str, client=None):
        self.document = load_file(file_path)       # File content kept in memory
        self.client = client or Anthropic()        # Client reads API key from env
        self.history = []                          # Conversation so far (for follow-ups)

    def _system_prompt(self) -> str:
        """Instructions telling the model to stay within the file."""
        return (
            "You answer questions using ONLY the document below. "
            "If the answer is not in the document, say 'I don't know based on the file.'\n\n"
            f"<document>\n{self.document}\n</document>"
        )

    def ask(self, question: str) -> str:
        """Send a question to the model and return its answer."""
        self.history.append({"role": "user", "content": question})
        response = self.client.messages.create(
            model=MODEL,
            max_tokens=1000,
            system=self._system_prompt(),
            messages=self.history,
        )
        answer = response.content[0].text           # First text block of the reply
        self.history.append({"role": "assistant", "content": answer})  # Remember it
        return answer
