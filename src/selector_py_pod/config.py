import os
from dotenv import dotenv_values


def build_config(env_file: str = '.env') -> dict:
    return {
        **dotenv_values(env_file),
        # **os.environ,
    }
