# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.filtering.arithmetic import MaskScalarVolume

def test_MaskScalarVolume_inputs():
    input_map = dict(InputVolume=dict(argstr='%s',
    position=-3,
    ),
    MaskVolume=dict(argstr='%s',
    position=-2,
    ),
    OutputVolume=dict(argstr='%s',
    hash_files=False,
    position=-1,
    ),
    args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    label=dict(argstr='--label %d',
    ),
    replace=dict(argstr='--replace %d',
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = MaskScalarVolume.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_MaskScalarVolume_outputs():
    output_map = dict(OutputVolume=dict(position=-1,
    ),
    )
    outputs = MaskScalarVolume.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

