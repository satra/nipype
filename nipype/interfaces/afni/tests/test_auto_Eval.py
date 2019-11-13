# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import Eval


def test_Eval_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        expr=dict(argstr='-expr "%s"', mandatory=True, position=3),
        in_file_a=dict(argstr="-a %s", extensions=None, mandatory=True, position=0),
        in_file_b=dict(argstr="-b %s", extensions=None, position=1),
        in_file_c=dict(argstr="-c %s", extensions=None, position=2),
        num_threads=dict(nohash=True, usedefault=True),
        other=dict(argstr="", extensions=None),
        out1D=dict(argstr="-1D"),
        out_file=dict(
            argstr="-prefix %s",
            extensions=None,
            name_source="in_file_a",
            name_template="%s_calc",
        ),
        outputtype=dict(),
        single_idx=dict(),
        start_idx=dict(requires=["stop_idx"]),
        stop_idx=dict(requires=["start_idx"]),
    )
    inputs = Eval.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Eval_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = Eval.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
