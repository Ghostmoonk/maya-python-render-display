from pymel.core import *
from pymel.core.nodetypes import *
from pymel.core.rendering import *
from Utils.Utils import *
from abc import ABCMeta

refresh()


class LightFactory:
    def createLight(self, position, lightData):
        if(lightData.lightType == 1):
            return PointLight(position, lightData)
        elif (lightData.lightType == 2):
            return AreaLight(position, lightData)
        elif (lightData.lightType == 3):
            return SpotLight(position, lightData)


class ALight:
    __metaclass__ = ABCMeta

    pass


class LightData:
    def __init__(self, intensity, temperature, color, lightType):
        self.intensity = intensity
        self.temperature = temperature
        self.color = color
        self.lightType = lightType


class PointLight(ALight):

    def __init__(self, position, lightData):
        color = lightData.color
        intensity = lightData.intensity
        self.light = pointLight(i=intensity, rgb=(color.x, color.y, color.z))
        move(position. x, position.y, position.z, a=True)


class SpotLight(ALight):

    def __init__(self, position, lightData):
        color = lightData.color
        intensity = lightData.intensity
        self.light = spotLight(i=intensity, rgb=(color.x, color.y, color.z))
        move(position. x, position.y, position.z, a=True)


class AreaLight(ALight):

    def __init__(self, position, lightData):
        color = lightData.color
        intensity = lightData.intensity
        self.light = shadingNode('areaLight', al=True,)
        move(position. x, position.y, position.z, a=True)
        print(getAttr("areaLight1.color"))

    def LookAt(self, target):
        aimConstraint(self.light, target)


lightFactory = LightFactory()

light = lightFactory.createLight(
    Vector3(10, 0, 0), LightData(10, 4000, Vector3(1, 1, 1), 2))
