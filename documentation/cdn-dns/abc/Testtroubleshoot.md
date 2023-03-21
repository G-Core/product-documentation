---
title: Troubleshoot IPMI errors
displayName: Troubleshooting
published: true
order: 3
---
<h4 id="h_01F3M5PW0DPE30164P0C3CATNW">&nbsp;</h4>
<table style="border-collapse: collapse; height: 80px; width: 100%;">
  <tbody>
    <tr>
      <td style="width: 100%;">
        <a href="#h_01F3M5JGH6S87GJSZ6QQ182YWJ" target="_self">The fields "login" and "password" are not filled in automatically</a><span style="font-weight: 400;"><br></span>
      </td>
    </tr>
    <tr style="height: 20px;">
      <td style="width: 100%; height: 20px;">
        <a href="#h_01F3M5JPP2ZK816VNK0W0FC91H" target="_self"><span style="font-weight: 400;">Error "Server disconnected: (code: 1006)"</span></a>
      </td>
    </tr>
    <tr style="height: 20px;">
      <td style="width: 100%; height: 20px;">
        <a href="#h_01F3M5JYRTQXDJZBZRQE0464AY" target="_self"><span style="font-weight: 400;">Error "IPMI URL ... of selected server is not available"</span></a>
      </td>
    </tr>
    <tr style="height: 20px;">
      <td style="width: 100%; height: 20px;">
        <p class="article-title" title="IPMI. Remote Console in IPMI does not open">
          <a href="#h_01GVR8CQS4DR8762X4D7HJ96H0" target="_self">Remote Console in IPMI does not open</a>
        </p>
      </td>
    </tr>
  </tbody>
</table>
<h4 id="h_01F3M5PW0DPE30164P0C3CATNW">
  <span style="font-weight: 400;">You may encounter various errors when logging into IPMI. We will tell you what to do in each case.</span>
</h4>
<h2 id="h_01F3M5JGH6S87GJSZ6QQ182YWJ">
  <span style="font-weight: 400;">The fields "login" and "password" are not filled in automatically</span>
</h2>
<p>
  <span style="font-weight: 400;">Usually, it’s not needed to type username and password manually. They will be filled in automatically if you click on the field and then on the appropriate button in a corner of the screen.</span>
</p>
<p>
  <span style="font-weight: 400;"><img src="/hc/article_attachments/360019142778/1_eng.bmp" alt="1_eng.bmp"></span>
</p>
<p>
  <span style="font-weight: 400;">If autocomplete doesn't work, try to enter data manually. You can find your login and password in </span><a href="https://support.gcorelabs.com/hc/en-us/articles/115003759869" target="_self"><span style="font-weight: 400;">DCImanager </span></a><span style="font-weight: 400;">— point the mouse cursor to a monitor icon, and you will see the login information.</span>
</p>
<p>
  <span style="font-weight: 400;"><img src="/hc/article_attachments/360019091997/2eng.bmp" alt="2eng.bmp"><br></span>
</p>
<p>
  <span style="font-weight: 400;">Even if you managed to log in with manual data entering, </span><a href="https://support.gcorelabs.com/hc/en-us/articles/115003753885" target="_self"><span style="font-weight: 400;">write to technical support</span></a>
  <span style="font-weight: 400;">— we will repair fields autocomplete. If you can't log in, contact support too. We will help to establish a connection to IPMI.</span>
</p>
<h2 id="h_01F3M5JPP2ZK816VNK0W0FC91H">
  <span style="font-weight: 400;">Error "Server disconnected: (code: 1006)"</span>
</h2>
<p>
  <span style="font-weight: 400;">This error appears when two sessions with IPMI are opened simultaneously — for example, when you connect from two devices or from different tabs of the browser.</span>
</p>
<p>
  <span style="font-weight: 400;"><img src="/hc/article_attachments/360019067117/3.png" alt="3.png"></span>
</p>
<p>
  <span style="font-weight: 400;">When you see the error 1006, try doing four things in turn:</span>
</p>
<ol>
  <li style="font-weight: 400;" aria-level="1">
    <span style="font-weight: 400;">Check if you have two open tabs with IPMI. If so, close one of them and work with IPMI from another</span>
  </li>
  <li style="font-weight: 400;" aria-level="1">
    <span style="font-weight: 400;">Close your current browser, open another and connect to IPMI through it</span>
  </li>
  <li style="font-weight: 400;" aria-level="1">
    <span style="font-weight: 400;">Clear browser cookies and connect to IPMI</span>
  </li>
  <li style="font-weight: 400;" aria-level="1">
    <span style="font-weight: 400;">Connect to IPMI from another device — for example, from a mobile</span>
  </li>
</ol>
<p>
  <span style="font-weight: 400;">If none of these methods helped, </span><a href="https://support.gcorelabs.com/hc/en-us/articles/115003753885" target="_self"><span style="font-weight: 400;">write to technical support</span></a><span style="font-weight: 400;"> — we will make IPMI work again. Please inform our support that you have done all the steps from the article: we will immediately understand what the matter is, and will not ask you to connect to IPMI in different ways.</span>
</p>
<h2 id="h_01F3M5JYRTQXDJZBZRQE0464AY">
  <span style="font-weight: 400;">Error "IPMI URL ... of selected server is not available"</span>
</h2>
<p>
  <span style="font-weight: 400;">This error occurs when the server fails or when emergency or planned work is taking place in the location.</span>
</p>
<p>
  <span style="font-weight: 400;"><img src="/hc/article_attachments/360019119238/4.png" alt="4.png"></span>
</p>
<p>
  <span style="font-weight: 400;">If you experience this error, </span><a href="https://support.gcorelabs.com/hc/en-us/articles/115003753885" target="_self"><span style="font-weight: 400;">write to technical support</span></a><span style="font-weight: 400;"> — we will help to establish a connection to IPMI. When writing the message, please attach a copy of the error description or a screenshot of the screen: it will help us to understand what the matter is.</span>
</p>
<h2 id="h_01GVR8CQS4DR8762X4D7HJ96H0" class="article-title" title="IPMI. Remote Console in IPMI does not open">Remote Console in IPMI does not open</h2>
<p>Connection failed Error</p>
<p>
  <img src="/hc/article_attachments/13832346165777" alt="mceclip0.png">
</p>
<p>
  - make the KVM reset. In the IPMI panel, open the «Maintenance» menu and choose
  «IKVM Reset».<br>
  - make the Unit reset. In the IPMI panel, open the «Maintenance» menu and choose
  «Unit Reset».
</p>
<p id="id-[G-Host]СложностисRemoteconsoleвIPMI-3)Какоткрытьконсольнавесьэкран?">
  <span class="wysiwyg-font-size-large">How to run full-screen mode?</span>
</p>
<p>
  Open IPMI and click Options --&gt; Full-Screen Mode. To return, press F3.
</p>
<p>
  <span class="wysiwyg-font-size-large">How to switch between browser and console?&nbsp;</span>
</p>
<p id="id-[G-Host]СложностисRemoteconsoleвIPMI-2)Какпереключатьсямеждубраузеромиконсолью?">
  IPMI doesn't support switching between browser and console. The Remote console
  shuts down after clicking on browser, and you need to restart it.
</p>