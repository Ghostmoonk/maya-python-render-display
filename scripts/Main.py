#commandPort -n "localhost:7001" -stp "mel" -echoOutput; To execute in maya
from pymel.core import *
import maya.cmds as cmds

cmds.file(f=True, new=True)

import Python_projet_RenderBase.scripts.Interface as Interface
import Python_projet_RenderBase.scripts.Lighting as Lighting
import Python_projet_RenderBase.scripts.Background as Background
import Python_projet_RenderBase.scripts.Modele as Modele
import Python_projet_RenderBase.scripts.Support as Support
import Python_projet_RenderBase.scripts.Camera as Camera
from Python_projet_RenderBase.scripts.Utils.Utils import *
from mGui.bindings import bind

reload(Interface)
reload(Lighting)
reload(Background)
reload(Support)
reload(Camera)
reload(Modele)

def ShowObject(obj, toggle):
    if toggle:
        showHidden(obj)
    else:
        hide(obj)

# Init modele

centerLocator = spaceLocator(0,0,0, n ="Center")

# Init support

# Init Lights

    #Main
mainLightCol = Vector3(Interface.mainColor.rgbValue[0], Interface.mainColor.rgbValue[1], Interface.mainColor.rgbValue[2])
mainLight = Lighting.CreateLight("KeyLight", Vector3(-2, 2, -2),Lighting.LightData(1, Interface.mainExposure.value, 3000, mainLightCol, 2))
mainAimConstraint = aimConstraint(centerLocator, mainLight, aim=(0,0,-1), u=(0,1,0), mo = False)
Interface.mainCBox.bind.value > bind() > str(mainLight) +'.visibility'
# Interface.mainExposure.bind.value > bind() > listRelatives(mainLight)[0] +'.aiExposure'
Interface.mainExposure.dragCommand = "Lighting.ChangeLightExposure(mainLight, Interface.mainExposure.value)"
Interface.mainColor.dragCommand = "Lighting.ChangeLightColor(mainLight,Vector3(Interface.mainColor.rgbValue[0], Interface.mainColor.rgbValue[1], Interface.mainColor.rgbValue[2]))"
Interface.mainExposure.changeCommand = "Lighting.ChangeLightExposure(mainLight, Interface.mainExposure.value)"
Interface.mainColor.changeCommand = "Lighting.ChangeLightColor(mainLight,Vector3(Interface.mainColor.rgbValue[0], Interface.mainColor.rgbValue[1], Interface.mainColor.rgbValue[2]))"

Interface.mainAimCBox.bind.value > bind() > mainAimConstraint+".CenterW0"
    #Rim
rimLightCol = Vector3(Interface.rimColor.rgbValue[0], Interface.rimColor.rgbValue[1], Interface.rimColor.rgbValue[2])
rimLight = Lighting.CreateLight("RimLight", Vector3(2, 2,2),Lighting.LightData(1, Interface.rimExposure.value, 3000, rimLightCol, 2))
rimAimConstraint = aimConstraint(centerLocator, rimLight, aim=(0,0,-1), u=(0,1,0), mo = False)
Interface.rimCBox.bind.value > bind() > str(rimLight) + '.visibility'
# Interface.rimExposure.bind.value > bind() > listRelatives(rimLight)[0] +'.aiExposure'
Interface.rimExposure.dragCommand = "Lighting.ChangeLightExposure(rimLight, Interface.rimExposure.value)"
Interface.rimColor.dragCommand = "Lighting.ChangeLightColor(rimLight,Vector3(Interface.rimColor.rgbValue[0], Interface.rimColor.rgbValue[1], Interface.rimColor.rgbValue[2]))"
Interface.rimExposure.changeCommand = "Lighting.ChangeLightExposure(rimLight, Interface.rimExposure.value)"
Interface.rimColor.changeCommand = "Lighting.ChangeLightColor(rimLight,Vector3(Interface.rimColor.rgbValue[0], Interface.rimColor.rgbValue[1], Interface.rimColor.rgbValue[2]))"

Interface.rimAimCBox.bind.value > bind() > rimAimConstraint+".CenterW0"

    #Fill
fillLightCol = Vector3(Interface.fillColor.rgbValue[0], Interface.fillColor.rgbValue[1], Interface.fillColor.rgbValue[2])
fillLight = Lighting.CreateLight("FillLight",Vector3(-2, 2, 1.5), Lighting.LightData(1, Interface.fillExposure.value, 3000, fillLightCol, 2))
Interface.fillCBox.bind.value > bind() > str(fillLight) + '.visibility'
fillAimConstraint = aimConstraint(centerLocator, fillLight, aim=(0,0,-1), u=(0,1,0), mo = False)
#Interface.fillExposure.bind.value > bind() > listRelatives(fillLight)[0] +'.aiExposure'
Interface.fillExposure.dragCommand = "Lighting.ChangeLightExposure(fillLight, Interface.fillExposure.value)"
Interface.fillColor.dragCommand = "Lighting.ChangeLightColor(fillLight,Vector3(Interface.fillColor.rgbValue[0], Interface.fillColor.rgbValue[1], Interface.fillColor.rgbValue[2]))"
Interface.fillExposure.changeCommand = "Lighting.ChangeLightExposure(fillLight, Interface.fillExposure.value)"
Interface.fillColor.changeCommand = "Lighting.ChangeLightColor(fillLight,Vector3(Interface.fillColor.rgbValue[0], Interface.fillColor.rgbValue[1], Interface.fillColor.rgbValue[2]))"

Interface.fillAimCBox.bind.value > bind() > fillAimConstraint+".CenterW0"

#shadingNode("spotLight", al=True)
# Interface.fillLightType.changeCommand = "Interface."

    #Directional
directionalLightCol = Vector3(Interface.dirColor.rgbValue[0], Interface.dirColor.rgbValue[1], Interface.dirColor.rgbValue[2])
dirLight = Lighting.CreateLight("DirectionalLight", Vector3(0, 5, 0), Lighting.LightData(1, Interface.dirExposure.value, 3000, fillLightCol, 4))
Interface.dirCBox.bind.value > bind() > str(dirLight) + '.visibility'
#aimConstraint(centerLocator, dirLight, aim=(0,0,-1), u=(0,1,0), mo = False)
#Interface.fillExposure.bind.value > bind() > listRelatives(fillLight)[0] +'.aiExposure'
Interface.dirExposure.dragCommand = "Lighting.ChangeLightIntensity(dirLight, Interface.dirExposure.value)"
Interface.dirColor.dragCommand = "Lighting.ChangeLightColor(dirLight,Vector3(Interface.dirColor.rgbValue[0], Interface.dirColor.rgbValue[1], Interface.dirColor.rgbValue[2]))"
Interface.dirExposure.changeCommand = "Lighting.ChangeLightIntensity(dirLight, Interface.dirExposure.value)"
Interface.dirColor.changeCommand = "Lighting.ChangeLightColor(dirLight,Vector3(Interface.dirColor.rgbValue[0], Interface.dirColor.rgbValue[1], Interface.dirColor.rgbValue[2]))"


ShowObject(mainLight, Interface.mainCBox.value)
ShowObject(rimLight, Interface.rimCBox.value)
ShowObject(fillLight, Interface.fillCBox.value)

#Init background
bgModel = Background.BackgroundModel()

Interface.bgModelColor.dragCommand =  "bgModel.SetNewColor(Vector3(Interface.bgModelColor.rgbValue[0],Interface.bgModelColor.rgbValue[1],Interface.bgModelColor.rgbValue[2]))"
Interface.bgModelColor.changeCommand =  "bgModel.SetNewColor(Vector3(Interface.bgModelColor.rgbValue[0],Interface.bgModelColor.rgbValue[1],Interface.bgModelColor.rgbValue[2]))"

Interface.loadBGModelButton.command = "bgModel.SetBGModel();"
Interface.loadBGModelButton.command += "SetFieldText(\"BGModelField\", bgModel.name)"

Interface.backgroundCBox.bind.value > bind() > bgModel.name+'.visibility'
Interface.backgroundCBox.bind.value < bind() < bgModel.name+'.visibility'
#Init background HDRI
currentHDRI = ""
Interface.loadHDRIButton.command = "currentHDRI = Background.SetHDRIFile(Interface.showHDRIBox.value, 4);"
Interface.loadHDRIButton.command += "SetFieldText(\"HDRIField\", currentHDRI)"

Interface.hdriRadioPresets.onCommand = "currentHDRI = Background.SetHDRIFile(Interface.showHDRIBox.value, Interface.hdriRadioPresets.select);"

Interface.hdriRadioPresets.onCommand += "SetFieldText(\"HDRIField\", currentHDRI)"

Interface.skyDomeCBox.bind.value > bind() > str(Background.skyDome[0].split("|")[1]) + '.visibility'
Interface.hdriExposure.bind.value > bind() > str(Background.skyDome[0].split("|")[2]) + '.aiExposure'
Interface.skyDomeColor.dragCommand = "Lighting.ChangeLightColor(Background.skyDome[0].split('|')[2],Vector3(Interface.skyDomeColor.rgbValue[0], Interface.skyDomeColor.rgbValue[1], Interface.skyDomeColor.rgbValue[2]))"
Interface.skyDomeColor.changeCommand = "Lighting.ChangeLightColor(Background.skyDome[0].split('|')[2],Vector3(Interface.skyDomeColor.rgbValue[0], Interface.skyDomeColor.rgbValue[1], Interface.skyDomeColor.rgbValue[2]))"

Interface.showHDRIBox.onCommand = "LinkAttr(Background.hdriFile+\".outColor\", Background.skyDome[0].split('|')[2]+\".color\", True)"
Interface.showHDRIBox.offCommand = "LinkAttr(Background.hdriFile+\".outColor\", Background.skyDome[0].split('|')[2]+\".color\", False)"

def SetFieldText(fieldName, text):
    textField(fieldName, e=True, tx=text)

def LinkAttr(source, dest, toggle):
    if toggle and not isConnected(source, dest):
        connectAttr(source, dest)
    elif not toggle and isConnected(source, dest):
        disconnectAttr(source, dest)

# Socle
Interface.socleColor.dragCommand = "socle.changeColor(Interface.socleColor.rgbValue)"
Interface.socleColor.changeCommand = "socle.changeColor(Interface.socleColor.rgbValue)"

Interface.loadSocle.command = "loadSupportModeleCommand_handler(4)"
Interface.socle1.command = "loadSupportModeleCommand_handler(1)"
Interface.socle2.command = "loadSupportModeleCommand_handler(2)"
Interface.socle3.command = "loadSupportModeleCommand_handler(3)"

def loadSupportModeleCommand_handler(value):
    socle.importSocle(value)
    socle.setScale(Interface.socleScaleSlider.value)
#Modele
Interface.loadModele.command = "loadModeleCommand_handler()"

def loadModeleCommand_handler():
    modele.importModele()
    modele.setScale(Interface.modelScaleSlider.value)
    

#Background turnaround

Interface.backgroundTurnaroundCBox.onCommand = "Background.SetTurnaroundKeyframes(Interface.backgroundTurnDuration.value,Interface.backgroundTurnSpeed.value);"
Interface.backgroundTurnaroundCBox.onCommand += "Background.ToggleMuteKeyframes(True)"

Interface.backgroundTurnaroundCBox.offCommand = "Background.ToggleMuteKeyframes(False)"

Interface.backgroundTurnDuration.dragCommand = "Background.SetTurnaroundKeyframes(Interface.backgroundTurnDuration.value,Interface.backgroundTurnSpeed.value)"
Interface.backgroundTurnSpeed.dragCommand = "Background.SetTurnaroundKeyframes(Interface.backgroundTurnDuration.value,Interface.backgroundTurnSpeed.value)"
Interface.backgroundTurnDuration.changeCommand = "Background.SetTurnaroundKeyframes(Interface.backgroundTurnDuration.value,Interface.backgroundTurnSpeed.value)"
Interface.backgroundTurnSpeed.changeCommand = "Background.SetTurnaroundKeyframes(Interface.backgroundTurnDuration.value,Interface.backgroundTurnSpeed.value)"

Background.SetTurnaroundKeyframes(Interface.backgroundTurnDuration.value,Interface.backgroundTurnSpeed.value)
Background.ToggleMuteKeyframes(Interface.skyDomeCBox.value)

#Camera

Interface.addCameraButton.command = 'addCamera_handler(Interface.newCameraField.text)'
Interface.newCameraField.enterCommand = 'addCamera_handler(Interface.newCameraField.text)'
Interface.newCameraField.changeCommand = "Interface.ToggleAddCameraButton(Interface.newCameraField.text)"
Interface.newCameraField.receiveFocusCommand = "Interface.ToggleAddCameraButton(Interface.newCameraField.text)"

def addCamera_handler(cameraName):
    Callback(Interface.ToggleCameraActive, newCurrentCameName = cameraName)
    Interface.AddCamera(cameraName)
    Interface.ToggleAddCameraButton(cameraName)

renderCam = Interface.AddCamera("RenderCam",Vector3(-8,2,0), Vector3(0, 2, 0))

# cameraView(c="RenderCam", n="Default render view")
Interface.ToggleCameraActive(newCurrentCameName="RenderCam")
# lookThru("perspView", "RenderCam")

#Support
socle = Support.Support()

#Model
group(n="Model", w=True, em=True)
modele = Modele.Modele(socle)
socle.setModel(modele)


