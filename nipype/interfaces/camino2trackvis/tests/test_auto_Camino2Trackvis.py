from __future__ import unicode_literals
# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.camino2trackvis.convert import Camino2Trackvis

def test_Camino2Trackvis_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    data_dims=dict(argstr='-d %s',
    mandatory=True,
    position=4,
    sep=',',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-i %s',
    mandatory=True,
    position=1,
    ),
    min_length=dict(argstr='-l %d',
    position=3,
    units='mm',
    ),
    nifti_file=dict(argstr='--nifti %s',
    position=7,
    ),
    out_file=dict(argstr='-o %s',
    genfile=True,
    position=2,
    ),
    terminal_output=dict(nohash=True,
    ),
    voxel_dims=dict(argstr='-x %s',
    mandatory=True,
    position=5,
    sep=',',
    ),
    voxel_order=dict(argstr='--voxel-order %s',
    mandatory=True,
    position=6,
    ),
    )
    inputs = Camino2Trackvis.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Camino2Trackvis_outputs():
    output_map = dict(trackvis=dict(),
    )
    outputs = Camino2Trackvis.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

