from pymel.core import *
from Utils.Utils import Vector3
import Python_projet_RenderBase.scripts.Playback as PlayBack

reload(PlayBack)

class Camera:
    camerasGroup = group(n="Cameras", w=True)
    def __init__(self, name, iniCamPos, pivotPos):
        cam = camera()
        self.name = name

        PlayBack.PlayBack.AddPlaybackCol(self.name, 10)
        self.turnSpeed = 0
        rename(cam[0], self.name)
        move(iniCamPos.x, iniCamPos.y, iniCamPos.z)
        self.cameraShape = cam[1]
        self.camPivot = spaceLocator(n=self.name +"_Pivot")
        parent(self.camPivot, Camera.camerasGroup)
        move(pivotPos.x, pivotPos.y, pivotPos.z)
        parent(self.name, self.camPivot)

        self.aimConstraint = aimConstraint(self.camPivot, self.name, aim=(0,0,-1), u=(0,1,0), mo = False)
        self.ToggleAimPivot(toggle=False)
        #delete(aimC)
    
    def ToggleAimPivot(self, **kwargs):
        if kwargs["toggle"]:
            setAttr(self.aimConstraint+"."+self.camPivot+"W0", 1)
        else :
            setAttr(self.aimConstraint+"."+self.camPivot+"W0", 0)

    def SetTurnaroundKeyframes(self, **kwargs):
        self.ClearTurnaroundKeyframes()
        duration = floatSliderGrp(self.name+"_f_turnduration",q=True,v=True)
        speed = floatSliderGrp(self.name+"_f_turnspeed",q=True,v=True)

        frameRate = mel.eval('float $fps = `currentTimeUnitToFPS`')
        lastFrame = duration * float(frameRate)
        select(self.camPivot)
        setCurrentTime(0)
        setKeyframe(v=0,at='rotateY')
        playbackOptions(e=True, ast = 0)

        PlayBack.PlayBack.SetMinValuePlayback(self.name, lastFrame)

        setCurrentTime(lastFrame)
        setKeyframe(v=speed*10,at='rotateY')

        self.ToggleMuteKeyframes(checkBox(self.name+"_boxTurnaround",q=True,v=True))

    def ClearTurnaroundKeyframes(self, **kwargs):
        select(self.camPivot)
        cutKey(cl=True)

    def ToggleMuteKeyframes(self, toggle):
        if toggle:
            mute(self.camPivot + '.rotateY', d=True, f=True)
        else :
            mute(self.camPivot + '.rotateY')

    @classmethod
    def SetCurrentCamera(cls, **kwargs):
        lookThru("perspView", kwargs["newCurrentCameName"])