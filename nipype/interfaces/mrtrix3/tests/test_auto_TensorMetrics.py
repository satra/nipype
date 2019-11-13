# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import TensorMetrics


def test_TensorMetrics_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        component=dict(argstr="-num %s", sep=",", usedefault=True),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-1),
        in_mask=dict(argstr="-mask %s", extensions=None),
        modulate=dict(argstr="-modulate %s"),
        out_adc=dict(argstr="-adc %s", extensions=None),
        out_eval=dict(argstr="-value %s", extensions=None),
        out_evec=dict(argstr="-vector %s", extensions=None),
        out_fa=dict(argstr="-fa %s", extensions=None),
    )
    inputs = TensorMetrics.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_TensorMetrics_outputs():
    output_map = dict(
        out_adc=dict(extensions=None),
        out_eval=dict(extensions=None),
        out_evec=dict(extensions=None),
        out_fa=dict(extensions=None),
    )
    outputs = TensorMetrics.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
