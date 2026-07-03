import anthropic

client = anthropic.Anthropic(api_key="your-api-key")  # or set ANTHROPIC_API_KEY env var

# ── 1. Basic message ──────────────────────────────────────────────────────────
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude!"}],
)
print(message.content[0].text)


# ── 2. System prompt ──────────────────────────────────────────────────────────
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system="You are a helpful Python tutor. Be concise.",
    messages=[{"role": "user", "content": "What is a list comprehension?"}],
)
print(message.content[0].text)


# ── 3. Multi-turn conversation ────────────────────────────────────────────────
conversation = []

def chat(user_input):
    conversation.append({"role": "user", "content": user_input})
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=conversation,
    )
    reply = response.content[