import asyncio
from rustplus import RustSocket
from dotenv import load_dotenv
from src.scripts.read_envs_to_dict import read_envs_to_dict
from src.scripts.check_if_dict_elements_are_defined import check_if_dict_elements_are_defined

async def main():

    load_dotenv()

    envs = ["IP", "PORT", "STEAMID", "TOKEN"]
    info = read_envs_to_dict(envs)
    [is_definied, element_not_defined] = check_if_dict_elements_are_defined(info)

    if (not is_definied):
        print(f"La variable d'environnement {element_not_defined} n'existe pas ou n'a pas de valeur !")
    else:
        socket = None
        socket = RustSocket(info["IP"], info["PORT"], int(info["STEAMID"]), int(info["TOKEN"]))
        if (socket is not None):
            await socket.connect()
            # rustplus Bot code
            await socket.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
