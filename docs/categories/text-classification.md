# <img src="../../assets/icons/text-classification.svg" alt="Text and Classification icon" width="40" height="40" align="absmiddle" /> Text and AI Classification

[Back to Directory](../../README.md) | [Learning Path](../learning-path.md)

<!-- CATEGORY_META:START -->
- **Listed projects**: 10
- **Difficulty mix**: 7 Beginner, 2 Intermediate, 1 Advanced
- **Learning phases covered**: Phase 1 - Foundations, Phase 2 - Chatbots and Voice, Phase 3 - Documents, Vision and Data, Phase 4 - Advanced Agents and Integrations
- **Latest dataset check date**: 2026-11-11
<!-- CATEGORY_META:END -->

## Overview

Text and AI classification workflows analyze incoming messages, emails, support tickets, GitHub issues, and user feedback to assign labels, scores, sentiment, and routing destinations. Operations and engineering teams rely on these foundational patterns for inbox triage, lead qualification, spam and toxicity filtering, and automated ticket routing. Because they have minimal setup overhead, these workflows serve as the ideal starting point for learning n8n and prompt-driven control flow.

## What You Will Learn

- Triggering on incoming emails (Gmail, Outlook), chat messages (Telegram, Discord), forms (Typeform), or HTTP webhooks.
- Enforcing constrained classification outputs (urgent, important, info, spam, sentiment, confidence scores) using LLM nodes.
- Combining **Switch** and **IF** nodes to route records to labels, Slack alerts, Notion tables, or Google Sheets.
- Running privacy-first classification locally via **Ollama** or exposing classification as a reusable webhook REST API.

## Prerequisites and Credentials

- A local or cloud n8n instance.
- Credentials for one messaging or mail provider (**Gmail**, **Outlook**, **Discord**, or **Telegram**) or **Google Sheets** / **Notion**.
- Either a cloud LLM credential (OpenAI, Google Natural Language) or a local **Ollama** instance running on the same Docker network.

## Projects

<!-- PROJECTS:START -->
| ID | Title | Difficulty | Phase | Tools | Source type | Description | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 17 | [InboxZero Lite Email Classifier](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/InboxZero%20Lite%20-%20AI%20Email%20Classifier.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](../learning-path.md#phase-1---foundations) | n8n, Gmail, OpenAI, Google Sheets | GitHub file | Classifies email as urgent, important, info or spam | Third-party template collected in a mirror repo; check original license |
| 18 | [Gmail Auto-Labelling with OpenAI](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/Basic%20Automatic%20Gmail%20Email%20Labelling%20with%20OpenAI%20and%20Gmail%20API.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](../learning-path.md#phase-1---foundations) | n8n, Gmail API, OpenAI | GitHub file | Analyses new emails and assigns or creates labels | Third-party template collected in a mirror repo; check original license |
| 19 | [Auto-Categorise Outlook Email](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/Auto%20Categorise%20Outlook%20Emails%20with%20AI.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](../learning-path.md#phase-1---foundations) | n8n, Outlook, LLM | GitHub file | Moves and categorises Outlook messages by content | Third-party template collected in a mirror repo; check original license |
| 20 | [Email Auto-Responder with Ollama](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/AI%20Email%20Auto-Responder%20with%20Ollama.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](../learning-path.md#phase-2---chatbots-and-voice) | n8n, Ollama (local LLM) | GitHub file | Classifies email, filters spam and drafts replies with no external API | Third-party template collected in a mirror repo; check original license |
| 21 | [Toxic Language Detection in Telegram](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Detect%20toxic%20language%20in%20Telegram%20messages.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](../learning-path.md#phase-1---foundations) | n8n, Telegram, LLM moderation | GitHub file | Flags toxic messages in chats | Third-party template collected in a mirror repo; check original license |
| 22 | [Lead Qualification with GPT-4](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Qualify%20new%20leads%20in%20Google%20Sheets%20via%20OpenAI_s%20GPT-4.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](../learning-path.md#phase-1---foundations) | n8n, Google Sheets, OpenAI | GitHub file | Scores and qualifies new leads in a sheet | Third-party template collected in a mirror repo; check original license |
| 23 | [Text Classification API + Issue Triage](https://github.com/CodingAbdullah/n8n-workflows) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n, webhook, OpenAI, GitHub | GitHub repo | POST endpoint returning topic, sentiment, confidence and summary; also GitHub issue labelling | None |
| 24 | [emailPlus (StructUK)](https://github.com/StructUK) *(profile page: open the pinned repo)* | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, LLM, Google Sheets | GitHub profile (pinned repo) | Classifies enquiry emails, drafts replies, auto-sends or escalates, logs to Sheets | Profile page; open the pinned repo named in the description |
| 25 | [Feedback Sentiment into Notion](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Notion/Add%20positive%20feedback%20messages%20to%20a%20table%20in%20Notion.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](../learning-path.md#phase-1---foundations) | n8n, Typeform, Google NL, Notion, Slack | GitHub file | Runs sentiment analysis on feedback and stores positive items in Notion | Third-party template collected in a mirror repo; check original license |
| 26 | [Discord AI Routing Bot](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Discord/Discord%20AI-powered%20bot.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](../learning-path.md#phase-1---foundations) | n8n, Discord, LLM | GitHub file | Categorises messages and routes them to the right team | Third-party template collected in a mirror repo; check original license |
<!-- PROJECTS:END -->

## Suggested Order

1. Begin with **Beginner** Phase 1 email, chat moderation, lead scoring, and feedback workflows to master triggers, classification prompts, and branching.
2. Try **Intermediate** local-model auto-responders to learn private Ollama inference, followed by webhook classification APIs and issue-triage workflows.
3. Finish with **Advanced** multi-step email drafting and escalation architectures.

## Risks and Good Practice

- **Prompt injection via untrusted text**: Emails, Discord messages, and form submissions come from external users. Separate system instructions from user content and validate output labels with a Switch fallback branch rather than executing arbitrary LLM suggestions.
- **Auto-send guardrails**: Before enabling automatic email replies or issue closures, run workflows in draft-only or log-only mode and verify precision on historical messages.
- **API cost and volume spikes**: High-volume inboxes or chat channels can trigger continuous LLM calls. Filter obvious newsletters/bots with deterministic rules before invoking LLM nodes, and apply rate or token budgets.
