# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..base import AssertEqual


def test_AssertEqual_inputs():
    input_map = dict(
        volume1=dict(extensions=None, mandatory=True),
        volume2=dict(extensions=None, mandatory=True),
    )
    inputs = AssertEqual.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
