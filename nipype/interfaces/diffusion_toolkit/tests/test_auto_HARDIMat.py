# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..odf import HARDIMat


def test_HARDIMat_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        bvals=dict(extensions=None, mandatory=True),
        bvecs=dict(argstr="%s", extensions=None, mandatory=True, position=1),
        environ=dict(nohash=True, usedefault=True),
        image_info=dict(argstr="-info %s", extensions=None),
        image_orientation_vectors=dict(argstr="-iop %f"),
        oblique_correction=dict(argstr="-oc"),
        odf_file=dict(argstr="-odf %s", extensions=None),
        order=dict(argstr="-order %s"),
        out_file=dict(argstr="%s", extensions=None, position=2, usedefault=True),
        reference_file=dict(argstr="-ref %s", extensions=None),
    )
    inputs = HARDIMat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_HARDIMat_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = HARDIMat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
