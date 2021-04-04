from mGui.gui import *
from pymel.core import *
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

# class Inteface(QtWidgets.QDialog):
#     def __init__(self, parent=maya_main_window()):
#         super(Inteface, self).__init__(parent)
        
#         self.setWindowTitle("Test")
#         self.setMinimumWidth(200)
#         # self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

#         self.create_widgets()
#         self.create_layouts()
    
#     def create_widgets(self):
#         self.lineEdit = QtWidgets.QLineEdit()
#         self.checkbox1 = QtWidgets.QCheckBox("Checkbox1")
#         self.checkbox1 = QtWidgets.QCheckBox("Checkbox2")
#         self.dial = QtWidgets.QDial()

#     def create_layouts(self):
#         mainLayout = QtWidgets.QFormLayout(self)
#         mainTabs = QtWidgets.QTabBar(mainLayout)
#         mainTabs.addTab("Model")
#         mainTabs.addTab("Support")
#         mainTabs.addTab("Background")
#         mainTabs.addTab("Lighting")
#         mainTabs.addTab("Camera")
#         mainTabs.addTab("Render Settings")
#         mainLayout.addWidget(self.lineEdit)
#         mainLayout.addWidget(self.checkbox1)
#         mainLayout.addWidget(self.dial)

# if __name__ == "__main__":
#     d= Inteface()
#     d.show()

with Window(t='root', w=440, h=370) as w:
    with ColumnLayout(adj=2):
        with FormLayout() as form:
            with TabLayout(innerMarginWidth=5, innerMarginHeight=5, width=440, h=370) as tabs:
                with ColumnLayout("Model", rs = 10, adj=1, cat=("both",10)) as modelLayout:
                    Separator(h=10, st="none")
                    with RowLayout(nc=4, adj=2):
                        Text("Model :", al="left")
                        TextField("ModelField", en=False)
                        IconTextButton(i=":/browseFolder.png",c="LoadSupportModel('Import support model')")
                        PySide2.QtWidgets.QDial()
                with ColumnLayout("Support", rs = 10, adj=1, cat=("both", 10)) as supportLayout:
                    Separator(h=10, st="none")
                    with RowLayout(nc=3, adj=2):
                        Text("Model :", al="left")
                        TextField("SupportModelField", en=False)
                        IconTextButton(i=":/browseFolder.png",c="LoadSupportModel('Import support model')")
                    with RowLayout(nc=2, adj=2):
                        Text("Material :", al="left")
                        with GridLayout(nc = 4):
                            IconTextButton(i=":/simplexNoise.png")
                            IconTextButton(i=":/simplexNoise.png")
                            IconTextButton(i=":/simplexNoise.png")
                            IconTextButton(i=":/simplexNoise.png")
                    with RowLayout(nc=2, adj=2):
                        Text("Scale :", al="left")
                        FloatSliderGrp(f=True, v=1.0, min=0.1, max=20.0)
                with ColumnLayout("Background", rs=10, adj=True) as backgroundLayout:
                    Separator(h=10, st="none")
                    with RowLayout(nc=2):
                        CheckBox(l="", v=True)
                        Text("HDRI", fn="boldLabelFont")
                    with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                        with RowLayout(nc=2, adj=2):
                            Text("Show HDRI ", al="left")
                            CheckBox(l="",v=False, w = 10)
                        with RowLayout(nc=3, adj=2):
                            Text("HDRI ", al="left")
                            TextField("SupportModelField", en=False)
                            IconTextButton(i=":/browseFolder.png",c="LoadSupportModel('Import support model')")
                        with RowLayout(nc=2,adj=2):
                            Text("Preset", w=60, al="left")
                            with ColumnLayout(adj=1):
                                RadioButtonGrp("HDRIPreset",vr=True, nrb=4, la4=["Sunset","Night","Studio","Interior"], da1=1, da2=2, da3=3, da4=4)
                        with RowLayout(nc=2,adj=2):
                            Text("Intensity", w=60, al="left")
                            FloatSliderGrp(f=True, v=1.0,min=0.0, max=10.0)
                    with RowLayout(nc=2):
                        CheckBox(l="",v=False, w = 10)
                        Text("Turnaround", fn="boldLabelFont", w = 100)
                    with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                        with RowLayout(nc=2, adj=2):
                            Text("Speed", w=60, al="left")
                            FloatSliderGrp(f=True, v=1.0,min=0.0, max=10.0)
                        with RowLayout(nc=2, adj=2):
                            Text("Duration (s) ", w=60, al="left")
                            FloatSliderGrp(f=True, v=10.0,min=1.0, max=30.0)
                with ColumnLayout("Lights", rs=10, adj=True) as lightsLayout:
                    Separator(h=10, st="none")
                    with RowLayout(nc=2):
                        CheckBox(l="", v=True)
                        Text("Rim light", fn="boldLabelFont")
                    with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                        with RowLayout(nc=2, adj=2):
                            Text("Color", w=60, al="left")
                            ColorSliderGrp()
                        with RowLayout(nc=2, adj=2):
                            Text("Intensity", w=60, al="left")
                            FloatSliderGrp(f=True, v=1.0, max=20.0)
                    with RowLayout(nc=2):
                        CheckBox(l="", v=True)
                        Text("Fill light", fn="boldLabelFont")
                    with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                        with RowLayout(nc=2, adj=2):
                            Text("Color", w=60, al="left")
                            ColorSliderGrp()
                        with RowLayout(nc=2, adj=2):
                            Text("Intensity", w=60, al="left")
                            FloatSliderGrp(f=True, v=1.0, max=20.0)
                    with RowLayout(nc=2):
                        CheckBox(l="", v=True)
                        Text("Main light", fn="boldLabelFont")
                    with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                        with RowLayout(nc=2, adj=2):
                            Text("Color", w=60, al="left")
                            ColorSliderGrp()
                        with RowLayout(nc=2,adj=2):
                            Text("Intensity", w=60, al="left")
                            FloatSliderGrp(f=True, v=1.0, max=20.0)
                        with RowLayout(nc=3):
                            Text("Type", w=60, al="left")
                            OptionMenu()
                            MenuItem(l="Point")
                            MenuItem(l="Area")
                            MenuItem(l="Spot")
                with ColumnLayout("Camera",rs = 10, adj=2, cat=("both",10),cal="center") as cameraLayout:
                    Separator(h=10, st="none")
                    with RowLayout(nc=2):
                        CheckBox(l="",v=False, w = 10)
                        Text("Placement", fn="boldLabelFont", w = 100)
                    Text("Demander a Alain comment creer un Dial")
                    with RowLayout(nc=2):
                        CheckBox(l="",v=False, w = 10)
                        Text("Focus", fn="boldLabelFont", w = 100)
                    with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                        with RowLayout(nc=2, adj=2):
                            Text("Intensity", w=60, al="left")
                            FloatSliderGrp(f=True, v=1.0,min=0.0, max=10.0)
                        with RowLayout(nc=2, adj=2):
                            Text("Distance", w=60, al="left")
                            FloatSliderGrp(f=True, v=1.0,min=0.0, max=10.0)
                    with RowLayout(nc=2):
                        CheckBox(l="",v=False, w = 10)
                        Text("Turnaround", fn="boldLabelFont", w = 100)
                    with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                        with RowLayout(nc=2, adj=2):
                            Text("Speed", w=60, al="left")
                            FloatSliderGrp(f=True, v=1.0,min=0.0, max=10.0)
                        with RowLayout(nc=2, adj=2):
                            Text("Duration (s) ", w=60, al="left")
                            FloatSliderGrp(f=True, v=10.0,min=1.0, max=30.0)
                with ColumnLayout("Render Settings", rs = 10, adj=1, cat=("both", 10)) as rsLayout:
                    Text("Export",fn="boldLabelFont")
                    with RowLayout(nc=3, adj=2):
                        Text("Export path ", al="left")
                        TextField("ExportPath", en=False)
                        IconTextButton(i=":/browseFolder.png",c="SetExportPath('Set export path')")
                    with ColumnLayout():
                        pass
        with RowLayout(nc=3, adj=2):
            Separator(w=100, st="in")
            Button("Render")
            Separator(w=100, st="in")

w.show()

def LoadSupportModel(caption):
    fileName = cmds.fileDialog2(okc="Import", fm=1, ff="All Files (*.*)",cap=caption, ds=2, dir="\..")

    if(fileName == None):
        return

    parsedFile = fileName[0].split("/")
    fileName = parsedFile[len(parsedFile)-1].split(".")[0]
    textField("SupportModelField", e=True, tx=fileName)

def SetExportPath(caption):
    fileName = cmds.fileDialog2(okc="Select", fm=3, ff="All Files (*.*)",cap=caption, ds=2, dir="\..")
    if(fileName == None):
        return
    textField("ExportPath", e=True, tx=fileName)

# def importImage( fileName, fileType):
#    cmds.file( fileName, i=True )

# cmds.fileBrowserDialog( m=0, fc=importImage, ft='image', an='Import_Image', om='Import' )

# window = window(title="Render display",
#                 iconName="Auto RD", widthHeight=(370, 300))

# form = formLayout()
# tabs = tabLayout(innerMarginWidth=5, innerMarginHeight=5)
# formLayout(form, edit=True, attachForm=((tabs, 'top', 0),
#                                         (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))

# modelLayout = rowColumnLayout()

# setParent("..")

# supportLayout = rowColumnLayout()
# setParent("..")

# renderSettingsLayout = rowColumnLayout()
# setParent("..")

# # Lights
# lightsLayout = columnLayout(
#     rs=10, cal='center', adj=True, cat=('both', 25))

# # separator(hr=False, h=5, st="none")
# # RimLight Column
# rowLayout(nc=2)
# checkBox(l="")
# text("Rim light", fn="boldLabelFont")
# setParent("..")

# columnLayout(co=("both", 25))
# rowLayout(nc=2)
# text("Color : ")
# colorSliderGrp()
# setParent("..")

# rowLayout(nc=2)
# text("Intensity : ")
# floatSliderGrp(f=True)
# setParent("..")

# setParent("..")

# # FillLight Column
# rowLayout(nc=2)
# checkBox(l="")
# text("Fill light", fn="boldLabelFont")
# setParent("..")

# columnLayout(co=("both", 25))
# rowLayout(nc=2)
# text("Color : ")
# colorSliderGrp()
# setParent("..")

# rowLayout(nc=2)
# text("Intensity : ")
# floatSliderGrp(f=True)
# setParent("..")
# setParent("..")

# # MainLight Column
# rowLayout(nc=2)
# checkBox(l="")
# text("Main light", fn="boldLabelFont")
# setParent("..")

# columnLayout(co=("both", 25), cal="right")
# rowLayout(nc=2)
# text("Color : ")
# colorSliderGrp()
# setParent("..")

# rowLayout(nc=2)
# text("Intensity : ")
# floatSliderGrp(f=True)
# setParent("..")

# rowLayout(nc=2)
# text("Type : ")
# mainLightType = optionMenu()
# menuItem(l="Point")
# menuItem(l="Area")
# menuItem(l="Spot")
# setParent("..")

# setParent("..")

# setParent("..")
# # Camera

# cameraLayout = rowColumnLayout()
# setParent("..")


# tabLayout(tabs, e=True, tabLabel=(
#     (modelLayout, "Model"),
#     (supportLayout, "Support"),
#     (renderSettingsLayout, "RenderSettings"),
#     (lightsLayout, "Lights"),
#     (cameraLayout, "Camera")))

# showWindow()
