from envparse import Env


env = Env()
REAL_DATABASE_URL = env.str('REAL_DATABASE_URL', default='postgresql+asyncpg://fast_api:fast_api@0.0.0.0:5433/fast_api')
