# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..connectivity import LabelConfig


def test_LabelConfig_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        in_config=dict(argstr="%s", extensions=None, position=-2),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-3),
        lut_aal=dict(argstr="-lut_aal %s", extensions=None),
        lut_basic=dict(argstr="-lut_basic %s", extensions=None),
        lut_fs=dict(argstr="-lut_freesurfer %s", extensions=None),
        lut_itksnap=dict(argstr="-lut_itksnap %s", extensions=None),
        nthreads=dict(argstr="-nthreads %d", nohash=True),
        out_file=dict(
            argstr="%s", extensions=None, mandatory=True, position=-1, usedefault=True
        ),
        spine=dict(argstr="-spine %s", extensions=None),
    )
    inputs = LabelConfig.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_LabelConfig_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = LabelConfig.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
