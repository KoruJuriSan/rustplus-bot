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