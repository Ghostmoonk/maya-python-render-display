from pymel.core import *
from Utils.Utils import *

supportsFolderPath = internalVar(usd=True) + "Python_projet_RenderBase/assets/Socles"



class Support:
    def __init__(self):
        self.socle = importFile(supportsFolderPath+ '/Socle1.ma', namespace="socle",gr=True, gn="Socle", returnNewNodes=True)

        
        self.shader = cmds.shadingNode('aiStandardSurface', asShader=True, n="socleMaterial")
        print(self.shader)
        select(self.socle)
        hyperShade(a=self.shader)
        #self.changeColor()

    def importSocle(self, num):
        #delete(self.socle)
        if(num<4):
            #cmds.file( 'D:\Users\Justine\ATI\python\maya-python-render-display\scenes\Socle\Socle1.ma', r=True, namespace='socle' )
            fichier = importFile(supportsFolderPath+ '/Socle'+str(num)+'.ma', namespace="socle",gr=True, gn="Socle", returnNewNodes=True)
            self.name = ls(fichier,typ="transform")[1]
            print(self.name)
            return self.name
        else:
            
            filters = "Fbx Files (*.fbx);; OBJ Files(*.obj);; Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
            bgModelFilePath = self.importAsset(filters, "Import your socle model", supportsFolderPath, 1)[0]
            importedNodes = importFile(bgModelFilePath, returnNewNodes=True)

            #self.socle = ls(importedNodes,typ="transform")[0]
            #parent(self.socle, "Socle")
    
    def importAsset(self, filters, caption, folderPath, fileMode):
        #hdriPath = fileDialog2(dir=hdriFolderPath, fm=1, cap= "Import a HDRI file", ff=filters)
        hdriPath = fileDialog2(dir=folderPath, fm=fileMode, cap= caption, ff=filters)
        return hdriPath

    def changeColor(self, color):
        print("color")
        setAttr(self.shader + ".baseColor", color[0], color[1], color[2])

socle = Support()
