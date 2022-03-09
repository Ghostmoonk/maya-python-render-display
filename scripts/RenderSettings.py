from pymel.core import *
import mtoa.core as core

# core.createOptions()

def OpenRenderView(**kwargs):
    mel.eval('RenderViewWindow')

def OpenArnoldRenderView(**kwargs):
    arnoldRenderView()
