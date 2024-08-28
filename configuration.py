class Configuration:
    def __init__(self):
        self.assistant_name = "DecidArchV2Assistant"
        self.uri_ollama = "http://192.168.1.206:11434"
        self.model_name = "llama2"

        self.MAX_PLAYERS = 4
        self.MIN_PLAYERS = 2
        self.MAX_STAKEHOLDERS = 2
        self.MAX_CONCERNS = 9
        self.MAX_EVENTS = 5