# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..brainsuite import Hemisplit


def test_Hemisplit_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        inputHemisphereLabelFile=dict(argstr="-l %s", extensions=None, mandatory=True),
        inputSurfaceFile=dict(argstr="-i %s", extensions=None, mandatory=True),
        outputLeftHemisphere=dict(argstr="--left %s", extensions=None, genfile=True),
        outputLeftPialHemisphere=dict(argstr="-pl %s", extensions=None, genfile=True),
        outputRightHemisphere=dict(argstr="--right %s", extensions=None, genfile=True),
        outputRightPialHemisphere=dict(argstr="-pr %s", extensions=None, genfile=True),
        pialSurfaceFile=dict(argstr="-p %s", extensions=None),
        timer=dict(argstr="--timer"),
        verbosity=dict(argstr="-v %d"),
    )
    inputs = Hemisplit.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Hemisplit_outputs():
    output_map = dict(
        outputLeftHemisphere=dict(extensions=None),
        outputLeftPialHemisphere=dict(extensions=None),
        outputRightHemisphere=dict(extensions=None),
        outputRightPialHemisphere=dict(extensions=None),
    )
    outputs = Hemisplit.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
