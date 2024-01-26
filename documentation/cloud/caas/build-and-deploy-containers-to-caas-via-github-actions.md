---
title: build-and-deploy-containers-to-caas-via-github-actions
displayName: Deploy via GitHub actions
published: true
order: 20
toc:
   --1--Overview: "overview"
   --1--GitHub actions: "github-actions"
   --1--Use: how-to-use-the-gcore-action"
pageTitle: Learn to Deploy Containers to Gcore CaaS via GitHub Actions | Gcore
pageDescription: Comprehensive guide to deploying containers to Gcore's Container as a Service directly using GitHub Actions.
---
# Build and deploy containers to CaaS via GitHub actions

## Overview

We've developed a public GitHub action that allows you to deploy your containers to <a href="https://gcore.com/docs/cloud/caas" target="_blank">Gcore Container as a Service</a> directly via GitHub workflows. This action can be found in the <a href="https://github.com/gcore-github-actions/deploy-container" target="_blank">deploy-container repository</a> repository and in the Marketplace under <a href="https://github.com/marketplace/actions/deploy-to-gcore-container-as-a-service" target="_blank">GitHub Actions</a>.

## GitHub actions

The principle of actions is described in the <a href="https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions" target="_blank">detailed GitHub documentation</a>. You create a YAML file in your repository's *.github/workflows* directory. This YAML file contains the code that is executed during a workflow run. Other key components of GitHub Actions include:

- **Events** that trigger workflows (e.g., pull_request).
- **Jobs** that define the steps that will be executed on the runner or actions that will be run.
- **Actions**, which are applications (<a href="https://github.com/marketplace?type=actions" target="_blank">GitHub actions</a>) that contain repeating code for simplification.
- **Runners**, which are servers where workflows are executed. 

## How to use the Gcore action

1\. In the *.github/workflows/* directory, create a file with the *.yml* extension.

2\. Add the following content to your *.yml* file: 

```
name: Deploy

on:
  workflow_dispatch:

jobs:
  deploy:
    name: deploy
    runs-on: ubuntu-latest

    steps:
      - id: deploy
        uses: gcore-github-actions/deploy-container@v1
        with:
          api-token: ${{ secrets.GCLOUD_API_TOKEN }}
          project-id: ${{ vars.GCLOUD_PROJECT }}
          region-id: ${{ vars.GCLOUD_REGION }}
          name: my-container
          image: nginx:latest

      - name: Use output
        run: echo "${{ steps.deploy.outputs.address }}"
```

Where there are required and optional fields.

**Required fields**:

- ```api-token``` is a <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">permanent API token</a> that authenticates the GitHub action to Gcore API.
- ```project-id``` is the ID of the Gcore project where the container should be deployed. You can use the <a href="https://api.gcore.com/docs/cloud#tag/Projects/operation/ProjectListViewSet.get" target="_blank">list projects</a> API request to retrieve this.
- ```region-id``` is the ID of the region where the container should be deployed. This can be obtained using the <a href="https://api.gcore.com/docs/cloud#tag/Regions/operation/RegionHandler.get" target="_blank">list regions</a> API request.
- ```name``` is the name of the container to be deployed.
- ```image``` in the name of the container image to be deployed (e.g., *docker.io/nginx:latest*).

**Optional fields**:

- ```listening-port``` is the port on which the container will be listening for network connections. The default value is ```80```.
- ```description``` is a custom description of the container.
- ```envs``` is the list of newline-separated - key-value pairs to set as environment variables. For example:

```
with:
   envs: |
     FOO=bar
     BAZ=biz
```

- ```flavor``` is the container flavor that determines the amount of memory and CPU allocated to each container instance. The default value is ```80mCPU-128MB```.
- ```timeout``` is the duration in seconds to wait before scaling down container instances. The default value is ```60```.
- ```scale-min``` is the minimum number of instances to run. When set to ```0```, the container will scale down to zero running instances when it receives no traffic for the duration of ```timeout```. The default value is ```1```.
- ```scale-max``` is the maximum number of instances to run. The value must be greater than or equal to scale-min. The default value is ```1```.
- ```is-disabled``` is the field (boolean) that controls the state of the container (on or off). When ```true``` is set, the container is disabled, and any running instances are shut down. The default value is ```false```.
- ```is-api-key-auth``` is the field (boolean) that enables API key authentication for the container endpoint address. You can create and assign API keys to the container in the Gcore Customer Portal. When ```true``` is set, API keys are enabled. The default value is ```false```.
- ```pull-secret``` is the name of the private registry credentials to use when fetching the container image. The credentials must already be configured in the Gcore Customer Portal.

3\. Create a *.secrets* file with your ```GCLOUD_API_TOKEN``` value obtained from the <a href="https://accounts.gcore.com/profile/api-tokens" target="_blank">Customer Portal</a>.

4\. Create a *.vars* file with your ```GCLOUD_API_URL```, ```GCLOUD_PROJECT``` and ```GCLOUD_REGION``` values.

The Gcore action has the following output elements:

- ```address``` is the endpoint address of your container.
- ```status``` is the status of your container (e.g., *Pending*, *Deploying*, *Ready*, or *Error*).
- ```status-message``` is the last message associated with the current container status. This can be useful for troubleshooting deployment issues.