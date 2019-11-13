# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import TCatSubBrick


def test_TCatSubBrick_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        in_files=dict(argstr="%s%s ...", copyfile=False, mandatory=True, position=-1),
        num_threads=dict(nohash=True, usedefault=True),
        out_file=dict(argstr="-prefix %s", extensions=None, genfile=True),
        outputtype=dict(),
        rlt=dict(argstr="-rlt%s", position=1),
    )
    inputs = TCatSubBrick.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_TCatSubBrick_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = TCatSubBrick.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
