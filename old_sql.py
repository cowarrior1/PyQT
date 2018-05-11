import dicom
import re
import os
import datetime
import imagetools
import plasmatools
import vputils
import vpitk
import dicomloader
import plasma

def insert_volume_dicominfo(dicom_path, time = datetime.now()):
    if not dicom_path:
        return

    if not Exist(dicom_path):
        return;

    if IsFile(dicom_path):
        dicomFile = dicom_path
    else:
        fs = dirfullpath(dicom_path)
        for dicomFile in fs:
            if IsDicomFile(dicomFile):
                break

    dicom_info = dicom.ReadFile(dicomFile)
    d = dicom_info

    if series:
        uid = d.SeriesInstanceUID
    else:
        uid = d.SOPInstanceUID
    # o is sql table
    volume_id = uid
    series = series
    num_slices = slices
    dicom_path = unicode(os.path.abspath(dicom_path), errors='ignore')
    #dicom_path = apply_substitution_rules(dicom_path)
    ##f:/xray//5001.IMA -> f:/xray/5001.IMA
    #dicom_path = re.sub(r'\\','/',dicom_path)
    #dicom_path = re.sub(r'[/]+','/',dicom_path)

    try:
        patient_name = re.sub(r'\\','/',d.PatientsName)
    except:
        patient_name = "NA"
    PatientsName =  unicode(patient_name)

    try:
        Modality = d.Modality
    except:
        Modality = "NA"
    try:
        SliceThickness = float(d.SliceThickness)
    except:
        SliceThickness = -1.0
    try:
        t = d.PatientsAge[-1]
        if t.upper()=='Y':
            PatientsAge = int(int(d.PatientsAge[:-1])+0.5)
        elif t.upper()=='M':
            PatientsAge = int((int(d.PatientsAge[:-1]))/12.0+0.5)
        elif t.upper()=='D':
            PatientsAge = int((int(d.PatientsAge[:-1]))/365.0+0.5)
        else:
            PatientsAge = int(float(d.PatientsAge)+0.5)
    except:
        PatientsAge = -1
    try:
        SliceThickness = float(d.SliceThickness)
    except:
        SliceThickness = -1.0

    try:
        MagneticFieldStrength = float(d.MagneticFieldStrength)
    except:
        MagneticFieldStrength = 1.5

    try:
        FlipAngle = float(d.FlipAngle)
    except:
        FlipAngle = -1e6

    try:
        RepetitionTime = float(d.RepetitionTime)
    except:
        RepetitionTime = -1e6

    try:
        EchoTime = float(d.EchoTime)
    except:
        EchoTime = -1e6

    try:
        ImagingFrequency = float(d.ImagingFrequency)
    except:
        ImagingFrequency = -1e6

    try:
        EchoTrainLength = float(d.EchoTrainLength)
    except:
        EchoTrainLength = -1e6


    keys = ['BodyPartExamined','Manufacturer','ProtocolName','SeriesDescription']
    keys += ['PatientsSex','StudyDescription', 'RequestedProcedureDescription']
    keys += ['PixelSpacing','PatientPosition','ConvolutionKernel']
    keys += ['ImageType', 'WindowWidth', 'ImageComments','StudyInstanceUID']
    keys += ['PhotometricInterpretation', 'WindowCenter']
    keys += ['ImageOrientationPatient']
    keys += ['SequenceName', 'ImagedNucleus', 'TransmitCoilName']
    keys += ['InversionTime', 'ScanningSequence']
    #keys += ['CoilList']


    for key in keys:
        try:
            val = str(d.__getattr__(key))
            if key.lower().find('description') > 0:
                #import pdb
                #pdb.set_trace()
                val = val.replace('"', '_')
                val = val.replace('#', '_')
                val = val.replace('^', '_')
        except:
            val = "NA"
        __setattr__(key, val)

    # set coil list, dicom tag '0051|100F'
    #import pdb
    #pdb.set_trace()
    try:
        val = d[0x0051, 0x100f].value
        __setattr__('CoilList', val)
    except:
        __setattr__('CoilList', "")

    try:
        val = d[0x0018, 0x0010].value
        __setattr__('ContrastBolusAgent', val)
    except:
        __setattr__('ContrastBolusAgent', "")

    try:
        val = d[0x0020, 0x0052].value
        __setattr__('FrameOfReferenceUID', val)
    except:
        __setattr__('FrameOfReferenceUID', "")

    last_accessed = time


     try:
        plasma.die()
        plasma.start()
        img = dicomloader.load(dicom_path, "img")
        xyz_min, xyz_max = imagetools.imagecorner(img)
        x_min, y_min, z_min = xyz_min
        x_max, y_max, z_max = xyz_max

        space_x, space_y, space_z = plasmatools.get_image_voxel_sizes(img)
        width, height, depth = plasmatools.get_image_sizes(img)

        box_str = vputils.getbox(img)
        orientation = vpitk.getorientation(img)
    except:
        pass

def Exist(file):
    if IsFile(file):
        return os.path.exists(file)
    else:
        try:
            return len(os.listdir(file))>0
        except:
            return False
def IsFile(file):
    return os.path.isfile(file);

def dirfullpath(folder, fileExt = '', isSortingNeeded=False):
    if isSortingNeeded:
        fileList = sorted(os.listdir(folder))
    else:
        fileList = os.listdir(folder)
    if fileExt and fileExt != "*" and fileExt != "*.*":
        fileList = filterstring(fileList, fileExt)
    fileList = [folder + "\\" + item for item in fileList]
    return fileList

def filterstring(fileList, findstring = ''):
    if not findstring:
        return fileList

    returnFiles = [];
    for item in fileList:
        if item.lower().find(findstring.lower()) != -1:
            returnFiles.append(item);
    return returnFiles


def IsDicomFile(file):
    #pdb.set_trace()

    #if type(file) is not StringType and type(file) is not path:
    #    return False
    #pdb.set_trace()
    if not Exist(file):
        return False;
    if not IsFile(file):
        if len(dir(file)) > 1 or len(dir(file)) < 1:
            return False;
        else:
            file = dirfullpath(file)[0]
    #pdb.set_trace()
    notDicom = ['.log', '.jpg', '.jpeg', '.pgm', '.exe', '.txt', \
    '.xml', '.xls', '.doc', '.ppt', '.zip', '.rar', '.txt~', '.py', '.m', '.pyc', '.para',\
    '.trainlog', '.fplog']

    [a, b, c, d1] = SplitFile(file.lower())
    if d1 in notDicom:
        return False

    try:
        dicomFile = dicom.ReadFile(str(file))
        modality = dicomFile.get('Modality')
        if modality:
            return True
        else:
            return False
    except:
        return False

def SplitFile(file):
    [path, filename] = os.path.split(file)
    [nameonly, ext] = os.path.splitext(filename)
    return path, filename, nameonly, ext
