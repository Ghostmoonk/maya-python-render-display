from pymel.core import *
from arnold import *
from mtoa.utils import *

hdriFolderPath = internalVar(usd=True) + "Python_projet_RenderBase/sourceimages"
assetsFolderPath = internalVar(usd=True) + "Python_projet_RenderBase/assets"

skyDome = createLocator("aiSkyDomeLight", asLight=True)

hdriFile = shadingNode('file', name="CustomHDRIFile", asTexture=True, isColorManaged = True)

#Default HDRI Files

hdriPresetsFile = {
    1 : hdriFolderPath + "/spiaggia_di_mondello_8k.hdr",
    2 : hdriFolderPath + "/dikhololo_night_4k.hdr",
    3 : hdriFolderPath + "/studio_small_02_8k.hdr"
}

def ImportHDRI():
    filters = "HDRI Files (*.hdr)"
    hdriPath = fileDialog2(dir=hdriFolderPath, fm=1, cap= "Import a HDRI file", ff=filters)
    return hdriPath

def SetHDRIFile(connect, presetIndex):
    if(presetIndex == 4): 
        hdriFilePath = ImportHDRI()[0]
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

    select(skyDome[0].split("|")[1])
    setCurrentTime(0)
    setKeyframe(v=0,at='rotateY')
    playbackOptions(e=True, ast = 0)
    playbackOptions(e=True, aet = lastFrame)
    setCurrentTime(lastFrame)
    setKeyframe(v=speed*10,at='rotateY')

def ClearTurnaroundKeyframes():
    select(skyDome[0].split("|")[1])
    cutKey(cl=True)

def SetFieldText(fieldName, text):
    textField(fieldName, e=True, tx=text)

ground = importFile(assetsFolderPath + "/Ground.ma")