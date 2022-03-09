from pymel.core import *
from Utils.Utils import *
import Python_projet_RenderBase.scripts.Modele as Modele
from Python_projet_RenderBase.scripts.Interface import socleScaleSlider
import Python_projet_RenderBase.scripts.Interface as Interface

supportsFolderPath = internalVar(usd=True) + "Python_projet_RenderBase/assets/Socles"

class Support:
    def __init__(self, model = ""):
        importedNodes = importFile(supportsFolderPath+ '/Socle1.ma', namespace="socle",gr=True, gn="Socle", returnNewNodes=True)
        transformNodes = ls(importedNodes, typ="transform")
        self.name = transformNodes[len(transformNodes) -1]
        self.shader = cmds.shadingNode('aiStandardSurface', asShader=True, n="socleMaterial")
        self.model = model
        select(self.name)
        hyperShade(a=self.shader)
        
        socleScaleSlider.dragCommand = "socle.setScale(Interface.socleScaleSlider.value)"
        socleScaleSlider.changeCommand = "socle.setScale(Interface.socleScaleSlider.value)"
        select(cl=True)

    def setModel(self, model):
        self.model = model

    def assignShader(self):
        select(self.name)
        hyperShade(a=self.shader)
        
    def importSocle(self, num):
        if(num<4):
            #cmds.file( 'D:\Users\Justine\ATI\python\maya-python-render-display\scenes\Socle\Socle1.ma', r=True, namespace='socle' )
            delete(self.name)
            importedNodes = importFile(supportsFolderPath+ '/Socle'+str(num)+'.ma', returnNewNodes=True)
            transformNodes = ls(importedNodes, typ="transform")
            self.name = transformNodes[len(transformNodes) -1]
            if self.model != "":
                self.model.place()
                
            parent(self.name, "Socle")
            self.assignShader()

        else:
            filters = "All Files (*.*);;Fbx Files (*.fbx);; OBJ Files(*.obj);; Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb)"
            try :
                supportModelFilePath = self.importAsset(filters, "Import your socle model", supportsFolderPath, 1)[0]
            except:  
                #print("EST EGAL A NONE")
                return
            delete(self.name)
            
            
            importedNodes = importFile(supportModelFilePath, returnNewNodes=True)
            transformNodes = ls(importedNodes, typ="transform")
            self.name = transformNodes[len(transformNodes) -1]
            if self.model.name != '':
                self.model.place()
            parent(self.name, "Socle")
            self.assignShader()

        textField("SupportModelField", e=True, tx=self.name)
        select(cl=True)
        return self.name
            #self.socle = ls(importedNodes,typ="transform")[0]
            #parent(self.socle, "Socle")

    def setScale(self, newScale):
        scale(self.name, newScale, newScale,newScale)
        if self.model.name != '':
            self.model.place()

    def importAsset(self, filters, caption, folderPath, fileMode):
        #hdriPath = fileDialog2(dir=hdriFolderPath, fm=1, cap= "Import a HDRI file", ff=filters)
        hdriPath = fileDialog2(dir=folderPath, fm=fileMode, cap= caption, ff=filters)
        return hdriPath

    def changeColor(self, color):
        setAttr(self.shader + ".baseColor", color[0], color[1], color[2])

