# <img src="../../assets/icons/whatsapp.svg" alt="WhatsApp icon" width="40" height="40" align="absmiddle" /> WhatsApp Automation

[Back to Directory](../../README.md) | [Learning Path](../learning-path.md)

<!-- CATEGORY_META:START -->
- **Listed projects**: 6
- **Difficulty mix**: 3 Intermediate, 3 Advanced
- **Learning phases covered**: Phase 2 - Chatbots and Voice, Phase 4 - Advanced Agents and Integrations
- **Latest dataset check date**: 2026-11-11
<!-- CATEGORY_META:END -->

## Overview

WhatsApp workflows connect conversational messaging directly to business backends, LLM agents, voice transcription, and ticketing or booking systems. In production, teams use these patterns for customer support triage, order status lookup, appointment booking, and omnichannel field-service desks where customers already communicate on mobile. Because messages arrive asynchronously as text, audio notes, or images, WhatsApp workflows teach webhook handling, media download, and multi-agent tool invocation.

## What You Will Learn

- Receiving inbound WhatsApp webhook events and routing text, voice, and image payloads to specialized branches.
- Integrating both official WhatsApp Business Cloud API nodes and self-hosted HTTP messaging gateways (such as WAHA) via Docker and community nodes.
- Designing omnichannel multi-agent workflows with tool calling, memory persistence, and human escalation.
- Structuring reply formatting and message pacing for mobile conversational UX.

## Prerequisites and Credentials

- An n8n instance reachable over HTTPS (or a local tunnel such as ngrok or Cloudflare Tunnel for webhook testing).
- Either a **Meta Developer / WhatsApp Business Cloud API** test phone number and token, or Docker to run **WAHA** locally on a sandbox number.
- An LLM API credential (for example OpenAI or Google Gemini) and, for voice-enabled workflows, speech-to-text or ElevenLabs credentials.

## Projects

<!-- PROJECTS:START -->
| ID | Title | Difficulty | Phase | Tools | Source type | Description | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [Jacobo AI Agent (7 production workflows)](https://github.com/santifer/jacobo-workflows) | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, WhatsApp, ElevenLabs, multi-agent tool calling | GitHub repo | Omnichannel WhatsApp and voice multi-agent system from a phone repair business | WhatsApp unofficial APIs risk number bans; use official Business API for production |
| 2 | [n8n WhatsApp AI Agent](https://github.com/ZohaibCodez/n8n-whatsapp-ai-agent) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](../learning-path.md#phase-2---chatbots-and-voice) | n8n, WhatsApp Business API, Gemini | GitHub repo | WhatsApp assistant handling text, audio and image messages | WhatsApp unofficial APIs risk number bans; use official Business API for production |
| 3 | [WhatsApp Hospitality Chatbot](https://github.com/lucaswalter/n8n-ai-automations) *(open the named workflow: `whatsapp_ai_chatbot_agent.json`)* | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](../learning-path.md#phase-2---chatbots-and-voice) | n8n, WhatsApp, LLM | GitHub repo | Answers guest queries and recommends services (whatsapp_ai_chatbot_agent.json) | WhatsApp unofficial APIs risk number bans; use official Business API for production; Repo with several workflows; open the named workflow |
| 4 | [WAHA n8n Community Node](https://github.com/devlikeapro/n8n-nodes-waha) | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | n8n community node, WAHA | GitHub repo | Node for the WhatsApp HTTP API with example workflows | WhatsApp unofficial APIs risk number bans; use official Business API for production |
| 5 | [WAHA (WhatsApp HTTP API)](https://github.com/devlikeapro/waha) | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | Docker, REST, webhooks | GitHub repo | Self-hosted WhatsApp API that connects to n8n | WhatsApp unofficial APIs risk number bans; use official Business API for production |
| 6 | [WhatsApp Template Folder](https://github.com/enescingoz/awesome-n8n-templates/tree/main/WhatsApp) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](../learning-path.md#phase-2---chatbots-and-voice) | n8n, WhatsApp, OpenAI | GitHub folder | Collection of WhatsApp chatbot templates | WhatsApp unofficial APIs risk number bans; use official Business API for production |
<!-- PROJECTS:END -->

## Suggested Order

1. Start with the **Intermediate** chatbot workflows and template collections to understand inbound webhooks, message parsing, and reply nodes.
2. Explore multi-modal text, audio, and image message routing next.
3. Progress to **Advanced** self-hosted gateway setups (WAHA and its n8n community node) and full multi-agent production systems once you have tested message delivery reliably.

## Risks and Good Practice

- **Account ban risk with unofficial APIs**: Unofficial or reverse-engineered WhatsApp bridges (including session-based WAHA engines) violate WhatsApp terms of service and can result in permanent phone number bans. Use the **official Meta WhatsApp Business Cloud API** for production workloads, and test unofficial tools strictly on disposable sandbox numbers.
- **Opt-in and anti-spam compliance**: Only message users who explicitly opted in, respect Meta's 24-hour customer service window and approved message templates, and implement rate limiting.
- **Webhook security**: Validate webhook verification tokens and signatures (`X-Hub-Signature-256`) so unauthenticated callers cannot inject fake customer messages.
