# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..diffusion import ResampleDTIVolume


def test_ResampleDTIVolume_inputs():
    input_map = dict(
        Inverse_ITK_Transformation=dict(argstr="--Inverse_ITK_Transformation "),
        Reference=dict(argstr="--Reference %s", extensions=None),
        args=dict(argstr="%s"),
        centered_transform=dict(argstr="--centered_transform "),
        correction=dict(argstr="--correction %s"),
        defField=dict(argstr="--defField %s", extensions=None),
        default_pixel_value=dict(argstr="--default_pixel_value %f"),
        direction_matrix=dict(argstr="--direction_matrix %s", sep=","),
        environ=dict(nohash=True, usedefault=True),
        hfieldtype=dict(argstr="--hfieldtype %s"),
        image_center=dict(argstr="--image_center %s"),
        inputVolume=dict(argstr="%s", extensions=None, position=-2),
        interpolation=dict(argstr="--interpolation %s"),
        notbulk=dict(argstr="--notbulk "),
        number_of_thread=dict(argstr="--number_of_thread %d"),
        origin=dict(argstr="--origin %s"),
        outputVolume=dict(argstr="%s", hash_files=False, position=-1),
        rotation_point=dict(argstr="--rotation_point %s"),
        size=dict(argstr="--size %s", sep=","),
        spaceChange=dict(argstr="--spaceChange "),
        spacing=dict(argstr="--spacing %s", sep=","),
        spline_order=dict(argstr="--spline_order %d"),
        transform=dict(argstr="--transform %s"),
        transform_matrix=dict(argstr="--transform_matrix %s", sep=","),
        transform_order=dict(argstr="--transform_order %s"),
        transform_tensor_method=dict(argstr="--transform_tensor_method %s"),
        transformationFile=dict(argstr="--transformationFile %s", extensions=None),
        window_function=dict(argstr="--window_function %s"),
    )
    inputs = ResampleDTIVolume.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ResampleDTIVolume_outputs():
    output_map = dict(outputVolume=dict(extensions=None, position=-1))
    outputs = ResampleDTIVolume.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
