---
title: http-status-codes
displayName: HTTP status codes
published: true
order: 20
pageTitle: Video Streaming HTTP Status Codes | Gcore
pageDescription: An explanation of the HTTP status codes returned when requesting videos and live streams for manifests or chunks.
---

# Video Streaming HTTP Status Codes

The following table includes all possible HTTP status codes returned when requesting videos and live streams for manifests (e.g., .m3u8 and .mpd) or chunks (e.g., .ts, .mp4, etc.).

<table>
<thead>
  <th>Code</th><th>Status</th><th>Description</th>
</thead>
<tbody>
  <tr>
    <td>200</td>
    <td>OK</td>
    <td>All OK</td>
  </tr>
  <tr>
    <td>403</td>
    <td>Forbidden</td>
    <td>Access is denied. If you use any distribution restriction such as geo-restriction or token, you must satisfy this condition for access.</td>
  </tr>
  <tr>
    <td>404</td>
    <td>Not Found</td>
    <td>There's no requested video, or the live stream is temporarily not delivering chunks. Check the request link or activate your video.<br/>For Live streams in CMAF format, you can check the extra header "X-Err-Code":<ul><li>1000 – Master-stream is missed. The stream is not pushed or not transcoded, so start a stream or restart transcoding.</li><li>2000 – Invalid StreamID. The identifier is not parsed from the requested URL; check the URL.</li><li>3000 – Stream is not ready for delivery. Inspect the logs or contact support. Oftentimes, this happens when the master-stream has wrong parameters, such as video and audio codecs, FPS, or bitrate. Verify the parameters to ensure everything works as expected. </li></ul>
    </td>
  </tr>
  <tr>
    <td>422</td>
    <td>Unprocessable Content</td>
    <td>This is advanced functionality (e.g., custom encoding presets). To enable it, contact your manager or the support team.</td>
  </tr>
  <tr>
    <td>500</td>
    <td>Internal Server Error</td>
    <td>An unexpected issue happened on the server. This may be a local error in a specific video. In this case, check the video processing status in your personal account. If the error is global, the information will be on the status page.</td>
  </tr>
  <tr>
    <td>502</td>
    <td>Bad Gateway</td>
    <td>An unexpected issue happened on the server. This may happen when VOD or Live can't be delivered over CDN because an incorrect response was received from an origin (storage or live transcoder). In this case, check the video processing status or live stream transcoding in your personal account. If the error is global, the information will appear on the status page.</td>
  </tr>
  <tr>
    <td>503</td>
    <td>Service Unavailable</td>
    <td>An unexpected issue happened on the server. This may be a local error in a specific video. In this case, check the video processing status in your personal account. If the error is global, the information will be on the status page.</td>
  </tr>
  <tr>
    <td>504</td>
    <td>Gateway Time-out</td>
    <td>Timeout for receiving data from the source. Try checking the status of video sending/ingesting and transcoding.</td>
  </tr>
</tbody>
</table>

<alert-element type="info" title="Info">
 
The system health status page is available at [https://status.gcore.com/](https://status.gcore.com/)
 
</alert-element>
