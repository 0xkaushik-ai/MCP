import json 
from pathlib import Path 

from mcp.server.mcpserver import MCPServer 
from mcp.server.mcpserver.exceptions import  ToolError
from mcp.server.mcpserver.exceptions import ResourceNotFoundError

mcp = MCPServer("notes")

NOTES_FILE = Path(__file__).parent/"notes.json" 

def load_notes()->dict[str,str]:
    if not NOTES_FILE.exists():
        return{}
    return json.loads(NOTES_FILE.read_text())

def save_notes(notes:dict[str,str]):
    NOTES_FILE.write_text(json.dumps(notes, indent=2)) 
    
    
    
    
@mcp.tool() 

def add_note(name:str,text:str):
    """Save a note with the given name and the text"""
    notes = load_notes()
    replaced = name in notes 
    notes[name]= text 
    save_notes(notes)
    if replaced: 
        return f"Replaced note '{name}'." 
    return f"Added note '{name}'."



@mcp.tool() 
def list_notes() -> list[str]:
    """Return the name of all saved notes.""" 
    return sorted(load_notes())

@mcp.tool() 
def read_note(name:str)->str:
    """Return the full text of one note,given its exact name."""
    notes = load_notes()
    if name not in notes:
        raise ToolError(f"No note names'{name}'.Use list_notes to see the available names")
    return notes[name]

@mcp.tool() 
def delete_note(name:str):
    """Delete a note with the given name."""
    notes = load_notes()
    if name not in notes:
        raise ToolError(f"No note named '{name}'. Use list_notes to see the available names.")
    del notes[name]
    save_notes(notes)
    return f"Deleted note '{name}'."

@mcp.tool()
def search_notes(query:str)->list[str]:
    """Return a list of note names that contain the given query string."""
    notes = load_notes()
    return sorted(name for name in notes if query in name or query in notes[name])


@mcp.resource("notes//{name}")
def note_resource(name:str)->str:
    """The next of one note"""
    notes = load_notes()
    if name not in notes:
        raise ResourceNotFoundError(f"No note named '{name}'.")
    return notes[name]


@mcp.prompt()
def summarize_notes()->str:
    """Summarize all saved notes."""
    notes = load_notes()
    if not notes:
        return "No notes saved."
    body= "\n\n".join(f"##{name}\n{text}"for name,text in notes.items())
    return f"#Here are my notes:\n\n{body}\n\nSummarise them in a few bullet points ."


if __name__ == "__main__":
    mcp.run()
    
    
    