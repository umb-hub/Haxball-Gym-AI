from gym import error
from gym import utils
from gym.spaces import Discrete, Box
from GameObjects import StadiumObject, Disc


class HaxballEnv(Env):
    
    def __init__(self):
        """
        Default Environment for 1v1 classic game
        """
        # Define action space as discrete space 
        # 8(directions)+1(no direction))*2(shot input) = 18
        self.action_space(Discrete(18))

        # Define observation space for determine features to be considered 
        # PlayerInfo (Team, position_x, position_y, vel_x, vel_y) x2
        # 
        self.observation_space = Box(low=-5000, high=5000)

        # Define time_limit
        self._ticks = 0
        self.max_ticks = 3*60*60 # 3 minutes * 60 second * 60 frame per second
        
        # Define Stadium
        self.stadium = StadiumObject("classic")

        # Define Dynamic Objects
        self.red_team = [Disc()]
        self.blue_team = [Disc()]
        self.ball = [Disc()]
        self.score = (0, 0)
        self.StatusKO = -1 # {-1 : blue scored or initial situation, 0 : current playing, 1: red scored}
        
        self.reset()
    
    def step(self):
        pass

    def render(self):
        pass

    def reset(self):
        pass