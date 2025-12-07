import json
from fastmcp import FastMCP
from pathlib import Path

notes_mcp = FastMCP("Notes MCP Server")

NOTES_FILE = Path.home() / "notes.json"

def load_notes() -> dict[str, str]:
    if NOTES_FILE.exists():
        return json.loads(NOTES_FILE.read_text())
    
    return {}

def save_note(notes: dict[str, str]):
    NOTES_FILE.write_text(json.dumps(notes, indent=2))

@notes_mcp.tool
def add_note(name: str, content: str):
    notes = load_notes()
    notes[name] = content
    save_note(notes)

    return f"Note {name} added successfully"

@notes_mcp.tool
def delete_note(name: str) -> str:
    notes = load_notes()
    if name not in notes:
        return f"Note {name} not found"
    del notes[name]
    save_note(notes)

    return f"Note {name} deleted successfully"

@notes_mcp.tool
def get_note(name: str) -> str:
    notes = load_notes()
    if name not in notes:
        return f"Note {name} not found"
    return notes[name]

@notes_mcp.tool
def list_notes() -> list[str]:
    notes = load_notes()
    return list(notes.keys())    

@notes_mcp.resource("resource://{name}")
def get_note_resource(name: str) -> str:
    notes = load_notes()
    if name not in notes:
        return f"Note {name} not found"
    return notes[name]

@notes_mcp.resource("resource://reference")
def reference_resource() -> str:
    return "In order save a note you need to provide a name and a content"

@notes_mcp.prompt
def summarize_note(note_name: str) -> str:
    """
    Generate a user message to summarize a note
    """
    note = load_notes()[note_name]
    return f"Here is my note: {note}. Summarize this note and give me the key takeaways in 100 words or less"


if __name__ == "__main__":
    notes_mcp.run()


