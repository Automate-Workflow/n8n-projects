# <img src="../../assets/icons/computer-vision.svg" alt="Computer Vision icon" width="40" height="40" align="absmiddle" /> Computer Vision

[Back to Directory](../../README.md) | [Learning Path](../learning-path.md)

<!-- CATEGORY_META:START -->
- **Listed projects**: 4
- **Difficulty mix**: 3 Intermediate, 1 Advanced
- **Learning phases covered**: Phase 3 - Documents, Vision and Data, Phase 4 - Advanced Agents and Integrations
- **Latest dataset check date**: 2026-11-11
<!-- CATEGORY_META:END -->

## Overview

Computer vision workflows move beyond descriptive captions into structured visual extraction, security inspection, OCR pipelines, and object-detection inference. Practical industry applications include vehicle gate/parking license-plate reading, automated phishing detection from email screenshots, document-to-CSV digitization, and invoking YOLO object detection models from AI agents. These projects demonstrate how n8n combines multimodal foundation models with specialized self-hosted vision inference servers.

## What You Will Learn

- Accepting image uploads via n8n Forms and extracting exact alphanumeric identifiers (such as license plates) with Vision LLMs.
- Combining email header inspection with ChatGPT Vision screenshot analysis to triage suspected phishing messages.
- Routing mixed PDF and image files to Vertex AI Gemini for structured OCR output into CSV files.
- Connecting n8n AI agents to a containerized **Ultralytics YOLO MCP server** for object detection, training, and batch prediction.

## Prerequisites and Credentials

- Credentials for a Vision LLM (**OpenAI Vision** or **Google Vertex AI Gemini**) and optional **Gmail** / **n8n Forms**.
- Docker environment if deploying the **Ultralytics YOLO MCP server** locally (GPU recommended for training or high-throughput inference).

## Projects

<!-- PROJECTS:START -->
| ID | Title | Difficulty | Phase | Tools | Source type | Description | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 36 | [License Plate Extraction](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Extract%20license%20plate%20number%20from%20image%20uploaded%20via%20an%20n8n%20form.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n Forms, vision LLM | GitHub file | Extracts plate numbers from uploaded images | Third-party template collected in a mirror repo; check original license |
| 37 | [Phishing Email Analysis with Vision](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/Analyze%20Suspicious%20Email%20Contents%20with%20ChatGPT%20Vision.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n, Gmail, ChatGPT Vision | GitHub file | Analyses email screenshots and headers to flag phishing | Third-party template collected in a mirror repo; check original license |
| 38 | [OCR from PDFs and Images to CSV](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Extract%20text%20from%20PDF%20and%20image%20using%20Vertex%20AI%20(Gemini)%20into%20CSV.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n, Vertex AI Gemini | GitHub file | Routes by file type and extracts text into CSV | Third-party template collected in a mirror repo; check original license |
| 39 | [Ultralytics YOLO MCP Server](https://github.com/MetehanYasar11/ultralytics_mcp_server) | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | Docker, YOLO, MCP, n8n | GitHub repo | Object detection, training and batch prediction callable from n8n | None |
<!-- PROJECTS:END -->

## Suggested Order

1. Start with the **Intermediate** Vision LLM pipelines to learn form-based extraction, security screenshot analysis, and mixed-document OCR to CSV.
2. Advance to **Advanced** containerized MCP inference servers to explore calling dedicated local computer-vision tools from n8n.

## Risks and Good Practice

- **Accuracy and false positives**: Vision OCR and phishing classifiers can misread blurry characters or misclassify legitimate marketing emails. Require confidence checks or human confirmation before blocking senders, issuing access, or posting accounting CSVs.
- **Untrusted visual inputs**: Isolate inference containers (such as Dockerized YOLO servers), enforce strict file-size and format checks, and strip EXIF metadata if storing user uploads.
- **Privacy on captured frames**: License plates and email screenshots frequently contain PII; mask sensitive regions or limit retention timelines in accordance with privacy rules.
