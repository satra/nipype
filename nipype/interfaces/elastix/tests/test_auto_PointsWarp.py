# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..registration import PointsWarp


def test_PointsWarp_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        num_threads=dict(argstr="-threads %01d", nohash=True, usedefault=True),
        output_path=dict(argstr="-out %s", mandatory=True, usedefault=True),
        points_file=dict(argstr="-def %s", extensions=None, mandatory=True),
        transform_file=dict(argstr="-tp %s", extensions=None, mandatory=True),
    )
    inputs = PointsWarp.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_PointsWarp_outputs():
    output_map = dict(warped_file=dict(extensions=None))
    outputs = PointsWarp.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
