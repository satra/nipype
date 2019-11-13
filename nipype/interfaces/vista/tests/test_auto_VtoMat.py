# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..vista import VtoMat


def test_VtoMat_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(argstr="-in %s", extensions=None, mandatory=True, position=1),
        out_file=dict(
            argstr="-out %s",
            extensions=None,
            hash_files=False,
            keep_extension=False,
            name_source=["in_file"],
            name_template="%s.mat",
            position=-1,
        ),
    )
    inputs = VtoMat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_VtoMat_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = VtoMat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
