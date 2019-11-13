# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..stats import StatsCommand


def test_StatsCommand_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=2),
        larger_voxel=dict(argstr="-t %f", position=-3),
        mask_file=dict(argstr="-m %s", extensions=None, position=-2),
    )
    inputs = StatsCommand.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_StatsCommand_outputs():
    output_map = dict(output=dict())
    outputs = StatsCommand.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
