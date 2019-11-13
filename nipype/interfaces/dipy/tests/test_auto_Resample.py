# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import Resample


def test_Resample_inputs():
    input_map = dict(
        in_file=dict(extensions=None, mandatory=True),
        interp=dict(mandatory=True, usedefault=True),
        vox_size=dict(),
    )
    inputs = Resample.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Resample_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = Resample.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
