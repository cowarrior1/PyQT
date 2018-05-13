import time
import sys
# import PythonPipeClient
from FlaskWebProject1.cad.Plasma.plugins.python27 import PythonPipeClient
import vputils
import iv
import vpiv
import pdb
#import tools
import plasma
import vpsynth
from win32api import GetSystemMetrics
import imagetools
import numpy
import dicomloader


gUse3DViewer = 1
def getpipename():
    pipename = ''
    name = PythonPipeClient.getforcedpipename(pipename,'.')
    return name

def show(f = r"I:\batch_data\QC_Cardiac\1.2.124.113532.10.131.14.22.20060215.144952.159006"):
    '''
import plasma
plasma.die()

#global pipeParent
#PythonPipeClient.setforcedpipe(pipeParent,'.')
#vpiv.switchtoview("test",2,1)
#vpiv.center()

    '''
    #pdb.set_trace()
    plasma.die()
    plasma.start()
    screenW = GetSystemMetrics(0)
    screenH = GetSystemMetrics(1)

    w = screenH/4 - 5
    startW = screenW / 5
    #startW = 100
    viewW = int((screenW - startW) / 2.)
    viewH = int(screenH / 2.)

    layout = ['DemoTL', 'DemoTR', 'DemoBL', 'DemoBR']
    landmarkSet= [[], [], [], []]
    modalitySet = ['NA', 'NA', 'NA', 'NA']
    reval = [];
    time.sleep(0.5)
    PythonPipeClient.setforcedpipe(getpipename(),'.')
    vputils.newbuff('dump', 'USHORT', 0, 10, 10, 10)
    if gUse3DViewer:
        iv.viewwithsize('3DMRSHIFT',getpipename(), startW, 0, viewW, viewH)
    else:
        iv.viewwithsize('RelativeLayoutWithBar', getpipename(), startW, 0, viewW*2, viewH*1.8)

    img = dicomloader.load(f, "img")
    vputils.delete('dump')

    modality = vpsynth.getdicomfield(img, 'Modality', 0)
    if modality.strip().lower() == 'ct':
        vpiv.setscalarwindow(fid=img, wmin=800, wmax=1300, refresh_flag=1)
    else:
        ivtools.autoWindow(img)

    size = imagetools.sizes(img)
    nn = numpy.average([ numpy.linalg.norm(i) for i in size])
    vpiv.setfov(nn)
    iv.gotovoxel(size[0]/2., size[1] /2., size[2]/2.)
    vpiv.refresh()
