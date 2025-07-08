# agent.py
import asyncio
from agents import Agent, Runner
from .tools import (
    download_youtube_video,
    extract_youtube_transcript,
    search_google,
    execute_command,
    search_papers,
)

assistant = Agent(
    name="Research Assistant",
    instructions=(
        "Ты помогаешь искать информацию: умеешь работать с YouTube, веб-поиском, "
        "терминалом и ArXiv. Когда требуется действие — вызывай соответствующую тулу."
    ),
    model="gpt-4.1-mini",  # или любой ChatCompletion-совместимый
    tools=[
        download_youtube_video,
        extract_youtube_transcript,
        search_google,
        execute_command,
        search_papers,
    ],
)

async def main():
    res = await Runner.run(
        assistant,
        "Скачай видео https://www.youtube.com/watch?v=vXMDVnXGsW8 и пришли русские субтитры",
    )
    print(res.final_output)

if __name__ == "__main__":
    asyncio.run(main())
