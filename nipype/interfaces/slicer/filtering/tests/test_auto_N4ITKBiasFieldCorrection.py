from __future__ import unicode_literals
# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.filtering.n4itkbiasfieldcorrection import N4ITKBiasFieldCorrection

def test_N4ITKBiasFieldCorrection_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bsplineorder=dict(argstr='--bsplineorder %d',
    ),
    convergencethreshold=dict(argstr='--convergencethreshold %f',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    histogramsharpening=dict(argstr='--histogramsharpening %s',
    sep=',',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputimage=dict(argstr='--inputimage %s',
    ),
    iterations=dict(argstr='--iterations %s',
    sep=',',
    ),
    maskimage=dict(argstr='--maskimage %s',
    ),
    meshresolution=dict(argstr='--meshresolution %s',
    sep=',',
    ),
    outputbiasfield=dict(argstr='--outputbiasfield %s',
    hash_files=False,
    ),
    outputimage=dict(argstr='--outputimage %s',
    hash_files=False,
    ),
    shrinkfactor=dict(argstr='--shrinkfactor %d',
    ),
    splinedistance=dict(argstr='--splinedistance %f',
    ),
    terminal_output=dict(nohash=True,
    ),
    weightimage=dict(argstr='--weightimage %s',
    ),
    )
    inputs = N4ITKBiasFieldCorrection.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_N4ITKBiasFieldCorrection_outputs():
    output_map = dict(outputbiasfield=dict(),
    outputimage=dict(),
    )
    outputs = N4ITKBiasFieldCorrection.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

