from os import getenv

def read_envs_to_dict(envs: list[str]):
    """look for variable in .env file which are in the list provided as "envs".

    Args:
        envs (list): A list of .env vriable name

    Returns:
        {key: value, ...}
        the "key" is the variable name in .env (envs)
        the "value" is the value associated to it in .env OR None if nothing exist for a key
        ... foreach value in "envs" arg.
    """
    assert isinstance(envs, list)
    return dict((env, getenv(env)) for env in envs)