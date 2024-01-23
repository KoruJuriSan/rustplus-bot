from os import getenv

def read_envs_to_dict(envs: list[str]):
    assert isinstance(envs, list)
    return dict((env, getenv(env)) for env in envs)