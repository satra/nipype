# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..diffusion import dtiestim


def test_dtiestim_inputs():
    input_map = dict(
        B0=dict(argstr="--B0 %s", hash_files=False),
        B0_mask_output=dict(argstr="--B0_mask_output %s", hash_files=False),
        DTI_double=dict(argstr="--DTI_double "),
        args=dict(argstr="%s"),
        bad_region_mask=dict(argstr="--bad_region_mask %s", extensions=None),
        brain_mask=dict(argstr="--brain_mask %s", extensions=None),
        correction=dict(argstr="--correction %s"),
        defaultTensor=dict(argstr="--defaultTensor %s", sep=","),
        dwi_image=dict(argstr="--dwi_image %s", extensions=None),
        environ=dict(nohash=True, usedefault=True),
        idwi=dict(argstr="--idwi %s", hash_files=False),
        method=dict(argstr="--method %s"),
        shiftNeg=dict(argstr="--shiftNeg "),
        shiftNegCoeff=dict(argstr="--shiftNegCoeff %f"),
        sigma=dict(argstr="--sigma %f"),
        step=dict(argstr="--step %f"),
        tensor_output=dict(argstr="--tensor_output %s", hash_files=False),
        threshold=dict(argstr="--threshold %d"),
        verbose=dict(argstr="--verbose "),
        weight_iterations=dict(argstr="--weight_iterations %d"),
    )
    inputs = dtiestim.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_dtiestim_outputs():
    output_map = dict(
        B0=dict(extensions=None),
        B0_mask_output=dict(extensions=None),
        idwi=dict(extensions=None),
        tensor_output=dict(extensions=None),
    )
    outputs = dtiestim.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
