# Why do we need mcp ? 
- MCP exits because a model on its own can only produce text; it cant read your files ,query yoy database or call your API unless something connects it to thme. MCP is the standard way to make that connection .
- Instead of making M*N custom integrations.We write the one MCP server for a service  any MCP-compatible clinet can use it .That turn M*N integration into M+N .
- An MCP server can offer three main things to an AI App and it can also ask how a few things of the app in the reuturn .
  - Funtion that perform actions or computation 
  - Read only data identified by URI 
  - Resuable prompt templates with arguments 
- The model uses the JSON-RPC2.0 message to establish communication between .

- These all defination came from the language server protocol (LSP) is to standardize the protocol how such server and development tools communicate .

- MCP has two layers 
  - Protocol => What the message say  [jso-rpc]
  - Transport => How those message travel  [http/stdio]





# MCP versioning 
- The MCP uses string-based version indentifiers following the format YYYY-MM-DD to indicate the last date backwards incompatible chages were made .

# MCP server 
- MCP servers are programs that expose specific capabilities to AI applications through standardized protocol interfaces. 
- Tools are schema-defined interfaces that LLMs can invoke. MCP uses JSON Schema for validation. Each tool performs a single operation with clearly defined inputs and outputs. Tools may require user consent prior to execution, helping to ensure users maintain control over actions taken by a model
- 
# MCP client 
- The client is the only piece that speaks the MCP protocols to one server ,the host is the whole app around it ,client is the specfic chat interface of any terminal interface .
- It contains the connection handling and it lives inside the AI app .It has no model but the app it lives in does .
# Host 
- It is the whole app around it .
- The host is the AI application you actually open and type into,such as CLAUDE Desktop or cursor .
- Host hold the model
- Host create the client => It creates the one clinet per MCP server and manages those connections . It reads the config 
- Host provides the interface => The chat window ,terminal or editor 
- One host can create many client .
- One client can be connected to one server only .
- To add a server into the host we make the changes in the host config file .

# Connection 
- Each connection is isloated .
- MCP server connection depends upon the transport channel 
  - A stdio server handles exactly one connection 
  - While an HTTP SERVER can handle many with the no limit set by protocol 
  - 




# STDIO
- State live per process 
- Environments and secrets 



# First project 
- A small notes server 
- Build order

1. Set up the project and the SDK.
2. Add the storage helpers (load and save the JSON file).
3. Add the add and list tools, then test them in the Inspector.
4. Add the read, delete and search tools, with the error cases.
5. Add the resource and the prompt.
6. Connect to Claude Code.
7. Build the Ollama host.