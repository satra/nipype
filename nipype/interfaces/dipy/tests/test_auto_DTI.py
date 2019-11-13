# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..tensors import DTI


def test_DTI_inputs():
    input_map = dict(
        b0_thres=dict(usedefault=True),
        in_bval=dict(extensions=None, mandatory=True),
        in_bvec=dict(extensions=None, mandatory=True),
        in_file=dict(extensions=None, mandatory=True),
        mask_file=dict(extensions=None),
        out_prefix=dict(),
    )
    inputs = DTI.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DTI_outputs():
    output_map = dict(
        ad_file=dict(extensions=None),
        color_fa_file=dict(extensions=None),
        fa_file=dict(extensions=None),
        md_file=dict(extensions=None),
        out_file=dict(extensions=None),
        rd_file=dict(extensions=None),
    )
    outputs = DTI.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
