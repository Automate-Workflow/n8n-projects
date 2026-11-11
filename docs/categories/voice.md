# <img src="../../assets/icons/voice.svg" alt="Voice icon" width="40" height="40" align="absmiddle" /> Voice and Audio AI

[Back to Directory](../../README.md) | [Learning Path](../learning-path.md)

<!-- CATEGORY_META:START -->
- **Listed projects**: 5
- **Difficulty mix**: 1 Beginner, 3 Intermediate, 1 Advanced
- **Learning phases covered**: Phase 2 - Chatbots and Voice, Phase 4 - Advanced Agents and Integrations
- **Latest dataset check date**: 2026-11-11
<!-- CATEGORY_META:END -->

## Overview

Voice workflows handle spoken audio capture, speech-to-text (STT) transcription, language translation, conversational reasoning, and text-to-speech (TTS) synthesis. Common industry applications include multilingual voice translation bots, hands-free personal assistants on Telegram, and automated phone or appointment-scheduling agents backed by Google Calendar. These projects teach binary audio file handling, chaining transcription with LLM reasoning, and managing conversational state across voice and text turns.

## What You Will Learn

- Downloading binary voice notes from Telegram or voice webhooks and forwarding them to transcription models (such as Whisper).
- Combining speech-to-text, translation across dozens of languages, and LLM assistant tool calls in a single flow.
- Building unified agents that handle both text and audio messages seamlessly.
- Connecting real-time voice AI assistants to scheduling systems such as Google Calendar.

## Prerequisites and Credentials

- A **Telegram Bot token** (via BotFather) for the Telegram voice workflows, or voice-provider webhooks for telephony voice agents.
- Credentials for speech transcription and LLM processing (OpenAI Whisper/GPT or compatible STT/LLM endpoints).
- **Google Calendar** OAuth2 credentials if running appointment-scheduling workflows.

## Projects

<!-- PROJECTS:START -->
| ID | Title | Difficulty | Phase | Tools | Source type | Description | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 27 | [Telegram Audio Translator (55 languages)](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Translate%20Telegram%20audio%20messages%20with%20AI%20(55%20supported%20languages).json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](../learning-path.md#phase-2---chatbots-and-voice) | n8n, Telegram, speech-to-text | GitHub file | Transcribes voice messages and translates them | Third-party template collected in a mirror repo; check original license |
| 28 | [Angie Voice and Text Assistant](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Angie,%20Personal%20AI%20Assistant%20with%20Telegram%20Voice%20and%20Text.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](../learning-path.md#phase-2---chatbots-and-voice) | n8n, Telegram, LLM | GitHub file | Personal assistant that handles voice and text | Third-party template collected in a mirror repo; check original license |
| 29 | [Voice and Text Assistant Template](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20AI%20bot%20assistant_%20ready-made%20template%20for%20voice%20&%20text%20messages.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 2](../learning-path.md#phase-2---chatbots-and-voice) | n8n, Telegram, LLM | GitHub file | Ready-made bot for voice and text messages | Third-party template collected in a mirror repo; check original license |
| 30 | [Multimodal Messaging Agent](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/%F0%9F%A4%96%20Telegram%20Messaging%20Agent%20for%20Text_Audio_Images.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](../learning-path.md#phase-2---chatbots-and-voice) | n8n, Telegram, LLM | GitHub file | Processes text, audio and images in one agent | Third-party template collected in a mirror repo; check original license |
| 31 | [Dental Practice Voice Agent](https://github.com/lucaswalter/n8n-ai-automations) *(open the named workflow: `dental_practice_voice_agent.json`)* | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, voice AI, Google Calendar | GitHub repo | Voice agent for appointment scheduling (dental_practice_voice_agent.json) | Repo with several workflows; open the named workflow |
<!-- PROJECTS:END -->

## Suggested Order

1. Start with the **Beginner** voice-and-text bot template to see how audio attachments enter n8n and branch alongside text messages.
2. Explore the **Intermediate** audio translation, personal assistant, and multimodal messaging agents.
3. Move to **Advanced** domain voice agents to study calendar tool integration and multi-turn dialog handling.

## Risks and Good Practice

- **Audio cost and latency**: Transcription and TTS services charge per minute or per character and introduce round-trip delay. Enforce maximum audio duration/file size checks before processing.
- **Consent and recording privacy**: Voice recordings often contain sensitive personal details and biometric identifiers. Inform users when audio is processed by third-party cloud APIs and avoid storing raw audio files longer than necessary.
- **Fallback handling**: Background noise or heavy accents can produce garbled transcripts; design confirmation prompts before executing irreversible calendar bookings or external actions.
