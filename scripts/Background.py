from pymel.core import *
from arnold import *
from mtoa.utils import *
import Python_projet_RenderBase.scripts.Playback as PlayBack
from Utils.Utils import Vector3

reload(PlayBack)

hdriFolderPath = internalVar(usd=True) + "Python_projet_RenderBase/sourceimages/HDRI"
bgFolderPath = internalVar(usd=True) + "Python_projet_RenderBase/assets/Backgrounds"

skyDome = createLocator("aiSkyDomeLight", asLight=True)

hdriFile = shadingNode('file', name="CustomHDRIFile", asTexture=True, isColorManaged = True)

#Default HDRI Files

hdriPresetsFile = {
    1 : hdriFolderPath + "/kiara_8_sunset_4k.hdr",
    2 : hdriFolderPath + "/dikhololo_night_4k.hdr",
    3 : hdriFolderPath + "/studio_small_02_04k.hdr"
}

def ImportAsset(filters, caption, folderPath, fileMode):
    #hdriPath = fileDialog2(dir=hdriFolderPath, fm=1, cap= "Import a HDRI file", ff=filters)
    hdriPath = fileDialog2(dir=folderPath, fm=fileMode, cap= caption, ff=filters)
    return hdriPath

def SetHDRIFile(connect, presetIndex):
    if(presetIndex == 4):
        try: 
            hdriFilePath = ImportAsset("HDRI Files (*.hdr)", "Import a HDRI file", hdriFolderPath, 1)[0]
        except:
            print("No HDRI selected")
            return
        setAttr(hdriFile + ".fileTextureName", hdriFilePath)
    else :
        hdriFilePath = hdriPresetsFile[presetIndex]
        setAttr(hdriFile + ".fileTextureName", hdriFilePath)
    
    if(not isConnected(hdriFile + ".outColor",skyDome[0].split("|")[2]+".color") and connect):
        connectAttr( hdriFile + ".outColor", skyDome[0].split("|")[2]+".color")

    fileName = hdriFilePath.split("/")
    return fileName[len(fileName)-1].split('.')[0]

def SetTurnaroundKeyframes(duration, speed):
    frameRate = mel.eval('float $fps = `currentTimeUnitToFPS`')
    lastFrame = duration * float(frameRate)

    ClearTurnaroundKeyframes()
    select(skyDome[0].split("|")[1])
    setCurrentTime(0)
    setKeyframe(v=0, at='rotateY')
    playbackOptions(e=True, ast = 0)
    PlayBack.PlayBack.SetMinValuePlayback(skyDome[0].split("|")[1], lastFrame)

    setCurrentTime(lastFrame)
    setKeyframe(v=speed*10,at='rotateY')

def ToggleMuteKeyframes(toggle):
    select(skyDome[0].split("|")[1])
    if toggle:
        mute(skyDome[0].split("|")[1] + '.rotateY', d=True, f=True)
    else :
        mute(skyDome[0].split("|")[1] + '.rotateY')


def ClearTurnaroundKeyframes():
    select(skyDome[0].split("|")[1])
    cutKey(cl=True)

def SetFieldText(fieldName, text):
    textField(fieldName, e=True, tx=text)

class BackgroundModel():
    def __init__(self):
        importedNodes = importFile(bgFolderPath + "/Ground.ma",gr=True, gn="Background", returnNewNodes=True)
        self.name = ls(importedNodes,typ="transform")[1]

        self.shader = cmds.shadingNode('aiStandardSurface', asShader=True, n="socleMaterial")
        select(self.name)
        hyperShade(a=self.shader)

    def SetBGModel(self):
        filters = "All Files (*.*);;Fbx Files (*.fbx);; OBJ Files(*.obj);; Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb)"
        try:
            bgModelFilePath = ImportAsset(filters, "Import your background model", bgFolderPath, 1)[0]
        except:
            print("No background selected")
            return
        delete(self.name)
        importedNodes = importFile(bgModelFilePath, returnNewNodes=True)
        self.name = ls(importedNodes,typ="transform")[0]
        self.shader = cmds.shadingNode('aiStandardSurface', asShader=True, n="socleMaterial")
        select(self.name)
        hyperShade(a=self.shader)
        parent(self.name, "Background")
    
    def SetNewColor(self, color):
        setAttr(self.shader+".baseColor",(color.x,color.y,color.z))