from fileinput import filename
from mGui.gui import *
from mGui.bindings import bind
from mGui import lists
from mGui import forms
from pymel.core import *
from mGui.observable import ViewCollection
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from Utils.Utils import Vector3
import Python_projet_RenderBase.scripts.Camera as Camera
import Python_projet_RenderBase.scripts.RenderSettings as RenderSettings

# reload(Camera)
reload(RenderSettings)

iconsPath = internalVar(usd=True) + "Python_projet_RenderBase/sourceimages/Icons"
# def maya_main_window():
#     main_window_ptr = omui.MQtUtil.mainWindow()
#     return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

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

camerasDict = {}

class CameraWidget(lists.ItemTemplate):

    def widget(self, item):
        # with forms.HorizontalExpandForm(tag=item) as root:
        with RowLayout(nc=3, rat=[(1,'top',0), (3,'top',0)], adj=2) as root:
            camActiveButton = IconTextButton(item+"_activeButton",i=iconsPath +"/close-eye.png", c=Callback(ToggleCameraActive, newCurrentCameName = item))
            with FrameLayout(item, cll=True) as cameraL:
                with ColumnLayout(rs=5, adj=True):
                    with RowLayout(nc=2, adj=2, rat=(1,'top',5), cat=(1,'right',5)):
                        dofCBox = CheckBox(item +"_f_dof",l="",v=False)
                        with FrameLayout("Focus", cll=True):
                            with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                                with RowLayout(nc=2, adj=2):
                                    Text("FStop", w=60, al="left")
                                    cameraFStop = FloatSliderGrp(item+"_f_fstop",f=True, v=1.0,min=0.0, max=64.0)
                                with RowLayout(nc=2, adj=2):
                                    Text("Distance", w=60, al="left")
                                    cameraFocusDistance = FloatSliderGrp(item+"_f_distance", f=True, v=1.0,min=0.0, max=10.0)
                                with RowLayout(nc=2, adj=2):
                                    Text("Focus region scale", w=60, al="left")
                                    cameraFocusRegion = FloatSliderGrp(item+"_f_focusscale", f=True, v=1.0,min=0.0, max=20.0)
                    with RowLayout(nc=2, adj=2, rat=(1,'top',5), cat=(1,'right',5)):
                        camTurnaroundCBox = CheckBox(item + "_boxTurnaround",l="",v=False)
                        with FrameLayout("Turnaround", cll=True):
                            with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                                with RowLayout(nc=2, adj=2):
                                    Text("Speed", w=60, al="left")
                                    cameraTurnaroundSpeed = FloatSliderGrp(str(item) + "_f_turnspeed",f=True, v=1.0,min=0.0, max=300.0)
                                with RowLayout(nc=2, adj=2):
                                    Text("Duration (s) ", w=60, al="left")
                                    cameraTurnaroundDuration = FloatSliderGrp(str(item) + "_f_turnduration", f=True, v=10.0,min=1.0, max=15.0)
                    with RowLayout(nc=2, adj=2, cal=(2,"left"), cat=(2,"left",32)):
                        Text("Focale", fn="plainLabelFont")
                        camFocale = FloatSliderGrp(str(item) + "_f_focale", f=True, v=35.0, min=10.0, max=350.0)
                    with RowLayout(nc=2, adj=2, cal=(2,"left"), cat=(2,"left",32)):
                        camOrientPivot = CheckBox(item+"_camOrientCBox", l="", v=False)
                        Text("Aim child 'LookAt' locator",fn="plainLabelFont")
            IconTextButton(i=":/delete.png", c= Callback(RemoveCamera, item, p=1))

        dofCBox.bind.value > bind() > item+"Shape.depthOfField"
        cameraFStop.bind.value > bind() > item+"Shape.fStop"
        cameraFocusRegion.bind.value > bind() > item+"Shape.focusRegionScale"
        cameraFocusDistance.bind.value > bind() > item+"Shape.focusDistance"
        camFocale.dragCommand = Callback(camerasDict[item].SetFocale, newFocale = camFocale.value)
        camFocale.changeCommand = Callback(camerasDict[item].SetFocale, newFocale = camFocale.value)
        #camFocale.bind.value > bind() > item+"Shape.focalLength"

        camTurnaroundCBox.onCommand = Callback(camerasDict[item].SetTurnaroundKeyframes, p = 1)
        camTurnaroundCBox.offCommand = Callback(camerasDict[item].SetTurnaroundKeyframes, p = 1)
        
        cameraTurnaroundSpeed.dragCommand = Callback(camerasDict[item].SetTurnaroundKeyframes, p = 1)
        cameraTurnaroundDuration.dragCommand = Callback(camerasDict[item].SetTurnaroundKeyframes, p = 1)
        cameraTurnaroundSpeed.changeCommand = Callback(camerasDict[item].SetTurnaroundKeyframes, p = 1)
        cameraTurnaroundDuration.changeCommand = Callback(camerasDict[item].SetTurnaroundKeyframes, p = 1)

        camOrientPivot.onCommand = Callback(camerasDict[item].ToggleAimPivot, toggle = True)
        camOrientPivot.offCommand = Callback(camerasDict[item].ToggleAimPivot, toggle = False)

        #camActiveButton.command = Callback(Camera.Camera.SetCurrentCamera, newCurrentCameName = item)
        #camActiveButton.command = Callback(ToggleCameraActive, newCurrentCameName = item)
        
        return lists.Templated(item, root)

    def __call__(self, item):
        return self.widget(item)

def RemoveCamera(item, **kwargs):
    cameraCollection.remove(item)
    camerasDict.pop(item)
    delete(item+"_Pivot")
    if(objExists(item)):
        delete(item)

def ShowObject(obj, toggle):
    if toggle:
        showHidden(obj)
    else:
        hide(obj)

with BindingWindow(t='Auto Render setup', w=450, h=370) as w:
    with ColumnLayout(adj=2):
        with FormLayout() as form:
            with TabLayout(innerMarginWidth=5, innerMarginHeight=5, width=450, h=370) as tabs:
                with ColumnLayout("Model", rs = 10, adj=1, cat=("both",10)) as modelLayout:
                    Separator(h=10, st="none")
                    with RowLayout(nc=3, adj=2):
                        Text("Model ", al="left")
                        modelField = TextField("ModelField", en=False)
                        loadModele = IconTextButton(i=iconsPath +"/browseFolder.png", c="LoadSupportModel('Import support model')")
                    with RowLayout(nc=2, adj=2):
                        Text("Scale ", al="left")
                        modelScaleSlider = FloatSliderGrp(f=True, v=1.0, min=0.1, max=20.0)
                    with RowLayout(nc=2, adj=2):
                        Text("Rotation ", al="left")
                        modelRotationSlider = FloatSliderGrp(f=True, v=1.0, min=0.1, max=360.0)
                with ColumnLayout("Support", rs = 10, adj=1, cat=("both", 10)) as supportLayout:
                    Separator(h=10, st="none")
                    with RowLayout(nc=3, adj=2):
                        Text("Model ", al="left")
                        TextField("SupportModelField", en=False)
                        loadSocle = IconTextButton(i=iconsPath +"/browseFolder.png")
                    with RowLayout(nc=2, adj=2):
                        Text("Preset ", al="left")
                        with GridLayout(nc = 4):
                            socle1 = IconTextButton(i=iconsPath+"/socle1.png", st="iconOnly")
                            socle2 = IconTextButton(i=iconsPath+"/socle2.png", st="iconOnly")
                            socle3 = IconTextButton(i=iconsPath+"/socle3.png", st="iconOnly")
                    with RowLayout(nc=2, adj=2):
                        Text("Scale ", al="left")
                        socleScaleSlider = FloatSliderGrp(f=True, v=1.0, min=0.1, max=20.0)
                    with RowLayout(nc=2, adj=2):
                        Text("Color ", al="left")
                        socleColor = ColorSliderGrp()
                with ScrollLayout("Background",cr=True, horizontalScrollBarThickness = 8, verticalScrollBarThickness = 8) as backgroundLayout:
                    Separator(h=10, st="none")
                    with ColumnLayout("LightsCol", rs=10, adj=True) as backgroundColLayout:
                        with RowLayout(nc=2, rat=(1,'top',5), cat=(1,'right',5), adj=2):
                            skyDomeCBox = CheckBox(l="", v=True)
                            with FrameLayout("Skydome", cll=True):
                                with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                                    with RowLayout(nc=2, adj=2):
                                        Text("Color", w=60, al="left")
                                        skyDomeColor = ColorSliderGrp()
                                    with RowLayout(nc=2, adj=2):
                                        Text("Activate HDRI ", al="left")
                                        showHDRIBox = CheckBox(l="",v=False)
                                    with RowLayout(nc=2,adj=2):
                                        Text("HDRI Preset", w=60, al="left")
                                        with ColumnLayout(adj=1):
                                            hdriRadioPresets = RadioButtonGrp("HDRIPreset",vr=True, nrb=4, la4=["Sunset","Night","Studio","Custom"], da1=1, da2=2, da3=3, da4=4, sl=4)
                                    with RowLayout(nc=3, adj=2):
                                        Text("HDRI ", al="left")
                                        TextField("HDRIField", en=False)
                                        loadHDRIButton = IconTextButton(i=iconsPath +"/browseFolder.png")
                                    with RowLayout(nc=2,adj=2):
                                        Text("Exposure", w=60, al="left")
                                        hdriExposure = FloatSliderGrp(f=True, v=1.0,min=-10.0, max=5.0)
                                    with RowLayout(nc=2, rat=(1,'top',5), cat=(1,'right',5), adj=2):
                                        backgroundTurnaroundCBox = CheckBox(l="",v=False)
                                        with FrameLayout("Turnaround", cll=True):
                                            with RowLayout(nc=2):
                                                with ColumnLayout(rs=0, adj=True):
                                                    with RowLayout(nc=2, adj=2):
                                                        Text("Speed", w=60, al="left")
                                                        backgroundTurnSpeed = FloatSliderGrp(f=True, v=1.0,min=0.0, max=300.0)
                                                    with RowLayout(nc=2, adj=2):
                                                        Text("Duration (s) ", w=60, al="left")
                                                        backgroundTurnDuration = FloatSliderGrp(f=True, v=10.0,min=1.0, max=15.0)
                        with RowLayout(nc=2, rat=(1,'top',5), cat=(1,'right',5), adj=2):
                            backgroundCBox = CheckBox(l="", v=True)
                            with FrameLayout("Background model", cll=True):
                                with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                                    with RowLayout(nc=3, adj=2):
                                        Text("Model ", al="left")
                                        bgTextField = TextField("BGModelField", en=False)
                                        loadBGModelButton = IconTextButton(i=iconsPath +"/browseFolder.png")
                                    with RowLayout(nc=2, adj=2):
                                        Text("Color", w=60, al="left")
                                        bgModelColor = ColorSliderGrp()
                with ScrollLayout("Lights", cr=True, horizontalScrollBarThickness = 8, verticalScrollBarThickness = 8) as lightsLayout:
                    with ColumnLayout("LightsCol", rs=10, adj=True, cal="left") as lightsColLayout:
                        Separator(h=10, st="none")
                        with RowLayout(nc=2, rat=(1,'top',5), cat=(1,'right',5),adj=2):
                            rimCBox = CheckBox(l="", v=True)
                            with FrameLayout("Rim light", cll=True):
                                # with RowLayout(nc=2):
                                    # Text("Rim light", fn="boldLabelFont")
                                with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                                    with RowLayout(nc=2, adj=2):
                                        Text("Color", w=60, al="left")
                                        rimColor = ColorSliderGrp()
                                    with RowLayout(nc=2, adj=2):
                                        Text("Exposure", w=60, al="left")
                                        rimExposure = FloatSliderGrp(f=True, v=1.0, max=20.0)
                                    with RowLayout(nc=2, adj=2, cal=(2,"left"), cat=(2,"left",32)):
                                        rimAimCBox = CheckBox(l="", v=False)
                                        Text("Aim Center",fn="plainLabelFont")
                                    # with RowLayout(nc=3):
                                    #     Text("Type", w=60, al="left")
                                    #     rimLightType = OptionMenu()
                                    #     MenuItem(l="Point")
                                    #     MenuItem(l="Area")
                                    #     MenuItem(l="Spot")
                        
                        with RowLayout(nc=2, rat=(1,'top',5), cat=(1,'right',5), adj=2):
                            fillCBox = CheckBox(l="", v=True)
                            with FrameLayout("Fill light", cll=True):
                                with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                                    with RowLayout(nc=2, adj=2):
                                        Text("Color", w=60, al="left")
                                        fillColor = ColorSliderGrp()
                                    with RowLayout(nc=2, adj=2):
                                        Text("Exposure", w=60, al="left")
                                        fillExposure = FloatSliderGrp(f=True, v=1.0, max=20.0)
                                    with RowLayout(nc=2, adj=2, cal=(2,"left"), cat=(2,"left",32)):
                                        fillAimCBox = CheckBox(l="", v=False)
                                        Text("Aim Center",fn="plainLabelFont")
                                    # with RowLayout(nc=3):
                                    #     Text("Type", w=60, al="left")
                                    #     fillLightType = OptionMenu()
                                    #     MenuItem(l="Point")
                                    #     MenuItem(l="Area")
                                    #     MenuItem(l="Spot")
                        with RowLayout(nc=2, rat=(1,'top',5), cat=(1,'right',5), adj=2):
                            mainCBox = CheckBox(l="", v=True)
                            with FrameLayout("Main light", cll=True):
                                with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                                    with RowLayout(nc=2, adj=2):
                                        Text("Color", w=60, al="left")
                                        mainColor = ColorSliderGrp()
                                    with RowLayout(nc=2,adj=2):
                                        Text("Exposure", w=60, al="left")
                                        mainExposure = FloatSliderGrp(f=True, v=1.0, max=20.0)
                                    with RowLayout(nc=2, adj=2, cal=(2,"left"), cat=(2,"left",32)):
                                        mainAimCBox = CheckBox(l="", v=False)
                                        Text("Aim Center",fn="plainLabelFont")
                                    # with RowLayout(nc=3):
                                    #     Text("Type", w=60, al="left")
                                    #     mainLightType = OptionMenu()
                                    #     MenuItem(l="Point")
                                    #     MenuItem(l="Area")
                                    #     MenuItem(l="Spot")
                        with RowLayout(nc=2, rat=(1,'top',5), cat=(1,'right',5), adj=2):
                            dirCBox = CheckBox(l="", v=True)
                            with FrameLayout("Directional light", cll=True):
                                with ColumnLayout(rs=0, adj=True, cat=('both', 25)):
                                    with RowLayout(nc=2, adj=2):
                                        Text("Color", w=60, al="left")
                                        dirColor = ColorSliderGrp()
                                    with RowLayout(nc=2, adj=2):
                                        Text("Intensity", w=60, al="left")
                                        dirExposure = FloatSliderGrp(f=True, v=0.1, max=10.0)
                                    # with RowLayout(nc=2, adj=2):
                                    #     Text("Angle", w=60, al="left")
                                    #     dirAngle = FloatSliderGrp(f=True, v=0.1, max=180.0)       
                with ScrollLayout("Cameras", cr=True, horizontalScrollBarThickness = 8, verticalScrollBarThickness = 8) as cameraScrollLayout:
                    with ColumnLayout("CameraCol", rs=10, adj=True, cal="left") as cameraLayout:
                        Separator(h=10, st="none")
                        with RowLayout(nc=3,adj=2):
                            Text("New Camera name", al="left")
                            newCameraField = TextField("NewCameraField", tx="", aie=True)
                            addCameraButton = IconTextButton(i=iconsPath+"/add-video.png")
                        
                        cameraCollection = ViewCollection()
                        cameraList = lists.VerticalList(synchronous=True, itemTemplate=CameraWidget)
                        cameraCollection > bind() > cameraList.collection
        
                # with ColumnLayout("Render Settings", rs = 10, adj=1, cat=("both", 10)) as rsLayout:
                #     Text("Export",fn="boldLabelFont")
                #     #Mettre renderview
                #     with RowLayout(nc=3, adj=2):
                #         Text("Export path ", al="left")
                #         TextField("ExportPath", en=False)
                #         IconTextButton(i=iconsPath +"/browseFolder.png",c="SetExportPath('Set export path')")
                #     with ColumnLayout():
                #         pass
        Separator(h=10, st="none")
        with RowLayout(nc=3, adj=2):
            Separator(w=100, st="in")
            renderButton = Button("Render", c = Callback(RenderSettings.OpenRenderView, p = 1))
            Separator(w=100, st="in")
        Separator(h=15, st="none")
        with RowLayout(nc=3, adj=2):
            Separator(w=150, st="out")
            renderButton = Button("With Arnold", c = Callback(RenderSettings.OpenArnoldRenderView, p = 1))
            Separator(w=150, st="out")
        Separator(h=10, st="none")
w.show()

form.attachForm = [(tabs,'left',0), (tabs,'right',0)]

def AddCamera(name, position = Vector3(0,0,0), pivotPos = Vector3(0,0,0)):
    if(not cameraCollection.__contains__(name) and name != '' and name != None):
        newCam = Camera.Camera(name, position, pivotPos)
        camerasDict[newCam.name] = newCam
        cameraCollection.add(name)
        return newCam

def ToggleCameraActive(**kwargs):
    for camera in camerasDict:
        if(camera == kwargs["newCurrentCameName"]):
            #print("set open  ; " + camera)
            iconTextButton(camera + "_activeButton", e=True, i=iconsPath +"/open-eye.png")
            camerasDict[camera].SetCurrentCamera()
        else:
            #print("set close  ; " + camera)
            iconTextButton(camera + "_activeButton", e=True, i=iconsPath +"/close-eye.png")

def ToggleAddCameraButton(name):
    #print(name)
    addCameraButton.enable = not cameraCollection.__contains__(name)
    #print(not cameraCollection.__contains__(name))

#Trash

def LoadSupportModel(caption):
    fileName = cmds.fileDialog2(okc="Import", fm=1, ff="All Files (*.*)",cap=caption, ds=2, dir="\..")
    #print('filenale is : ' + fileName)
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
