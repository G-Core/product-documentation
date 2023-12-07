---
title: troubleshoot-errors-with-iso-image-installation
displayName: ISO images
published: true
order: 40
toc:
--1--Can't upload ISO in the panel: "Can-t-upload-iso-in-the-panel"
--1--Error in DCI manager: "error-in-dci-manager"
pageTitle: Troubleshoot errors with ISO image | Gcore
pageDescription: Troubleshoot ISO image installation errors with this guide.
---
# Troubleshoot errors with ISO image installation

Read more on <a href="https://gcore.com/docs/hosting/dedicated-servers/manage/operating-system/install-a-linux-os-from-your-iso-image" target="_blank">OS reinstalling from ISO</a>.

## Can't upload ISO in the panel

Check name of the file you're uploading - you should use only lowercase letters in the file extension. So, it should be «.iso», not «.ISO». Also, use only letters and numbers.

Check if the ISO file meets the following requirements.
- The file size shouldn't exceed 9 GBT
- Total amount of ISO images is 4 images per account

## Error in DCI manager

```
Error occurred when mounting ISO-image on the IPMI proxy server. Script output: ''
```

Try to delete ISO from the panel and upload it one more time. If you're still experiencing issues, contact us via chat or ticket from Control panel.