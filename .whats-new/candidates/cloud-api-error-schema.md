---
product: Cloud
status: Include
release_date: 2026-10-22
published_page: null
---

# Cloud API error response schema

Customer change: Cloud API error bodies use Content-Type application/problem+json. Clients can branch on type. Each body includes title, detail, hint, request_id, and trace_id. Validation errors list invalid inputs in errors. title, detail, hint, and errors detail follow Accept-Language. ru, de, zh, and az were checked. Some responses still include exception_class and message.
Affected users: Customers and integrations that read Cloud API error responses
Release evidence: GCLOUD2-30097 is Done, released in cloud-api 14.496.0 and 14.497.0 on 2026-10-22. On 2026-10-23, preprod and production returned the new body for a missing token and an unknown URL. Production returned validation-error, not-found, and method-not-allowed with the same fields.
Open verification: none
Source tickets/PRs: GCLOUD2-30097, DOC-2838
Documentation links: developer-tools/rest-api/error-handling.mdx
Duplicate check: not found on a What's new page or in the candidate register
Published entry: null
