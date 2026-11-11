# Learning Path

This curated curriculum organizes every project in `data/n8n_list.csv` into four progressive phases. Follow the phases in order if you are new to n8n, or jump directly to the phase matching your current engineering skills.

All project tables below are generated automatically from `data/n8n_list.csv` by `scripts/build_readme.py`.

---

## <a id="phase-1---foundations"></a>Phase 1 - Foundations

<p><img src="../assets/badges/phase-1.svg" alt="Phase 1 - Foundations" height="20" /></p>

**Goal:** Build confidence with triggers, credentials, LLM classification/generation nodes, and single-hop destinations.

### What You Will Learn in Phase 1

- Connecting standard SaaS triggers and actions (Gmail, Outlook, Telegram, Discord, Typeform, Google Drive, Google Sheets, Notion).
- Writing deterministic classification and scoring prompts with explicit category labels.
- Handling binary image or PDF inputs inside basic Telegram and Drive pipelines.
- Testing workflows manually with sample payloads before turning schedules on.

### Phase 1 Projects

<!-- PHASE_1:START -->
| ID | Title | Category | Difficulty | Tools | Notes |
| --- | --- | --- | --- | --- | --- |
| 17 | [InboxZero Lite Email Classifier](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/InboxZero%20Lite%20-%20AI%20Email%20Classifier.json) | [Text/Classification](categories/text-classification.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, Gmail, OpenAI, Google Sheets | Third-party template collected in a mirror repo; check original license |
| 18 | [Gmail Auto-Labelling with OpenAI](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/Basic%20Automatic%20Gmail%20Email%20Labelling%20with%20OpenAI%20and%20Gmail%20API.json) | [Text/Classification](categories/text-classification.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, Gmail API, OpenAI | Third-party template collected in a mirror repo; check original license |
| 19 | [Auto-Categorise Outlook Email](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/Auto%20Categorise%20Outlook%20Emails%20with%20AI.json) | [Text/Classification](categories/text-classification.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, Outlook, LLM | Third-party template collected in a mirror repo; check original license |
| 21 | [Toxic Language Detection in Telegram](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Detect%20toxic%20language%20in%20Telegram%20messages.json) | [Text/Classification](categories/text-classification.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, Telegram, LLM moderation | Third-party template collected in a mirror repo; check original license |
| 22 | [Lead Qualification with GPT-4](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Qualify%20new%20leads%20in%20Google%20Sheets%20via%20OpenAI_s%20GPT-4.json) | [Text/Classification](categories/text-classification.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, Google Sheets, OpenAI | Third-party template collected in a mirror repo; check original license |
| 25 | [Feedback Sentiment into Notion](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Notion/Add%20positive%20feedback%20messages%20to%20a%20table%20in%20Notion.json) | [Text/Classification](categories/text-classification.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, Typeform, Google NL, Notion, Slack | Third-party template collected in a mirror repo; check original license |
| 26 | [Discord AI Routing Bot](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Discord/Discord%20AI-powered%20bot.json) | [Text/Classification](categories/text-classification.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, Discord, LLM | Third-party template collected in a mirror repo; check original license |
| 32 | [Telegram Image Analysis Bot](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Automated%20AI%20image%20analysis%20and%20response%20via%20Telegram.json) | [Image](categories/image.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, Telegram, vision LLM | Third-party template collected in a mirror repo; check original license |
| 33 | [Background Removal for Drive Images](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Automatic%20Background%20Removal%20for%20Images%20in%20Google%20Drive.json) | [Image](categories/image.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, Google Drive, image API | Third-party template collected in a mirror repo; check original license |
| 34 | [AI Product Images](https://github.com/enescingoz/awesome-n8n-templates/blob/main/AI%20product%20imagines.json) | [Image](categories/image.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, image generation | Third-party template collected in a mirror repo; check original license |
| 40 | [YouTube Summaries to Discord](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Discord/Share%20YouTube%20Videos%20with%20AI%20Summaries%20on%20Discord.json) | [Video](categories/video.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, YouTube, LLM, Discord | Third-party template collected in a mirror repo; check original license |
| 49 | [Telegram Chat with PDF](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20chat%20with%20PDF.json) | [Paper](categories/paper.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, Telegram, LLM | Third-party template collected in a mirror repo; check original license |
<!-- PHASE_1:END -->

---

## <a id="phase-2---chatbots-and-voice"></a>Phase 2 - Chatbots and Voice

<p><img src="../assets/badges/phase-2.svg" alt="Phase 2 - Chatbots and Voice" height="20" /></p>

**Goal:** Move from one-shot automations to conversational assistants, speech processing, local models, and document Q&A.

### What You Will Learn in Phase 2

- Maintaining conversational memory and routing multimodal inputs (text, voice notes, images).
- Transcribing audio with speech-to-text models and translating across languages.
- Running privacy-preserving local inference using Ollama without external LLM APIs.
- Building Retrieval-Augmented Generation (RAG) workflows with embeddings, vector stores, and source citations.

### Phase 2 Projects

<!-- PHASE_2:START -->
| ID | Title | Category | Difficulty | Tools | Notes |
| --- | --- | --- | --- | --- | --- |
| 2 | [n8n WhatsApp AI Agent](https://github.com/ZohaibCodez/n8n-whatsapp-ai-agent) | [WhatsApp](categories/whatsapp.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, WhatsApp Business API, Gemini | WhatsApp unofficial APIs risk number bans; use official Business API for production |
| 3 | [WhatsApp Hospitality Chatbot](https://github.com/lucaswalter/n8n-ai-automations) *(open the named workflow: `whatsapp_ai_chatbot_agent.json`)* | [WhatsApp](categories/whatsapp.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, WhatsApp, LLM | WhatsApp unofficial APIs risk number bans; use official Business API for production; Repo with several workflows; open the named workflow |
| 6 | [WhatsApp Template Folder](https://github.com/enescingoz/awesome-n8n-templates/tree/main/WhatsApp) | [WhatsApp](categories/whatsapp.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, WhatsApp, OpenAI | WhatsApp unofficial APIs risk number bans; use official Business API for production |
| 20 | [Email Auto-Responder with Ollama](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/AI%20Email%20Auto-Responder%20with%20Ollama.json) | [Text/Classification](categories/text-classification.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, Ollama (local LLM) | Third-party template collected in a mirror repo; check original license |
| 27 | [Telegram Audio Translator (55 languages)](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Translate%20Telegram%20audio%20messages%20with%20AI%20(55%20supported%20languages).json) | [Voice](categories/voice.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, Telegram, speech-to-text | Third-party template collected in a mirror repo; check original license |
| 28 | [Angie Voice and Text Assistant](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Angie,%20Personal%20AI%20Assistant%20with%20Telegram%20Voice%20and%20Text.json) | [Voice](categories/voice.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, Telegram, LLM | Third-party template collected in a mirror repo; check original license |
| 29 | [Voice and Text Assistant Template](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20AI%20bot%20assistant_%20ready-made%20template%20for%20voice%20&%20text%20messages.json) | [Voice](categories/voice.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, Telegram, LLM | Third-party template collected in a mirror repo; check original license |
| 30 | [Multimodal Messaging Agent](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/%F0%9F%A4%96%20Telegram%20Messaging%20Agent%20for%20Text_Audio_Images.json) | [Voice](categories/voice.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, Telegram, LLM | Third-party template collected in a mirror repo; check original license |
| 35 | [Text and Image Generation Bot](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20AI%20Bot_%20NeurochainAI%20Text%20&%20Image%20-%20NeurochainAI%20Basic%20API%20Integration.json) | [Image](categories/image.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, Telegram, NeurochainAI | Third-party template collected in a mirror repo; check original license |
| 48 | [Chat with PDF (quoting sources)](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Chat%20with%20PDF%20docs%20using%20AI%20(quoting%20sources).json) | [Paper](categories/paper.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, embeddings, vector store | Third-party template collected in a mirror repo; check original license |
<!-- PHASE_2:END -->

---

## <a id="phase-3---documents-vision-and-data"></a>Phase 3 - Documents, Vision and Data

<p><img src="../assets/badges/phase-3.svg" alt="Phase 3 - Documents, Vision and Data" height="20" /></p>

**Goal:** Extract reliable structured records from messy real-world documents, screenshots, web pages, and forms.

### What You Will Learn in Phase 3

- Parsing PDFs, resumes, invoices, and academic papers into strict JSON or CSV schemas.
- Applying multimodal vision LLMs for OCR, license plate reading, and phishing screenshot inspection.
- Orchestrating external document renderers and parsers (Gotenberg, LlamaParse, Firecrawl, Vertex AI Gemini).
- Building webhook APIs and form handlers with validation, prompt-injection safeguards, and database/spreadsheet persistence.

### Phase 3 Projects

<!-- PHASE_3:START -->
| ID | Title | Category | Difficulty | Tools | Notes |
| --- | --- | --- | --- | --- | --- |
| 11 | [Resume Bot](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/ResumeBot.json) | [Resume/HR](categories/resume-hr.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | n8n, Telegram, Supabase, LaTeX | Handles personal data; review privacy and bias before use; Third-party template collected in a mirror repo; check original license |
| 12 | [CV Parsing with Multimodal Vision AI](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/CV%20Resume%20PDF%20Parsing%20with%20Multimodal%20Vision%20AI.json) | [Resume/HR](categories/resume-hr.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, Vision LLM | Handles personal data; review privacy and bias before use; Third-party template collected in a mirror repo; check original license |
| 13 | [Resume Data Extraction to PDF (Gotenberg)](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Extract%20data%20from%20resume%20and%20create%20PDF%20with%20Gotenberg.json) | [Resume/HR](categories/resume-hr.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, LLM, Gotenberg | Handles personal data; review privacy and bias before use; Third-party template collected in a mirror repo; check original license |
| 14 | [Job Application Handling with n8n Forms](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Airtable/Handling%20Job%20Application%20Submissions%20with%20AI%20and%20n8n%20Forms.json) | [Resume/HR](categories/resume-hr.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n Forms, LLM, Airtable | Handles personal data; review privacy and bias before use; Third-party template collected in a mirror repo; check original license |
| 15 | [Screen Applicants with AI](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Screen%20Applicants%20With%20AI,%20notify%20HR%20and%20save%20them%20in%20a%20Google%20Sheet.json) | [Resume/HR](categories/resume-hr.md) | <img src="../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | n8n, LLM, Google Sheets | Handles personal data; review privacy and bias before use; Third-party template collected in a mirror repo; check original license |
| 16 | [Internship Informer](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Internship%20Informer.json) | [Resume/HR](categories/resume-hr.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, Telegram, Firecrawl, WhatsApp | Handles personal data; review privacy and bias before use; Third-party template collected in a mirror repo; check original license |
| 23 | [Text Classification API + Issue Triage](https://github.com/CodingAbdullah/n8n-workflows) | [Text/Classification](categories/text-classification.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, webhook, OpenAI, GitHub | None |
| 36 | [License Plate Extraction](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Extract%20license%20plate%20number%20from%20image%20uploaded%20via%20an%20n8n%20form.json) | [Computer Vision](categories/computer-vision.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n Forms, vision LLM | Third-party template collected in a mirror repo; check original license |
| 37 | [Phishing Email Analysis with Vision](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/Analyze%20Suspicious%20Email%20Contents%20with%20ChatGPT%20Vision.json) | [Computer Vision](categories/computer-vision.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, Gmail, ChatGPT Vision | Third-party template collected in a mirror repo; check original license |
| 38 | [OCR from PDFs and Images to CSV](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Extract%20text%20from%20PDF%20and%20image%20using%20Vertex%20AI%20(Gemini)%20into%20CSV.json) | [Computer Vision](categories/computer-vision.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, Vertex AI Gemini | Third-party template collected in a mirror repo; check original license |
| 41 | [Drive to Instagram and TikTok](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Upload%20to%20Instagram%20and%20Tiktok%20from%20Google%20Drive.json) | [Video](categories/video.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, Google Drive, social APIs | Third-party template collected in a mirror repo; check original license |
| 45 | [Hugging Face Papers to Notion](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Notion/Analyse%20papers%20from%20Hugging%20Face%20with%20AI%20and%20store%20them%20in%20Notion.json) | [Paper](categories/paper.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, Hugging Face, LLM, Notion | Third-party template collected in a mirror repo; check original license |
| 47 | [arXiv Paper Summariser](https://n8n.io/workflows/2904-arxiv-paper-summarization-with-chatgpt/) | [Paper](categories/paper.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, webhook, ChatGPT | None |
| 50 | [Invoice Extraction (LlamaParse + OpenAI)](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Invoice%20data%20extraction%20with%20LlamaParse%20and%20OpenAI.json) | [Paper](categories/paper.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, LlamaParse, OpenAI | Third-party template collected in a mirror repo; check original license |
<!-- PHASE_3:END -->

---

## <a id="phase-4---advanced-agents-and-integrations"></a>Phase 4 - Advanced Agents and Integrations

<p><img src="../assets/badges/phase-4.svg" alt="Phase 4 - Advanced Agents and Integrations" height="20" /></p>

**Goal:** Architect production-grade multi-agent systems, custom self-hosted services, MCP tool servers, and multi-step media pipelines.

### What You Will Learn in Phase 4

- Designing multi-agent orchestration with tool calling, escalation paths, and calendar/CRM integration.
- Integrating self-hosted microservices and Model Context Protocol (MCP) servers (WAHA, Ultralytics YOLO MCP) over Docker and REST webhooks.
- Building asynchronous multi-stage media pipelines (script generation, voiceover synthesis, clipping, rendering, and cross-platform publishing).
- Managing rate limits, compliance boundaries, human-in-the-loop review, and cost controls in complex workflows.

### Phase 4 Projects

<!-- PHASE_4:START -->
| ID | Title | Category | Difficulty | Tools | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | [Jacobo AI Agent (7 production workflows)](https://github.com/santifer/jacobo-workflows) | [WhatsApp](categories/whatsapp.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | n8n, WhatsApp, ElevenLabs, multi-agent tool calling | WhatsApp unofficial APIs risk number bans; use official Business API for production |
| 4 | [WAHA n8n Community Node](https://github.com/devlikeapro/n8n-nodes-waha) | [WhatsApp](categories/whatsapp.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | n8n community node, WAHA | WhatsApp unofficial APIs risk number bans; use official Business API for production |
| 5 | [WAHA (WhatsApp HTTP API)](https://github.com/devlikeapro/waha) | [WhatsApp](categories/whatsapp.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | Docker, REST, webhooks | WhatsApp unofficial APIs risk number bans; use official Business API for production |
| 7 | [LinkedIn Job Alerts](https://github.com/simonleybovich/linkedin-job-alerts) | [LinkedIn](categories/linkedin.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | n8n, Gemini, Notion, Telegram | Scraping may conflict with LinkedIn terms; check before use |
| 8 | [LinkedIn Outreach with Notion and OpenAI](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Notion/Automate%20LinkedIn%20Outreach%20with%20Notion%20and%20OpenAI.json) | [LinkedIn](categories/linkedin.md) | <img src="../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | n8n, Notion, OpenAI, LinkedIn | Scraping may conflict with LinkedIn terms; check before use; Third-party template collected in a mirror repo; check original license |
| 9 | [Content Repurposing Factory](https://github.com/lucaswalter/n8n-ai-automations) *(open the named workflow)* | [LinkedIn](categories/linkedin.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | n8n, Apify, Claude | Scraping may conflict with LinkedIn terms; check before use; Repo with several workflows; open the named workflow |
| 10 | [TalentFlow AI](https://n8n.io/workflows/5099-talentflow-ai-instantly-evaluate-applicants-github-linkedin-using-ai/) | [LinkedIn](categories/linkedin.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | n8n, JotForm, ScrapingDog, Apify, OpenRouter | Scraping may conflict with LinkedIn terms; check before use |
| 24 | [emailPlus (StructUK)](https://github.com/StructUK) *(profile page: open the pinned repo)* | [Text/Classification](categories/text-classification.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | n8n, LLM, Google Sheets | Profile page; open the pinned repo named in the description |
| 31 | [Dental Practice Voice Agent](https://github.com/lucaswalter/n8n-ai-automations) *(open the named workflow: `dental_practice_voice_agent.json`)* | [Voice](categories/voice.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | n8n, voice AI, Google Calendar | Repo with several workflows; open the named workflow |
| 39 | [Ultralytics YOLO MCP Server](https://github.com/MetehanYasar11/ultralytics_mcp_server) | [Computer Vision](categories/computer-vision.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | Docker, YOLO, MCP, n8n | None |
| 42 | [Video Cross-Posting Framework](https://github.com/StructUK) *(profile page: open the pinned repo)* | [Video](categories/video.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | n8n, posting-provider adapters | Profile page; open the pinned repo named in the description |
| 43 | [Faceless Video Pipeline](https://n8n.io/workflows/6014) | [Video](categories/video.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | n8n, Gemini, ElevenLabs, Whisper, Shotstack | None |
| 44 | [Viral Video Clipper](https://github.com/lucaswalter/n8n-ai-automations) *(open the named workflow)* | [Video](categories/video.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | n8n, Vizard AI, Slack | Repo with several workflows; open the named workflow |
| 46 | [Research Automation (5 Academic APIs)](https://github.com/chidoziemanagwu/Research-Automation-Workflow) | [Paper](categories/paper.md) | <img src="../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | n8n, Groq, Sheets, Gmail | None |
<!-- PHASE_4:END -->
