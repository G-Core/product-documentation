---
title: troubleshoot-ipmi-errors
displayName: IPMI
published: true
order: 10
toc:
   --1--The fields "login" and "password" are not filled in automatically: "the-fields-login--and--password--are-not-filled-in-automatically"
   --1--Error "Server disconnected (code 1006)": "error-server-disconnected--code-1006"
   --1--Error "IPMI URL ... of selected server is not available": "error-ipmi-url-----of-selected-server-is-not-available"
   --1--Remote Console in IPMI does not open: "remote-console-in-ipmi-does-not-open"
---
  

#### You may encounter various errors when logging into IPMI. We will tell you what to do in each case.

The fields "login" and "password" are not filled in automatically
-----------------------------------------------------------------

Usually, it’s not needed to type username and password manually. They will be filled in automatically if you click on the field and then on the appropriate button in a corner of the screen.

<img src="https://support.gcore.com/hc/article_attachments/360019142778/1_eng.bmp" alt="1_eng.bmp">

If autocomplete doesn't work, try to enter data manually. You can find your login and password in [DCImanager](https://support.gcorelabs.com/hc/en-us/articles/115003759869) — point the mouse cursor to a monitor icon, and you will see the login information.

<img src="https://support.gcore.com/hc/article_attachments/360019091997/2eng.bmp" alt="2eng.bmp">  

Even if you managed to log in with manual data entering, [write to technical support](https://support.gcorelabs.com/hc/en-us/articles/115003753885) — we will repair fields autocomplete. If you can't log in, contact support too. We will help to establish a connection to IPMI.

Error "Server disconnected: (code: 1006)"
-----------------------------------------

This error appears when two sessions with IPMI are opened simultaneously — for example, when you connect from two devices or from different tabs of the browser.

<img src="https://support.gcore.com/hc/article_attachments/360019067117/3.png" alt="3.png">

When you see the error 1006, try doing four things in turn:

1.  Check if you have two open tabs with IPMI. If so, close one of them and work with IPMI from another
2.  Close your current browser, open another and connect to IPMI through it
3.  Clear browser cookies and connect to IPMI
4.  Connect to IPMI from another device — for example, from a mobile

If none of these methods helped, [write to technical support](https://support.gcorelabs.com/hc/en-us/articles/115003753885) — we will make IPMI work again. Please inform our support that you have done all the steps from the article: we will immediately understand what the matter is, and will not ask you to connect to IPMI in different ways.

Error "IPMI URL ... of selected server is not available"
--------------------------------------------------------

This error occurs when the server fails or when emergency or planned work is taking place in the location.

<img src="https://support.gcore.com/hc/article_attachments/360019119238/4.png" alt="4.png">

If you experience this error, [write to technical support](https://support.gcorelabs.com/hc/en-us/articles/115003753885) — we will help to establish a connection to IPMI. When writing the message, please attach a copy of the error description or a screenshot of the screen: it will help us to understand what the matter is.

Remote Console in IPMI does not open
------------------------------------

Connection failed Error

<img src="https://support.gcore.com/hc/article_attachments/13832346165777" alt="mceclip0.png">

\- make the KVM reset. In the IPMI panel, open the «Maintenance» menu and choose «IKVM Reset».  
\- make the Unit reset. In the IPMI panel, open the «Maintenance» menu and choose «Unit Reset».

How to run full-screen mode?

Open IPMI and click Options --> Full-Screen Mode. To return, press F3.

How to switch between browser and console? 

IPMI doesn't support switching between browser and console. The Remote console shuts down after clicking on browser, and you need to restart it.