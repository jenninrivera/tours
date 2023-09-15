'''
Server
    Attributes:
        name
        country
    Properties
        name must be uppercase
Message
    Attributes
        content
    Properties
        content must not be empty

Client
    Attributes
        name
'''

class Server:
    MAX_MSGS = 3
    instances = []
    def __init__(self, name, country) -> None:
        self.name = name
        self.country = country
        self.message_log = []

        self.instances.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if new_name.isupper():
            self._name = new_name
        else:
            raise ValueError("server name must be upper case")
        
    @classmethod
    def create_american_server(cls, name):
        return cls(name, 'USA')
    @classmethod
    def create_armenian_server(cls, name):
        return cls(name, 'ARM')
        
        
class Message:
    def __init__(self, content: str, server: Server, client) -> None:
        self.content = content
        self.server = server
        self.client = client
        self.send_msg()
        client.sent_messages.append(self)
    @property
    def content(self):
        return self._content
    @content.setter
    def content(self, new_content):
        if new_content == '':
            raise ValueError("message must not be empty")
        if hasattr(self, "_content"):
            raise ValueError("cannot edit messages")
        self._content = new_content
    
    def send_msg(self):
        if len(self.server.message_log) < Server.MAX_MSGS:
            self.server.message_log.append(self)
        else:
            print('server full')



class Client:
    def __init__(self, name:str) -> None:
        self.name = name
        self.sent_messages = []
        

server1 = Server("ABC", "USA")
client1 = Client("test")
msg1 = Message("Hello", server1, client1)

#msg1.content = "edited message"
