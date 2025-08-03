from openai import AsyncOpenAI

client = AsyncOpenAI()

async def ask_ethalyn(prompt: str):
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content
