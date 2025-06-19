import asyncio
import json
import traceback
from mcp.client.session import ClientSession
from mcp.client.sse import sse_client
import mcp.types as types

async def message_handler(message):
    """Handle incoming messages from the server."""
    if isinstance(message, Exception):
        print(f"Error in message handler: {message}")
        traceback.print_exc()
        return
    
    print(f"Received message from server: {message}")

async def main():
    print("Connecting to Notes MCP server...")
    try:
        # Connect to the MCP server using the sse_client
        print("Establishing SSE connection...")
        async with sse_client("http://localhost:8080/sse") as (read_stream, write_stream):
            print("SSE connection established")
            
            # Create a client session
            print("Creating client session...")
            async with ClientSession(
                read_stream,
                write_stream,
                message_handler=message_handler,
                client_info=types.Implementation(name="TestClient", version="1.0.0")
            ) as session:
                # Initialize the session
                print("Initializing session...")
                await session.initialize()
                print("Session initialized")
                
                # List tools
                print("Listing tools...")
                tools = await session.list_tools()
                print(f"Available tools: {[tool.name for tool in tools.tools]}")
                
                # Read the notes resource
                print("Getting notes...")
                notes_resource = await session.read_resource("resource://notes")
                notes_json = notes_resource.contents[0].text
                notes = json.loads(notes_json)
                print(f"Available notes: {notes['note_ids']}")
                
                # Read a note
                print("Reading note1...")
                note1_result = await session.call_tool("ReadNote", {"note_id": "note1"})
                note1_content = note1_result.content[0].text
                print(f"Note 1 says: {note1_content}")
                
                # Create a new note
                print("Creating a new note...")
                create_result = await session.call_tool("CreateNote", {
                    "note_id": "note4", 
                    "content": "Learn more about MCP"
                })
                create_message = create_result.content[0].text
                print(f"Create note result: {create_message}")
                
                # Check that our new note exists
                print("Getting updated notes...")
                updated_notes_resource = await session.read_resource("resource://notes")
                updated_notes_json = updated_notes_resource.contents[0].text
                updated_notes = json.loads(updated_notes_json)
                print(f"Updated notes: {updated_notes['note_ids']}")
                
                # Read our newly created note
                print("Reading new note...")
                new_note_result = await session.call_tool("ReadNote", {"note_id": "note4"})
                new_note_content = new_note_result.content[0].text
                print(f"New note says: {new_note_content}")
                
    except Exception as e:
        print(f"Error connecting to MCP server: {e}")
        traceback.print_exc()
        print("Make sure the server is running with: python new_notes_server.py")

if __name__ == "__main__":
    asyncio.run(main())
