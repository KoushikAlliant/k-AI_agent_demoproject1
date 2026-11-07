"""Tests run with: pytest  (the API is mocked, so no key or network needed)."""

from types import SimpleNamespace

import pytest

from agent import FileAgent, load_file


class FakeClient:
    """Stands in for the Anthropic client and returns a fixed answer."""

    def __init__(self):
        self.calls = []
        self.messages = self                         # So client.messages.create works

    def create(self, **kwargs):
        self.calls.append(kwargs)                    # Record what was sent
        return SimpleNamespace(content=[SimpleNamespace(text="Paris")])


def test_load_file(tmp_path):
    f = tmp_path / "doc.txt"
    f.write_text("hello", encoding="utf-8")
    assert load_file(str(f)) == "hello"              # File content is read correctly


def test_missing_file():
    with pytest.raises(FileNotFoundError):           # Bad path raises a clear error
        load_file("nope.txt")


def test_ask_includes_document_and_returns_answer(tmp_path):
    f = tmp_path / "doc.txt"
    f.write_text("The capital of France is Paris.", encoding="utf-8")
    client = FakeClient()
    agent = FileAgent(str(f), client=client)

    assert agent.ask("Capital of France?") == "Paris"
    assert "capital of France" in client.calls[0]["system"]  # File is in the prompt
    assert len(agent.history) == 2                            # user + assistant saved
