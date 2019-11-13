# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import WarpUtils


def test_WarpUtils_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(argstr="--in=%s", extensions=None, mandatory=True),
        knot_space=dict(argstr="--knotspace=%d,%d,%d"),
        out_file=dict(
            argstr="--out=%s",
            extensions=None,
            name_source=["in_file"],
            output_name="out_file",
            position=-1,
        ),
        out_format=dict(argstr="--outformat=%s"),
        out_jacobian=dict(argstr="--jac=%s", extensions=None),
        output_type=dict(),
        reference=dict(argstr="--ref=%s", extensions=None, mandatory=True),
        warp_resolution=dict(argstr="--warpres=%0.4f,%0.4f,%0.4f"),
        with_affine=dict(argstr="--withaff"),
        write_jacobian=dict(mandatory=True, usedefault=True),
    )
    inputs = WarpUtils.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_WarpUtils_outputs():
    output_map = dict(
        out_file=dict(extensions=None), out_jacobian=dict(extensions=None)
    )
    outputs = WarpUtils.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
