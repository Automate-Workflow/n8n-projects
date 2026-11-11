# Getting Started with n8n

This guide explains how to run a local isolated n8n instance, import third-party workflow JSON files safely, and configure credentials without exposing secrets.

## 1. Install n8n Locally

Running n8n locally keeps your experiments separate from any production instance.

### Option A: Docker (Recommended)

Docker isolates n8n, pins versions cleanly, and persists workflows and encrypted credentials in a named volume.

```bash
docker volume create n8n_data

docker run -it --rm \
  --name n8n-local \
  -p 5678:5678 \
  -e GENERIC_TIMEZONE="UTC" \
  -e N8N_ENCRYPTION_KEY="replace-with-a-random-32-char-secret" \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

For multi-step projects that also require local helper containers (such as Gotenberg, Ollama, WAHA, or an MCP server), create a `compose.yaml` file on a shared Docker network:

```yaml
services:
  n8n:
    image: docker.n8n.io/n8nio/n8n:latest
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - N8N_ENCRYPTION_KEY=replace-with-a-random-32-char-secret
      - N8N_SECURE_COOKIE=false
    volumes:
      - n8n_data:/home/node/.n8n

volumes:
  n8n_data:
```

Start the stack with `docker compose up -d` and open `http://localhost:5678` in your browser.

### Option B: Node.js and npm

If you already have Node.js LTS installed, launch n8n directly using `npx`:

```bash
npx n8n
```

Or install globally:

```bash
npm install -g n8n
n8n start
```

Open `http://localhost:5678` once initialization completes.

## 2. Import a Workflow JSON

Projects in this directory link to external GitHub files, repositories, or `n8n.io` template pages:

1. Open the linked project URL.
   - For **GitHub file** links, click **Raw** (or download the `.json` file).
   - For **GitHub repo** links marked *open the named workflow*, open the specified `.json` file inside that repository.
   - For **GitHub profile (pinned repo)** links, open the pinned repository named in the project title or description.
   - For **n8n.io template** links, click **Use for free** or **Copy template to clipboard**.
2. In your local n8n editor, create a new workflow.
3. Open the workflow menu (top-right ellipsis) and choose **Import from File** (or paste copied JSON directly onto the canvas with `Ctrl+V` / `Cmd+V`).
4. Keep the workflow **Inactive** while inspecting nodes.

## 3. Audit Nodes Before Running

Before adding credentials or clicking **Execute Workflow**, review:

- **Code** and **Execute Command** nodes: verify what JavaScript, Python, or shell commands run.
- **HTTP Request** nodes: confirm all outbound URLs point only to expected APIs.
- **Community nodes**: verify package names and maintenance history before installing external npm community nodes.

For full security hygiene, see [SECURITY.md](../SECURITY.md).

## 4. Configure Credentials Safely

Never hard-code API keys, bearer tokens, or passwords inside HTTP headers or Code nodes.

1. Open **Credentials** in the n8n left sidebar and create scoped test credentials (OpenAI, Gemini, Telegram, Gmail, Notion, or Google Sheets).
2. Re-bind each placeholder credential inside the imported nodes to your local credential record.
3. Prefer test accounts, sandbox phone numbers, or dummy spreadsheets over live production workspaces.
4. Keep `N8N_ENCRYPTION_KEY` backed up safely in a password manager (never commit `.env` or encryption keys to Git).

## 5. Test with Sample Data

1. Pin sample test input on the trigger node (or trigger a manual webhook with `curl` or test payload) before activating schedules or live webhooks.
2. Run node-by-node execution and inspect the JSON output items in each step.
3. Enable an **Error Workflow** (`Settings -> Error Workflow`) before promoting any pattern to long-running use.

Next step: browse the four-stage progression in [Learning Path](learning-path.md).
