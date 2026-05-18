<div align="center">

# ad-supply-chain-transparency-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/ad-supply-chain-transparency-governance-pack.svg)](https://pypi.org/project/ad-supply-chain-transparency-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/ad-supply-chain-transparency-governance-pack.svg)](https://pypi.org/project/ad-supply-chain-transparency-governance-pack/)
[![License](https://img.shields.io/pypi/l/ad-supply-chain-transparency-governance-pack.svg)](https://pypi.org/project/ad-supply-chain-transparency-governance-pack/)
[![Publish](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/actions/workflows/publish.yml)

</div>

Installable SSOT governance pack for ads.txt, app-ads.txt, sellers.json, SupplyChain Object, buyers.json, DemandChain Object, and ads.cert.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `ad-supply-chain-transparency-governance-pack` is an installable SSOT governance pack for Advertising Supply Chain Transparency. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern advertising supply chain transparency, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`ad-supply-chain-transparency-governance-pack`](https://pypi.org/project/ad-supply-chain-transparency-governance-pack/)
- GitHub package repository: [`groupsum/ad-supply-chain-transparency-governance-pack`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack)
- Import package: `ssot_pack_ad_supply_chain_transparency`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:ad-supply-chain-transparency`
- PyPI package: `ad-supply-chain-transparency-governance-pack`
- Import package: `ssot_pack_ad_supply_chain_transparency`
- GitHub repository: `groupsum/ad-supply-chain-transparency-governance-pack`
- Reservation owner: `extension-pack:ad-supply-chain-transparency-governance-pack`

## Domain Focus

Advertising Supply Chain Transparency

## Authority Sources

- [ads.txt / app-ads.txt](https://iabtechlab.com/ads.txt)
- [sellers.json and SupplyChain Object](https://iabtechlab.com/sellers-json/)
- [buyers.json and DemandChain Object](https://iabtechlab.com/buyers-json-demand-chain/)
- [ads.cert](https://iabtechlab.com/ads-cert/)
- [OpenRTB supply-chain fields](https://iabtechlab.com/standards/openrtb/)

## Included ADRs

- [`adr:ads-txt-authorized-digital-seller-policy`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/adr/ADR-1001-ads-txt-authorized-digital-seller-policy.yaml) - Ads.txt Authorized Digital Seller Policy
- [`adr:app-ads-txt-authorized-app-seller-policy`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/adr/ADR-1002-app-ads-txt-authorized-app-seller-policy.yaml) - App-ads.txt Authorized App Seller Policy
- [`adr:sellers-json-seller-identity-policy`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/adr/ADR-1003-sellers-json-seller-identity-policy.yaml) - Sellers.json Seller Identity Policy
- [`adr:supplychain-object-path-transparency-policy`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/adr/ADR-1004-supplychain-object-path-transparency-policy.yaml) - SupplyChain Object Path Transparency Policy
- [`adr:buyers-json-buyer-identity-policy`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/adr/ADR-1005-buyers-json-buyer-identity-policy.yaml) - Buyers.json Buyer Identity Policy
- [`adr:demandchain-object-path-transparency-policy`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/adr/ADR-1006-demandchain-object-path-transparency-policy.yaml) - DemandChain Object Path Transparency Policy
- [`adr:ads-cert-authenticated-inventory-policy`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/adr/ADR-1007-ads-cert-authenticated-inventory-policy.yaml) - Ads.cert Authenticated Inventory Policy
- [`adr:supply-chain-transparency-reconciliation-policy`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/adr/ADR-1008-supply-chain-transparency-reconciliation-policy.yaml) - Supply Chain Transparency Reconciliation Policy

## Included SPECs

- [`spc:ads-txt-file-discovery-and-parsing-requirements`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/specs/SPEC-2001-ads-txt-file-discovery-and-parsing-requirements.yaml) - Ads.txt File Discovery And Parsing Requirements
- [`spc:ads-txt-authorized-seller-record-requirements`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/specs/SPEC-2002-ads-txt-authorized-seller-record-requirements.yaml) - Ads.txt Authorized Seller Record Requirements
- [`spc:app-ads-txt-discovery-and-parsing-requirements`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/specs/SPEC-2003-app-ads-txt-discovery-and-parsing-requirements.yaml) - App-ads.txt Discovery And Parsing Requirements
- [`spc:sellers-json-file-and-seller-record-requirements`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/specs/SPEC-2004-sellers-json-file-and-seller-record-requirements.yaml) - Sellers.json File And Seller Record Requirements
- [`spc:supplychain-object-node-requirements`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/specs/SPEC-2005-supplychain-object-node-requirements.yaml) - SupplyChain Object Node Requirements
- [`spc:supplychain-object-openrtb-transport-requirements`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/specs/SPEC-2006-supplychain-object-openrtb-transport-requirements.yaml) - SupplyChain Object OpenRTB Transport Requirements
- [`spc:buyers-json-file-and-buyer-record-requirements`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/specs/SPEC-2007-buyers-json-file-and-buyer-record-requirements.yaml) - Buyers.json File And Buyer Record Requirements
- [`spc:demandchain-object-node-requirements`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/specs/SPEC-2008-demandchain-object-node-requirements.yaml) - DemandChain Object Node Requirements
- [`spc:ads-cert-signature-validation-requirements`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/specs/SPEC-2009-ads-cert-signature-validation-requirements.yaml) - Ads.cert Signature Validation Requirements
- [`spc:seller-authorization-reconciliation-requirements`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/specs/SPEC-2010-seller-authorization-reconciliation-requirements.yaml) - Seller Authorization Reconciliation Requirements
- [`spc:buyer-demand-path-reconciliation-requirements`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/specs/SPEC-2011-buyer-demand-path-reconciliation-requirements.yaml) - Buyer Demand Path Reconciliation Requirements
- [`spc:supply-chain-transparency-audit-evidence-requirements`](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack/blob/master/src/ssot_pack_ad_supply_chain_transparency/templates/specs/SPEC-2012-supply-chain-transparency-audit-evidence-requirements.yaml) - Supply Chain Transparency Audit Evidence Requirements

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

- GitHub package repository: [groupsum/ad-supply-chain-transparency-governance-pack](https://github.com/groupsum/ad-supply-chain-transparency-governance-pack)
- PyPI package: [ad-supply-chain-transparency-governance-pack](https://pypi.org/project/ad-supply-chain-transparency-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
