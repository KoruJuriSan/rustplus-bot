import asyncio
from src.scripts.create_rustsocket_with_envs_variables import create_rust_socket_with_envs_variables

async def main():
    socket = create_rust_socket_with_envs_variables()
    if (socket is not None):
        await socket.connect()
        print( await socket.get_info())
        await socket.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
