---
title: prepare-a-custom-ai-model-for-deployment
displayName: Prepare a custom AI model for deployment
published: true
order: 
toc:
  --1-- Train, test, and optimize the model for inference: "train-test-and-optimize-the-model-for-inference"
  --1-- Containerize the model: "containerize-the-model"
  --1-- Build, tag, and publish the image: "build-tag-and-publish-the-image"
pageTitle: Edge AIeverywhere Inference—Prepare a custom AI model for deployment | Gcore
pageDescription: Learn how to get started with Gcore Edge AI services.
---
# Prepare a custom AI model for deployment

While we don’t have any specific requirements for model packaging or its dependencies, this guide will help you understand the steps you should take the following tips into account before deploying an AI model to Everywhere Inference.

## Train, test, and optimize the model for inference

The model should be properly trained, validated, and tested. Fine-tuning an AI model is essential to help ensure that it makes accurate and reliable predictions.

## Containerize the model

Package the model into a container image for consistent deployment across different environments. There are no specific requirements for building a container image or its dependencies. You only need to make sure it complies with the image registry standards. For example, if you’re using [Docker](https://www.docker.com/), you must prepare a Dockerfile with your AI model.

If you need more general information about Docker and its setup for running AI models, read [the Docker guide for AI development and deployment](https://github.com/saikhu/Docker-Guide-for-AI-Model-Development-and-Deployment).

Here’s an example of a Dockerfile configuration:

```
# Set the base image the model is built from
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
EXPOSE 5000&lt;/span&gt;

# Run the application
CMD \["python3", "inference.py"\]
```

<alert-element type="tip" title="Tip">
For a full list of Dockerfile requirements and supported syntax, check the [official Docker documentation](https://docs.docker.com/reference/dockerfile/).
</alert-element>

## Build, tag, and publish the image

The image with your AI model must be built for the x86-64(AMD64) architecture. Apart from this compatibility requirement, we have no specific constraints on the structure or organization of your container image.

The following steps explain how to build, tag, and publish a [Docker image](https://docs.docker.com/guides/docker-concepts/building-images/build-tag-and-publish-an-image/):

1\. If you’re building a Docker image on Apple Silicon machines, use the following command:

```
docker buildx build --platform linux/amd64 instead of docker build
```

2\. Tag the image:

```
docker image tag SOURCE_IMAGE\[:TAG\] TARGET_IMAGE\[:TAG\]
```

3\. Push the image to the registry:

```
docker push my-username/my-image
```
