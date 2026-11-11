# <img src="../../assets/icons/video.svg" alt="Video icon" width="40" height="40" align="absmiddle" /> Video Automation

[Back to Directory](../../README.md) | [Learning Path](../learning-path.md)

<!-- CATEGORY_META:START -->
- **Listed projects**: 5
- **Difficulty mix**: 1 Beginner, 1 Intermediate, 3 Advanced
- **Learning phases covered**: Phase 1 - Foundations, Phase 3 - Documents, Vision and Data, Phase 4 - Advanced Agents and Integrations
- **Latest dataset check date**: 2026-11-11
<!-- CATEGORY_META:END -->

## Overview

Video automation workflows orchestrate media ingestion, AI summarization from captions, short-form clipping, programmatic rendering, and multi-platform social distribution. Media teams and creators use these architectures to announce new YouTube uploads with AI summaries on Discord, automate faceless video production (script, voiceover, timestamps, visuals, and render), extract viral short clips, and cross-post finished videos across TikTok, Instagram, YouTube, and LinkedIn. These workflows teach asynchronous job handling, multi-service orchestration, and adapter design patterns.

## What You Will Learn

- Fetching YouTube feeds/captions, summarizing content with LLMs, and publishing updates to Discord or Slack.
- Publishing finished media assets from Google Drive to Instagram and TikTok via social APIs.
- Chaining multi-modal generation services (Gemini, ElevenLabs, Whisper, Shotstack) into end-to-end rendering pipelines.
- Structuring provider-adapter frameworks for multi-platform cross-posting and automated video clipping (Vizard AI).

## Prerequisites and Credentials

- Content and channel credentials (**YouTube**, **Discord**, **Slack**, **Google Drive**, or social publishing platform tokens).
- Media AI and rendering API keys depending on workflow scope (**OpenAI** / **Gemini**, **ElevenLabs**, **Shotstack**, or **Vizard AI**).

## Projects

<!-- PROJECTS:START -->
| ID | Title | Difficulty | Phase | Tools | Source type | Description | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | [YouTube Summaries to Discord](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Discord/Share%20YouTube%20Videos%20with%20AI%20Summaries%20on%20Discord.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](../learning-path.md#phase-1---foundations) | n8n, YouTube, LLM, Discord | GitHub file | Posts new videos with AI summaries from captions | Third-party template collected in a mirror repo; check original license |
| 41 | [Drive to Instagram and TikTok](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Upload%20to%20Instagram%20and%20Tiktok%20from%20Google%20Drive.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n, Google Drive, social APIs | GitHub file | Publishes media from Drive to social platforms | Third-party template collected in a mirror repo; check original license |
| 42 | [Video Cross-Posting Framework](https://github.com/StructUK) *(profile page: open the pinned repo)* | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, posting-provider adapters | GitHub profile (pinned repo) | Distributes short video to TikTok, Instagram, YouTube, LinkedIn and more | Profile page; open the pinned repo named in the description |
| 43 | [Faceless Video Pipeline](https://n8n.io/workflows/6014) | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, Gemini, ElevenLabs, Whisper, Shotstack | n8n.io template | Script, voiceover, timestamps, images and final render | None |
| 44 | [Viral Video Clipper](https://github.com/lucaswalter/n8n-ai-automations) *(open the named workflow)* | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, Vizard AI, Slack | GitHub repo | Finds viral clips in YouTube videos and shares them | Repo with several workflows; open the named workflow |
<!-- PROJECTS:END -->

## Suggested Order

1. Begin with **Beginner** caption summarization workflows to understand media triggers and text formatting.
2. Move to **Intermediate** Drive-to-social publishing workflows to inspect media upload payloads and social platform authentication.
3. Study the **Advanced** rendering, clipping, and cross-posting frameworks to master asynchronous processing and multi-provider adapters.

## Risks and Good Practice

- **Rendering and synthesis costs**: Combining LLM scripting, ElevenLabs voiceovers, transcription, and cloud video rendering (Shotstack/Vizard) consumes significant paid credits per video. Test with short 10-second clips and strict budget caps.
- **Asynchronous timeouts**: Video rendering and clipping can exceed synchronous HTTP timeouts. Prefer webhook callbacks or bounded wait-and-poll loops with maximum retry limits.
- **Copyright and platform policies**: Only clip or cross-post video assets you own or have explicit rights to distribute, and review TikTok/Instagram/YouTube API rules before enabling unattended auto-publishing.
