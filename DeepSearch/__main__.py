# agent.py
import asyncio
from agents import Agent, Runner
from tools import download_youtube_video, extract_youtube_transcript

assistant = Agent(
    name="YouTube Assistant",
    instructions=(
        "Ты помогаешь работать с YouTube: скачиваешь видео и достаёшь субтитры. "
        "Когда нужно действие — вызывай соответствующий инструмент."
    ),
    model="gpt-4.1-mini",  # или любой ChatCompletion-совместимый
    tools=[download_youtube_video, extract_youtube_transcript],
    # можно задать temperature, guardrails, tracing и др.
)

async def main():
    res = await Runner.run(
        assistant,
        "Скачай видео https://youtu.be/dQw4w9WgXcQ и пришли русские субтитры",
    )
    print(res.final_output)

if __name__ == "__main__":
    asyncio.run(main())
