"""
LLM Interface

Handles communication with the local Ollama server.
"""

import ollama

from app.config import (
    OLLAMA_HOST,
    OLLAMA_MODEL
)


client = ollama.Client(host=OLLAMA_HOST)


def ask_llm(prompt: str) -> str:
    """
    Send a prompt to the Local LLM and return the response.
    """

    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    try:

        response = client.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt.strip()
                }
            ]
        )

    except Exception as e:

        raise RuntimeError(
            "Unable to connect to the Local AI.\n\n"
            "Please check:\n"
            "- Ollama is running\n"
            "- The model is installed\n"
            "- OLLAMA_HOST is correct\n\n"
            f"Reason: {str(e)}"
        )

    if "message" not in response:
        raise RuntimeError(
            "The Local AI returned an invalid response."
        )

    message = response["message"]

    if "content" not in message:
        raise RuntimeError(
            "The Local AI response does not contain any content."
        )

    content = message["content"].strip()

    if not content:
        raise RuntimeError(
            "The Local AI returned an empty response."
        )

    return content
