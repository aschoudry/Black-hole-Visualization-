import numpy as np
import sys
#Specify where visit is installed in your system
sys.path.append("/home/aschoudhary/local/2.12.2/linux-x86_64/lib/site-packages/")

import visit
from visit import*
Launch()

##########################################################################################################
#################### Specify the location of data ########################################################

Poynting_fluxZ_data = "localhost:/datarepo/forashok/separation_10p4__nonspinning__vertBfield/Poynz.file_* database"

###########################################################################################################
########################## Open data files ################################################################

OpenDatabase(Poynting_fluxZ_data , 0, "CarpetHDF5")

##########################################################################################################
############ Defining the reqired funstions ##############################################################
def Volume_plot():
	AddPlot("Volume", "SMALLBPOYNET--Poynz", 1, 0)
	AddOperator("Box", 0)
	BoxAtts = BoxAttributes()
	BoxAtts.amount = BoxAtts.Some  # Some, All
	BoxAtts.minx = -10
	BoxAtts.maxx = 10
	BoxAtts.miny = -10
	BoxAtts.maxy = 10
	BoxAtts.minz = 0
	BoxAtts.maxz = 100
	BoxAtts.inverse = 0
	SetOperatorOptions(BoxAtts, 0)
	DrawPlots()		


def side_view():
	View3DAtts = View3DAttributes()
	View3DAtts.viewNormal = (-0.231781, -0.809433, 0.539533)
	View3DAtts.focus = (21.3333, 21.3333, 21.3333)
	View3DAtts.viewUp = (-0.444246, 0.581499, 0.681546)
	View3DAtts.viewAngle = 30
	View3DAtts.parallelScale = 3510.29
	View3DAtts.nearPlane = -7020.58
	View3DAtts.farPlane = 7020.58
	View3DAtts.imagePan = (0, 0)
	View3DAtts.imageZoom = 45.2593
	View3DAtts.perspective = 1
	View3DAtts.eyeAngle = 2
	View3DAtts.centerOfRotationSet = 0
	View3DAtts.centerOfRotation = (21.3333, 21.3333, 21.3333)
	View3DAtts.axis3DScaleFlag = 0
	View3DAtts.axis3DScales = (1, 1, 1)
	View3DAtts.shear = (0, 0, 1)
	View3DAtts.windowValid = 1
	SetView3D(View3DAtts)

def Annotations():
	AnnotationAtts = AnnotationAttributes()
	AnnotationAtts.axes3D.visible = 1
	AnnotationAtts.axes3D.autoSetTicks = 1
	AnnotationAtts.axes3D.autoSetScaling = 1
	AnnotationAtts.axes3D.lineWidth = 0
	AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
	AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
	AnnotationAtts.axes3D.triadFlag = 1
	AnnotationAtts.axes3D.bboxFlag = 1
	AnnotationAtts.axes3D.xAxis.title.visible = 1
	AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axes3D.xAxis.title.font.scale = 1
	AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
	AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes3D.xAxis.title.font.bold = 0
	AnnotationAtts.axes3D.xAxis.title.font.italic = 0
	AnnotationAtts.axes3D.xAxis.title.userTitle = 0
	AnnotationAtts.axes3D.xAxis.title.userUnits = 0
	AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
	AnnotationAtts.axes3D.xAxis.title.units = ""
	AnnotationAtts.axes3D.xAxis.label.visible = 1
	AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axes3D.xAxis.label.font.scale = 1
	AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
	AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes3D.xAxis.label.font.bold = 0
	AnnotationAtts.axes3D.xAxis.label.font.italic = 0
	AnnotationAtts.axes3D.xAxis.label.scaling = 0
	AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
	AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
	AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
	AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
	AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
	AnnotationAtts.axes3D.xAxis.grid = 0
	AnnotationAtts.axes3D.yAxis.title.visible = 1
	AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axes3D.yAxis.title.font.scale = 1
	AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
	AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes3D.yAxis.title.font.bold = 0
	AnnotationAtts.axes3D.yAxis.title.font.italic = 0
	AnnotationAtts.axes3D.yAxis.title.userTitle = 0
	AnnotationAtts.axes3D.yAxis.title.userUnits = 0
	AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
	AnnotationAtts.axes3D.yAxis.title.units = ""
	AnnotationAtts.axes3D.yAxis.label.visible = 1
	AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axes3D.yAxis.label.font.scale = 1
	AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
	AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes3D.yAxis.label.font.bold = 0
	AnnotationAtts.axes3D.yAxis.label.font.italic = 0
	AnnotationAtts.axes3D.yAxis.label.scaling = 0
	AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
	AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
	AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
	AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
	AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
	AnnotationAtts.axes3D.yAxis.grid = 0
	AnnotationAtts.axes3D.zAxis.title.visible = 1
	AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axes3D.zAxis.title.font.scale = 1
	AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
	AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes3D.zAxis.title.font.bold = 0
	AnnotationAtts.axes3D.zAxis.title.font.italic = 0
	AnnotationAtts.axes3D.zAxis.title.userTitle = 0
	AnnotationAtts.axes3D.zAxis.title.userUnits = 0
	AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
	AnnotationAtts.axes3D.zAxis.title.units = ""
	AnnotationAtts.axes3D.zAxis.label.visible = 1
	AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axes3D.zAxis.label.font.scale = 1
	AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
	AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes3D.zAxis.label.font.bold = 0
	AnnotationAtts.axes3D.zAxis.label.font.italic = 0
	AnnotationAtts.axes3D.zAxis.label.scaling = 0
	AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
	AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
	AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
	AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
	AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
	AnnotationAtts.axes3D.zAxis.grid = 0
	AnnotationAtts.axes3D.setBBoxLocation = 1
	AnnotationAtts.axes3D.bboxLocation = (-10, 10, -10, 10, 0, 100)
	AnnotationAtts.userInfoFlag = 1
	AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
	AnnotationAtts.userInfoFont.scale = 1
	AnnotationAtts.userInfoFont.useForegroundColor = 1
	AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
	AnnotationAtts.userInfoFont.bold = 0
	AnnotationAtts.userInfoFont.italic = 0
	AnnotationAtts.databaseInfoFlag = 1
	AnnotationAtts.timeInfoFlag = 1
	AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
	AnnotationAtts.databaseInfoFont.scale = 1
	AnnotationAtts.databaseInfoFont.useForegroundColor = 1
	AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
	AnnotationAtts.databaseInfoFont.bold = 0
	AnnotationAtts.databaseInfoFont.italic = 0
	AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
	AnnotationAtts.databaseInfoTimeScale = 1
	AnnotationAtts.databaseInfoTimeOffset = 0
	AnnotationAtts.legendInfoFlag = 1
	AnnotationAtts.backgroundColor = (255, 255, 255, 255)
	AnnotationAtts.foregroundColor = (0, 0, 0, 255)
	AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
	AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
	AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
	AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
	AnnotationAtts.backgroundImage = ""
	AnnotationAtts.imageRepeatX = 1
	AnnotationAtts.imageRepeatY = 1
	AnnotationAtts.axesArray.visible = 1
	AnnotationAtts.axesArray.ticksVisible = 1
	AnnotationAtts.axesArray.autoSetTicks = 1
	AnnotationAtts.axesArray.autoSetScaling = 1
	AnnotationAtts.axesArray.lineWidth = 0
	AnnotationAtts.axesArray.axes.title.visible = 1
	AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axesArray.axes.title.font.scale = 1
	AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
	AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
	AnnotationAtts.axesArray.axes.title.font.bold = 0
	AnnotationAtts.axesArray.axes.title.font.italic = 0
	AnnotationAtts.axesArray.axes.title.userTitle = 0
	AnnotationAtts.axesArray.axes.title.userUnits = 0
	AnnotationAtts.axesArray.axes.title.title = ""
	AnnotationAtts.axesArray.axes.title.units = ""
	AnnotationAtts.axesArray.axes.label.visible = 1
	AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axesArray.axes.label.font.scale = 1
	AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
	AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
	AnnotationAtts.axesArray.axes.label.font.bold = 0
	AnnotationAtts.axesArray.axes.label.font.italic = 0
	AnnotationAtts.axesArray.axes.label.scaling = 0
	AnnotationAtts.axesArray.axes.tickMarks.visible = 1
	AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
	AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
	AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
	AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
	AnnotationAtts.axesArray.axes.grid = 0
	SetAnnotationAttributes(AnnotationAtts)

SetTimeSliderState(1000)
Volume_plot()
side_view()
Annotations()
