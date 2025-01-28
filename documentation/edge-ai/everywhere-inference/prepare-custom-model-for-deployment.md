---
title: prepare-custom-model-for-deployment
displayName: Prepare a custom model for deployment
order: 5
published: true
toc:
--1-- Ensure a model is trained and optimized: "step-1-ensure-your-model-is-trained-and-optimized-for-inference"
--1--Step 2. Containerize a model: "step-2-containerize-a-model"
--1--Step 3. Build, tag, and push: "step-3-build-tag-and-push-an-image"
--1--Step 4. Deploy the model: "step-4-deploy-the-model"
pageTitle: Prepare a custom AI model for deployment in the Gcore Customer Portal | Gcore
pageDescription: Learn how to prepare and build an image with a custom AI model for deployment on inference nodes.
---
# Prepare a custom AI model for deployment

If you want to run a custom AI model on Gcore inference nodes, refer to the following guidelines.

While we don’t have any specific requirements for model packaging or its dependencies, this guide will help you get a general understanding of the key steps you should complete before deploying your model to our Customer Portal.

## Step 1. Ensure your model is trained and optimized for inference

Your model should be properly trained, validated, and tested.

Fine-tuning an AI model is essential to ensure that it makes accurate and reliable predictions.

## Step 2. Containerize a model

To ensure consistent deployment of your model across different environments, you need to package the model into a container image.

There are no specific requirements for building a container image or its dependencies. You only need to ensure that it’s compliant with the image registry standards. For example, if you’re using <a href="https://www.docker.com/" target="_blank">Docker</a>, you need to prepare a `Dockerfile` with your AI model.

If you need more general information about Docker and its setup for running AI models, read the <a href="https://github.com/saikhu/Docker-Guide-for-AI-Model-Development-and-Deployment" target="_blank">Docker guide for AI development and deployment</a>.

Here’s an example of a `Dockerfile` configuration:

```
# Set the base image your model is built from  
FROM python:3.11-slim

# Set the working directory inside a container 
WORKDIR /app

# Set environment variables 
ENV USE_TORCH=1
ENV NVIDIA_VISIBLE_DEVICES=all 
ENV CLI_ARGS=""

# Install any required dependencies 
pip install -r requirements.txt

# Install Python packages 
RUN pip3 install onnxruntime flask 

# Copy the model into the container 
COPY my_model.onnx /app/my_model.onnx

# Copy your inference script 
COPY inference.py /app/inference.py 

# Expose the port the app runs on 
EXPOSE 5000</span>

# Run the application 
CMD ["python3", "inference.py"]
```

<alert-element type="tip" title="Tip">

For a full list of `Dockerfile` requirements and supported syntax, check the <a href="https://docs.docker.com/reference/dockerfile/" target="_blank">official Docker documentation</a>.

</alert-element>

## Step 3. Build, tag, and push an image

The image with your AI model must be built for the x86-64(AMD64) architecture. Apart from this compatibility requirement, we have no specific constraints on the structure or organization of your container image.

The following steps demonstrate how to build, tag, and push a <a href="https://docs.docker.com/guides/docker-concepts/building-images/build-tag-and-publish-an-image/" target="_blank">Docker image</a>:

1\. If you’re building a Docker image on Apple Silicon machines, use the following command:

`docker buildx build --platform linux/amd64` instead of `docker build`

2\. Tag the image: `docker image tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]`

3\. Push the image to the registry: `docker push my-username/my-image`

## Step 4. Deploy the model

After you’ve built and pushed a Docker image with your AI model, <a href="https://gcore.com/docs/cloud/everywhere-inference/deploy-ai-model" target="_blank">deploy it on edge inference nodes</a> in the Gcore Customer Portal.
