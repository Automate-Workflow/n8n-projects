# <img src="../../assets/icons/image.svg" alt="Image icon" width="40" height="40" align="absmiddle" /> Image Generation and Processing

[Back to Directory](../../README.md) | [Learning Path](../learning-path.md)

<!-- CATEGORY_META:START -->
- **Listed projects**: 4
- **Difficulty mix**: 3 Beginner, 1 Intermediate
- **Learning phases covered**: Phase 1 - Foundations, Phase 2 - Chatbots and Voice
- **Latest dataset check date**: 2026-11-11
<!-- CATEGORY_META:END -->

## Overview

Image workflows automate visual understanding, batch image editing, background removal, and AI image generation inside n8n. E-commerce teams, creative studios, and marketing operations use these patterns to clean product photos in Google Drive folders, generate catalog imagery from prompts, and analyze user-submitted photos in messaging apps. Working through these projects teaches binary image upload/download handling, MIME type routing, and external media API integration.

## What You Will Learn

- Processing binary image attachments received from Telegram or watched Google Drive folders.
- Calling vision LLMs to describe, inspect, or answer questions about uploaded photos.
- Integrating external image manipulation and generation APIs (background removal and product-image synthesis) and saving outputs back to Drive or chat.
- Chaining text and image generation capabilities inside a single conversational bot.

## Prerequisites and Credentials

- Credentials for **Telegram** and/or **Google Drive** OAuth2.
- Vision LLM or image generation/editing API credentials (such as OpenAI, NeurochainAI, or dedicated background-removal APIs).
- Optional cloud storage folder for input/output test images.

## Projects

<!-- PROJECTS:START -->
| ID | Title | Difficulty | Phase | Tools | Source type | Description | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 32 | [Telegram Image Analysis Bot](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Automated%20AI%20image%20analysis%20and%20response%20via%20Telegram.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](../learning-path.md#phase-1---foundations) | n8n, Telegram, vision LLM | GitHub file | Users send images and receive AI analysis | Third-party template collected in a mirror repo; check original license |
| 33 | [Background Removal for Drive Images](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Automatic%20Background%20Removal%20for%20Images%20in%20Google%20Drive.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](../learning-path.md#phase-1---foundations) | n8n, Google Drive, image API | GitHub file | Removes backgrounds from images in a Drive folder | Third-party template collected in a mirror repo; check original license |
| 34 | [AI Product Images](https://github.com/enescingoz/awesome-n8n-templates/blob/main/AI%20product%20imagines.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](../learning-path.md#phase-1---foundations) | n8n, image generation | GitHub file | Generates product imagery | Third-party template collected in a mirror repo; check original license |
| 35 | [Text and Image Generation Bot](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20AI%20Bot_%20NeurochainAI%20Text%20&%20Image%20-%20NeurochainAI%20Basic%20API%20Integration.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](../learning-path.md#phase-2---chatbots-and-voice) | n8n, Telegram, NeurochainAI | GitHub file | Generates text and images inside Telegram | Third-party template collected in a mirror repo; check original license |
<!-- PROJECTS:END -->

## Suggested Order

1. Begin with the **Beginner** Phase 1 projects to learn single-image analysis, Drive folder triggers, background removal, and basic product image generation.
2. Continue to **Intermediate** multi-capability bots to see combined text and image command routing.

## Risks and Good Practice

- **Per-image cost and rate limits**: Image generation and background-removal APIs typically enforce strict per-minute quotas and higher unit costs than text endpoints. Add throttling or batch limits before running against large Google Drive folders.
- **File size and format checks**: Validate MIME types (`image/png`, `image/jpeg`, `image/webp`) and maximum byte size before sending payloads to external APIs.
- **Usage rights and content moderation**: Review upstream model terms regarding commercial ownership of generated product imagery and filter inappropriate prompts on public-facing bots.
