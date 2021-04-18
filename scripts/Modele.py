from pymel.core import *
from Utils.Utils import *
from Python_projet_RenderBase.scripts.Interface import modelScaleSlider, modelRotationSlider

supportsFolderPath = internalVar(usd=True) + "Python_projet_RenderBase/assets/Modeles"


class Modele:
    def __init__(self, support):
        self.name=''
        self.boundingBox = Vector3(0,0,0)
        self.support = support

    def importModele(self):
        filters = "All Files (*.*);;Fbx Files (*.fbx);; OBJ Files(*.obj);; Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb)"
        modelFilePath = self.importAsset(filters, "Import your model", supportsFolderPath, 1)

        if modelFilePath != None :
            modelFilePath = modelFilePath[0]
            importedNodes = importFile(modelFilePath, returnNewNodes=True)
            if(self.name != ''):
                delete(self.name)
            transformNodes = ls(importedNodes, typ="transform")
            self.name = transformNodes[len(transformNodes) -1]
            self.boundingBox = exactWorldBoundingBox(self.name)

            modelScaleSlider.dragCommand = "modele.setScale(Interface.modelScaleSlider.value)"
            modelRotationSlider.dragCommand = "modele.rotateY(Interface.modelRotationSlider.value)"
            parent(self.name, "Model")
            self.place()

    def setScale(self, newScale):
        scale(self.name, newScale, newScale,newScale)

    def importAsset(self, filters, caption, folderPath, fileMode):
        hdriPath = fileDialog2(dir=folderPath, fm=fileMode, cap= caption, ff=filters)
        return hdriPath
    
    def place(self):
        if(self.name):
            #Reset position
            setAttr(self.name+".translate",(0,0,0))
            
            #Set pivot
            newPivPosition = Vector3(
                (exactWorldBoundingBox(self.name)[0] + exactWorldBoundingBox(self.name)[3])/2,
                exactWorldBoundingBox(self.name)[1],
                (exactWorldBoundingBox(self.name)[2] + exactWorldBoundingBox(self.name)[5])/2
            )
            select(self.name)
            xform(piv=(newPivPosition.x, newPivPosition.y, newPivPosition.z), ws=True)
            select(cl=True)

            #Replace
            move(-newPivPosition.x, - newPivPosition.y + exactWorldBoundingBox(self.support.name)[4], -newPivPosition.z, self.name, r=True)
            makeIdentity(self.name, a =True, r=True, t=True)
    def rotateY(self, newRotation):
        currentRotation = getAttr(self.name+".rotate")
        currentRotation = Vector3(currentRotation.x,currentRotation.y,currentRotation.z)
        rotate(self.name,currentRotation.x,newRotation,currentRotation.z)
    # def importModele(self):
    #     filters = "All Files (*.*);;Fbx Files (*.fbx);; OBJ Files(*.obj);; Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb)"
    #     bgModelFilePath = self.importAsset(filters, "Import your socle model", supportsFolderPath, 1)[0]
    #     importedNodes = importFile(bgModelFilePath, returnNewNodes=True)
    
