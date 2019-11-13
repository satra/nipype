# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..misc import MergeCSVFiles


def test_MergeCSVFiles_inputs():
    input_map = dict(
        column_headings=dict(),
        extra_column_heading=dict(),
        extra_field=dict(),
        in_files=dict(mandatory=True),
        out_file=dict(extensions=None, usedefault=True),
        row_heading_title=dict(usedefault=True),
        row_headings=dict(),
    )
    inputs = MergeCSVFiles.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MergeCSVFiles_outputs():
    output_map = dict(csv_file=dict(extensions=None))
    outputs = MergeCSVFiles.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
