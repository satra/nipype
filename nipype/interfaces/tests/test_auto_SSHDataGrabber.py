# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..io import SSHDataGrabber


def test_SSHDataGrabber_inputs():
    input_map = dict(
        base_directory=dict(mandatory=True),
        download_files=dict(usedefault=True),
        drop_blank_outputs=dict(usedefault=True),
        hostname=dict(mandatory=True),
        password=dict(),
        raise_on_empty=dict(usedefault=True),
        sort_filelist=dict(mandatory=True),
        ssh_log_to_file=dict(usedefault=True),
        template=dict(mandatory=True),
        template_args=dict(),
        template_expression=dict(usedefault=True),
        username=dict(),
    )
    inputs = SSHDataGrabber.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_SSHDataGrabber_outputs():
    output_map = dict()
    outputs = SSHDataGrabber.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
