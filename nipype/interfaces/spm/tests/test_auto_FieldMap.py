# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import FieldMap


def test_FieldMap_inputs():
    input_map = dict(
        anat_file=dict(copyfile=False, extensions=None, field="subj.anat"),
        blip_direction=dict(field="subj.defaults.defaultsval.blipdir", mandatory=True),
        echo_times=dict(field="subj.defaults.defaultsval.et", mandatory=True),
        epi_file=dict(
            copyfile=False, extensions=None, field="subj.session.epi", mandatory=True
        ),
        epifm=dict(field="subj.defaults.defaultsval.epifm", usedefault=True),
        jacobian_modulation=dict(
            field="subj.defaults.defaultsval.ajm", usedefault=True
        ),
        jobtype=dict(usedefault=True),
        magnitude_file=dict(
            copyfile=False,
            extensions=None,
            field="subj.data.presubphasemag.magnitude",
            mandatory=True,
        ),
        mask_fwhm=dict(field="subj.defaults.defaultsval.mflags.fwhm", usedefault=True),
        maskbrain=dict(field="subj.defaults.defaultsval.maskbrain", usedefault=True),
        matchanat=dict(field="subj.matchanat", usedefault=True),
        matchvdm=dict(field="subj.matchvdm", usedefault=True),
        matlab_cmd=dict(),
        method=dict(field="subj.defaults.defaultsval.uflags.method", usedefault=True),
        mfile=dict(usedefault=True),
        ndilate=dict(field="subj.defaults.defaultsval.mflags.ndilate", usedefault=True),
        nerode=dict(field="subj.defaults.defaultsval.mflags.nerode", usedefault=True),
        pad=dict(field="subj.defaults.defaultsval.uflags.pad", usedefault=True),
        paths=dict(),
        phase_file=dict(
            copyfile=False,
            extensions=None,
            field="subj.data.presubphasemag.phase",
            mandatory=True,
        ),
        reg=dict(field="subj.defaults.defaultsval.mflags.reg", usedefault=True),
        sessname=dict(field="subj.sessname", usedefault=True),
        template=dict(
            copyfile=False,
            extensions=None,
            field="subj.defaults.defaultsval.mflags.template",
        ),
        thresh=dict(field="subj.defaults.defaultsval.mflags.thresh", usedefault=True),
        total_readout_time=dict(field="subj.defaults.defaultsval.tert", mandatory=True),
        unwarp_fwhm=dict(
            field="subj.defaults.defaultsval.uflags.fwhm", usedefault=True
        ),
        use_mcr=dict(),
        use_v8struct=dict(min_ver="8", usedefault=True),
        writeunwarped=dict(field="subj.writeunwarped", usedefault=True),
        ws=dict(field="subj.defaults.defaultsval.uflags.ws", usedefault=True),
    )
    inputs = FieldMap.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_FieldMap_outputs():
    output_map = dict(vdm=dict(extensions=None))
    outputs = FieldMap.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
