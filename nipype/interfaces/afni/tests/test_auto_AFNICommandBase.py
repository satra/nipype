# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..base import AFNICommandBase


def test_AFNICommandBase_inputs():
    input_map = dict(args=dict(argstr="%s"), environ=dict(nohash=True, usedefault=True))
    inputs = AFNICommandBase.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
