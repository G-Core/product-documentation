---
title: generate-ai-subtitles-and-add-them-to-video
displayName: Generate and translate captions
published: true
order: 10
toc:
   --1--How it works: "how-it-works"
   --1--Key benefits: "key-benefits"
   --1--Generate and translate captions: "generate-and-translate-ai-captions-for-your-video-content"
pageTitle: AI ASR for AI-Generated Subtitles and Translation | Gcore
pageDescription: Effortlessly generate and add AI subtitles in numerous languages with Gcore AI ASR.
customUrl: /streaming-platform/video-hosting/ai-for-video/generate-ai-subtitles-and-add-them-to-video
---
# Generate and translate captions 

Gcore <a href="https://gcore.com/streaming-platform/ai-for-video" target="_blank">AI automated speech recognition (ASR)</a> functionality allows you to automatically generate <a href="https://gcore.com/docs/streaming-platform/video-hosting/subtitles-and-closed-captions-for-vod#what-are-subtitles-and-closed-captions" target="_blank">video captions</a> (also referred to as subtitles) using AI models. This serves two use cases: 

* **Transcription**: Generate video captions from the original audio. Our AI models transcribe the speech of one or multiple speakers, even if they use different languages. 
* **Translation**: Translate captions into more than 100 languages to make your video accessible to multilingual audiences. 

## How it works

We use <a href="https://openai.com/research/whisper" target="_blank">Whisper ASR</a> from OpenAI, along with a range of other specialized AI models. These AI ASR models operate on the Gcore infrastructure, so no files are transferred to external services. After processing, all original files are also deleted from the AI system’s local storage. 

## Key benefits

- **Ease of use.** You can generate ready-to-use subtitles in the Customer Portal or with a few API requests.
- **Supported languages.** AI can recognize and transcribe audio in over 100 languages worldwide. If your desired language isn't listed, please contact [Gcore support team](maito:support@gcore.com), and we'll consider adding it in the future. 
- **Multi-platform support**. Generate video captions for any MP4 video that’s uploaded to Gcore Video Hosting or stored externally, for instance, on AWS. 
- **Multi-language support.** We support the recognition of multiple spoken languages in a single video (the “code-switching” feature). This accounts for video participants switching between several languages in their speech.

## Generate and translate AI captions for your video content

You can transcribe and translate subtitles in two ways: via API or in the Customer Portal. For step-by-step instructions, check out the relevant guide: 

* <a href="https://gcore.com/docs/streaming-platform/video-hosting/ai-for-video/generate-ai-subtitles-and-add-them-to-video" target="_blank">Transcribe and translate captions in the Customer Portal</a>
* <a href="" target="_blank">Transcribe and translate captions via API</a>