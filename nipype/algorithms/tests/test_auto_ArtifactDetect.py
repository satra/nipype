# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..rapidart import ArtifactDetect


def test_ArtifactDetect_inputs():
    input_map = dict(
        bound_by_brainmask=dict(usedefault=True),
        global_threshold=dict(usedefault=True),
        intersect_mask=dict(usedefault=True),
        mask_file=dict(extensions=None),
        mask_threshold=dict(),
        mask_type=dict(mandatory=True),
        norm_threshold=dict(
            mandatory=True, xor=["rotation_threshold", "translation_threshold"]
        ),
        parameter_source=dict(mandatory=True),
        plot_type=dict(usedefault=True),
        realigned_files=dict(mandatory=True),
        realignment_parameters=dict(mandatory=True),
        rotation_threshold=dict(mandatory=True, xor=["norm_threshold"]),
        save_plot=dict(usedefault=True),
        translation_threshold=dict(mandatory=True, xor=["norm_threshold"]),
        use_differences=dict(maxlen=2, minlen=2, usedefault=True),
        use_norm=dict(requires=["norm_threshold"], usedefault=True),
        zintensity_threshold=dict(mandatory=True),
    )
    inputs = ArtifactDetect.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ArtifactDetect_outputs():
    output_map = dict(
        displacement_files=dict(),
        intensity_files=dict(),
        mask_files=dict(),
        norm_files=dict(),
        outlier_files=dict(),
        plot_files=dict(),
        statistic_files=dict(),
    )
    outputs = ArtifactDetect.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
