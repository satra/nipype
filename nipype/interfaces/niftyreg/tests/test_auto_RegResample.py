# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..regutils import RegResample


def test_RegResample_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        flo_file=dict(argstr="-flo %s", extensions=None, mandatory=True),
        inter_val=dict(argstr="-inter %d"),
        omp_core_val=dict(argstr="-omp %i", usedefault=True),
        out_file=dict(
            argstr="%s",
            extensions=None,
            name_source=["flo_file"],
            name_template="%s",
            position=-1,
        ),
        pad_val=dict(argstr="-pad %f"),
        psf_alg=dict(argstr="-psf_alg %d"),
        psf_flag=dict(argstr="-psf"),
        ref_file=dict(argstr="-ref %s", extensions=None, mandatory=True),
        tensor_flag=dict(argstr="-tensor "),
        trans_file=dict(argstr="-trans %s", extensions=None),
        type=dict(argstr="-%s", position=-2, usedefault=True),
        verbosity_off_flag=dict(argstr="-voff"),
    )
    inputs = RegResample.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_RegResample_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = RegResample.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
