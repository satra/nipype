# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..brains import insertMidACPCpoint


def test_insertMidACPCpoint_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        inputLandmarkFile=dict(argstr="--inputLandmarkFile %s", extensions=None),
        outputLandmarkFile=dict(argstr="--outputLandmarkFile %s", hash_files=False),
    )
    inputs = insertMidACPCpoint.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_insertMidACPCpoint_outputs():
    output_map = dict(outputLandmarkFile=dict(extensions=None))
    outputs = insertMidACPCpoint.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
