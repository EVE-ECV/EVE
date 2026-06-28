# Installation Guide

This guide explains how to install and run EVE locally.

## Requirements

- Python 3.10 or newer
- Ollama installed
- Telegram account
- Telegram bot token

## Step 1: Install Ollama

Download and install Ollama from:

https://ollama.com

## Step 2: Download a local model

Recommended:

```bash
ollama pull llama3.2:3b
```

For weaker computers:

```bash
ollama pull llama3.2:1b
```

## Step 3: Install Python dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Create environment file

Copy `.env.example` to `.env`.

Then update:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
OLLAMA_MODEL=llama3.2:3b
```

## Step 5: Test EVE without Telegram

Before connecting Telegram, test the workflow locally:

```bash
python app/test_workflow.py
```

## Current Status

At this stage, EVE can test a sample boss instruction and convert it into structured task information.

Telegram integration will be added next.
