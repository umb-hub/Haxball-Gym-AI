from gym import error, spaces
from gym import utils

try:
    import hfo_py
except ImportError as e:
    raise error.DependencyNotInstalled("{}. (HINT: you can install HFO dependencies with 'pip install gym[soccer].)'".format(e))


class HaxballEnv(Env):
    
    def __init__(self):
        pass
    
    def step(self):
        pass

    def render(self):
        pass

    def reset(self):
        pass