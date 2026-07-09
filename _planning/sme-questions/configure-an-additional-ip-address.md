# SME questions — Configure an additional IP address

**Ticket:** DOC-1717
**Audited:** 2026-07-09

## Questions

| # | Location in article | What the article claims | What we observed | Question for SME |
|---|---------------------|------------------------|-----------------|-----------------|
| 1 | All sections — interface name `eth0` in code examples | Interface is named `eth0` | VMmanager Network settings shows interface `ens3` on the test KVM VDS (Ubuntu 20.04, Mexico DC). Cannot SSH to verify OS-level name. | What is the standard interface name on Gcore KVM VDS images? Is it always `ens3`, or does it vary by DC or template? Should the docs use `ens3` instead of `eth0` as the example? |
| 2 | Debian/Ubuntu section — `/etc/network/interfaces` | Ubuntu can be configured by editing `/etc/network/interfaces` | Ubuntu 20.04 uses netplan by default (`/etc/netplan/*.yaml`). Could not verify whether the Gcore Ubuntu 20.04 image uses the legacy `ifupdown` stack. | Does the Gcore Ubuntu 20.04 VDS image use `ifupdown` (`/etc/network/interfaces`) or `netplan`? If netplan, the entire Debian/Ubuntu section needs rewriting with `netplan` syntax. |
| 3 | CentOS section — step 4: `service network restart` | `service network restart` restarts the network | Cannot verify — no CentOS server in test account. On CentOS 8+, the `network` service was removed. | Which CentOS versions are currently supported on Gcore VDS? On CentOS 7 the command is valid. On CentOS 8+ the `network` service does not exist — `nmcli connection reload` or `systemctl restart NetworkManager` should be used instead. Should the article cover CentOS 7 only, or also CentOS 8+? |
| 4 | CentOS section — all steps | Configuration via `ifcfg-eth0:N` files in `/etc/sysconfig/network-scripts/` | Cannot verify — no CentOS server in test account. On CentOS 8+, this directory may still exist for backward compatibility, but the preferred method is NetworkManager. | Is the `ifcfg` file approach valid for currently supported CentOS versions on Gcore VDS? |
| 5 | Windows Server section — all steps | Steps documented for Windows Server 2012 (Server Manager → Local Server → Properties → Advanced) | Cannot verify — no Windows server in test account. Windows Server 2012 reached EOL October 2023. | Which Windows Server versions (2016, 2019, 2022) are currently available on Gcore VDS? Do the documented steps (Server Manager → Local Server → IP properties → Advanced) still apply identically on those versions? |
