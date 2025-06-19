# 📝 Notes MCP Server

> A lightweight Model Context Protocol (MCP) server for managing notes - perfect for learning MCP fundamentals!

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 What is this?

This is a **super simple MCP server** that demonstrates the core concepts of the Model Context Protocol by managing a collection of notes. It's designed to be your first step into the MCP ecosystem - easy to understand, modify, and extend!

## ✨ Features

- 📖 **Read Notes**: Retrieve individual notes or view all notes at once
- ✍️ **Create Notes**: Add new notes with custom IDs and content
- 🔍 **Resource Discovery**: Expose notes as MCP resources
- 🌐 **HTTP API**: RESTful endpoints with Server-Sent Events (SSE) transport
- 🐛 **Debug Mode**: Comprehensive logging for development

## 🛠️ Available Tools

| Tool | Description | Parameters |
|------|-------------|------------|
| `ReadAllNotes` | Get all notes in the system | None |
| `ReadNote` | Read a specific note by ID | `note_id` (string) |
| `CreateNote` | Create a new note | `note_id` (string), `content` (string) |

## 📋 Resources

- **`resource://notes`** - Returns a JSON list of all available note IDs

## 🏃‍♂️ Quick Start

### Prerequisites

```bash
pip install mcp starlette
```

### Running the Server

```bash
python notes_server.py
```

The server will start on `http://localhost:8080` with debug logging enabled.

### Testing with the Client

```bash
python test_client.py
```

## 💡 Example Usage

### Server Response
```json
{
  "status": "ok",
  "message": "Notes MCP Server is running",
  "endpoints": {
    "sse": "/sse"
  }
}
```

### Sample Notes
The server comes pre-loaded with sample notes:
- `note1`: "Brincar com os gatos!"
- `note2`: "Ligar para a mãe no domingo" 
- `note3`: "Finalizar o projeto do trabalho"

### Creating a New Note
```python
# Via MCP client
result = await session.call_tool("CreateNote", {
    "note_id": "note4", 
    "content": "Learn more about MCP"
})
```

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   MCP Client    │◄──►│   Notes Server  │◄──►│  In-Memory DB   │
│  (test_client)  │    │ (FastMCP/SSE)   │    │  (Dictionary)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🔧 Configuration

The server runs with these default settings:
- **Host**: `0.0.0.0` (all interfaces)
- **Port**: `8080`
- **Transport**: Server-Sent Events (SSE)
- **Debug Mode**: Enabled
- **Log Level**: DEBUG

## 🎯 Learning Objectives

This project teaches you:

1. **MCP Basics**: Understanding tools, resources, and client-server communication
2. **FastMCP Framework**: Using the Python MCP framework for rapid development
3. **SSE Transport**: Implementing real-time communication with Server-Sent Events
4. **Tool Definition**: Creating properly annotated MCP tools with input schemas
5. **Resource Management**: Exposing data as MCP resources

## 🚀 Next Steps

Ready to level up? Try these enhancements:

- [ ] Add persistent storage (SQLite, JSON files)
- [ ] Implement note editing and deletion
- [ ] Add note categories and tags
- [ ] Create a web UI for the notes
- [ ] Add authentication and user management
- [ ] Implement note search functionality

## 📚 References

- [Getting Started with MCP Servers: The Beginner's Guide](https://community.aws/content/2ygVh3GU4r5UwNlKa9QWwSAsCu9/getting-started-with-mcp-servers-the-beginner-s-guide)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io)
- [FastMCP Framework](https://github.com/modelcontextprotocol/python-sdk)

## 🤝 Contributing

Feel free to fork, modify, and experiment! This is a learning project designed to be your playground for MCP development.

---

**Happy coding!** 🎉 This simple notes server is your gateway to building more complex MCP applications.