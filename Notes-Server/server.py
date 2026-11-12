import json 
from pathlib import Path 

from mcp.server.mcpserver import MCPServer 

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


if __name__ == "__main__":
    mcp.run()
    
    
    