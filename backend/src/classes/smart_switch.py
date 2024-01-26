from  rustplus import RustSocket

class Smart_switch():
    entity_id: int
    is_on: bool
    name: str
    desc: str


    def __init__(self, entity_id: int, name: str, desc: str):
        self.entity_id = entity_id
        self.name = name
        self.desc = desc
        self.is_on = False


    async def toggle(self, socket: RustSocket):
        if (self.is_on):
            await socket.turn_off_smart_switch(self.entity_id)
            self.is_on = False
        else:
            await socket.turn_on_smart_switch(self.entity_id)
            self.is_on = True

    
    async def turn_on(self, socket: RustSocket):
        """
        Turn on this Smart switch 
        (will probably not work if the smart switch as been update manually in the game)

        Args:
            socket (RustScoket): current rustsocket

        Return: void
        """
        await socket.turn_on_smart_switch(self.entity_id)
        self.is_on = True
    

    async def turn_off(self, socket: RustSocket):
        """
        Turn off this Smart switch 
        (will probably not work if the smart switch as been update manually in the game)

        Args:
            socket (RustSocket): current rustsocket

        Return: void
        """
        await socket.turn_off_smart_switch(self.entity_id)
        self.is_on = False


    async def update(self, socket: RustSocket):
        """
        Update instance information about the Switch current value 
        (could be important to run before turn_off/on or toggle method to make them work in any case)

        Args:
            socket (RustSocket): current rustsocket

        Return: void
        """
        switch_data = await socket.get_entity_info(self.entity_id)
        self.is_on = switch_data.value