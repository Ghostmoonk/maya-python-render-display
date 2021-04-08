from pymel.core import *
from Utils.Utils import Vector3

class Camera:
    def __init__(self, name, iniCamPos, pivotPos):
        cam = camera()
        self.name = name
        rename(cam[0], self.name)
        move(iniCamPos.x, iniCamPos.y, iniCamPos.z)
        self.cameraShape = cam[1]
        self.camPivot = spaceLocator(n=self.name +"_Pivot")
        move(pivotPos.x, pivotPos.y, pivotPos.z)
        parent(self.name, self.camPivot)

        aimC = aimConstraint(self.camPivot,self.name,aim=(0,0,-1), u=(0,1,0), mo = False)
        delete(aimC)

