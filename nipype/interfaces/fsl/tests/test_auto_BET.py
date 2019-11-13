# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import BET


def test_BET_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        center=dict(argstr="-c %s", units="voxels"),
        environ=dict(nohash=True, usedefault=True),
        frac=dict(argstr="-f %.2f"),
        functional=dict(
            argstr="-F",
            xor=(
                "functional",
                "reduce_bias",
                "robust",
                "padding",
                "remove_eyes",
                "surfaces",
                "t2_guided",
            ),
        ),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=0),
        mask=dict(argstr="-m"),
        mesh=dict(argstr="-e"),
        no_output=dict(argstr="-n"),
        out_file=dict(
            argstr="%s", extensions=None, genfile=True, hash_files=False, position=1
        ),
        outline=dict(argstr="-o"),
        output_type=dict(),
        padding=dict(
            argstr="-Z",
            xor=(
                "functional",
                "reduce_bias",
                "robust",
                "padding",
                "remove_eyes",
                "surfaces",
                "t2_guided",
            ),
        ),
        radius=dict(argstr="-r %d", units="mm"),
        reduce_bias=dict(
            argstr="-B",
            xor=(
                "functional",
                "reduce_bias",
                "robust",
                "padding",
                "remove_eyes",
                "surfaces",
                "t2_guided",
            ),
        ),
        remove_eyes=dict(
            argstr="-S",
            xor=(
                "functional",
                "reduce_bias",
                "robust",
                "padding",
                "remove_eyes",
                "surfaces",
                "t2_guided",
            ),
        ),
        robust=dict(
            argstr="-R",
            xor=(
                "functional",
                "reduce_bias",
                "robust",
                "padding",
                "remove_eyes",
                "surfaces",
                "t2_guided",
            ),
        ),
        skull=dict(argstr="-s"),
        surfaces=dict(
            argstr="-A",
            xor=(
                "functional",
                "reduce_bias",
                "robust",
                "padding",
                "remove_eyes",
                "surfaces",
                "t2_guided",
            ),
        ),
        t2_guided=dict(
            argstr="-A2 %s",
            extensions=None,
            xor=(
                "functional",
                "reduce_bias",
                "robust",
                "padding",
                "remove_eyes",
                "surfaces",
                "t2_guided",
            ),
        ),
        threshold=dict(argstr="-t"),
        vertical_gradient=dict(argstr="-g %.2f"),
    )
    inputs = BET.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BET_outputs():
    output_map = dict(
        inskull_mask_file=dict(extensions=None),
        inskull_mesh_file=dict(extensions=None),
        mask_file=dict(extensions=None),
        meshfile=dict(extensions=None),
        out_file=dict(extensions=None),
        outline_file=dict(extensions=None),
        outskin_mask_file=dict(extensions=None),
        outskin_mesh_file=dict(extensions=None),
        outskull_mask_file=dict(extensions=None),
        outskull_mesh_file=dict(extensions=None),
        skull_mask_file=dict(extensions=None),
    )
    outputs = BET.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
