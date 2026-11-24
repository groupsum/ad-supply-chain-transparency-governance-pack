"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_ad_supply_chain_transparency import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:ads-txt-file-discovery-and-parsing-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-ads-txt-file-discovery-and-parsing-requirements.yaml"
