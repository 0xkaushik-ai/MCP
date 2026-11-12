# Why do we need mcp ? 
- MCP exits because a model on its own can only produce text; it cant read your files ,query yoy database or call your API unless something connects it to thme. MCP is the standard way to make that connection .
- Instead of making M*N custom integrations.We write the one MCP server for a service  any MCP-compatible clinet can use it .That turn M*N integration into M+N .
- An MCP server can offer three main things to an AI App and it can also ask how a few things of the app in the reuturn .
  - Funtion that perform actions or computation 
  - Read only data identified by URI 
  - Resuable prompt templates with arguments 
- The model uses the JSON-RPC2.0 message to establish communication between .

- These all defination came from the language server protocol (LSP) is to standardize the protocol how such server and development tools communicate .
# MCP versioning 
- The MCP uses string-based version indentifiers following the format YYYY-MM-DD to indicate the last date backwards incompatible chages were made .

# MCP server 
- MCP servers are programs that expose specific capabilities to AI applications through standardized protocol interfaces. 
- Tools are schema-defined interfaces that LLMs can invoke. MCP uses JSON Schema for validation. Each tool performs a single operation with clearly defined inputs and outputs. Tools may require user consent prior to execution, helping to ensure users maintain control over actions taken by a model
- 
# MCP client 

# Host 
- It is the whole app around it .
- The host is the AI application you actually open and type into,such as CLAUDE Desktop or cursor .
- Host hold the model
- Host create the client => It creates the one clinet per MCP server and manages those connections . It reads the config 
- Host provides the interface => The chat window ,terminal or editor 
- 