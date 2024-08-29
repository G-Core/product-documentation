---
title: use-annotations-for-load-balancers
displayName: Annotations
published: true
order: 40
toc:
   --1--Add DDoS profile: "ddos-profile"
   --1--Name flavor: "flavor"
   --1--Clean up floating IP: "floating-cleanup"
   --1--Set topic name for logging (mandatory): "logging-topic-name"
   --1--Set region ID for logging (mandatory): "logging-destination-region-id"
   --1--Set retention policy for logging: "logging-retention-policy-period"
   --1--Enable proxy for listeners: "proxy-protocol"
   --1--Set client data timeouts: "timeout-client-data"
   --1--Set member connect timeouts: "timeout-member-connect"
   --1--Set member data timeouts: "timeout-member-data"
   --1--Add X-Forwarded headers: "x-forwarded-for"
   --1--Make Load Balancer non-public: "gcore-internal-load-balancer"
   --1--Make Load Balancer public: "gcore-external-load-balancer"
   --1--Examples: "examples"
pageTitle: Optimizing Kubernetes Clusters with Load Balancer Annotations | Gcore
pageDescription: Discover how to enhance your Kubernetes clusters using Gcore service Load Balancer annotations.
---
# Use annotations for Load Balancers

Annotations are a way to add custom, non-identifiable metadata to objects. They are used to configure additional behavior for Load Balancers service in <a href="https://gcore.com/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster" target="_blank">Kubernetes clusters</a> beyond the standard configuration offerings. Learn more about annotations in the <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/" target="_blank">official Kubernetes documentation</a>. 

You can add annotations via the <a href="https://kubernetes.io/docs/reference/kubectl/generated/kubectl_annotate/" target="_blank">command line (kubectl)</a> or the Kubernetes service manifest using the annotations field as follows:

```
metadata: {
 annotations: {
   key: "value"
 }
}
```

Below, we have compiled annotations that apply to clusters created in Gcore:

<table>
    <thead>
        <tr>
            <th>Key (annotation)</th>
            <th>Value sample</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: left" id="ddos-profile"><code>loadbalancer.gcorelabs.com/<br>ddos-profile</code></td>
            <td style="text-align: left"><code>{ "profile_template":65,<br> "fields": [{ "base_field":272,<br> "field_value":40 }] }</code></td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">Configures and ads the DDoS Protection profile to the Load Balancer</td>
        </tr>
        <tr>
            <td style="text-align: left" id="flavor"><code>loadbalancer.gcorelabs.com/<br>flavor</code></td>
            <td style="text-align: left"><code>lb1-1-2</code></td>
            <td style="text-align: left">String</td>
            <td style="text-align: left">Specifies a custom name for the flavor</td>
        </tr>
        <tr>
            <td style="text-align: left" id="floating-cleanup"><code>loadbalancer.gcorelabs.com/<br>floating-cleanup</code></td>
            <td style="text-align: left"><code>true</code></td>
            <td style="text-align: left">Boolean</td>
            <td style="text-align: left">Automatically cleans up the floating IP assigned to the Load Balancer after deleting the service</td>
        </tr>
        <tr>
            <td style="text-align: left" id="logging-topic-name"><code>loadbalancer.gcorelabs.com/<br>logging-topic-name</code></td>
            <td style="text-align: left"><code>topic-123</code></td>
            <td style="text-align: left">String</td>
            <td style="text-align: left">Specifies <a href="https://gcore.com/docs/cloud/logging-as-a-service/about-logging-as-a-service" target="_blank">LaaS</a> topic name for pushing logs.<br><b>Note:</b> Must be used with the logging-destination-region-id, otherwise logs won’t be sent to LaaS </td>
        </tr>
        <tr>
            <td style="text-align: left" id="logging-destination-region-id" style="text-align: left"><code>loadbalancer.gcorelabs.com/<br>logging-destination-region-id</code></td>
            <td style="text-align: left"><code>1</code></td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">Specifies <a href="https://gcore.com/docs/cloud/logging-as-a-service/about-logging-as-a-service" target="_blank">LaaS</a> destination region.<br> <b>Note:</b> Must be used with the logging-topic-name, otherwise logs won’t be sent to LaaS </td>
        </tr>
        <tr>
            <td style="text-align: left" id="logging-retention-policy-period"><code>loadbalancer.gcorelabs.com/<br>logging-retention-policy-period</code></td>
            <td style="text-align: left"><code>45</code></td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">Configures log retention policy for LaaS topic (in days)</td>
        </tr>
        <tr>
            <td style="text-align: left" id="proxy-protocol"><code>loadbalancer.gcorelabs.com/<br>proxy-protocol</code></td>
            <td style="text-align: left"><code>true</code></td>
            <td style="text-align: left">Boolean</td>
            <td style="text-align: left">Enables proxy protocol type for <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer#listener" target="_blank">Load Balancer listeners</a></td>
        </tr>
        <tr>
            <td style="text-align: left" id="timeout-client-data"><code>loadbalancer.gcorelabs.com/<br>timeout-client-data</code></td>
            <td style="text-align: left"><code>6000</code></td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">Sets client data timeouts for <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer#timeouts" target="_blank">Load Balancer listeners</a> (in msec). <br><b>Note:</b> When removed, the previously set value in effect</td>
        </tr>
        <tr>
            <td style="text-align: left" id="timeout-member-connect"><code>loadbalancer.gcorelabs.com/<br>timeout-member-connect </code></td>
            <td style="text-align: left"><code>6000</code></td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">Sets member connect timeouts for <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer#timeouts" target="_blank">Load Balancer listeners</a> (in msec). <br><b>Note:</b> When removed, the previously set value in effect</td>
        </tr>
        <tr>
            <td style="text-align: left" id="timeout-member-data"><code>loadbalancer.gcorelabs.com/<br>timeout-member-data</code></td>
            <td style="text-align: left"><code>6000</code></td>
            <td style="text-align: left">Integer</td>
            <td style="text-align: left">Sets member data timeouts for <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer#timeouts" target="_blank">Load Balancer listeners</a> (in msec). <br><b>Note:</b> When removed, the previously set value in effect</td>
        </tr>
        <tr>
            <td style="text-align: left" id="x-forwarded-for"><code>loadbalancer.gcorelabs.com/<br>x-forwarded-for</code></td>
            <td style="text-align: left"><code>true</code></td>
            <td style="text-align: left">Boolean</td>
            <td style="text-align: left">Adds the “X-Forwarded-For,” “X-Forwarded-Port” and “X-Forwarded-Proto“ headers to requests</td>
        </tr>
        <tr>
            <td style="text-align: left" id="gcore-internal-load-balancer"><code>service.beta.kubernetes.io/<br>gcore-internal-load-balancer</code></td>
            <td style="text-align: left"><code>true</code></td>
            <td style="text-align: left">Boolean</td>
            <td style="text-align: left">Disables floating IP creation and makes the Load Balancer non available for external requests</td>
        </tr>
        <tr>
            <td style="text-align: left" id="gcore-external-load-balancer"><code>service.beta.kubernetes.io/<br>gcore-external-load-balancer</code></td>
            <td style="text-align: left"><code>true</code></td>
            <td style="text-align: left">Boolean</td>
            <td style="text-align: left">Makes the Load Balancer public</td>
        </tr>
    </tbody>
</table>

## Examples

Here, several examples of annotations using are presented. 

To assign an Advanced DDoS protection profile to your cluster, use the following code in the manifest: 

```
apiVersion: v1
kind: Service
metadata:
  annotations:
    loadbalancer.gcorelabs.com/ddos-profile: |
  {"profile_template":65,"fields":[{"base_field":272,"field_value":40}]}
  labels:
    app: grafana
  name: grafana
  namespace: default
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: grafana
  type: LoadBalancer
```

Instead of the sample values (```65```, ```272```, and ```40```), use the appropriate values for your project. The value format is the same as supported by the public <a href="https://api.gcore.com/docs/cloud#tag/DDOS-Protection" target="_blank">DDoS Protection API</a>. 

To enable logging for your cluster, use the following one:  

```
apiVersion: v1
kind: Service
metadata:
  annotations:
    loadbalancer.gcorelabs.com/logging-topic-name: test123
    loadbalancer.gcorelabs.com/logging-destination-region-id: 15
  labels:
    app: grafana
  name: grafana
  namespace: default
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: grafana
  type: LoadBalancer
```

Instead of the sample values (```test123``` and ```15```), use the appropriate values for your project.  