# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..segmentation import LaplacianThickness


def test_LaplacianThickness_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        dT=dict(argstr="%s", position=6, requires=["prior_thickness"]),
        environ=dict(nohash=True, usedefault=True),
        input_gm=dict(
            argstr="%s", copyfile=True, extensions=None, mandatory=True, position=2
        ),
        input_wm=dict(
            argstr="%s", copyfile=True, extensions=None, mandatory=True, position=1
        ),
        num_threads=dict(nohash=True, usedefault=True),
        output_image=dict(
            argstr="%s",
            extensions=None,
            hash_files=False,
            keep_extension=True,
            name_source=["input_wm"],
            name_template="%s_thickness",
            position=3,
        ),
        prior_thickness=dict(argstr="%s", position=5, requires=["smooth_param"]),
        smooth_param=dict(argstr="%s", position=4),
        sulcus_prior=dict(argstr="%s", position=7, requires=["dT"]),
        tolerance=dict(argstr="%s", position=8, requires=["sulcus_prior"]),
    )
    inputs = LaplacianThickness.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_LaplacianThickness_outputs():
    output_map = dict(output_image=dict(extensions=None))
    outputs = LaplacianThickness.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
