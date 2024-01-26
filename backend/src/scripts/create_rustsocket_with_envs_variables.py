from rustplus import RustSocket, CommandOptions
from dotenv import load_dotenv
from src.scripts.read_envs_to_dict import read_envs_to_dict
from src.scripts.check_if_dict_elements_are_defined import check_if_dict_elements_are_defined

cmd_prefix = "#"

def create_rust_socket_with_envs_variables():
    socket: RustSocket or None = None
    load_dotenv()
    envs: list = ["IP", "PORT", "STEAMID", "TOKEN"]
    info: dict = read_envs_to_dict(envs)
    cmd_options = CommandOptions(cmd_prefix)
    [is_definied, element_not_defined] = check_if_dict_elements_are_defined(info)
    
    if (not is_definied):
        print(f"La variable d'environnement {element_not_defined} n'existe pas ou n'a pas de valeur !")
    else:
        socket = RustSocket(info["IP"], info["PORT"], int(info["STEAMID"]), int(info["TOKEN"]), command_options=cmd_options)
    return socket