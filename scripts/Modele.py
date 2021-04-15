from pymel.core import *
from Utils.Utils import *

supportsFolderPath = internalVar(usd=True) + "Python_projet_RenderBase/assets"



class Modele:
    def __init__(self):
        self.modele=''

    def importModele(self):
        print("import")
        filters = "Fbx Files (*.fbx);; OBJ Files(*.obj);; Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
        bgModelFilePath = self.importAsset(filters, "Import your socle model", supportsFolderPath, 1)[0]
        importedNodes = importFile(bgModelFilePath, returnNewNodes=True)
    
    def importAsset(self, filters, caption, folderPath, fileMode):
        #hdriPath = fileDialog2(dir=hdriFolderPath, fm=1, cap= "Import a HDRI file", ff=filters)
        hdriPath = fileDialog2(dir=folderPath, fm=fileMode, cap= caption, ff=filters)
        return hdriPath

modele = Modele()