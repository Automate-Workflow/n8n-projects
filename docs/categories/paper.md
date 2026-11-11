# <img src="../../assets/icons/paper.svg" alt="Research Papers icon" width="40" height="40" align="absmiddle" /> Research Papers and Document Intelligence

[Back to Directory](../../README.md) | [Learning Path](../learning-path.md)

<!-- CATEGORY_META:START -->
- **Listed projects**: 6
- **Difficulty mix**: 1 Beginner, 4 Intermediate, 1 Advanced
- **Learning phases covered**: Phase 1 - Foundations, Phase 2 - Chatbots and Voice, Phase 3 - Documents, Vision and Data, Phase 4 - Advanced Agents and Integrations
- **Latest dataset check date**: 2026-11-11
<!-- CATEGORY_META:END -->

## Overview

Research paper and document intelligence workflows fetch academic publications, parse long PDFs into embeddings or structured summaries, answer questions with quoted citations, and extract structured fields from dense documents. Researchers, engineering teams, and analysts use these pipelines to track Hugging Face daily papers into Notion, query multiple academic APIs for automated literature reviews, summarize arXiv preprints on demand, and extract structured invoice tables via LlamaParse. Note that this category in `data/n8n_list.csv` includes both academic paper pipelines and PDF/invoice document-parsing workflows that share the same RAG and structured-extraction architecture.

## What You Will Learn

- Querying Hugging Face, arXiv, and multi-source academic APIs and scoring paper relevance automatically.
- Chunking PDFs into vector embeddings for source-quoted retrieval-augmented generation (RAG).
- Designing Telegram and webhook interfaces where users upload PDFs or pass arXiv IDs for structured answers.
- Using specialized document parsers (**LlamaParse**) paired with structured output parsers to extract clean tabular records from complex PDFs and invoices.

## Prerequisites and Credentials

- Credentials for LLM and embedding providers (**OpenAI**, **Groq**, or compatible models) plus optional **LlamaParse** API access.
- Storage or destination credentials (**Notion**, **Google Sheets**, **Gmail**, **Telegram**, or a vector database configured in n8n).

## Projects

<!-- PROJECTS:START -->
| ID | Title | Difficulty | Phase | Tools | Source type | Description | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 45 | [Hugging Face Papers to Notion](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Notion/Analyse%20papers%20from%20Hugging%20Face%20with%20AI%20and%20store%20them%20in%20Notion.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n, Hugging Face, LLM, Notion | GitHub file | Fetches and analyses papers, stores structured data in Notion | Third-party template collected in a mirror repo; check original license |
| 46 | [Research Automation (5 Academic APIs)](https://github.com/chidoziemanagwu/Research-Automation-Workflow) | <img src="../../assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](../learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, Groq, Sheets, Gmail | GitHub repo | Queries academic APIs, extracts insights, scores relevance and emails a report | None |
| 47 | [arXiv Paper Summariser](https://n8n.io/workflows/2904-arxiv-paper-summarization-with-chatgpt/) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n, webhook, ChatGPT | n8n.io template | Takes an arXiv ID and returns a structured summary | None |
| 48 | [Chat with PDF (quoting sources)](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Chat%20with%20PDF%20docs%20using%20AI%20(quoting%20sources).json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](../learning-path.md#phase-2---chatbots-and-voice) | n8n, embeddings, vector store | GitHub file | Q&A over a PDF with quoted sources | Third-party template collected in a mirror repo; check original license |
| 49 | [Telegram Chat with PDF](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20chat%20with%20PDF.json) | <img src="../../assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](../learning-path.md#phase-1---foundations) | n8n, Telegram, LLM | GitHub file | Upload a PDF in Telegram and ask questions | Third-party template collected in a mirror repo; check original license |
| 50 | [Invoice Extraction (LlamaParse + OpenAI)](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Invoice%20data%20extraction%20with%20LlamaParse%20and%20OpenAI.json) | <img src="../../assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](../learning-path.md#phase-3---documents-vision-and-data) | n8n, LlamaParse, OpenAI | GitHub file | Extracts structured invoice data with a structured output parser | Third-party template collected in a mirror repo; check original license |
<!-- PROJECTS:END -->

## Suggested Order

1. Start with the **Beginner** chat-with-PDF workflow to learn simple PDF upload and Q&A.
2. Progress to **Intermediate** workflows covering source-quoted RAG, preprint summarization, paper-to-Notion tracking, and structured document extraction.
3. Finish with **Advanced** multi-API research pipelines to see parallel academic querying, relevance scoring, and automated email reporting.

## Risks and Good Practice

- **Hallucinated citations and numbers**: LLMs can fabricate quotes, DOIs, or numeric line items when summaries exceed context limits. Always enforce source-quoting prompts, validate structured schemas, and verify extracted invoice totals independently before financial use.
- **Academic API rate limits**: Respect arXiv, Semantic Scholar, and Hugging Face API rate limits by caching responses and spacing batch queries.
- **Document confidentiality**: Avoid uploading proprietary invoices, unpublished manuscripts, or confidential PDFs to unapproved third-party cloud parsers without verifying data-retention terms.
