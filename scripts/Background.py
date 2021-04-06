from pymel.core import *
from arnold import *
from mtoa.utils import *

hdriFolderPath = internalVar(usd=True) + "Python_projet_RenderBase/sourceimages"
assetsFolderPath = internalVar(usd=True) + "Python_projet_RenderBase/assets"

skyDome = createLocator("aiSkyDomeLight", asLight=True)
hdriFile = shadingNode('file', name="HDRIFile", asTexture=True, isColorManaged = True)

def ImportHDRI():
    filters = "HDRI Files (*.hdr)"
    hdriPath = fileDialog2(dir=hdriFolderPath, fm=1, cap= "Import a HDRI file", ff=filters)
    return hdriPath

def SetHDRIFile(connect):
    hdriFilePath = ImportHDRI()[0]
    setAttr(hdriFile+".fileTextureName", hdriFilePath)
    
    if(not isConnected(hdriFile+".outColor",skyDome[0].split("|")[2]+".color") and connect):
        connectAttr( hdriFile+".outColor", skyDome[0].split("|")[2]+".color")

    fileName = hdriFilePath.split("/")
    return fileName[len(fileName)-1]

def SetTurnaroundKeyframes(duration, speed):

    frameRate = mel.eval('float $fps = `currentTimeUnitToFPS`')
    print(frameRate)
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

ground = importFile(assetsFolderPath + "/Ground.ma")