# Evercrew Local Telegram Task Bot

A free local LLM Telegram workflow that helps SME bosses turn messy instructions into clear employee tasks.

Built by **Evercrew Venture Pte Ltd**, Singapore.

## What this workflow does

Boss sends a message in Telegram.

The local LLM checks whether the message is a task instruction.

If yes, the bot confirms with the boss first.

After confirmation, the bot rewrites the instruction into simple steps for the employee.

## Example

Boss says:

> Ask Ah Tan to prepare the June sales report and send it to me by Friday.

Bot confirms:

> Do you want to assign this task?
>
> Employee: Ah Tan  
> Task: Prepare June sales report  
> Deadline: Friday

Employee receives:

1. Prepare the June sales report.
2. Check the figures.
3. Send the completed report to boss by Friday.
4. Reply DONE when completed.

## Why local LLM?

This project is designed for SMEs that want simple AI workflow automation without sending internal instructions to cloud AI services.

Recommended local models:

- llama3.2:1b
- llama3.2:3b
- gemma3:1b
- qwen small models

## Version 1 Features

- Telegram bot
- Local LLM via Ollama
- Boss intent confirmation
- Task breakdown
- Employee task message
- Simple DONE reply

## Tech Stack

- Python
- Telegram Bot API
- Ollama
- Local LLM

## Status

This project is currently in early development.

## About Evercrew

Evercrew Venture Pte Ltd helps Singapore SMEs deploy practical AI workflow automation, local LLM tools, AI assistants, and business automation systems.

Website: https://evercrew.ai/
