# File Q&A Agent (simple demo)

An agent that reads a text file and answers questions using only that file.

## Files
- `agent.py` – the agent (loads file, calls Claude)
- `main.py` – command-line chat loop
- `test_agent.py` – tests (API mocked)
- `sample_data.txt` – example input file
- `requirements.txt`, `.env.example` – dependencies and API key template

## Setup
```bash
pip install -r requirements.txt
copy .env.example .env     # then edit .env and add your ANTHROPIC_API_KEY
```

## Run
```bash
python main.py                  # uses sample_data.txt
python main.py my_notes.txt     # use your own file
```
Try: "What time do you open on Saturday?" or "Who won the World Cup?" (it should say it doesn't know).

## Test
```bash
pytest
```
