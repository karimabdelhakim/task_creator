def get_dot_env(base_dir=None):
    """
    Get environment variables from .env file
    Usage:
        env = get_dot_env()
        ENV_VAR = env.str('ENV_VAR')

    @param:base_dir:required if function used in settings module
    returns:environ.Env instance.
    """

    import os
    import environ
    from django.conf import settings

    base_dir = settings.BASE_DIR if base_dir is None else base_dir
    env = environ.Env()
    environ.Env.read_env(env_file=os.path.join(base_dir, ".env"))

    return env
