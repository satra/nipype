# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..dti import ModelFit


def test_ModelFit_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        bgmask=dict(argstr="-bgmask %s", extensions=None),
        bgthresh=dict(argstr="-bgthresh %G"),
        cfthresh=dict(argstr="-csfthresh %G"),
        environ=dict(nohash=True, usedefault=True),
        fixedbvalue=dict(argstr="-fixedbvalue %s"),
        fixedmodq=dict(argstr="-fixedmod %s"),
        in_file=dict(argstr="-inputfile %s", extensions=None, mandatory=True),
        inputdatatype=dict(argstr="-inputdatatype %s"),
        model=dict(argstr="-model %s", mandatory=True),
        noisemap=dict(argstr="-noisemap %s", extensions=None),
        out_file=dict(argstr="> %s", extensions=None, genfile=True, position=-1),
        outlier=dict(argstr="-outliermap %s", extensions=None),
        outputfile=dict(argstr="-outputfile %s", extensions=None),
        residualmap=dict(argstr="-residualmap %s", extensions=None),
        scheme_file=dict(argstr="-schemefile %s", extensions=None, mandatory=True),
        sigma=dict(argstr="-sigma %G"),
        tau=dict(argstr="-tau %G"),
    )
    inputs = ModelFit.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ModelFit_outputs():
    output_map = dict(fitted_data=dict(extensions=None))
    outputs = ModelFit.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
