# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..featuredetection import CannyEdge


def test_CannyEdge_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        inputVolume=dict(argstr="--inputVolume %s", extensions=None),
        lowerThreshold=dict(argstr="--lowerThreshold %f"),
        outputVolume=dict(argstr="--outputVolume %s", hash_files=False),
        upperThreshold=dict(argstr="--upperThreshold %f"),
        variance=dict(argstr="--variance %f"),
    )
    inputs = CannyEdge.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CannyEdge_outputs():
    output_map = dict(outputVolume=dict(extensions=None))
    outputs = CannyEdge.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
