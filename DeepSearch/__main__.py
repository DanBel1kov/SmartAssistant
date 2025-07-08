# agent.py
import asyncio
from agents import Agent, Runner
from .tools import (
    download_youtube_video,
    extract_youtube_transcript,
    search_google,
    execute_command,
    search_papers,
    wiki_search,
    wiki_get_content,
    wiki_get_history,
    wiki_get_summary
)

assistant = Agent(
    name="Research Assistant",
    instructions=(
        "Ты помогаешь искать информацию, используй тулы для ответа"
    ),
    model="gpt-4.1-mini",  # или любой ChatCompletion-совместимый
    tools=[
        wiki_search,
        wiki_get_content,
        wiki_get_history,
        wiki_get_summary
    ],
)

async def main():
    res = await Runner.run(
        assistant,
        "How many studio albums were published by Mercedes Sosa between 2000 and 2009 (included)? You can use the latest 2022 version of english wikipedia.",
    )
    print(res.final_output)

if __name__ == "__main__":
    asyncio.run(main())
