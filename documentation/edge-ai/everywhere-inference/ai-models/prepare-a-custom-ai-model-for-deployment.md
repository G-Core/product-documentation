---
title: prepare-a-custom-ai-model-for-deployment
displayName: Prepare a custom AI model for deployment
published: true
order: 1
toc:
  --1-- Train, test, and optimize the model for inference: "train-test-and-optimize-the-model-for-inference"
  --1-- Containerize the model: "containerize-the-model"
  --2-- vLLM: "vllm"
  --3-- 1. Choose a base image: "1-choose-a-base-image"
  --3-- 2. Modify and build the image: "2-modify-and-build-the-image"
  --3-- 3. Push to a registry: "3-push-to-a-registry"
  --3-- Configuration options: "configuration-options"
  --2-- Diffusers: "diffusers"
  --3-- 1. Choose a base image: "1-choose-a-base-image"
  --3-- 2. Implement an inference API: "implement-an-inference-api"
  --3-- 3. Create a Dockerfile: "create-a-dockerfile"
  --3-- 4. Push to a registry: "push-to-a-registry"
  --1-- Deploy the model: "deploy-the-model"
pageTitle: Everywhere Inference—Prepare a custom AI model for deployment | Gcore
pageDescription: Learn how to get started with Gcore Edge AI services.
---
# Prepare a custom AI model for deployment

This guide covers preparing, containerizing, and deploying AI models. It explains how to package models into containers, push them to a registry, and deploy them for text-based inference with vLLM or image generation with Diffusers.

## Train, test, and optimize the model for inference

Before packaging a model into a container, it must be trained, validated, and optimized for inference. This includes training on relevant data, verifying accuracy, and applying optimization techniques such as quantization, pruning, or distillation to reduce computational overhead.

## Containerize the model

To deploy an AI model, it must be packaged into a container image that meets industry standards. While there are no strict structural requirements, the image must be compatible with the target registry and deployment environment. 

If you need more general information about Docker and its setup for running AI models, read [the Docker guide for AI development and deployment](https://github.com/saikhu/Docker-Guide-for-AI-Model-Development-and-Deployment).

### vLLM

vLLM is a fast and easy-to-use library for Large Language Model inference and serving, optimized for efficient execution. It features PagedAttention for memory efficiency, continuous batching, and acceleration via CUDA/HIP graphs and FlashAttention. With support for speculative decoding, chunked prefill, and multiple quantization formats (GPTQ, AWQ, INT4, INT8, FP8), vLLM is well-suited for scalable LLM deployment.

#### 1. Choose a base image

vLLM integrates with Hugging Face and other model repositories, making it optimal for tasks like chatbots, summarization, and code generation. You can find the latest vLLM images in the <a href="https://docs.docker.com/reference/dockerfile/" target="_blank">Docker Hub repository</a>.

Use the official vLLM base image that supports the required model architecture for deployment:

`FROM vllm/vllm-openai:latest`

For custom models, modify the image during the build process.

#### 2. Modify and build the image

To include a specific model from Hugging Face, create a Dockerfile, update the container with the required model, and build the image:

```
FROM vllm/vllm-openai:latest
 
RUN huggingface-cli download state-spaces/mamba-130m-hf

ENTRYPOINT ["vllm", "serve", "state-spaces/mamba-130m-hf", "--host", "0.0.0.0", "--port", "80"]
```

Then, build the container:

`docker build -t <IMAGE>:<TAG> .`

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/ai-models/prepare-a-custom-ai-model-for-deployment/build-the-specific-model-from-hugging-face.png" alt="Build the specific model from Hugging Face" width="80%">

If you are building on macOS with Apple Silicon (M chips), use:

`docker buildx build --platform linux/amd64 -t <IMAGE>:<TAG> .`

This forces the build to use the `linux/amd64` architecture, preventing potential compatibility issues when running on x86-64 cloud servers.

#### 3. Push to a registry

After building the image, push it to a registry for deployment:

`docker tag <IMAGE> <REGISTRY>/<REPOSITORY>:<TAG>`

`docker push <REGISTRY>/<REPOSITORY>:<TAG>`

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/ai-models/prepare-a-custom-ai-model-for-deployment/tag-and-push-the-image-to-a-registry.png" alt="Tag and push the image to a registry" width="80%">

This process embeds the model in the container, making it available for inference. You can also use the <a href="https://gcore.com/docs/cloud/container-registry/create-container-registry" target="_blank">Gcore Container Registry</a> to store and manage your images for seamless deployment.

#### Configuration options

vLLM provides various options to fine-tune performance and behavior. Some notable configurations include:

<table>
        <tr>
            <th>Parameter</th>
            <th>Example</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>--trust-remote-code</td>
            <td>vllm serve state-spaces/mamba-130m-hf --trust-remote-code --host 0.0.0.0 --port 80</td>
            <td>Allows running models that rely on custom Python code from Hugging Face’s Model Hub. By default, this setting is False, meaning vLLM will not execute any remote code unless explicitly allowed.</td>
        </tr>
        <tr>
            <td>--max-model-len</td>
            <td>vllm serve state-spaces/mamba-130m-hf --max-model-len 2048 --host 0.0.0.0 --port 80</td>
            <td>Sets the maximum number of tokens the model can process in a single request. This helps control memory usage and ensures proper processing of long texts.</td>
        </tr>
        <tr>
            <td>--tensor-parallel-size</td>
            <td>vllm serve state-spaces/mamba-130m-hf --tensor-parallel-size 4 --host 0.0.0.0 --port 80</td>
            <td>Splits the model tensors across multiple GPUs to balance memory usage and allow larger models to fit into available hardware.</td>
        </tr>
        <tr>
            <td>--enable-prefix-caching</td>
            <td>vllm serve state-spaces/mamba-130m-hf --enable-prefix-caching --host 0.0.0.0 --port 80</td>
            <td>Improves efficiency by caching repeated prompt prefixes to reduce redundant computations and speed up inference for similar queries.</td>
        </tr>
        <tr>
            <td>--served-model-name</td>
            <td>vllm serve state-spaces/mamba-130m-hf --served-model-name custom-model --host 0.0.0.0 --port 80</td>
            <td>Specifies a custom name for the deployed model, making it easier to reference in API requests.</td>
        </tr>
        <tr>
            <td>--enable-reasoning</td>
            <td>vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --enable-reasoning --reasoning-parser deepseek_r1 --host 0.0.0.0 --port 80</td>
            <td>Enables reasoning mode, allowing models to provide intermediate reasoning steps for better insight into the decision-making process. Requires --reasoning-parser to extract reasoning content from the model output.</td>
        </tr>
    </table>

These parameters can be combined in a single command. The <a href="https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#cli-reference" target="_blank">vLLM documentation</a> provides a full list of configuration options and CLI commands.

### Diffusers

Diffusers is a library for running diffusion-based image generation models. Unlike vLLM, which provides a standardized inference system, it lacks a built-in serving interface, requiring additional code for integration. The environment must include  CUDA, cuDNN, and PyTorch for smooth deployment. The models can be retrieved from the <a href="https://huggingface.co/models" target="_blank">Hugging Face model hub</a>.

#### 1. Choose a base image

Instead of building from scratch, use official images of the <a href="https://catalog.ngc.nvidia.com/" target="_blank">NVIDIA NGC AI Catalog</a> or <a href="https://hub.docker.com/r/pytorch/pytorch/tags" target="_blank">PyTorch</a>.

The following Dockerfile starts with a PyTorch base image and installs Diffusers:

```
FROM pytorch/pytorch:2.6.0-cuda11.8-cudnn9-devel 
RUN pip install diffusers 
```

At this stage, the container does not yet have inference functionality.

#### 2. Implement an inference API

Since diffusers don’t include a built-in inference server, an API must be implemented. The following script loads a Stable Diffusion model, accepts a text prompt via API, and returns a generated image.

```
from fastapi import FastAPI, Request
from diffusers import StableDiffusionPipeline
import base64
from io import BytesIO
from PIL import Image

app = FastAPI()
pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1").to("cuda")

@app.post("/generate")
async def generate_image(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    n = data.get("n", 1)
    images = pipe(prompt).images[:n]

    encoded_images = []
    for img in images:
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        encoded_images.append({"b64_json": base64.b64encode(buffered.getvalue()).decode("utf-8")})

    return {"data": encoded_images}
```

This API allows applications to send HTTP requests for on-demand image generation.

#### 3. Create a Dockerfile

The Dockerfile should include Diffusers and the API service. If authentication is required for specific models, provide the necessary token.

```
FROM pytorch/pytorch:2.6.0-cuda11.8-cudnn9-devel 
WORKDIR /app 
RUN pip install --no-cache-dir diffusers fastapi uvicorn transformers 
COPY inference.py /app/inference.py 
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "80"] 
```

This setup prepares the model and API server to start automatically after deployment.

#### 4. Push to a registry

After building the container, push it to a registry for deployment:

`docker build -t <IMAGE>:<TAG> .` 

`docker tag <IMAGE> <REGISTRY>/<REPOSITORY>` 

`docker push <REGISTRY>/<REPOSITORY>`

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/ai-models/prepare-a-custom-ai-model-for-deployment/tag-and-push-the-image-with-diffusers-library-to-a-registry.png" alt="Tag and push the image with diffusers library to a registry" width="80%">

<alert-element type="warning" title="Warning">
 
Assign a new tag when updating the container to prevent Kubernetes from using outdated images.
 
</alert-element>

### Deployment

After uploading the container to a registry, you can deploy it. During this process, enter the model image URL from the registry. If the registry is public, use the model image URL directly. If the registry is private, provide authentication credentials, including the URL, username, and password. Find more details in the guide on <a href="https://gcore.com/docs/edge-ai/everywhere-inference/container-image-registries/add-a-registry" target="_blank">adding a container image registry</a>.

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/ai-models/prepare-a-custom-ai-model-for-deployment/enter-the-model-image-url-in-deploy-custom-model.png" alt="Enter the model image url in Deploy custom model" width="80%">

After deployment, you will receive an endpoint to send requests and receive responses from the model. You can find additional instructions in the inference instance <a href="https://gcore.com/docs/edge-ai/everywhere-inference/ai-models/deploy-an-ai-model" target="_blank">deployment guide</a>.
