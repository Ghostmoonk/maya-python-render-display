from pymel.core import *
from Utils.Utils import *
from Python_projet_RenderBase.scripts.Interface import modelScaleSlider

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
            parent(self.name, "Model")
            self.place()

    def setScale(self, newScale):
        scale(self.name, newScale, newScale,newScale)

    def importAsset(self, filters, caption, folderPath, fileMode):
        hdriPath = fileDialog2(dir=folderPath, fm=fileMode, cap= caption, ff=filters)
        return hdriPath
    
    def place(self):
        #Set pivot
        newPivPosition = Vector3(
            (exactWorldBoundingBox(self.name)[0] + exactWorldBoundingBox(self.name)[3])/2,
            exactWorldBoundingBox(self.name)[1],
            (exactWorldBoundingBox(self.name)[2] + exactWorldBoundingBox(self.name)[5])/2
        )
        print(exactWorldBoundingBox(self.name))
        print(newPivPosition)
        #Reset position
        setAttr(self.name+".translate",(0,0,0))
        
        select(self.name)
        print(xform(bb=True, q=True))
        
        xform(piv=(newPivPosition.x, newPivPosition.y, newPivPosition.z), ws=True)
        select(cl=True)

        #Replace
        move(0, - newPivPosition.y + exactWorldBoundingBox(self.support.name)[4], 0, self.name, r=True)

    # def importModele(self):
    #     filters = "All Files (*.*);;Fbx Files (*.fbx);; OBJ Files(*.obj);; Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb)"
    #     bgModelFilePath = self.importAsset(filters, "Import your socle model", supportsFolderPath, 1)[0]
    #     importedNodes = importFile(bgModelFilePath, returnNewNodes=True)
    
