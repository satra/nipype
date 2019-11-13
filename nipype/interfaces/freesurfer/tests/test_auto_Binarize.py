# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..model import Binarize


def test_Binarize_inputs():
    input_map = dict(
        abs=dict(argstr="--abs"),
        args=dict(argstr="%s"),
        bin_col_num=dict(argstr="--bincol"),
        bin_val=dict(argstr="--binval %d"),
        bin_val_not=dict(argstr="--binvalnot %d"),
        binary_file=dict(argstr="--o %s", extensions=None, genfile=True),
        count_file=dict(argstr="--count %s"),
        dilate=dict(argstr="--dilate %d"),
        environ=dict(nohash=True, usedefault=True),
        erode=dict(argstr="--erode  %d"),
        erode2d=dict(argstr="--erode2d %d"),
        frame_no=dict(argstr="--frame %s"),
        in_file=dict(argstr="--i %s", copyfile=False, extensions=None, mandatory=True),
        invert=dict(argstr="--inv"),
        mask_file=dict(argstr="--mask maskvol", extensions=None),
        mask_thresh=dict(argstr="--mask-thresh %f"),
        match=dict(argstr="--match %d..."),
        max=dict(argstr="--max %f", xor=["wm_ven_csf"]),
        merge_file=dict(argstr="--merge %s", extensions=None),
        min=dict(argstr="--min %f", xor=["wm_ven_csf"]),
        out_type=dict(argstr=""),
        rmax=dict(argstr="--rmax %f"),
        rmin=dict(argstr="--rmin %f"),
        subjects_dir=dict(),
        ventricles=dict(argstr="--ventricles"),
        wm=dict(argstr="--wm"),
        wm_ven_csf=dict(argstr="--wm+vcsf", xor=["min", "max"]),
        zero_edges=dict(argstr="--zero-edges"),
        zero_slice_edge=dict(argstr="--zero-slice-edges"),
    )
    inputs = Binarize.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Binarize_outputs():
    output_map = dict(
        binary_file=dict(extensions=None), count_file=dict(extensions=None)
    )
    outputs = Binarize.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
