from pymel.core import *
from pymel.core.nodetypes import *
from pymel.core.rendering import *
from abc import ABCMeta
from arnold.ai_shader_lights import *

class LightData:
    def __init__(self, intensity, exposure, temperature, color, lightType):
        self.intensity = intensity
        self.temperature = temperature
        self.color = color
        self.exposure = exposure
        self.lightType = lightType

class LightFactory:
    lightsGroup = group(n="Lights")
    def createLight(self, name, lightData):
        light = None
        if(lightData.lightType == 1):
            light = shadingNode("pointLight", asLight=True)
        elif (lightData.lightType == 2):
            light = shadingNode("aiAreaLight", asLight=True)
        elif (lightData.lightType == 3):
            light = shadingNode("spotLight", asLight=True)
        elif (lightData.lightType == 4):
            light = shadingNode("directionalLight", asLight=True)
        
        rename(light, name)
        setAttr(light + ".aiExposure", lightData.exposure)
        setAttr(light + ".aiColorTemperature", lightData.temperature)
        setAttr(light + ".color", (lightData.color.x, lightData.color.y, lightData.color.z))
        return light

lightFactory = LightFactory()

def CreateLight(name, position, lightDatas):
    light = lightFactory.createLight(name, lightDatas)
    parent(light, LightFactory.lightsGroup)
    move(position.x, position.y, position.z)
    return light

def ChangeLightColor(light, newColor):
    setAttr(light+".color",(newColor.x,newColor.y,newColor.z))

def ChangeLightExposure(light, newExposure):
    try:
        getAttr(light+".aiExposure")
    except:
        #print("fail")
        return
    setAttr(light+".aiExposure", newExposure)
    
def ChangeLightIntensity(light, newIntensity):
    print(getAttr(light+"Shape.intensity"))
    try:
        getAttr(light+"Shape.intensity")
    except:
        #print("fail")
        return
    setAttr(light+"Shape.intensity", newIntensity)

def ToggleAimCenter(light, toggle):
    if toggle:
        setAttr(light+".CenterW0",1)
    else:
        setAttr(light+".CenterW0",0)
# def ChangeLightType(lightName, type):
#     if(lightData.lightType == 1):
#         light = shadingNode("pointLight", asLight=True)
#     elif (lightData.lightType == 2):
#         light = shadingNode("aiAreaLight", asLight=True)
#     elif (lightData.lightType == 3):
#         light = shadingNode("spotLight", asLight=True)
#     elif (lightData.lightType == 4):
#         light = shadingNode("directionalLight", asLight=True)

#lightFactory.createLight(Vector3(0,0,0),1)

# class LightFactory:
#     def createLight(self, position, lightData):
#         if(lightData.lightType == 1):
#             return PointLight(position, lightData)
#         elif (lightData.lightType == 2):
#             return AreaLight(position, lightData)
#         elif (lightData.lightType == 3):
#             return SpotLight(position, lightData)
#         elif (lightData.lightType == 4):
#             return DirectionalLight(position, lightData)

# class ALight:
#     __metaclass__ = ABCMeta

#     pass



# class PointLight(ALight):

#     def __init__(self, position, lightData):
#         color = lightData.color
#         intensity = lightData.intensity
#         self.light = pointLight(i=intensity, rgb=(color.x, color.y, color.z))
#         move(position. x, position.y, position.z, a=True)


# class SpotLight(ALight):

#     def __init__(self, position, lightData):
#         color = lightData.color
#         intensity = lightData.intensity
#         self.light = spotLight(i=intensity, rgb=(color.x, color.y, color.z))
#         move(position. x, position.y, position.z, a=True)

# class AreaLight(ALight):

#     def __init__(self, position, lightData):
#         color = lightData.color
#         intensity = lightData.intensity
#         self.light = shadingNode('areaLight', al=True,)
#         self.light = AreaLight()
#         move(position. x, position.y, position.z, a=True)

#     def LookAt(self, target):
#         aimConstraint(self.light, target)


# lightFactory = LightFactory()

# light = lightFactory.createLight(
#     Vector3(10, 0, 0), LightData(10, 4000, Vector3(1, 1, 1), 2))
