#! python2
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
import time
import pdb
import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(user='admin',
                                         password= 'admin',
                                         host='127.0.0.1',
                                         port='3306',
                                         database = 'multivender_test')
    cursor = connection.cursor(buffered=True)

    # insertList(cursor)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Wrong Username/password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    else:
        print(err)

def main():
    var = raw_input("Enter .txt path: ")
    with open(var) as ins:
        fileExtension = ".dcm"
        lines = ins.read().splitlines() #gets rid of \n and stores in array lines[]
        for i in range(len(lines)):
                path = lines[i]
                global f
                if not path.endswith(fileExtension): #Folder path
                    slices = 0
                    process(path, slices, fileExtension)
                if path.endswith(fileExtension):
                    slices = 1
                    f = path
                    read(f, slices, path)

#folder path process
def process(path, slices, fileExtension):
    for file in os.listdir(path):
        if file.endswith(fileExtension):
            f = os.path.join(path, file)#file
            slices +=1 #needs to loop
    read(f, slices, path)

#common process both decision statements uses
def read(f, slices, path):
    pf = dicom.ReadFile(f)
    series = 1
    if series:
        uID = pf.SeriesInstanceUID
        uID = str(uID) #cast to str as the type is uid initially
    else:
        uID = pf.SOPInstanceUID
        uID = str(uID)
    filepath = path
    ts = time.time()
    lastAccessed = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') #need to parset to str/date
    try:
        seriesDescription= pf.SeriesDescription
    except:
        seriesDescription = "NA"
    try:
        t = pf.PatientsAge[-1]
        if t.upper()=='Y':
            patientsAge = int(int(pf.PatientsAge[:-1])+0.5)
        elif t.upper()=='M':
            patientsAge = int((int(pf.PatientsAge[:-1]))/12.0+0.5)
        elif t.upper()=='D':
            patientsAge = int((int(pf.PatientsAge[:-1]))/365.0+0.5)
        else:
            patientsAge = int(float(pf.PatientsAge)+0.5)
    except:
        patientsAge = -1
    patientSex = pf.PatientsSex
    try:
        patientName = re.sub(r'\\','/',pf.PatientsName)
    except:
        patientName = "NA"
    patientName = unicode(patientName)
    try:
        modality = pf.Modality
    except:
        modality = "NA"
    bodyPartExamined = pf.BodyPartExamined
    manufacturer = pf.Manufacturer
    protocolName = pf.ProtocolName
    imageOrientationPatient = pf.ImageOrientationPatient
    imageOrientationPatient = str(imageOrientationPatient)
    studyDescription = pf.StudyDescription
    studyInstanceUID = pf.StudyInstanceUID
    studyInstanceUID = str(studyInstanceUID)
    frameOfReferenceUID = pf.FrameOfReferenceUID
    frameOfReferenceUID = str(frameOfReferenceUID)
    requestedProcedureDescription = pf.RequestedProcedureDescription
    pixelSpacing = pf.PixelSpacing
    pixelSpacing = str(pixelSpacing)
    patientPosition = pf.PatientPosition
    convolutionKernel = pf.ConvolutionKernel
    photometricInterpretation = pf.PhotometricInterpretation
    windowCenter = pf.WindowCenter
    windowCenter = str(windowCenter)
    windowWidth = pf.WindowWidth
    windowWidth = str(windowWidth)
    imageType = pf.ImageType
    imageType = str(imageType)
    try:
        imageComments = pf.ImageComments
        imageComments = str(imageComments)
    except:
        imageComments = "NA"
    try:
        sliceThickness = float(pf.SliceThickness)
    except:
        sliceThickness = -1.0

    try:
        magneticFieldStrength = float(pf.MagneticFieldStrength)
    except:
        magneticFieldStrength = 1.5

    try:
        flipAngle = float(pf.FlipAngle)
    except:
        flipAngle = -1e6

    try:
        repetitionTime = float(pf.RepetitionTime)
    except:
        repetitionTime = -1e6

    try:
        echoTime = float(pf.EchoTime)
    except:
        echoTime = -1e6

    try:
        imagingFrequency = float(pf.ImagingFrequency)
    except:
        imagingFrequency = -1e6

    try:
        echoTrainLength = float(pf.EchoTrainLength)
    except:
        echoTrainLength = -1e6
    try:
        sequenceName = pf.SequenceName
    except:
        sequenceName = "NA"
    try:
        imagedNucleus = pf.ImagedNucleus
    except:
        imagedNucleus = "NA"
    try:
        transmitCoilName = pf.TransmitCoilName
    except:
        transmitCoilName = "NA"
    try:
        inversionTime = pf.InversionTime
    except:
        inversionTime = "NA"
    try:
        scanningSequence = pf.ScanningSequence
    except:
        scanningSequence = "NA"
    try:
        comment = pf.comment
    except:
        comment = "NA"
    try:
        box_str = pf.box_str
    except:
        box_str = "NA"
    try:
        orientation = pf.orientation
    except:
        orientation = "NA"
    try:
        coilList = pf.coilList
    except:
        coilList = ""
    try:
        origin_x = pf.origin_x
    except:
        origin_x = 0
    try:
        origin_y = pf.origin_y
    except:
        origin_y =0
    try:
        origin_z = pf.origin_z
    except:
        origin_z = 0

#-----------------------------------------------------------------------
#--------------------xmin,max,space-----------------------------------
#---------------------------------------------------------------------
    try:
        plasma.die()
        plasma.start()
        img = dicomloader.load(path, "img")
        xyz_min, xyz_max = imagetools.imagecorner(img)
        x_min, y_min, z_min = xyz_min
        x_max, y_max, z_max = xyz_max
        space_x, space_y, space_z = plasmatools.get_image_voxel_sizes(img)
        width, height, depth = plasmatools.get_image_sizes(img)
        box_str = vputils.getbox(img)
        orientation = vpitk.getorientation(img)
        xyz_min = str(xyz_min)
        xyz_max = str(xyz_max)
        x_min = str(x_min)
        y_min = str(y_min)
        z_min = str(z_min)
        x_max = str(x_max)
        y_max = str(y_max)
        z_max = str(z_max)
        space_x = str(space_x)
        space_y = str(space_y)
        space_z = str(space_z)
        width = str(width)
        height = str(height)
        depth = str(depth)
        box_str = str(box_str)
        orientation = str(orientation)
    except:
        pass
    print(uID, filepath, series, seriesDescription,
    patientName, patientsAge, modality, bodyPartExamined, manufacturer, protocolName,studyDescription, studyInstanceUID,
    frameOfReferenceUID, requestedProcedureDescription, pixelSpacing, imageOrientationPatient, patientPosition,
    sliceThickness, convolutionKernel, photometricInterpretation, windowCenter, windowWidth, imageType, imageComments, str(slices),
    width, height, depth, x_min, y_min, z_min, x_max, y_max, z_max, origin_x, origin_y, origin_z, space_x, space_y, space_z,
    orientation, box_str, lastAccessed, comment, magneticFieldStrength, flipAngle, repetitionTime, echoTime, imagingFrequency, echoTrainLength,
    sequenceName, imagedNucleus, transmitCoilName, inversionTime, scanningSequence, coilList)
    #quering with placeholder parameters
    query= """INSERT INTO volume_dicominfo(volume_id, dicom_path, series,
    SeriesDescription, PatientsName, PatientsAge, PatientsSex, Modality, BodyPartExamined, Manufacturer,
    ProtocolName, StudyDescription, StudyInstanceUID, FrameOfReferenceUID, RequestedProcedureDescription,
    PixelSpacing, ImageOrientationPatient, PatientPosition, SliceThickness, ConvolutionKernel,
    PhotometricInterpretation, WindowCenter, WindowWidth, ImageType, ImageComments, num_slices, width,
    height, depth, x_min, y_min, z_min, x_max, y_max, z_max, origin_x, origin_y, origin_z,
    space_x, space_y, space_z, orientation, box_str, last_accessed, comment, MagneticFieldStrength,
    FlipAngle, RepetitionTime, EchoTime, ImagingFrequency, EchoTrainLength, SequenceName, ImagedNucleus,
    TransmitCoilName, InversionTime, ScanningSequence, CoilList, DicomFiles) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s)
    ON DUPLICATE KEY UPDATE `volume_id` = `volume_id` """
    cursor.execute(query,(uID, filepath, series, seriesDescription,patientName,patientsAge, patientSex, modality, bodyPartExamined, manufacturer, protocolName, studyDescription, studyInstanceUID,
    frameOfReferenceUID, requestedProcedureDescription, pixelSpacing, imageOrientationPatient, patientPosition,
    sliceThickness, convolutionKernel, photometricInterpretation, windowCenter, windowWidth, imageType, imageComments, str(slices),
    width, height, depth, x_min, y_min, z_min, x_max, y_max, z_max, origin_x, origin_y, origin_z, space_x, space_y, space_z,
    orientation, box_str, lastAccessed, comment, magneticFieldStrength, flipAngle, repetitionTime, echoTime, imagingFrequency, echoTrainLength,
    sequenceName, imagedNucleus, transmitCoilName, inversionTime, scanningSequence, coilList, f))
    connection.commit()

if __name__ == "__main__":
    main()
