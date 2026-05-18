# ad-supply-chain-transparency-governance-pack

Installable SSOT governance pack for ads.txt, app-ads.txt, sellers.json, SupplyChain Object, buyers.json, DemandChain Object, and ads.cert.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:ad-supply-chain-transparency`
- Priority: `P3.2`
- PyPI package: `ad-supply-chain-transparency-governance-pack`
- Import package: `ssot_pack_ad_supply_chain_transparency`
- GitHub repository: `groupsum/ad-supply-chain-transparency-governance-pack`
- Reservation owner: `extension-pack:ad-supply-chain-transparency-governance-pack`

## Domain Focus

Advertising Supply Chain Transparency

## Authority Sources

- ads.txt / app-ads.txt
- sellers.json and SupplyChain Object
- buyers.json and DemandChain Object
- ads.cert
- OpenRTB supply-chain fields

## Included ADRs

- `adr:ads-txt-authorized-digital-seller-policy` - Ads.txt Authorized Digital Seller Policy
- `adr:app-ads-txt-authorized-app-seller-policy` - App-ads.txt Authorized App Seller Policy
- `adr:sellers-json-seller-identity-policy` - Sellers.json Seller Identity Policy
- `adr:supplychain-object-path-transparency-policy` - SupplyChain Object Path Transparency Policy
- `adr:buyers-json-buyer-identity-policy` - Buyers.json Buyer Identity Policy
- `adr:demandchain-object-path-transparency-policy` - DemandChain Object Path Transparency Policy
- `adr:ads-cert-authenticated-inventory-policy` - Ads.cert Authenticated Inventory Policy
- `adr:supply-chain-transparency-reconciliation-policy` - Supply Chain Transparency Reconciliation Policy

## Included SPECs

- `spc:ads-txt-file-discovery-and-parsing-requirements` - Ads.txt File Discovery And Parsing Requirements
- `spc:ads-txt-authorized-seller-record-requirements` - Ads.txt Authorized Seller Record Requirements
- `spc:app-ads-txt-discovery-and-parsing-requirements` - App-ads.txt Discovery And Parsing Requirements
- `spc:sellers-json-file-and-seller-record-requirements` - Sellers.json File And Seller Record Requirements
- `spc:supplychain-object-node-requirements` - SupplyChain Object Node Requirements
- `spc:supplychain-object-openrtb-transport-requirements` - SupplyChain Object OpenRTB Transport Requirements
- `spc:buyers-json-file-and-buyer-record-requirements` - Buyers.json File And Buyer Record Requirements
- `spc:demandchain-object-node-requirements` - DemandChain Object Node Requirements
- `spc:ads-cert-signature-validation-requirements` - Ads.cert Signature Validation Requirements
- `spc:seller-authorization-reconciliation-requirements` - Seller Authorization Reconciliation Requirements
- `spc:buyer-demand-path-reconciliation-requirements` - Buyer Demand Path Reconciliation Requirements
- `spc:supply-chain-transparency-audit-evidence-requirements` - Supply Chain Transparency Audit Evidence Requirements

## Install With uv

```bash
uv add ad-supply-chain-transparency-governance-pack
uv add ssot-registry ad-supply-chain-transparency-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ad-supply-chain-transparency-governance-pack
uvx --from ssot-registry ssot pack sync . ad-supply-chain-transparency-governance-pack
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
- PyPI package: https://pypi.org/project/ad-supply-chain-transparency-governance-pack/
- SSOT Registry: https://pypi.org/project/ssot-registry/
