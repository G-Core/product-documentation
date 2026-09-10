# Streaming AI — deferred items

## AI task statuses shared page

Create one shared page instead of duplicating the status table in every article.

### Current state

Articles that have `## AI task statuses` inline (both Portal and API tabs):
- `streaming/ai-video-service/generate-ai-subtitles-and-add-them-to-video/generate-captions-in-customer-portal.mdx`

Articles listed in tracking but DO NOT yet have the section anywhere:
- `streaming/ai-video-service/content-moderation/nsfw-detection.mdx`
- `streaming/ai-video-service/content-moderation/soft-nudity-detection.mdx`
- `streaming/ai-video-service/content-moderation/sport-detection.mdx`
- `streaming/ai-video-service/ai-nudity-detection.mdx`

### Canonical format

When the section is added inline (before the shared page exists), use this exact format:

```mdx
## AI task statuses

<p>Each AI task is processed in sub-stages. For example, the original language is first determined in a video, and then transcription is done.</p>

<p>In such cases, the video processing status may change from **Started** to **Pending** and back. This happens during the allocation of resources for a specific sub-stage. To view a general task processing status, check the progress percentage.</p>

<p>A task can have the following statuses:</p>

- **Success**: The processing has been completed.
- **Started**: The processing has started.
- **Pending**: The task is being processed and is awaiting the allocation of available resources.
- **Failure**: A task has failed. Create the task again.
- **Revoked**: The processing was canceled by a user or system.
- **Retry**: The task execution failed due to internal reasons, the task is queued for re-execution (up to 3 times).

<Info>
We delete task result data after one month.
</Info>
```

### TODO

When all affected articles are done — extract this into a shared snippet and replace inline sections with a single link/include.
