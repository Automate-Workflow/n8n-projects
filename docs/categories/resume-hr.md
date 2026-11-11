# <img src="../../assets/icons/resume-hr.svg" alt="Resume and HR icon" width="40" height="40" align="absmiddle" /> Resume and HR Automation

[Back to Directory](../../README.md) | [Learning Path](../learning-path.md)

<!-- CATEGORY_META:START -->
- **Listed projects**: 6
- **Difficulty mix**: 2 Beginner, 3 Intermediate, 1 Advanced
- **Learning phases covered**: Phase 3 - Documents, Vision and Data
- **Latest dataset check date**: 2026-11-11
<!-- CATEGORY_META:END -->

## Overview

Resume and HR workflows streamline intake, parsing, structured extraction, document generation, and applicant triage. Recruiting teams and career tools use these pipelines to accept PDF resumes via n8n Forms or chat bots, convert unstructured CVs into normalized database records in Airtable, Supabase, or Google Sheets, and generate formatted feedback or tailored documents. Studying this category teaches document ingestion, multimodal PDF handling, and structured screening workflows.

## What You Will Learn

- Capturing candidate applications and PDF uploads directly through n8n Forms and chat triggers.
- Extracting structured applicant fields from PDFs using text extraction, multimodal Vision LLMs, and JSON parsers.
- Generating polished PDF outputs with external rendering services such as Gotenberg or LaTeX pipelines.
- Routing applicant summaries to Airtable, Google Sheets, Supabase, and HR notification channels.

## Prerequisites and Credentials

- An n8n instance with **n8n Forms** enabled (built-in) and credentials for your target store (**Google Sheets**, **Airtable**, or **Supabase**).
- An LLM or Vision LLM API key (OpenAI, Gemini, or equivalent).
- Optional helper services depending on the workflow: **Gotenberg** (Docker container for PDF rendering), **Telegram**, **WhatsApp**, or **Firecrawl**.

## Projects

<!-- PROJECTS:START -->
| ID | Title | Difficulty | Phase | Tools | Source type | Description | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | [Resume Bot](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/ResumeBot.json) | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n, Telegram, Supabase, LaTeX | GitHub file | Parses PDF resumes and builds tailored LaTeX resumes and cover letters | Handles personal data; review privacy and bias before use; Third-party template collected in a mirror repo; check original license |
| 12 | [CV Parsing with Multimodal Vision AI](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/CV%20Resume%20PDF%20Parsing%20with%20Multimodal%20Vision%20AI.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n, Vision LLM | GitHub file | Converts resume PDFs to images and assesses fit, with hidden-prompt protection | Handles personal data; review privacy and bias before use; Third-party template collected in a mirror repo; check original license |
| 13 | [Resume Data Extraction to PDF (Gotenberg)](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Extract%20data%20from%20resume%20and%20create%20PDF%20with%20Gotenberg.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n, LLM, Gotenberg | GitHub file | Extracts structured resume data and generates a formatted PDF | Handles personal data; review privacy and bias before use; Third-party template collected in a mirror repo; check original license |
| 14 | [Job Application Handling with n8n Forms](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Airtable/Handling%20Job%20Application%20Submissions%20with%20AI%20and%20n8n%20Forms.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n Forms, LLM, Airtable | GitHub file | Extracts resume info from submitted PDFs into structured records | Handles personal data; review privacy and bias before use; Third-party template collected in a mirror repo; check original license |
| 15 | [Screen Applicants with AI](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Screen%20Applicants%20With%20AI,%20notify%20HR%20and%20save%20them%20in%20a%20Google%20Sheet.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n, LLM, Google Sheets | GitHub file | Screens applicants, notifies HR and saves results to Sheets | Handles personal data; review privacy and bias before use; Third-party template collected in a mirror repo; check original license |
| 16 | [Internship Informer](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Internship%20Informer.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n, Telegram, Firecrawl, WhatsApp | GitHub file | Parses internship postings, filters eligibility and alerts on WhatsApp | Handles personal data; review privacy and bias before use; Third-party template collected in a mirror repo; check original license |
<!-- PROJECTS:END -->

## Suggested Order

1. Start with the **Beginner** intake workflows using n8n Forms, Airtable, and Google Sheets to see end-to-end applicant capture and storage.
2. Explore **Intermediate** workflows covering Gotenberg PDF generation, multimodal PDF-to-image CV parsing, and eligibility filtering.
3. Finish with the **Advanced** Telegram + Supabase + LaTeX Resume Bot to learn stateful storage and custom document compilation.

## Risks and Good Practice

- **Personal data and privacy (PII)**: Resumes contain names, addresses, phone numbers, and employment histories. Minimize data retention, store records in access-controlled databases, comply with GDPR or applicable local privacy laws, and avoid sending unredacted PII to unapproved LLM endpoints.
- **Bias and fairness**: LLM screening scores can reflect training biases or penalize non-standard resume layouts. Never rely on automated scores for final rejection decisions without qualified human review.
- **Prompt injection in resumes**: Candidates can embed hidden white-text instructions inside PDFs. Study multimodal PDF-to-image assessment and prompt-injection defense patterns, and treat extracted resume text strictly as untrusted data.
