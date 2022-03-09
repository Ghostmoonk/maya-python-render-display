from pymel.core import *
from Utils.Utils import Vector3

class PlayBack:
    values = {}

    @classmethod
    def GetMaxPlaybackPossible(cls):
        return cls.values[max(cls.values,key=cls.values.get)]

    @classmethod  
    def SetMinValuePlayback(cls, key, value):
        cls.values[key] = value
        playbackOptions(e = True, aet = cls.GetMaxPlaybackPossible())
    
    @classmethod
    def AddPlaybackCol(cls, key, value):
        cls.values[key] = value