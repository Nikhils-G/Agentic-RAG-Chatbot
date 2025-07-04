# mcp/message_dispatcher.py

class MCPMessage:
    def __init__(self, sender, receiver, type, trace_id, payload):
        self.sender = sender
        self.receiver = receiver
        self.type = type
        self.trace_id = trace_id
        self.payload = payload

class MCPDispatcher:
    def __init__(self):
        self.handlers = {}

    def register_agent(self, agent_name, handler_func):
        self.handlers[agent_name] = handler_func

    def send_message(self, message: MCPMessage):
        handler = self.handlers.get(message.receiver)
        if handler:
            handler(message)
        else:
            print(f"No handler found for {message.receiver}")
