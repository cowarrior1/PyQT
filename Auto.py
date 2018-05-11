#! python2
#-------------------BruteForce-----------------
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
    cursor = connection.cursor(buffered=True)

    # insertList(cursor)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Wrong Username/password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    else:
        print(err)

#-----------------------------------------------------------------------
# --------Works only for hardcoded series(only folder functionality)----
#-----------------------------------------------------------------------
def main():
    time = datetime.datetime.now
    slices = 0
    #loops throught .dcm file names with full path (doesn't include subfolders)
    # and extracts the information
    path = "D:\Data\Auto\Examplepaths"
    fileExtension = ".dcm"
    # x_min, y_min, z_min = 0
    # x_max, y_max, z_max = 0
    # space_x, space_y, space_z = 0
    # width, height, depth = 0
    box_str = "NA"
    orientation = "NA"
    for file in os.listdir(path):
        if file.endswith(fileExtension):
            f = os.path.join(path, file)
            pf = dicom.ReadFile(f)
            series = 1
            slices += 1
            if series:
                uID = pf.SeriesInstanceUID
            else:
                uID = pf.SOPInstanceUID
            filepath = path
            lastAccessed = time
            seriesDescription= pf.SeriesDescription
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
            studyDescription = pf.StudyDescription
            studyInstanceUID = pf.StudyInstanceUID
            frameOfReferenceUID = pf.FrameOfReferenceUID
            requestedProcedureDescription = pf.RequestedProcedureDescription
            pixelSpacing = pf.PixelSpacing
            patientPosition = pf.PatientPosition
            convolutionKernel = pf.ConvolutionKernel
            photometricInterpretation = pf.PhotometricInterpretation
            windowCenter = pf.WindowCenter
            windowWidth = pf.WindowWidth
            imageType = pf.ImageType
            imageComments = pf.ImageComments
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

#-----------------------------------------------------------------------
#--------------------xmin,max,space-----------------------------------
#---------------------------------------------------------------------
            try:
                x_min = pf.x_min
            except:
                x_min = 0
            try:
                y_min = pf.y_min
            except:
                y_min =0
            try:
                z_min = pf.z_min
            except:
                z_min =0
            try:
                x_max = pf.x_max
            except:
                x_max = 0
            try:
                y_max = pf.y_max
            except:
                y_max =0
            try:
                z_max = pf.z_max
            except:
                z_max = 0
            try:
                space_x = pf.space_x
            except:
                space_x = 0
            try:
                space_y = pf.space_y
            except:
                space_y =0
            try:
                space_z = pf.space_z
            except:
                space_z = 0
            try:
                width = pf.width
            except:
                width = 0
            try:
                height = pf.height
            except:
                height =0
            try:
                depth = pf.depth
            except:
                depth = 0
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


            # try:
            #     val = d[0x0051, 0x100f].value
            #     pf.__setattr__('CoilList', val)
            # except:
            #     pf.__setattr__('CoilList', "")

            # try:
            #     val = d[0x0018, 0x0010].value
            #     pf.__setattr__('ContrastBolusAgent', val)
            # except:
            #     pf.__setattr__('ContrastBolusAgent', "")

            # try:
            #     val = d[0x0020, 0x0052].value
            #     pf.__setattr__('FrameOfReferenceUID', val)
            # except:
            #     pf.__setattr__('FrameOfReferenceUID', "")

            # try:
            #     plasma.die()
            #     plasma.start()
            #     img = dicomloader.load(path, "img")
            #     # xyz_min, xyz_max = vputils.getbox(img)
            #     pdb.set_trace()
            #
            #     xyz_min, xyz_max = imagetools.imagecorner(img) #error for correct usage
            #     x_min, y_min, z_min = xyz_min
            #     x_max, y_max, z_max = xyz_max
            #     space_x, space_y, space_z = plasmatools.get_image_voxel_sizes(img)
            #     width, height, depth = plasmatools.get_image_sizes(img)
            #     box_str = vputils.getbox(img)
            #     orientation = vpitk.getorientation(img)
            # except:
            #     x_min, y_min, z_min = 0
            #     x_max, y_max, z_max = 0
            #     space_x, space_y, space_z = 0
            #     width, height, depth = 0
            #     box_str = "NA"
            #     orientation = "NA"
            print(uID, filepath, series, seriesDescription,
            patientName, patientsAge, modality, bodyPartExamined, manufacturer, protocolName,studyDescription, studyInstanceUID,
            frameOfReferenceUID, requestedProcedureDescription, pixelSpacing, imageOrientationPatient, patientPosition,
            sliceThickness, convolutionKernel, photometricInterpretation, windowCenter, windowWidth, imageType, imageComments, str(slices),
            width, height, depth, x_min, y_min, z_min, x_max, y_max, z_max, origin_x, origin_y, origin_z, space_x, space_y, space_z,
            orientation, box_str, lastAccessed, comment, magneticFieldStrength, flipAngle, repetitionTime, echoTime, imagingFrequency, echoTrainLength,
            sequenceName, imagedNucleus, transmitCoilName, inversionTime, scanningSequence, coilList)


            query= """INSERT INTO volume_dicominfo(volume_id, dicom_path, series,
            SeriesDescription, PatientsName, PatientsAge, PatientsSex, Modality, BodyPartExamined, Manufacturer,
            ProtocolName, StudyDescription, StudyInstanceUID, FrameOfReferenceUID, RequestedProcedureDescription,
            PixelSpacing, ImageOrientationPatient, PatientPosition, SliceThickness, ConvolutionKernel,
            PhotometricInterpretation, WindowCenter, WindowWidth, ImageType, ImageComments, num_slices, width,
            height, depth, x_min, y_min, z_min, x_max, y_max, z_max, origin_x, origin_y, origin_z,
            space_x, space_y, space_z, orientation, box_str, last_accessed, comment, MagneticFieldStrength,
            FlipAngle, RepetitionTime, EchoTime, ImagingFrequency, EchoTrainLength, SequenceName, ImagedNucleus,
            TransmitCoilName, InversionTime, ScanningSequence, CoilList, DicomFiles) VALUES (uID, filepath, series, seriesDescription,
            patientName, patientsAge, modality, bodyPartExamined, manufacturer, protocolName, studyDescription, studyInstanceUID,
            frameOfReferenceUID, requestedProcedureDescription, pixelSpacing, imageOrientationPatient, patientPosition,
            sliceThickness, convolutionKernel, photometricInterpretation, windowCenter, windowWidth, imageType, imageComments, str(slices),
            width, height, depth, x_min, y_min, z_min, x_max, y_max, z_max, origin_x, origin_y, origin_z, space_x, space_y, space_z,
            orientation, box_str, lastAccessed, comment, magneticFieldStrength, flipAngle, repetitionTime, echoTime, imagingFrequency, echoTrainLength,
            sequenceName, imagedNucleus, transmitCoilName, inversionTime, scanningSequence, coilList, pf)"""
            cursor.execute(query)
            cursor.commit()


    print ("Total files = " + str(slices))

#-----------------------inserting sql statement(bad practice)----------------------------


if __name__ == "__main__":
    main()
