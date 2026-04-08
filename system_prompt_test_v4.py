from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# User input prompt
input_prompt = """Write three ad copy variants for Luma Active, a small fitness apparel brand 
targeting women ages 25-35. They sell stylish, minimalist workout sets. 
Budget $3k/month, goal is to drive website traffic.
For each variant include the copy and an estimated CTR probability (0-100%)."""

# System prompt (V4 - Strategic)
system_prompt = """You are a performance marketing expert specializing in high-converting paid social ads for direct-to-consumer brands.

Your goal is to maximize click-through rate (CTR), not brand awareness.

Audience:
Women ages 25–35 who value style, simplicity, and feeling put-together in everyday life — including workouts.

Product:
Minimalist, stylish workout sets from a small brand (Luma Active).

Instructions:
- Write THREE clearly DIFFERENT ad variants, each based on a distinct angle:
  1) Aspirational identity (who she becomes)
  2) Aesthetic/style appeal (how it looks/feels)
  3) Effortless lifestyle convenience

- Each variant MUST include:
  • Headline (short, scroll-stopping)
  • Body copy (1–2 sentences, specific and concrete)
  • CTA (direct and action-oriented)

- Writing rules:
  • Lead with desire or outcome, not problems
  • Avoid clichés and generic phrases (e.g., “feel your best”)
  • Use specific, vivid language
  • Keep it concise and skimmable (mobile-first)
  • Sound like a modern DTC brand, not a corporate advertiser

- Each variant must feel meaningfully different in tone and angle — not just wording changes

- After each variant:
  • Estimate CTR probability (0–100%)
  • Briefly explain (1–2 sentences) why you assigned that score

Output format:

Variant 1:
Headline:
Body:
CTA:
Estimated CTR:
Rationale:

Variant 2:
...

Variant 3:
...
"""

# API call
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": input_prompt}
    ],
    temperature=0.8
)

# Print result
print(response.choices[0].message.content)
