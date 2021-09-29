import numpy as np
import sys
#Specify where visit is installed in your system
sys.path.append("/home/aschoudhary/local/2.12.2/linux-x86_64/lib/site-packages/")

import visit
from visit import*
LaunchNowin()

###################################################################################
#################### Specify the location of data #################################

Bfield_data = "localhost:/datarepo/forashok/zero_Degrees_Rotation/Bxyz.file_* database"
Black_hole_horizon = "localhost:/datarepo/forashok/zero_Degrees_Rotation/BH_data/BBH.visit"

###################################################################################

#Open data files
OpenDatabase(Bfield_data, 0, "CarpetHDF5")
OpenDatabase(Black_hole_horizon, 0, "PlainText")

#create expressions to define each componets of normailzed magnetic ffield
# 1) for magnetic field data
ActivateDatabase(Bfield_data)
DefineScalarExpression("Bx", "<GIRAFFE--Bx>")
DefineScalarExpression("By", "<GIRAFFE--By>")
DefineScalarExpression("Bz", "<GIRAFFE--Bz>")
DefineScalarExpression("Bnorm", "sqrt(Bx*Bx + By*By + Bz*Bz)")
DefineVectorExpression("Bvec", "{Bx/Bnorm, By/Bnorm, Bz/Bnorm}")
# 2) for blackhole data
ActivateDatabase(Black_hole_horizon)
DefineScalarExpression("BBH_mesh", "var00")

#################################################################################################################################################
########################################## Finding particles with same time index as B field data ###############################################
#################################################################################################################################################
ActivateDatabase(Bfield_data)
print 'pseudocolour'
AddPlot("Pseudocolor", "GIRAFFE--Bx", 1, 0)
DrawPlots()

time_for_particle_data_output = []
#cycle_index = []

#TimeSliderGetNStates()
for state in range(1,TimeSliderGetNStates(),1):
	SetActivePlots(0)
	SetTimeSliderState(state)
	Query("Time") 
	time=GetQueryOutputValue()
	Query("Cycle") 
	cycle=GetQueryOutputValue()
	time_for_particle_data_output.extend([time])

DeleteActivePlots()

Seed = np.loadtxt('/datarepo/forashok/zero_Degrees_Rotation/particles.txt', skiprows = 2, unpack = True)
#Seed_list = Seed[:, time_index]


last_time_index_particledata = 8*680 -1 



particle_location_index = range(7,last_time_index_particledata, 8)





#################################################################################################################################################
#################################################################################################################################################


# Generate integral curves 
ActivateDatabase(Bfield_data)

def generate_streamlines(seeds):
	AddPlot("Pseudocolor", "operators/IntegralCurve/Bvec", 1, 0)
	IntegralCurveAtts = IntegralCurveAttributes()
	IntegralCurveAtts.sourceType = IntegralCurveAtts.PointList  # SpecifiedPoint, PointList, SpecifiedLine, Circle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection, FieldData
	IntegralCurveAtts.pointSource = (0, 0, 0)
	IntegralCurveAtts.lineStart = (0, 0, 0)
	IntegralCurveAtts.lineEnd = (1, 0, 0)
	IntegralCurveAtts.planeOrigin = (0, 0, 0)
	IntegralCurveAtts.planeNormal = (0, 0, 1)
	IntegralCurveAtts.planeUpAxis = (0, 1, 0)
	IntegralCurveAtts.radius = 1
	IntegralCurveAtts.sphereOrigin = (0, 0, 0)
	IntegralCurveAtts.boxExtents = (0, 1, 0, 1, 0, 1)
	IntegralCurveAtts.useWholeBox = 1
	IntegralCurveAtts.pointList = seeds 
	IntegralCurveAtts.fieldData = ()
	IntegralCurveAtts.sampleDensity0 = 2
	IntegralCurveAtts.sampleDensity1 = 2
	IntegralCurveAtts.sampleDensity2 = 2
	IntegralCurveAtts.dataValue = IntegralCurveAtts.TimeAbsolute  # Solid, SeedPointID, Speed, Vorticity, ArcLength, TimeAbsolute, TimeRelative, AverageDistanceFromSeed, CorrelationDistance, Difference, Variable
	IntegralCurveAtts.dataVariable = ""
	IntegralCurveAtts.integrationDirection = IntegralCurveAtts.Both  # Forward, Backward, Both, ForwardDirectionless, BackwardDirectionless, BothDirectionless
	IntegralCurveAtts.maxSteps = 1000
	IntegralCurveAtts.terminateByDistance = 1
	IntegralCurveAtts.termDistance = 20
	IntegralCurveAtts.terminateByTime = 0
	IntegralCurveAtts.termTime = 10
	IntegralCurveAtts.maxStepLength = 0.1
	IntegralCurveAtts.limitMaximumTimestep = 0
	IntegralCurveAtts.maxTimeStep = 0.1
	IntegralCurveAtts.relTol = 0.0001
	IntegralCurveAtts.absTolSizeType = IntegralCurveAtts.FractionOfBBox  # Absolute, FractionOfBBox
	IntegralCurveAtts.absTolAbsolute = 1e-06
	IntegralCurveAtts.absTolBBox = 1e-06
	IntegralCurveAtts.fieldType = IntegralCurveAtts.Default  # Default, FlashField, M3DC12DField, M3DC13DField, Nek5000Field, NektarPPField, NIMRODField
	IntegralCurveAtts.fieldConstant = 1
	IntegralCurveAtts.velocitySource = (0, 0, 0)
	IntegralCurveAtts.integrationType = IntegralCurveAtts.AdamsBashforth  # Euler, Leapfrog, DormandPrince, AdamsBashforth, RK4, M3DC12DIntegrator
	IntegralCurveAtts.parallelizationAlgorithmType = IntegralCurveAtts.VisItSelects  # LoadOnDemand, ParallelStaticDomains, MasterSlave, VisItSelects
	IntegralCurveAtts.maxProcessCount = 10
	IntegralCurveAtts.maxDomainCacheSize = 3
	IntegralCurveAtts.workGroupSize = 32
	IntegralCurveAtts.pathlines = 0
	IntegralCurveAtts.pathlinesOverrideStartingTimeFlag = 0
	IntegralCurveAtts.pathlinesOverrideStartingTime = 0
	IntegralCurveAtts.pathlinesPeriod = 0
	IntegralCurveAtts.pathlinesCMFE = IntegralCurveAtts.POS_CMFE  # CONN_CMFE, POS_CMFE
	IntegralCurveAtts.displayGeometry = IntegralCurveAtts.Lines  # Lines, Tubes, Ribbons
	IntegralCurveAtts.cleanupMethod = IntegralCurveAtts.NoCleanup  # NoCleanup, Merge, Before, After
	IntegralCurveAtts.cleanupThreshold = 1e-08
	IntegralCurveAtts.cropBeginFlag = 0
	IntegralCurveAtts.cropBegin = 0
	IntegralCurveAtts.cropEndFlag = 0
	IntegralCurveAtts.cropEnd = 0
	IntegralCurveAtts.cropValue = IntegralCurveAtts.Time  # Distance, Time, StepNumber
	IntegralCurveAtts.sampleDistance0 = 10
	IntegralCurveAtts.sampleDistance1 = 10
	IntegralCurveAtts.sampleDistance2 = 10
	IntegralCurveAtts.fillInterior = 1
	IntegralCurveAtts.randomSamples = 0
	IntegralCurveAtts.randomSeed = 0
	IntegralCurveAtts.numberOfRandomSamples = 1
	IntegralCurveAtts.issueAdvectionWarnings = 1
	IntegralCurveAtts.issueBoundaryWarnings = 1
	IntegralCurveAtts.issueTerminationWarnings = 1
	IntegralCurveAtts.issueStepsizeWarnings = 1
	IntegralCurveAtts.issueStiffnessWarnings = 1
	IntegralCurveAtts.issueCriticalPointsWarnings = 1
	IntegralCurveAtts.criticalPointThreshold = 0.001
	IntegralCurveAtts.correlationDistanceAngTol = 5
	IntegralCurveAtts.correlationDistanceMinDistAbsolute = 1
	IntegralCurveAtts.correlationDistanceMinDistBBox = 0.005
	IntegralCurveAtts.correlationDistanceMinDistType = IntegralCurveAtts.FractionOfBBox  # Absolute, FractionOfBBox
	IntegralCurveAtts.selection = ""
	SetOperatorOptions(IntegralCurveAtts, 0)
	AddOperator("Reflect", 0)
	ReflectAtts = ReflectAttributes()
	ReflectAtts.octant = ReflectAtts.PXPYPZ  # PXPYPZ, NXPYPZ, PXNYPZ, NXNYPZ, PXPYNZ, NXPYNZ, PXNYNZ, NXNYNZ
	ReflectAtts.useXBoundary = 0
	ReflectAtts.specifiedX = 0
	ReflectAtts.useYBoundary = 0
	ReflectAtts.specifiedY = 0
	ReflectAtts.useZBoundary = 0
	ReflectAtts.specifiedZ = 0
	ReflectAtts.reflections = (1, 0, 1, 0, 0, 0, 1, 0)
	SetOperatorOptions(ReflectAtts, 0)
	DrawPlots()



# End spontaneous state
def View_parameters():
	ViewCurveAtts = ViewCurveAttributes()
	ViewCurveAtts.domainCoords = (0, 1)
	ViewCurveAtts.rangeCoords = (0, 1)
	ViewCurveAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
	ViewCurveAtts.domainScale = ViewCurveAtts.LINEAR  # LINEAR, LOG
	ViewCurveAtts.rangeScale = ViewCurveAtts.LINEAR  # LINEAR, LOG
	SetViewCurve(ViewCurveAtts)
	View2DAtts = View2DAttributes()
	View2DAtts.windowCoords = (0, 1, 0, 1)
	View2DAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
	View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
	View2DAtts.fullFrameAutoThreshold = 100
	View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
	View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
	View2DAtts.windowValid = 0
	SetView2D(View2DAtts)
	View3DAtts = View3DAttributes()
	View3DAtts.viewNormal = (0, 0, 1)
	View3DAtts.focus = (0, 0, 0)
	View3DAtts.viewUp = (0, 1, 0)
	View3DAtts.viewAngle = 30
	View3DAtts.parallelScale = 24.4949
	View3DAtts.nearPlane = -48.9898
	View3DAtts.farPlane = 48.9898
	View3DAtts.imagePan = (0, 0)
	View3DAtts.imageZoom = 1
	View3DAtts.perspective = 1
	View3DAtts.eyeAngle = 2
	View3DAtts.centerOfRotationSet = 0
	View3DAtts.centerOfRotation = (0, 0, 0)
	View3DAtts.axis3DScaleFlag = 0
	View3DAtts.axis3DScales = (1, 1, 1)
	View3DAtts.shear = (0, 0, 1)
	View3DAtts.windowValid = 1
	SetView3D(View3DAtts)
	ViewAxisArrayAtts = ViewAxisArrayAttributes()
	ViewAxisArrayAtts.domainCoords = (0, 1)
	ViewAxisArrayAtts.rangeCoords = (0, 1)
	ViewAxisArrayAtts.viewportCoords = (0.15, 0.9, 0.1, 0.85)
	SetViewAxisArray(ViewAxisArrayAtts)



def add_blackholes():
	ActivateDatabase(Black_hole_horizon)
	AddPlot("Pseudocolor", "BBH_mesh", 1, 0)
	PseudocolorAtts = PseudocolorAttributes()
	PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
	PseudocolorAtts.skewFactor = 1
	PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
	PseudocolorAtts.minFlag = 0
	PseudocolorAtts.min = 0
	PseudocolorAtts.maxFlag = 0
	PseudocolorAtts.max = 1
	PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
	PseudocolorAtts.colorTableName = "hot"
	PseudocolorAtts.invertColorTable = 0
	PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
	PseudocolorAtts.opacityVariable = ""
	PseudocolorAtts.opacity = 1
	PseudocolorAtts.opacityVarMin = 0
	PseudocolorAtts.opacityVarMax = 1
	PseudocolorAtts.opacityVarMinFlag = 0
	PseudocolorAtts.opacityVarMaxFlag = 0
	PseudocolorAtts.pointSize = 0.05
	PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
	PseudocolorAtts.pointSizeVarEnabled = 0
	PseudocolorAtts.pointSizeVar = "default"
	PseudocolorAtts.pointSizePixels = 2
	PseudocolorAtts.lineStyle = PseudocolorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
	PseudocolorAtts.lineWidth = 0
	PseudocolorAtts.tubeResolution = 10
	PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
	PseudocolorAtts.tubeRadiusAbsolute = 0.125
	PseudocolorAtts.tubeRadiusBBox = 0.005
	PseudocolorAtts.tubeRadiusVarEnabled = 0
	PseudocolorAtts.tubeRadiusVar = ""
	PseudocolorAtts.tubeRadiusVarRatio = 10
	PseudocolorAtts.tailStyle = PseudocolorAtts.None  # None, Spheres, Cones
	PseudocolorAtts.headStyle = PseudocolorAtts.None  # None, Spheres, Cones
	PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
	PseudocolorAtts.endPointRadiusAbsolute = 0.125
	PseudocolorAtts.endPointRadiusBBox = 0.05
	PseudocolorAtts.endPointResolution = 10
	PseudocolorAtts.endPointRatio = 5
	PseudocolorAtts.endPointRadiusVarEnabled = 0
	PseudocolorAtts.endPointRadiusVar = ""
	PseudocolorAtts.endPointRadiusVarRatio = 10
	PseudocolorAtts.renderSurfaces = 1
	PseudocolorAtts.renderWireframe = 1
	PseudocolorAtts.renderPoints = 1
	PseudocolorAtts.smoothingLevel = 0
	PseudocolorAtts.legendFlag = 0
	PseudocolorAtts.lightingFlag = 1
	PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
	PseudocolorAtts.pointColor = (0, 0, 0, 0)
	SetPlotOptions(PseudocolorAtts)
	DrawPlots()

# The AnimationPlay RPC is not supported in the VisIt module so it will not be logged.
# Begin spontaneous state
def side_view():
	View3DAtts = View3DAttributes()
	View3DAtts.viewNormal = (-0.751802, -0.533877, 0.387)
	View3DAtts.focus = (-0.000119686, 0, 0)
	View3DAtts.viewUp = (0.160992, 0.42053, 0.892881)
	View3DAtts.viewAngle = 30
	View3DAtts.parallelScale = 25.02
	View3DAtts.nearPlane = -50.04
	View3DAtts.farPlane = 50.04
	View3DAtts.imagePan = (0, 0)
	View3DAtts.imageZoom = 0.5
	View3DAtts.perspective = 1
	View3DAtts.eyeAngle = 2
	View3DAtts.centerOfRotationSet = 0
	View3DAtts.centerOfRotation = (-0.000119686, 0, 0)
	View3DAtts.axis3DScaleFlag = 0
	View3DAtts.axis3DScales = (1, 1, 1)
	View3DAtts.shear = (0, 0, 1)
	View3DAtts.windowValid = 1
	SetView3D(View3DAtts)
	# End spontaneous state

def top_view():
	View3DAtts = View3DAttributes()
	View3DAtts.viewNormal = (0, 0, 1)
	View3DAtts.focus = (0, 0, 0)
	View3DAtts.viewUp = (0, 1, 0)
	View3DAtts.viewAngle = 30
	View3DAtts.parallelScale = 24.4949
	View3DAtts.nearPlane = -48.9898
	View3DAtts.farPlane = 48.9898
	View3DAtts.imagePan = (0, 0)
	View3DAtts.imageZoom = 0.9
	View3DAtts.perspective = 1
	View3DAtts.eyeAngle = 2
	View3DAtts.centerOfRotationSet = 0
	View3DAtts.centerOfRotation = (0, 0, 0)
	View3DAtts.axis3DScaleFlag = 0
	View3DAtts.axis3DScales = (1, 1, 1)
	View3DAtts.shear = (0, 0, 1)
	View3DAtts.windowValid = 1
	SetView3D(View3DAtts)



for time_index in range(1, TimeSliderGetNStates(), 1):
	print time_index
	Seed_list = Seed[:,particle_location_index[time_index-1]]
	radius_of_box = 1
	Particles_inside_box = []

	for i in range(1, len(Seed_list)-3, 3):
		particle_distance_from_centre_of_box = np.sqrt(Seed_list[i]*Seed_list[i] + Seed_list[i+1]*Seed_list[i+1] + Seed_list[i+2]*Seed_list[i+2])
		
		if particle_distance_from_centre_of_box < radius_of_box:
			Particles_inside_box.extend([Seed_list[i], Seed_list[i+1], Seed_list[i+2]])
	Particles_inside_box = tuple(Particles_inside_box)

	ActivateDatabase(Bfield_data)
	SetTimeSliderState(time_index)
	generate_streamlines(Particles_inside_box)
	
	# The AnimationPlay RPC is not supported in the VisIt module so it will not be logged.
	# Begin spontaneous state
	side_view()

	# End spontaneous state
	#################################
	Query("Time") 
	timeBf=GetQueryOutputValue()
	print 'B filed time query', timeBf
	print 'particle data time', Seed[0,particle_location_index[time_index-1]]
	######################################


	ActivateDatabase(Black_hole_horizon)
	SetTimeSliderState(4*time_index )
	add_blackholes()
	Query("Time") 
	timeBBH=GetQueryOutputValue()
	print 'Blackhole time query', timeBBH


	# The AnimationPlay RPC is not supported in the VisIt module so it will not be logged.
	# Begin spontaneous state
	
	side_view()
	SaveWindowAtts = SaveWindowAttributes()
	SaveWindowAtts.outputToCurrentDirectory = 0
	SaveWindowAtts.outputDirectory = "/home/aschoudhary/Streamline_project/plots/side_view_movingSeeds"
	SaveWindowAtts.fileName = "FigureTest" 
	SaveWindowAtts.family = 1
	SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
	SetSaveWindowAttributes(SaveWindowAtts)
	SaveWindow()

	top_view()
	SaveWindowAtts = SaveWindowAttributes()
	SaveWindowAtts.outputToCurrentDirectory = 0
	SaveWindowAtts.outputDirectory = "/home/aschoudhary/Streamline_project/plots/top_view_movingSeeds"
	SaveWindowAtts.fileName = "FigureTest" 
	SaveWindowAtts.family = 1
	SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
	SetSaveWindowAttributes(SaveWindowAtts)
	SaveWindow() 
	ActivateDatabase(Bfield_data)
	DeleteActivePlots()
	ActivateDatabase(Black_hole_horizon)
	DeleteActivePlots()



	

