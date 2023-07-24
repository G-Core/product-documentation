---
title: during-a-ddos-attack-we-changed-your-ip-address-but-we-still-have-problems-with-the-performance-why
displayName: During a DDoS attack, we changed your IP address, but we still have problems with the performance. Why?
published: true
order: 80
toc:
pageTitle: FAQ. Problems With Performance After Changing IP | Gcore
pageDescription: Possible reasons why performance issues continue even though we changed your IP during the DDoS attack.
---
# During a DDoS attack, we changed your IP address, but we still have problems with the performance. Why?

Possible causes:

- Some DNS servers haven't yet updated the records (it depends on TTL), and not all traffic has been redirected to Gcore for filtering. You need to wait.
- You haven't changed your real IP address to a new one after you had enabled Web Protection. It means that an attacker knows it, so you need to request a new IP address from your hosting.
- You haven't restricted access to your server. Contact your hosting provider or use a firewall to <a href="https://gcore.com/docs/web-security/set-the-access-policy-for-a-protected-resource" target="_blank">set up ACL</a>.