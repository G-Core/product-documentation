---
title: waap-cookies
displayName: What cookies are used by WAAP?
published: true
order: 10
toc:
pageTitle: A guide with required WAAP cookies | Gcore
pageDescription: View the list of required WAAP cookies, along with their descriptions and sample values.
---
# What are the required cookies used by WAAP?

Gcore WAAP uses different cookies to analyze user and browsing behavior. These cookies are required for the correct functioning of the Web Application and API Protection product. 

<expandable-element title="PRLST">

This cookie is created by the Set-Cookie response header. It gets the value from injected JavaScript, and the value contains a unique ID of the requested page.

* Duration: Session
* Sample value: AV
* Path: /
* SameSite: Lax

</expandable-element>

<expandable-element title="SPSI">

This cookie is created by the Set-Cookie response header. It contains the sessionID value.

* Duration: Session
* Sample value: 4e1ed32a27577bd95612f973777f8c3d
* Path: /
* HttpOnly: V
* SameSite: Lax

</expandable-element>

<expandable-element title="UTGv2">

This is a user tag token, a unique identifier of behavior on a domain. It's created by the Set-Cookie response header and gets values from injected JavaScript.

This cookie contains the usertag value, and is unique to browser and domain.

* Duration: Persistent
* Sample value: h4c5f3ab2d0ea64a63234ae2df4417f2d145
* Path: /
* SameSite: Lax

</expandable-element>

<expandable-element title="spcsrf">

This cookie is related to the CSRF protection module.

* Duration: Immediately
* Sample value: e98c27a664bbd73bd1b55be5a0f753eb
* Path: /
* HttpOnly: V
* SameSite: Strict

</expandable-element>

<expandable-element title="cnfc">

This is a CAPTCHA client-side cookie.

* Duration: Immediately
* Path: /
* SameSite: Lax

</expandable-element>

<expandable-element title="pvstr">

This is a CAPTCHA client-side cookie.

* Duration: Immediately
* Path: /
* SameSite: Lax

</expandable-element>

<expandable-element title="SPC">

This cookie is related to CAPTCHA validation.

* Duration: 4 days
* Sample value: G5g+JHlalFD1U0ZibWbs57jWH7h0cUNTagGqnvbxA5XjJ3I/WhkqS4X6dx 
ysiXNrjFBsJDcJqVRg+bqjiarVGVtO6fKYBBEBlW+Ik/PBRLTHwPeZlFAmW 
zECQ/lhv7rOBsNCJFCBRlnJ+qgFuWQHOg==
* Path: /
* HttpOnly: V
* SameSite: Lax

</expandable-element>

<expandable-element title="sbtsck">

This cookie is related to CAPTCHA and JavaScript validation.

* Duration: 1 day
* Sample value: javiVOxxF5xj9D1HJ62QVzjeM3I84j8KYF1VF7iS+uEoWE=
* Path: /
* SameSite: Lax

</expandable-element>

<expandable-element title="DCSS">

This cookie is related to DDoS protection.

* Duration: Session
* Sample value: F1046F5C84F1047ED441475A38AB15917B210EE
* Path: /
* SameSite: Lax

</expandable-element>

<expandable-element title="DGCC">

This cookie is related to DDoS protection.

* Duration: 1 day
* Sample value: ps
* Path: /
* SameSite: Lax

</expandable-element>

<expandable-element title="DSR">

This cookie is related to DDoS protection.

* Duration: Session
* Sample value: jyRENJbozdn/oyQae70NAYfKSeufcz4tPfbyMhLCOysLU3/FNaYu06nS01 
7SdLejOhXriDKOU2X/uLUCZaBb2Q==
* Path: /
* SameSite: Lax

</expandable-element>

<expandable-element title="DCST">

This cookie is related to DDoS protection.

* Duration: Session
* Sample value: pE9
* Path: /
* HttpOnly: V
* SameSite: Lax

</expandable-element>

<expandable-element title="SPSE">

This cookie is created by the Set-Cookie response header.

* Duration: Session
* Sample value: Eko0ihLuM2ND530rxn6S07NWKAWS3wW89XYxX3VbjVnFhREKfgyRAN 
3ttUFROFQqIpi+kmdrla9jH7EaII0nnA==
* Path: /
* HttpOnly: V
* SameSite: Lax

</expandable-element>

<expandable-element title="SPLB">

This cookie is related to load balancing.

* Duration: Session
* Path: /
* SameSite: Lax

</expandable-element>

<expandable-element title="sp_lit">

This is session-related cookie created by the <code>Set-Cookie</code> response header. It gets values from injected JavaScript.

* Duration: 5 minutes
* Sample value: gFYBNNtE+xA+GebbXECksQ==
* Path: /
* HttpOnly: V
* SameSite: Strict

</expandable-element>
