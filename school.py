# state file generated using paraview version 5.13.0
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1018, 789]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.CenterOfRotation = [0.0, 0.0, 20.206431664526463]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [63.99353730134589, -43.14644412877223, 69.22372465995399]
renderView1.CameraFocalPoint = [0.0, 0.0, 20.206431664526463]
renderView1.CameraViewUp = [-0.4595019394624451, 0.2771327365575528, 0.8438337596697429]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 34.64628654003838
renderView1.LegendGrid = 'Legend Grid Actor'
renderView1.PolarGrid = 'Polar Grid Actor'
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [1018, 789]
renderView2.AxesGrid = 'Grid Axes 3D Actor'
renderView2.CenterOfRotation = [-0.02483844757080078, -0.2478351593017578, 2.1997874826192856]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [34.479465864945055, -7.726172959202249, 12.397947874691411]
renderView2.CameraFocalPoint = [-0.024838447570801107, -0.24783515930175776, 2.199787482619286]
renderView2.CameraViewUp = [-0.23301958874145198, 0.21744703074192903, 0.9478494923163082]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 13.92548244478725
renderView2.LegendGrid = 'Legend Grid Actor'
renderView2.PolarGrid = 'Polar Grid Actor'
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [1018, 789]
renderView3.AxesGrid = 'Grid Axes 3D Actor'
renderView3.CenterOfRotation = [0.0, 0.0, 20.206431664526463]
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [86.52963090771208, -25.808261906247566, 34.5605273256683]
renderView3.CameraFocalPoint = [0.0, 0.0, 20.206431664526463]
renderView3.CameraViewUp = [-0.16764600821273484, -0.013824752428728014, 0.9857503193763724]
renderView3.CameraViewAngle = 28.89733840304182
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 34.64628654003838
renderView3.LegendGrid = 'Legend Grid Actor'
renderView3.PolarGrid = 'Polar Grid Actor'
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1018, 789)

# create new layout object 'Layout #2'
layout2 = CreateLayout(name='Layout #2')
layout2.AssignView(0, renderView2)
layout2.SetSize(1018, 789)

# create new layout object 'Layout #3'
layout3 = CreateLayout(name='Layout #3')
layout3.AssignView(0, renderView3)
layout3.SetSize(1018, 789)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Rectilinear Grid Reader'
binp_phot_hi_0vtr = XMLRectilinearGridReader(registrationName='binp_phot_hi_0.vtr', FileName=['/home/kostas/binp_phot_hi_0.vtr'])
binp_phot_hi_0vtr.PointArrayStatus = ['B']
binp_phot_hi_0vtr.TimeArray = 'None'

# create a new 'Extract Component'
extractComponent1 = ExtractComponent(registrationName='ExtractComponent1', Input=binp_phot_hi_0vtr)
extractComponent1.InputArray = ['POINTS', 'B']
extractComponent1.Component = 'Z'
extractComponent1.OutputArrayName = 'Bz'

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(registrationName='ExtractSubset1', Input=extractComponent1)
extractSubset1.VOI = [1, 260, 1, 260, 1, 1]

# create a new 'Compute Derivatives'
computeDerivatives1 = ComputeDerivatives(registrationName='ComputeDerivatives1', Input=binp_phot_hi_0vtr)
computeDerivatives1.Scalars = ['POINTS', '']
computeDerivatives1.Vectors = ['POINTS', 'B']
computeDerivatives1.OutputVectorType = 'Vorticity'
computeDerivatives1.OutputTensorType = 'Nothing'

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=computeDerivatives1)
calculator1.AttributeType = 'Cell Data'
calculator1.ResultArrayName = 'jmag'
calculator1.Function = 'mag(Vorticity)'

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=calculator1)
cellDatatoPointData1.CellDataArraytoprocess = ['Vorticity', 'jmag']

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=cellDatatoPointData1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]
slice1.PointMergeMethod = 'Uniform Binning'

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [-3.552713678800501e-15, -3.552713678800501e-15, 20.262857948030742]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [-3.552713678800501e-15, -3.552713678800501e-15, 20.262857948030742]

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=cellDatatoPointData1)
contour1.ContourBy = ['POINTS', 'jmag']
contour1.Isosurfaces = [40.0]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=binp_phot_hi_0vtr,
    SeedType='Point Cloud')
streamTracer1.Vectors = ['POINTS', 'B']
streamTracer1.MaximumStreamlineLength = 39.96000158786774

# init the 'Point Cloud' selected for 'SeedType'
streamTracer1.SeedType.Center = [-3.552713678800501e-15, -3.552713678800501e-15, 0.282857]
streamTracer1.SeedType.Radius = 5.0

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'B']
tube1.Radius = 0.15

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from extractComponent1
extractComponent1Display = Show(extractComponent1, renderView1, 'UniformGridRepresentation')

# get 2D transfer function for 'Bz'
bzTF2D = GetTransferFunction2D('Bz')
bzTF2D.ScalarRangeInitialized = 1
bzTF2D.Range = [-500.0, 500.0, 0.0, 1.0]

# get color transfer function/color map for 'Bz'
bzLUT = GetColorTransferFunction('Bz')
bzLUT.TransferFunction2D = bzTF2D
bzLUT.RGBPoints = [-500.0, 0.0, 0.0, 0.0, 500.0, 1.0, 1.0, 1.0]
bzLUT.ColorSpace = 'RGB'
bzLUT.NanColor = [1.0, 0.0, 0.0]
bzLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Bz'
bzPWF = GetOpacityTransferFunction('Bz')
bzPWF.Points = [-500.0, 0.0, 0.5, 0.0, 500.0, 1.0, 0.5, 0.0]
bzPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
extractComponent1Display.Representation = 'Outline'
extractComponent1Display.ColorArrayName = ['POINTS', 'Bz']
extractComponent1Display.LookupTable = bzLUT
extractComponent1Display.SelectNormalArray = 'None'
extractComponent1Display.SelectTangentArray = 'None'
extractComponent1Display.SelectTCoordArray = 'None'
extractComponent1Display.TextureTransform = 'Transform2'
extractComponent1Display.OSPRayScaleArray = 'B'
extractComponent1Display.OSPRayScaleFunction = 'Piecewise Function'
extractComponent1Display.Assembly = ''
extractComponent1Display.SelectedBlockSelectors = ['']
extractComponent1Display.SelectOrientationVectors = 'B'
extractComponent1Display.ScaleFactor = 3.996000158786774
extractComponent1Display.SelectScaleArray = 'B'
extractComponent1Display.GlyphType = 'Arrow'
extractComponent1Display.GlyphTableIndexArray = 'B'
extractComponent1Display.GaussianRadius = 0.1998000079393387
extractComponent1Display.SetScaleArray = ['POINTS', 'B']
extractComponent1Display.ScaleTransferFunction = 'Piecewise Function'
extractComponent1Display.OpacityArray = ['POINTS', 'B']
extractComponent1Display.OpacityTransferFunction = 'Piecewise Function'
extractComponent1Display.DataAxesGrid = 'Grid Axes Representation'
extractComponent1Display.PolarAxes = 'Polar Axes Representation'
extractComponent1Display.ScalarOpacityUnitDistance = 0.26723070664370624
extractComponent1Display.ScalarOpacityFunction = bzPWF
extractComponent1Display.TransferFunction2D = bzTF2D
extractComponent1Display.OpacityArrayName = ['POINTS', 'B']
extractComponent1Display.ColorArray2Name = ['POINTS', 'B']
extractComponent1Display.SliceFunction = 'Plane'
extractComponent1Display.Slice = 129
extractComponent1Display.SelectInputVectors = ['POINTS', 'B']
extractComponent1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
extractComponent1Display.ScaleTransferFunction.Points = [-275.2109817610294, 0.0, 0.5, 0.0, 360.42926382503197, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
extractComponent1Display.OpacityTransferFunction.Points = [-275.2109817610294, 0.0, 0.5, 0.0, 360.42926382503197, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
extractComponent1Display.SliceFunction.Origin = [-3.552713678800501e-15, -3.552713678800501e-15, 20.262857948030742]

# show data from extractSubset1
extractSubset1Display = Show(extractSubset1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
extractSubset1Display.Representation = 'Surface'
extractSubset1Display.ColorArrayName = ['POINTS', 'Bz']
extractSubset1Display.LookupTable = bzLUT
extractSubset1Display.SelectNormalArray = 'None'
extractSubset1Display.SelectTangentArray = 'None'
extractSubset1Display.SelectTCoordArray = 'None'
extractSubset1Display.TextureTransform = 'Transform2'
extractSubset1Display.OSPRayScaleArray = 'B'
extractSubset1Display.OSPRayScaleFunction = 'Piecewise Function'
extractSubset1Display.Assembly = ''
extractSubset1Display.SelectedBlockSelectors = ['']
extractSubset1Display.SelectOrientationVectors = 'B'
extractSubset1Display.ScaleFactor = 3.996000158786773
extractSubset1Display.SelectScaleArray = 'B'
extractSubset1Display.GlyphType = 'Arrow'
extractSubset1Display.GlyphTableIndexArray = 'B'
extractSubset1Display.GaussianRadius = 0.19980000793933866
extractSubset1Display.SetScaleArray = ['POINTS', 'B']
extractSubset1Display.ScaleTransferFunction = 'Piecewise Function'
extractSubset1Display.OpacityArray = ['POINTS', 'B']
extractSubset1Display.OpacityTransferFunction = 'Piecewise Function'
extractSubset1Display.DataAxesGrid = 'Grid Axes Representation'
extractSubset1Display.PolarAxes = 'Polar Axes Representation'
extractSubset1Display.ScalarOpacityUnitDistance = 1.3908297933582203
extractSubset1Display.ScalarOpacityFunction = bzPWF
extractSubset1Display.TransferFunction2D = bzTF2D
extractSubset1Display.OpacityArrayName = ['POINTS', 'B']
extractSubset1Display.ColorArray2Name = ['POINTS', 'B']
extractSubset1Display.SliceFunction = 'Plane'
extractSubset1Display.SelectInputVectors = ['POINTS', 'B']
extractSubset1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
extractSubset1Display.ScaleTransferFunction.Points = [-275.2109817610294, 0.0, 0.5, 0.0, 360.42926382503197, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
extractSubset1Display.OpacityTransferFunction.Points = [-275.2109817610294, 0.0, 0.5, 0.0, 360.42926382503197, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
extractSubset1Display.SliceFunction.Origin = [-3.552713678800501e-15, -3.552713678800501e-15, 0.2828571540968755]

# show data from tube1
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.SelectNormalArray = 'TubeNormals'
tube1Display.SelectTangentArray = 'None'
tube1Display.SelectTCoordArray = 'None'
tube1Display.TextureTransform = 'Transform2'
tube1Display.OSPRayScaleArray = 'AngularVelocity'
tube1Display.OSPRayScaleFunction = 'Piecewise Function'
tube1Display.Assembly = ''
tube1Display.SelectedBlockSelectors = ['']
tube1Display.SelectOrientationVectors = 'Normals'
tube1Display.ScaleFactor = 4.009809248149395
tube1Display.SelectScaleArray = 'AngularVelocity'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'AngularVelocity'
tube1Display.GaussianRadius = 0.20049046240746976
tube1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube1Display.ScaleTransferFunction = 'Piecewise Function'
tube1Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube1Display.OpacityTransferFunction = 'Piecewise Function'
tube1Display.DataAxesGrid = 'Grid Axes Representation'
tube1Display.PolarAxes = 'Polar Axes Representation'
tube1Display.SelectInputVectors = ['POINTS', 'Normals']
tube1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [-241.47600325443906, 0.0, 0.5, 0.0, 1051.1083772419906, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [-241.47600325443906, 0.0, 0.5, 0.0, 1051.1083772419906, 1.0, 0.5, 0.0]

# show data from cellDatatoPointData1
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Outline'
cellDatatoPointData1Display.ColorArrayName = ['POINTS', '']
cellDatatoPointData1Display.SelectNormalArray = 'None'
cellDatatoPointData1Display.SelectTangentArray = 'None'
cellDatatoPointData1Display.SelectTCoordArray = 'None'
cellDatatoPointData1Display.TextureTransform = 'Transform2'
cellDatatoPointData1Display.OSPRayScaleArray = 'jmag'
cellDatatoPointData1Display.OSPRayScaleFunction = 'Piecewise Function'
cellDatatoPointData1Display.Assembly = ''
cellDatatoPointData1Display.SelectedBlockSelectors = ['']
cellDatatoPointData1Display.SelectOrientationVectors = 'Vorticity'
cellDatatoPointData1Display.ScaleFactor = 3.996000158786774
cellDatatoPointData1Display.SelectScaleArray = 'jmag'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.GlyphTableIndexArray = 'jmag'
cellDatatoPointData1Display.GaussianRadius = 0.1998000079393387
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'jmag']
cellDatatoPointData1Display.ScaleTransferFunction = 'Piecewise Function'
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'jmag']
cellDatatoPointData1Display.OpacityTransferFunction = 'Piecewise Function'
cellDatatoPointData1Display.DataAxesGrid = 'Grid Axes Representation'
cellDatatoPointData1Display.PolarAxes = 'Polar Axes Representation'
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 0.26723070664370624
cellDatatoPointData1Display.OpacityArrayName = ['POINTS', 'jmag']
cellDatatoPointData1Display.ColorArray2Name = ['POINTS', 'jmag']
cellDatatoPointData1Display.IsosurfaceValues = [646.6960026983643]
cellDatatoPointData1Display.SliceFunction = 'Plane'
cellDatatoPointData1Display.Slice = 129
cellDatatoPointData1Display.SelectInputVectors = ['POINTS', 'Vorticity']
cellDatatoPointData1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
cellDatatoPointData1Display.ScaleTransferFunction.Points = [7.2522865616676295e-06, 0.0, 0.5, 0.0, 1293.391998144442, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
cellDatatoPointData1Display.OpacityTransferFunction.Points = [7.2522865616676295e-06, 0.0, 0.5, 0.0, 1293.391998144442, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
cellDatatoPointData1Display.SliceFunction.Origin = [-3.552713678800501e-15, -3.552713678800501e-15, 20.262857948030742]

# setup the color legend parameters for each legend in this view

# get color legend/bar for bzLUT in view renderView1
bzLUTColorBar = GetScalarBar(bzLUT, renderView1)
bzLUTColorBar.WindowLocation = 'Any Location'
bzLUTColorBar.Position = [0.8644400785854617, 0.47021546261089975]
bzLUTColorBar.Title = 'Bz'
bzLUTColorBar.ComponentTitle = ''
bzLUTColorBar.ScalarBarLength = 0.33000000000000007

# set color bar visibility
bzLUTColorBar.Visibility = 1

# show color legend
extractComponent1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
extractSubset1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.AmbientColor = [0.6666666666666666, 0.3333333333333333, 1.0]
contour1Display.ColorArrayName = ['POINTS', '']
contour1Display.DiffuseColor = [0.6666666666666666, 0.3333333333333333, 1.0]
contour1Display.Opacity = 0.56
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.SelectTCoordArray = 'None'
contour1Display.TextureTransform = 'Transform2'
contour1Display.OSPRayScaleArray = 'jmag'
contour1Display.OSPRayScaleFunction = 'Piecewise Function'
contour1Display.Assembly = ''
contour1Display.SelectedBlockSelectors = ['']
contour1Display.SelectOrientationVectors = 'Vorticity'
contour1Display.ScaleFactor = 2.00567569732666
contour1Display.SelectScaleArray = 'jmag'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'jmag'
contour1Display.GaussianRadius = 0.100283784866333
contour1Display.SetScaleArray = ['POINTS', 'jmag']
contour1Display.ScaleTransferFunction = 'Piecewise Function'
contour1Display.OpacityArray = ['POINTS', 'jmag']
contour1Display.OpacityTransferFunction = 'Piecewise Function'
contour1Display.DataAxesGrid = 'Grid Axes Representation'
contour1Display.PolarAxes = 'Polar Axes Representation'
contour1Display.SelectInputVectors = ['POINTS', 'Vorticity']
contour1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [100.0, 0.0, 0.5, 0.0, 100.015625, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [100.0, 0.0, 0.5, 0.0, 100.015625, 1.0, 0.5, 0.0]

# show data from tube1
tube1Display_1 = Show(tube1, renderView2, 'GeometryRepresentation')

# get 2D transfer function for 'B'
bTF2D = GetTransferFunction2D('B')
bTF2D.ScalarRangeInitialized = 1
bTF2D.Range = [10.0, 100.0, 0.0, 1.0]

# get color transfer function/color map for 'B'
bLUT = GetColorTransferFunction('B')
bLUT.TransferFunction2D = bTF2D
bLUT.RGBPoints = [10.0, 0.231373, 0.298039, 0.752941, 55.0, 0.865003, 0.865003, 0.865003, 100.0, 0.705882, 0.0156863, 0.14902]
bLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tube1Display_1.Representation = 'Surface'
tube1Display_1.ColorArrayName = ['POINTS', 'B']
tube1Display_1.LookupTable = bLUT
tube1Display_1.SelectNormalArray = 'TubeNormals'
tube1Display_1.SelectTangentArray = 'None'
tube1Display_1.SelectTCoordArray = 'None'
tube1Display_1.TextureTransform = 'Transform2'
tube1Display_1.OSPRayScaleArray = 'AngularVelocity'
tube1Display_1.OSPRayScaleFunction = 'Piecewise Function'
tube1Display_1.Assembly = ''
tube1Display_1.SelectedBlockSelectors = ['']
tube1Display_1.SelectOrientationVectors = 'Normals'
tube1Display_1.ScaleFactor = 4.009809248149395
tube1Display_1.SelectScaleArray = 'AngularVelocity'
tube1Display_1.GlyphType = 'Arrow'
tube1Display_1.GlyphTableIndexArray = 'AngularVelocity'
tube1Display_1.GaussianRadius = 0.20049046240746976
tube1Display_1.SetScaleArray = ['POINTS', 'AngularVelocity']
tube1Display_1.ScaleTransferFunction = 'Piecewise Function'
tube1Display_1.OpacityArray = ['POINTS', 'AngularVelocity']
tube1Display_1.OpacityTransferFunction = 'Piecewise Function'
tube1Display_1.DataAxesGrid = 'Grid Axes Representation'
tube1Display_1.PolarAxes = 'Polar Axes Representation'
tube1Display_1.SelectInputVectors = ['POINTS', 'Normals']
tube1Display_1.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
tube1Display_1.ScaleTransferFunction.Points = [-241.47600325443906, 0.0, 0.5, 0.0, 1051.1083772419906, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
tube1Display_1.OpacityTransferFunction.Points = [-241.47600325443906, 0.0, 0.5, 0.0, 1051.1083772419906, 1.0, 0.5, 0.0]

# show data from extractSubset1
extractSubset1Display_1 = Show(extractSubset1, renderView2, 'UniformGridRepresentation')

# trace defaults for the display properties.
extractSubset1Display_1.Representation = 'Surface'
extractSubset1Display_1.ColorArrayName = ['POINTS', 'Bz']
extractSubset1Display_1.LookupTable = bzLUT
extractSubset1Display_1.SelectNormalArray = 'None'
extractSubset1Display_1.SelectTangentArray = 'None'
extractSubset1Display_1.SelectTCoordArray = 'None'
extractSubset1Display_1.TextureTransform = 'Transform2'
extractSubset1Display_1.OSPRayScaleArray = 'B'
extractSubset1Display_1.OSPRayScaleFunction = 'Piecewise Function'
extractSubset1Display_1.Assembly = ''
extractSubset1Display_1.SelectedBlockSelectors = ['']
extractSubset1Display_1.SelectOrientationVectors = 'B'
extractSubset1Display_1.ScaleFactor = 3.996000158786773
extractSubset1Display_1.SelectScaleArray = 'B'
extractSubset1Display_1.GlyphType = 'Arrow'
extractSubset1Display_1.GlyphTableIndexArray = 'B'
extractSubset1Display_1.GaussianRadius = 0.19980000793933866
extractSubset1Display_1.SetScaleArray = ['POINTS', 'B']
extractSubset1Display_1.ScaleTransferFunction = 'Piecewise Function'
extractSubset1Display_1.OpacityArray = ['POINTS', 'B']
extractSubset1Display_1.OpacityTransferFunction = 'Piecewise Function'
extractSubset1Display_1.DataAxesGrid = 'Grid Axes Representation'
extractSubset1Display_1.PolarAxes = 'Polar Axes Representation'
extractSubset1Display_1.ScalarOpacityUnitDistance = 1.3908297933582203
extractSubset1Display_1.ScalarOpacityFunction = bzPWF
extractSubset1Display_1.TransferFunction2D = bzTF2D
extractSubset1Display_1.OpacityArrayName = ['POINTS', 'B']
extractSubset1Display_1.ColorArray2Name = ['POINTS', 'B']
extractSubset1Display_1.SliceFunction = 'Plane'
extractSubset1Display_1.SelectInputVectors = ['POINTS', 'B']
extractSubset1Display_1.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
extractSubset1Display_1.ScaleTransferFunction.Points = [-275.2109817610294, 0.0, 0.5, 0.0, 360.42926382503197, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
extractSubset1Display_1.OpacityTransferFunction.Points = [-275.2109817610294, 0.0, 0.5, 0.0, 360.42926382503197, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
extractSubset1Display_1.SliceFunction.Origin = [-3.552713678800501e-15, -3.552713678800501e-15, 0.2828571540968755]

# setup the color legend parameters for each legend in this view

# get color legend/bar for bzLUT in view renderView2
bzLUTColorBar_1 = GetScalarBar(bzLUT, renderView2)
bzLUTColorBar_1.Title = 'Bz'
bzLUTColorBar_1.ComponentTitle = ''

# set color bar visibility
bzLUTColorBar_1.Visibility = 1

# get color legend/bar for bLUT in view renderView2
bLUTColorBar = GetScalarBar(bLUT, renderView2)
bLUTColorBar.WindowLocation = 'Upper Right Corner'
bLUTColorBar.Title = 'B'
bLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
bLUTColorBar.Visibility = 1

# show color legend
tube1Display_1.SetScalarBarVisibility(renderView2, True)

# show color legend
extractSubset1Display_1.SetScalarBarVisibility(renderView2, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from extractSubset1
extractSubset1Display_2 = Show(extractSubset1, renderView3, 'UniformGridRepresentation')

# trace defaults for the display properties.
extractSubset1Display_2.Representation = 'Surface'
extractSubset1Display_2.ColorArrayName = ['POINTS', 'Bz']
extractSubset1Display_2.LookupTable = bzLUT
extractSubset1Display_2.SelectNormalArray = 'None'
extractSubset1Display_2.SelectTangentArray = 'None'
extractSubset1Display_2.SelectTCoordArray = 'None'
extractSubset1Display_2.TextureTransform = 'Transform2'
extractSubset1Display_2.OSPRayScaleArray = 'B'
extractSubset1Display_2.OSPRayScaleFunction = 'Piecewise Function'
extractSubset1Display_2.Assembly = ''
extractSubset1Display_2.SelectedBlockSelectors = ['']
extractSubset1Display_2.SelectOrientationVectors = 'B'
extractSubset1Display_2.ScaleFactor = 3.996000158786773
extractSubset1Display_2.SelectScaleArray = 'B'
extractSubset1Display_2.GlyphType = 'Arrow'
extractSubset1Display_2.GlyphTableIndexArray = 'B'
extractSubset1Display_2.GaussianRadius = 0.19980000793933866
extractSubset1Display_2.SetScaleArray = ['POINTS', 'B']
extractSubset1Display_2.ScaleTransferFunction = 'Piecewise Function'
extractSubset1Display_2.OpacityArray = ['POINTS', 'B']
extractSubset1Display_2.OpacityTransferFunction = 'Piecewise Function'
extractSubset1Display_2.DataAxesGrid = 'Grid Axes Representation'
extractSubset1Display_2.PolarAxes = 'Polar Axes Representation'
extractSubset1Display_2.ScalarOpacityUnitDistance = 1.3908297933582203
extractSubset1Display_2.ScalarOpacityFunction = bzPWF
extractSubset1Display_2.TransferFunction2D = bzTF2D
extractSubset1Display_2.OpacityArrayName = ['POINTS', 'B']
extractSubset1Display_2.ColorArray2Name = ['POINTS', 'B']
extractSubset1Display_2.SliceFunction = 'Plane'
extractSubset1Display_2.SelectInputVectors = ['POINTS', 'B']
extractSubset1Display_2.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
extractSubset1Display_2.ScaleTransferFunction.Points = [-275.2109817610294, 0.0, 0.5, 0.0, 360.42926382503197, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
extractSubset1Display_2.OpacityTransferFunction.Points = [-275.2109817610294, 0.0, 0.5, 0.0, 360.42926382503197, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
extractSubset1Display_2.SliceFunction.Origin = [-3.552713678800501e-15, -3.552713678800501e-15, 0.2828571540968755]

# show data from tube1
tube1Display_2 = Show(tube1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display_2.Representation = 'Surface'
tube1Display_2.ColorArrayName = [None, '']
tube1Display_2.SelectNormalArray = 'TubeNormals'
tube1Display_2.SelectTangentArray = 'None'
tube1Display_2.SelectTCoordArray = 'None'
tube1Display_2.TextureTransform = 'Transform2'
tube1Display_2.OSPRayScaleArray = 'AngularVelocity'
tube1Display_2.OSPRayScaleFunction = 'Piecewise Function'
tube1Display_2.Assembly = ''
tube1Display_2.SelectedBlockSelectors = ['']
tube1Display_2.SelectOrientationVectors = 'Normals'
tube1Display_2.ScaleFactor = 4.009809248149395
tube1Display_2.SelectScaleArray = 'AngularVelocity'
tube1Display_2.GlyphType = 'Arrow'
tube1Display_2.GlyphTableIndexArray = 'AngularVelocity'
tube1Display_2.GaussianRadius = 0.20049046240746976
tube1Display_2.SetScaleArray = ['POINTS', 'AngularVelocity']
tube1Display_2.ScaleTransferFunction = 'Piecewise Function'
tube1Display_2.OpacityArray = ['POINTS', 'AngularVelocity']
tube1Display_2.OpacityTransferFunction = 'Piecewise Function'
tube1Display_2.DataAxesGrid = 'Grid Axes Representation'
tube1Display_2.PolarAxes = 'Polar Axes Representation'
tube1Display_2.SelectInputVectors = ['POINTS', 'Normals']
tube1Display_2.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
tube1Display_2.ScaleTransferFunction.Points = [-241.47600325443906, 0.0, 0.5, 0.0, 1051.1083772419906, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
tube1Display_2.OpacityTransferFunction.Points = [-241.47600325443906, 0.0, 0.5, 0.0, 1051.1083772419906, 1.0, 0.5, 0.0]

# show data from extractComponent1
extractComponent1Display_1 = Show(extractComponent1, renderView3, 'UniformGridRepresentation')

# trace defaults for the display properties.
extractComponent1Display_1.Representation = 'Outline'
extractComponent1Display_1.ColorArrayName = [None, '']
extractComponent1Display_1.SelectNormalArray = 'None'
extractComponent1Display_1.SelectTangentArray = 'None'
extractComponent1Display_1.SelectTCoordArray = 'None'
extractComponent1Display_1.TextureTransform = 'Transform2'
extractComponent1Display_1.OSPRayScaleArray = 'B'
extractComponent1Display_1.OSPRayScaleFunction = 'Piecewise Function'
extractComponent1Display_1.Assembly = ''
extractComponent1Display_1.SelectedBlockSelectors = ['']
extractComponent1Display_1.SelectOrientationVectors = 'B'
extractComponent1Display_1.ScaleFactor = 3.996000158786774
extractComponent1Display_1.SelectScaleArray = 'B'
extractComponent1Display_1.GlyphType = 'Arrow'
extractComponent1Display_1.GlyphTableIndexArray = 'B'
extractComponent1Display_1.GaussianRadius = 0.1998000079393387
extractComponent1Display_1.SetScaleArray = ['POINTS', 'B']
extractComponent1Display_1.ScaleTransferFunction = 'Piecewise Function'
extractComponent1Display_1.OpacityArray = ['POINTS', 'B']
extractComponent1Display_1.OpacityTransferFunction = 'Piecewise Function'
extractComponent1Display_1.DataAxesGrid = 'Grid Axes Representation'
extractComponent1Display_1.PolarAxes = 'Polar Axes Representation'
extractComponent1Display_1.ScalarOpacityUnitDistance = 0.26723070664370624
extractComponent1Display_1.OpacityArrayName = ['POINTS', 'B']
extractComponent1Display_1.ColorArray2Name = ['POINTS', 'B']
extractComponent1Display_1.SliceFunction = 'Plane'
extractComponent1Display_1.Slice = 129
extractComponent1Display_1.SelectInputVectors = ['POINTS', 'B']
extractComponent1Display_1.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
extractComponent1Display_1.ScaleTransferFunction.Points = [-275.2109817610294, 0.0, 0.5, 0.0, 360.42926382503197, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
extractComponent1Display_1.OpacityTransferFunction.Points = [-275.2109817610294, 0.0, 0.5, 0.0, 360.42926382503197, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
extractComponent1Display_1.SliceFunction.Origin = [-3.552713678800501e-15, -3.552713678800501e-15, 20.262857948030742]

# show data from slice1
slice1Display = Show(slice1, renderView3, 'GeometryRepresentation')

# get 2D transfer function for 'Vorticity'
vorticityTF2D = GetTransferFunction2D('Vorticity')
vorticityTF2D.ScalarRangeInitialized = 1
vorticityTF2D.Range = [-75.0, 75.0, 0.0, 1.0]

# get color transfer function/color map for 'Vorticity'
vorticityLUT = GetColorTransferFunction('Vorticity')
vorticityLUT.TransferFunction2D = vorticityTF2D
vorticityLUT.RGBPoints = [-75.0, 0.231373, 0.298039, 0.752941, 0.0, 0.865003, 0.865003, 0.865003, 75.0, 0.705882, 0.0156863, 0.14902]
vorticityLUT.ScalarRangeInitialized = 1.0
vorticityLUT.VectorMode = 'Component'

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'Vorticity']
slice1Display.LookupTable = vorticityLUT
slice1Display.Opacity = 0.71
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.SelectTCoordArray = 'None'
slice1Display.TextureTransform = 'Transform2'
slice1Display.OSPRayScaleArray = 'jmag'
slice1Display.OSPRayScaleFunction = 'Piecewise Function'
slice1Display.Assembly = ''
slice1Display.SelectedBlockSelectors = ['']
slice1Display.SelectOrientationVectors = 'Vorticity'
slice1Display.ScaleFactor = 3.996000158786774
slice1Display.SelectScaleArray = 'jmag'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'jmag'
slice1Display.GaussianRadius = 0.1998000079393387
slice1Display.SetScaleArray = ['POINTS', 'jmag']
slice1Display.ScaleTransferFunction = 'Piecewise Function'
slice1Display.OpacityArray = ['POINTS', 'jmag']
slice1Display.OpacityTransferFunction = 'Piecewise Function'
slice1Display.DataAxesGrid = 'Grid Axes Representation'
slice1Display.PolarAxes = 'Polar Axes Representation'
slice1Display.SelectInputVectors = ['POINTS', 'Vorticity']
slice1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [9.720183833823986e-05, 0.0, 0.5, 0.0, 1003.1605532649135, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [9.720183833823986e-05, 0.0, 0.5, 0.0, 1003.1605532649135, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for bzLUT in view renderView3
bzLUTColorBar_2 = GetScalarBar(bzLUT, renderView3)
bzLUTColorBar_2.Title = 'Bz'
bzLUTColorBar_2.ComponentTitle = ''

# set color bar visibility
bzLUTColorBar_2.Visibility = 1

# get color legend/bar for vorticityLUT in view renderView3
vorticityLUTColorBar = GetScalarBar(vorticityLUT, renderView3)
vorticityLUTColorBar.WindowLocation = 'Upper Right Corner'
vorticityLUTColorBar.Position = [0.884871550903901, 0.6539923954372624]
vorticityLUTColorBar.Title = 'jx'
vorticityLUTColorBar.ComponentTitle = ''

# set color bar visibility
vorticityLUTColorBar.Visibility = 1

# show color legend
extractSubset1Display_2.SetScalarBarVisibility(renderView3, True)

# show color legend
slice1Display.SetScalarBarVisibility(renderView3, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'B'
bPWF = GetOpacityTransferFunction('B')
bPWF.Points = [10.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]
bPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'Vorticity'
vorticityPWF = GetOpacityTransferFunction('Vorticity')
vorticityPWF.Points = [-75.0, 0.0, 0.5, 0.0, 75.0, 1.0, 0.5, 0.0]
vorticityPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = [renderView1, renderView2, renderView3]
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 0.0

# initialize the animation scene

# ----------------------------------------------------------------
# restore active source
SetActiveSource(contour1)
# ----------------------------------------------------------------


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------