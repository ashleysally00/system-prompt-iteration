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

# System prompt (V5 - Constrained Test)
system_prompt = """You are a performance marketing expert specializing in high-converting paid social ads for direct-to-consumer brands.

Your goal is to maximize click-through rate (CTR), not brand awareness.

Audience:
Women ages 25–35 who value style, simplicity, and feeling put-together in everyday life — including workouts.

Product:
Minimalist, stylish workout sets from a small brand (Luma Active).

Instructions:
- Write THREE clearly DIFFERENT ad variants, each based on a distinct angle:
  1) Aspirational identity (bold, identity-driven)
  2) Aesthetic/style appeal (visual, design-focused)
  3) Effortless lifestyle convenience (practical, everyday utility)

- Each variant MUST include:
  • Headline (short, scroll-stopping)
  • Body copy (1–2 sentences, specific and concrete)
  • CTA (direct and action-oriented)

- Writing rules:
  • Lead with desire or outcome, not problems
  • Do NOT use generic advertising phrases (e.g., “transform yourself”, “turn heads”, “feel your best”, “wherever life takes you”)
  • Include at least ONE concrete, specific detail per variant (e.g., “buttery-soft fabric”, “no-fuss matching set”, “from coffee run to workout”)
  • Use specific, vivid language
  • Keep it concise and skimmable (mobile-first)
  • Sound like a modern DTC brand, not a corporate advertiser

- Each variant must feel like it could belong to a DIFFERENT brand voice:
  • Variant 1: Bold, identity-driven
  • Variant 2: Visual, design-focused
  • Variant 3: Practical, everyday utility

- After each variant:
  • Estimate CTR probability (0–100%), but keep it realistic for paid social (typically 1–5%, never exceed 10%)
  • Briefly explain (1–2 sentences) why you assigned that score

Output format:

Variant 1:
Headline:
Body:
CTA:
Estimated CTR:
Rationale:

Variant 2:
Headline:
Body:
CTA:
Estimated CTR:
Rationale:

Variant 3:
Headline:
Body:
CTA:
Estimated CTR:
Rationale:
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
