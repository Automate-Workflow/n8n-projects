# <img src="../../assets/icons/linkedin.svg" alt="LinkedIn icon" width="40" height="40" align="absmiddle" /> LinkedIn Automation

[Back to Directory](../../README.md) | [Learning Path](../learning-path.md)

<!-- CATEGORY_META:START -->
- **Listed projects**: 4
- **Difficulty mix**: 1 Intermediate, 3 Advanced
- **Learning phases covered**: Phase 4 - Advanced Agents and Integrations
- **Latest dataset check date**: 2026-11-11
<!-- CATEGORY_META:END -->

## Overview

LinkedIn workflows automate professional content drafting, multi-channel publishing, job-listing aggregation, and candidate research pipelines. Marketing teams use n8n to repurpose long-form videos or Notion content calendars into structured posts, while recruiting and job-search workflows combine external scraping or enrichment APIs with LLM scoring and spreadsheet or Notion tracking. These workflows illustrate multi-source data enrichment, prompt formatting for social copy, and scheduled publishing pipelines.

## What You Will Learn

- Pulling editorial drafts from Notion databases and transforming them into platform-ready posts via LLMs.
- Repurposing external media sources (such as YouTube transcripts) into structured social threads and posts.
- Aggregating job postings or public developer profiles (GitHub, LeetCode, resumes) and scoring candidate fit into Google Sheets or Notion.
- Sending formatted digest alerts to Telegram when high-scoring matches appear.

## Prerequisites and Credentials

- An n8n instance with **LinkedIn OAuth2** credentials (for official posting workflows) and/or workspace credentials for **Notion**, **Google Sheets**, and **Telegram**.
- LLM credentials (OpenAI, Claude, Gemini, or OpenRouter).
- For data enrichment or extraction workflows, external provider keys (such as Apify, ScrapingDog, or JotForm) if you choose to run those connectors.

## Projects

<!-- PROJECTS:START -->
| ID | Title | Difficulty | Phase | Tools | Source type | Description | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | [LinkedIn Job Alerts](https://github.com/simonleybovich/linkedin-job-alerts) | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, Gemini, Notion, Telegram | GitHub repo | Scrapes jobs, scores them against your CV, saves to Notion, alerts on Telegram | Scraping may conflict with LinkedIn terms; check before use |
| 8 | [LinkedIn Outreach with Notion and OpenAI](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Notion/Automate%20LinkedIn%20Outreach%20with%20Notion%20and%20OpenAI.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, Notion, OpenAI, LinkedIn | GitHub file | Pulls daily posts from Notion, formats them with OpenAI and posts to LinkedIn | Scraping may conflict with LinkedIn terms; check before use; Third-party template collected in a mirror repo; check original license |
| 9 | [Content Repurposing Factory](https://github.com/lucaswalter/n8n-ai-automations) *(open the named workflow)* | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, Apify, Claude | GitHub repo | Turns YouTube videos into X threads and LinkedIn posts | Scraping may conflict with LinkedIn terms; check before use; Repo with several workflows; open the named workflow |
| 10 | [TalentFlow AI](https://n8n.io/workflows/5099-talentflow-ai-instantly-evaluate-applicants-github-linkedin-using-ai/) | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, JotForm, ScrapingDog, Apify, OpenRouter | n8n.io template | Scores candidates from LinkedIn, GitHub, LeetCode and resume into Google Sheets | Scraping may conflict with LinkedIn terms; check before use |
<!-- PROJECTS:END -->

## Suggested Order

1. Begin with **Intermediate** editorial publishing workflows (pulling approved drafts from Notion and formatting posts).
2. Move to **Advanced** content-repurposing pipelines that turn video transcripts into drafts for human review.
3. Study the **Advanced** job-alert and multi-source candidate-scoring architectures last, paying close attention to rate limits and compliance gates.

## Risks and Good Practice

- **Terms of Service for scraping**: Automated scraping of LinkedIn profiles or job pages conflicts with LinkedIn's User Agreement and can lead to account suspension or IP blocks. Always verify platform terms, prefer official APIs or user-supplied inputs, and avoid running scrapers against your primary personal account.
- **Human-in-the-loop publishing**: Route LLM-generated posts through a Notion or Slack approval status before publishing to a company page to prevent off-brand messaging or hallucinations.
- **Fair evaluation**: When scoring candidates from public profiles and resumes, treat automated scores as triage aids only and review for bias before acting.
