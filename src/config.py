from pathlib import Path

from envparse import env

BASE_DIR = Path(__file__).resolve().parent.parent

if (env_path := BASE_DIR.joinpath('.env')) and env_path.is_file():
    env.read_envfile(env_path)

CURRENCY_APY_KEY = env.str('CURRENCY_APY_KEY')
