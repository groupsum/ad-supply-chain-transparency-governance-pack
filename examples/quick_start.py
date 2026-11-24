"""Inspect the installed pack identity."""

from ssot_pack_ad_supply_chain_transparency import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:ad-supply-chain-transparency"
print(metadata["origin"]["id"])
