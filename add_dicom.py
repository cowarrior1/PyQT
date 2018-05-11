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
import datetime
import pdb
import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(user='admin',
                                         password= 'admin',
                                         host='127.0.0.1',
                                         port='3306',
                                         database = 'multivender_test')
    cursor = connection.cursor()
    print("Connection Established!")

    # insertList(cursor)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Wrong Username/password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    else:
        print(err)
else:
    connection.close()

def insert_volume_dicominfo(dicom_path, time = datetime.datetime.now()):
    if not dicom_path:
        return

    if not Exist(dicom_path):
        return;
    # pdb.set_trace()
    if IsFile(dicom_path): # if path is file
        dicomFile = dicom_path
        series = 0
        slices = 1
    else: #if path is folder
        series = 1
        fs = dirfullpath(dicom_path) #displays all files
        slices = len(fs) #number of files
        for dicomFile in fs: #take first file
            if IsDicomFile(dicomFile): #see if its dicomefile
                break

    dicom_info = dicom.ReadFile(dicomFile)
    d = dicom_info

    if series:
        # pdb.set_trace()
        uid = d.SeriesInstanceUID
    else:
        uid = d.SOPInstanceUID
    # o is sql table
    cursor.volume_id = uid
    cursor.series = series
    cursor.num_slices = slices
    cursor.dicom_path = unicode(os.path.abspath(dicom_path), errors='ignore')
    #dicom_path = apply_substitution_rules(dicom_path)
    ##f:/xray//5001.IMA -> f:/xray/5001.IMA
    #dicom_path = re.sub(r'\\','/',dicom_path)
    #dicom_path = re.sub(r'[/]+','/',dicom_path)

    try:
        patient_name = re.sub(r'\\','/',d.PatientsName)
    except:
        patient_name = "NA"
    cursor.PatientsName =  unicode(patient_name)

    try:
        cursor.Modality = d.Modality
    except:
        cursor.Modality = "NA"
    try:
        cursor.SliceThickness = float(d.SliceThickness)
    except:
        cursor.SliceThickness = -1.0
    try:
        t = d.PatientsAge[-1]
        if t.upper()=='Y':
            cursor.PatientsAge = int(int(d.PatientsAge[:-1])+0.5)
        elif t.upper()=='M':
            cursor.PatientsAge = int((int(d.PatientsAge[:-1]))/12.0+0.5)
        elif t.upper()=='D':
            cursor.PatientsAge = int((int(d.PatientsAge[:-1]))/365.0+0.5)
        else:
            cursor.PatientsAge = int(float(d.PatientsAge)+0.5)
    except:
        cursor.PatientsAge = -1
    try:
        cursor.SliceThickness = float(d.SliceThickness)
    except:
        cursor.SliceThickness = -1.0

    try:
        cursor.MagneticFieldStrength = float(d.MagneticFieldStrength)
    except:
        cursor.MagneticFieldStrength = 1.5

    try:
        cursor.FlipAngle = float(d.FlipAngle)
    except:
        cursor.FlipAngle = -1e6

    try:
        cursor.RepetitionTime = float(d.RepetitionTime)
    except:
        cursor.RepetitionTime = -1e6

    try:
        cursor.EchoTime = float(d.EchoTime)
    except:
        cursor.EchoTime = -1e6

    try:
        cursor.ImagingFrequency = float(d.ImagingFrequency)
    except:
        cursor.ImagingFrequency = -1e6

    try:
        cursor.EchoTrainLength = float(d.EchoTrainLength)
    except:
        cursor.EchoTrainLength = -1e6

        cursor.BodyPartExamined = d.BodyPartExamined
    keys = ['BodyPartExamined','Manufacturer','ProtocolName','SeriesDescription']
    keys += ['PatientsSex','StudyDescription', 'RequestedProcedureDescription']
    keys += ['PixelSpacing','PatientPosition','ConvolutionKernel']
    keys += ['ImageType', 'WindowWidth', 'ImageComments','StudyInstanceUID']
    keys += ['PhotometricInterpretation', 'WindowCenter']
    keys += ['ImageOrientationPatient']
    keys += ['SequenceName', 'ImagedNucleus', 'TransmitCoilName']
    keys += ['InversionTime', 'ScanningSequence']
    #keys += ['CoilList']


    # for key in keys:
    #     try:
    #         val = str(d.__getattr__(key))
    #         #import pdb
    #         if key.lower().find('description') > 0:
    #             #pdb.set_trace()
    #             val = val.replace('"', '_')
    #             val = val.replace('#', '_')
    #             val = val.replace('^', '_')
    #     except:
    #         val = "NA"
    #     pdb.set_trace()

        #cursor.__setattr__(key, val)


    # set coil list, dicom tag '0051|100F'
    #import pdb
    #pdb.set_trace()
    try:
        val = d[0x0051, 0x100f].value
        cursor.__setattr__('CoilList', val)
    except:
        cursor.__setattr__('CoilList', "")

    try:
        val = d[0x0018, 0x0010].value
        cursor.__setattr__('ContrastBolusAgent', val)
    except:
        cursor.__setattr__('ContrastBolusAgent', "")

    try:
        val = d[0x0020, 0x0052].value
        cursor.__setattr__('FrameOfReferenceUID', val)
    except:
        cursor.__setattr__('FrameOfReferenceUID', "")
    cursor.last_accessed = time


    try:
        pdb.set_trace()
        plasma.die()
        plasma.start()
        img = dicomloader.load(dicom_path, "img")
        xyz_min, xyz_max = imagetools.imagecorner(img)
        cursor.x_min,cursor.y_min, cursor.z_min = xyz_min
        cursor.x_max, cursor.y_max, cursor.z_max = xyz_max

        cursor.space_x, cursor.space_y, cursor.space_z = plasmatools.get_image_voxel_sizes(img)
        cursor.width, cursor.height, cursor.depth = plasmatools.get_image_sizes(img)

        cursor.box_str = vputils.getbox(img)
        cursor.orientation = vpitk.getorientation(img)

    except:
        pass


    # -----------------------inserting sql statement----------------------------
    # insertion = ("INSERT INTO 'multivender_test'.volume_dicominfo (volume_id, PatientsName ) VALUES (cursor. "sAU");
    #              INSERT INTO 'multivender_test'.volume_dicominfo(volume_id, dicom_path,series,
    #              SeriesDescription, PatientsName, PatientsAge, PatientsSex, Modality, BodyPartExamined, Manufacturer,
    #              ProtocolName, StudyDescription, StudyInstanceUID, FrameOfReferenceUID, RequestedProcedureDescription,
    #              PixelSpacing, ImageOrientationPatient, PatientPosition, SliceThickness, ConvolutionKernel,
    #              PhotometricInterpretation, WindowCenter, WindowWidth, ImageType, ImageComments, num_slices, width,
    #              height, depth, x_min, y_min, z_min, x_max, y_max, z_max, origin_x, origin_y, origin_z,
    #              space_x, space_y, space_z, orientation, box_str, last_accessed, comment, MagneticFieldStrength,
    #              FlipAngle, RepetitionTime, EchoTime, ImagingFrequency, EchoTrainLength, SequenceName, ImagedNucleus,
    #              TransmitCoilName, InversionTime, ScanningSequence, CoilList) VALUES(cursor.volume_id, cursor.dicom_path, cursor.series,
    #              cursor.SeriesDescription, cursor.PatientsName, cursor.PatientAge, cursor.PatientsSex, cursor.Modality, cursor.BodyPartExamined,
    #               )

    # cursor.execute(insertion)

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

#doesnt read from sudirectories
def dirfullpath(folder, fileExt = '', isSortingNeeded=False):

    if isSortingNeeded:
        fileList = sorted(os.listdir(folder))
    else:
        fileList = os.listdir(folder)
    if fileExt and fileExt != "*" and fileExt != "*.*":
        fileList = filterstring(fileList, fileExt)
    fileList = [folder + "\\" + item for item in fileList]
    # pdb.set_trace()
    print(fileList)
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
