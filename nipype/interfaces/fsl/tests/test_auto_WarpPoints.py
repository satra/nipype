# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import WarpPoints


def test_WarpPoints_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        coord_mm=dict(argstr="-mm", xor=["coord_vox"]),
        coord_vox=dict(argstr="-vox", xor=["coord_mm"]),
        dest_file=dict(argstr="-dest %s", extensions=None, mandatory=True),
        environ=dict(nohash=True, usedefault=True),
        in_coords=dict(argstr="%s", extensions=None, mandatory=True, position=-1),
        out_file=dict(
            extensions=None,
            name_source="in_coords",
            name_template="%s_warped",
            output_name="out_file",
        ),
        src_file=dict(argstr="-src %s", extensions=None, mandatory=True),
        warp_file=dict(argstr="-warp %s", extensions=None, xor=["xfm_file"]),
        xfm_file=dict(argstr="-xfm %s", extensions=None, xor=["warp_file"]),
    )
    inputs = WarpPoints.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_WarpPoints_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = WarpPoints.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
