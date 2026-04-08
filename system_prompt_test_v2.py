from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

input_prompt = """Write three ad copy variants for a small fitness apparel brand 
targeting women ages 25-35, budget $3k/month, goal is to drive website traffic. 
For each variant include the copy and an estimated CTR probability (0-100%)."""

system_prompts = {
    "V1": "You are an advertising assistant. Write compelling ad copy that gets people to click.",
    
    "V2": "You are a senior advertising strategist with 20 years of experience driving high CTR campaigns for direct-to-consumer brands. Write ad copy that is specific, persuasive, and optimized for clicks.",
    
    "V3_REVISED": "You are a senior advertising strategist with 20 years of experience driving high CTR campaigns for direct-to-consumer brands. You understand that women 25-35 respond to authenticity over hype. You always write copy that leads with an aspiration or desire — never a problem or negative framing. Use clear, direct, positive language and end with a strong call to action. Format your response as three variants, each with the copy and your estimated CTR probability."
}

for version, system_prompt in system_prompts.items():
    print(f"\n{'='*50}")
    print(f"SYSTEM PROMPT {version}")
    print(f"{'='*50}")
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input_prompt}
        ]
    )
    
    print(response.choices[0].message.content)
