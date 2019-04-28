from gui import *
import os
import vtk
from vtk.util.misc import vtkGetDataRoot
import sys
from PyQt5 import QtCore, QtGui
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5 import QtWidgets, QtGui, QtCore


class AppWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.browse_btn.clicked.connect(self.browse)
        self.ui.iso.sliderReleased.connect(self.iso_valu)
        self.ui.surface_btn.clicked.connect(self.surface_rend)
        self.ui.ray_casting_btn.clicked.connect(self.ray_rend)

        self.vtkwid1 = QVTKRenderWindowInteractor(self.ui.surface_viewer)
        self.ren1 = vtk.vtkRenderer()
        self.vtkwid1.GetRenderWindow().AddRenderer(self.ren1)
        self.iren1 = self.vtkwid1.GetRenderWindow().GetInteractor()
        self.surfaceExtractor = vtk.vtkContourFilter()


        self.vtkwid2 = QVTKRenderWindowInteractor(self.ui.ray_casting_viewer)
        self.ren2 = vtk.vtkRenderer()
        self.vtkwid2.GetRenderWindow().AddRenderer(self.ren2)
        self.iren2 = self.vtkwid2.GetRenderWindow().GetInteractor()

        self.pathDir = ""
        self.reader =""

    def iso_valu(self):
        self.ui.range.setText(str(self.ui.iso.value()))
        self.surfaceExtractor.SetValue(0, self.ui.iso.value())
        self.vtkwid1.update()

    def surface_rend (self):
        self.surfaceExtractor.SetInputConnection(self.reader.GetOutputPort())
        self.surfaceExtractor.SetValue(0, 500)
        surfaceNormals = vtk.vtkPolyDataNormals()
        surfaceNormals.SetInputConnection(self.surfaceExtractor.GetOutputPort())
        surfaceNormals.SetFeatureAngle(60.0)
        surfaceMapper = vtk.vtkPolyDataMapper()
        surfaceMapper.SetInputConnection(surfaceNormals.GetOutputPort())
        surfaceMapper.ScalarVisibilityOff()
        self.surface = vtk.vtkActor()
        self.surface.SetMapper(surfaceMapper)

        aCamera = vtk.vtkCamera()
        aCamera.SetViewUp(0, 0, -1)
        aCamera.SetPosition(0, 1, 0)

        aCamera.SetFocalPoint(0, 0, 0)
        aCamera.ComputeViewPlaneNormal()

        self.ren1.AddActor(self.surface)
        self.ren1.SetActiveCamera(aCamera)
        self.ren1.ResetCamera()

        self.ren1.SetBackground(0, 0, 0)
        # self.renwin.SetSize(400, 400)

        self.ren1.ResetCameraClippingRange()

        self.iren1.Initialize()
        self.iren1.Start()

    def ray_rend(self):
        self.shifter = vtk.vtkImageShiftScale()
        offset = self.reader.GetRescaleOffset()
        slope = self.reader.GetRescaleSlope()

        self.shifter.SetScale(slope)
        self.shifter.SetShift(-1 * offset)
        self.shifter.SetInputConnection(self.reader.GetOutputPort())

        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetInputConnection(self.shifter.GetOutputPort())
        volumeMapper.SetBlendModeToComposite()

        volumeColor = vtk.vtkColorTransferFunction()
        volumeColor.AddRGBPoint(0, 0.0, 0.0, 0.0)
        volumeColor.AddRGBPoint(500, 1.0, 0.5, 0.3)
        volumeColor.AddRGBPoint(1000, 1.0, 0.5, 0.3)
        volumeColor.AddRGBPoint(1150, 1.0, 1.0, 0.9)

        volumeScalarOpacity = vtk.vtkPiecewiseFunction()
        volumeScalarOpacity.AddPoint(0, 0.00)
        volumeScalarOpacity.AddPoint(500, 0.15)
        volumeScalarOpacity.AddPoint(1000, 0.15)
        volumeScalarOpacity.AddPoint(1150, 0.85)

        volumeGradientOpacity = vtk.vtkPiecewiseFunction()
        volumeGradientOpacity.AddPoint(0, 0.0)
        volumeGradientOpacity.AddPoint(90, 0.5)
        volumeGradientOpacity.AddPoint(100, 1.0)

        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetColor(volumeColor)
        volumeProperty.SetScalarOpacity(volumeScalarOpacity)
        volumeProperty.SetGradientOpacity(volumeGradientOpacity)
        volumeProperty.SetInterpolationTypeToLinear()
        volumeProperty.ShadeOn()
        volumeProperty.SetAmbient(0.4)
        volumeProperty.SetDiffuse(0.6)
        volumeProperty.SetSpecular(0.2)

        volume = vtk.vtkVolume()
        volume.SetMapper(volumeMapper)
        volume.SetProperty(volumeProperty)

        self.ren2.AddViewProp(volume)

        camera = self.ren2.GetActiveCamera()
        c = volume.GetCenter()
        camera.SetFocalPoint(c[0], c[1], c[2])
        camera.SetPosition(c[0] + 800, c[1], c[2])
        camera.SetViewUp(0, 0, -1)

        # Interact with the data.
        self.iren2.Initialize()
        self.iren2.Start()

    def browse(self):
            self.pathDir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')  # Ask for folder
            self.reader = vtk.vtkDICOMImageReader()
            self.reader.SetDirectoryName(self.pathDir)
            self.reader.Update()
            self.vtkwid1.update()
            self.vtkwid2.update()
            self.ui.ray_casting_btn.setEnabled(True)
            self.ui.surface_btn.setEnabled(True)


def main():

    app = QtWidgets.QApplication(sys.argv)
    application = AppWindow()
    application.setWindowTitle("VTK Viewer")
    application.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
