# ssot-pack-ad-supply-chain-transparency

Installable SSOT governance pack for ads.txt, app-ads.txt, sellers.json, SupplyChain Object, buyers.json, DemandChain Object, and ads.cert.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:ad-supply-chain-transparency`
- Priority: `P3.2`
- PyPI package: `ssot-pack-ad-supply-chain-transparency`
- Import package: `ssot_pack_ad_supply_chain_transparency`
- GitHub repository: `groupsum/ad-supply-chain-transparency-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-ad-supply-chain-transparency`

## Domain Focus

Advertising Supply Chain Transparency

## Authority Sources

- ads.txt / app-ads.txt
- sellers.json and SupplyChain Object
- buyers.json and DemandChain Object
- ads.cert
- OpenRTB supply-chain fields

## Included ADRs

- `adr:ad-supply-chain-authority` - Ad Supply Chain Authority
- `adr:seller-buyer-transparency-boundary` - Seller Buyer Transparency Boundary

## Included SPECs

- `spc:ads-txt-app-ads-txt-contract` - Ads.txt App-ads.txt Contract
- `spc:sellers-json-schain-contract` - Sellers.json SupplyChain Contract
- `spc:buyers-json-demandchain-contract` - Buyers.json DemandChain Contract
- `spc:ads-cert-contract` - Ads.cert Contract

## Install With uv

```bash
uv add ssot-pack-ad-supply-chain-transparency
uv add ssot-registry ssot-pack-ad-supply-chain-transparency
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-ad-supply-chain-transparency
uvx --from ssot-registry ssot pack sync . ssot-pack-ad-supply-chain-transparency
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_ad_supply_chain_transparency import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/ad-supply-chain-transparency-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-ad-supply-chain-transparency/
- SSOT Registry: https://pypi.org/project/ssot-registry/
