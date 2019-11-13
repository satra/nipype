# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import Tensor2FractionalAnisotropy


def test_Tensor2FractionalAnisotropy_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        debug=dict(argstr="-debug", position=1),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-2),
        out_filename=dict(argstr="%s", extensions=None, genfile=True, position=-1),
        quiet=dict(argstr="-quiet", position=1),
    )
    inputs = Tensor2FractionalAnisotropy.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Tensor2FractionalAnisotropy_outputs():
    output_map = dict(FA=dict(extensions=None))
    outputs = Tensor2FractionalAnisotropy.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
