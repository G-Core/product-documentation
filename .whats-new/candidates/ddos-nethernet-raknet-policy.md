---
product: DDoS Protection
status: Needs verification
release_date: unknown
published_page: null
---

# Nethernet and RakNet in one protection policy

Customer change: A DDoS protection policy can include both the nethernet and the raknet countermeasure, so one policy can protect several Minecraft servers (NetherNet and Bedrock/RakNet).
Affected users: Customers who configure a custom protection profile for Minecraft servers.
Release evidence: not verified. DP-5080 is Resolved and PR G-Core/sifter#2634 is merged to main. A production API check on 2026-11-18 listed the nethernet template entries, but the policy list was truncated, so the shared-policy rule was not observed working.
Open verification: Confirm in the Customer Portal that one protection policy accepts both countermeasures, and record the labels the policy editor shows.
Source tickets/PRs: DOC-2977, DP-5080, G-Core/sifter#2634
Documentation links: ddos-protection/onboarding-service/custom-protection-profile-configuration.mdx
Duplicate check: not found
Published entry:
