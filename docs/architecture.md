# Architecture

Evercrew Local Telegram Task Bot is designed as the first example workflow of a future local AI workflow ecosystem for SMEs.

The goal is to keep the system simple, modular, local-first, and easy to extend.

## Core Idea

The Telegram bot is only a connector.

The real logic lives inside the workflow engine.

```text
Telegram
   |
Telegram Connector
   |
Workflow Engine
   |
Intent Detection
   |
Task Breakdown
   |
Approval Flow
   |
Telegram Connector
   |
Employee
