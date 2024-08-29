---
title: waap-cookies
displayName: WAAP cookies and storage variables
published: true
order: 10
toc:
pageTitle: A guide with required WAAP cookies and storage variables | Gcore
pageDescription: View the list of required WAAP cookies and storage variables, along with their descriptions and sample values.
---
# WAAP cookies and storage variables

Gcore WAAP uses different cookies to analyze user and browsing behavior. These cookies are required for the correct functioning of the Web Application and API Protection product. 

## Required cookies

<table>
<thead>
<tr>
    <th style="text-align: left; width:10%">Cookie</th>
    <th style="text-align: left; width:10%">Duration</th>
    <th style="text-align: left; width:30%">Description</th>
    <th style="text-align: left; width:20%">Sample value</th>
    <th style="text-align: left; width:10%">Path</th>
    <th style="text-align: left; width:10%">HttpOnly</th>
    <th style="text-align: left; width:10%">SameSite</th>
</tr>
</thead>
<tbody>
<tr style="text-align: left;">
    <td>PRLST</td>
    <td>Session</td>
    <td>
    <ul><li>Created by the <code>Set-Cookie</code> response header.</li>
    <li>Gets the value from injected JavaScript.</li>
    <li>The value contains a unique ID of the requested page.</li>
    </ul>
    </td>
    <td>AV</td>
    <td>/</td>
    <td></td>    
    <td>Lax</td>
</tr>
<tr style="text-align: left;">
    <td>SPSI</td>
    <td>Session</td>
    <td>
    <ul>
    <li>Created by the <code>Set-Cookie</code> response header.</li>
    <li>Contains the <code>sessionID</code> value.</li>
    </ul></td>
    <td>4e1ed32a27577bd95612f973777f8c3d</td>
    <td>/</td>
    <td>V</td>    
    <td>Lax</td>
</tr>
<tr style="text-align: left;">
    <td>UTGv2</td>
    <td>Persistent</td>
    <td>
    <ul>
    <li>User tag token, a unique identifier of behavior on a domain.</li>
    <li>Created by the <code>Set-Cookie</code> response header.</li>
    <li>Gets values from injected JavaScript.</li>
    <li>Contains the <code>usertag</code> value.</li>
    <li>Unique to browser and domain.</li></ul></td>
    <td>h4c5f3ab2d0ea64a63234ae2df4417f2d145</td>
    <td>/</td>
    <td></td>
    <td>Lax</td>    
</tr>
<tr style="text-align: left;">
    <td>spcsrf</td>
    <td>Immediately</td>
    <td>elated to the CSRF protection module.</td>
    <td>e98c27a664bbd73bd1b55be5a0f753eb</td>
    <td>/</td>
    <td>V</td>    
    <td>Strict</td>
</tr>
<tr style="text-align: left;">
    <td>cnfc</td>
    <td>Immediately</td>
    <td>CAPTCHA client-side cookie.</td>
    <td></td>
    <td>/</td>
    <td></td>    
    <td>Lax</td>
</tr>
<tr style="text-align: left;">
    <td>pvstr</td>
    <td>Immediately</td>
    <td>CAPTCHA client-side cookie.</td>
    <td></td>
    <td>/</td>
    <td></td>    
    <td>Lax</td>
</tr>
<tr style="text-align: left;">
    <td>SPC</td>
    <td>4 days</td>
    <td>Cookie related to CAPTCHA validation.</td>
    <td>G5g+JHlalFD1U0ZibWbs57jWH7h0cUNTagGqnvbxA5XjJ3I/WhkqS4X6dx 
ysiXNrjFBsJDcJqVRg+bqjiarVGVtO6fKYBBEBlW+Ik/PBRLTHwPeZlFAmW 
zECQ/lhv7rOBsNCJFCBRlnJ+qgFuWQHOg==</td>
    <td>/</td>
    <td>V</td>    
    <td>Lax</td>
</tr>
<tr style="text-align: left;">
    <td>sbtsck</td>
    <td>1 day</td>
    <td>Cookie related to CAPTCHA and JavaScript validation.</td>
    <td>javiVOxxF5xj9D1HJ62QVzjeM3I84j8KYF1VF7iS+uEoWE= </td>
    <td>/</td>
    <td></td>    
    <td>Lax</td>
</tr>
<tr style="text-align: left;">
    <td>DCSS</td>
    <td>Session </td>
    <td>Cookie related to DDoS protection.</td>
    <td>F1046F5C84F1047ED441475A38AB15917B210EE </td>
    <td>/</td>
    <td></td>    
    <td>Lax</td>
</tr>
<tr style="text-align: left;">
    <td>DGCC</td>
    <td>1 day</td>
    <td>Cookie related to DDoS protection.</td>
    <td>ps</td>
    <td>/</td>
    <td></td>    
    <td>Lax</td>
</tr>
<tr style="text-align: left;">
    <td>DSR</td>
    <td>Session</td>
    <td>Cookie related to DDoS protection.</td>
    <td>jyRENJbozdn/oyQae70NAYfKSeufcz4tPfbyMhLCOysLU3/FNaYu06nS01 
7SdLejOhXriDKOU2X/uLUCZaBb2Q==</td>
    <td>/</td>
    <td></td>    
    <td>Lax</td>
</tr>
<tr style="text-align: left;">
    <td>DCST</td>
    <td>Session</td>
    <td>Cookie related to DDoS protection.</td>
    <td>pE9</td>
    <td>/</td>
    <td>V</td>    
    <td>Lax</td>
</tr>
<tr style="text-align: left;">
    <td>SPSE</td>
    <td>Session</td>
    <td>Created by the <code>Set-Cookie</code> response header.</td>
    <td>Eko0ihLuM2ND530rxn6S07NWKAWS3wW89XYxX3VbjVnFhREKfgyRAN 
3ttUFROFQqIpi+kmdrla9jH7EaII0nnA==</td>
    <td>/</td>
    <td>V</td>    
    <td>Lax</td>
</tr>
<tr style="text-align: left;">
    <td>SPLB</td>
    <td></td>
    <td>Cookie related to load balancing.</td>
    <td></td>
    <td>/</td>
    <td></td>    
    <td>Lax</td>
</tr>
<tr style="text-align: left;">
    <td>sp_lit</td>
    <td>5 minutes</td>
    <td>
    <ul>
    <li>Session-related cookie.</li>
    <li>Created by the <code>Set-Cookie</code> response header.</li>
    <li>Gets values from injected JavaScript.</li>
    </ul></td>
    <td>gFYBNNtE+xA+GebbXECksQ==</td>
    <td>/</td>
    <td>V</td>    
    <td>Strict</td>
</tr>
</tbody>
</table>

## Storage variables 

The following table contains a list of local storage variables that are used to save key/value pairs in a web browser. These variables are not cookies. 

<table>
<thead>
<tr>
    <th style="text-align: left;">Variable</th>
    <th style="text-align: left;">Description</th>
    <th style="text-align: left;">Sample value</th>
</tr>
</thead>
<tbody>
<tr style="text-align: left;">
    <td>cnv</td>
    <td>CAPTCHA-related local storage data.</td>
    <td>51507208066</td>
</tr>
<tr style="text-align: left;">
    <td>csr</td>
    <td>CAPTCHA-related local storage data.</td>
    <td>RSNBLPNDACD</td>
</tr>
<tr style="text-align: left;">
    <td>otr</td>
    <td>Shell mouse script-related local storage data.</td>
    <td>cfc3f5050e9</td>
</tr>
<tr style="text-align: left;">
    <td>altutgv2 </td>
    <td>A variable related to the user tag token. Contains local storage data.</td>
    <td>h4d73db3157e44edb918eea80571a69f2776</td>
</tr>
</tbody>
</table>