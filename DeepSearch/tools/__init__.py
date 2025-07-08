from agents import function_tool
import os
from dotenv import load_dotenv
from ..base import ActionArguments
from .youtube import yt_service
from .search import SearchCollection
from .terminal import TerminalActionCollection
from .mcparxiv import ArxivActionCollection
from .wiki import WikipediaCollection

load_dotenv()

search_service = SearchCollection(
    ActionArguments(
        name="search_service",
        transport="stdio",
        workspace=os.getenv("AWORLD_WORKSPACE", "~"),
    )
)

terminal_service = TerminalActionCollection(
    ActionArguments(
        name="terminal_service",
        transport="stdio",
        workspace=os.getenv("AWORLD_WORKSPACE", "~"),
    )
)

arxiv_service = ArxivActionCollection(
    ActionArguments(
        name="arxiv_service",
        transport="stdio",
        workspace=os.getenv("AWORLD_WORKSPACE", "~"),
    )
)

wiki_service = WikipediaCollection(
    ActionArguments(
        name="wiki_service",
        transport="stdio",
        workspace=os.getenv("AWORLD_WORKSPACE", "~"),
    )
)

@function_tool(name_override="download_youtube_video")
async def download_youtube_video(
        url: str,
        timeout: int = 180,
        output_format: str = "markdown",
) -> str:
    """Скачивает ролик с YouTube и возвращает LLM-friendly описание результата."""
    res = await yt_service.mcp_download_youtube_video(
        url=url, timeout=timeout, output_format=output_format
    )
    return res.message  # → markdown / plain text / json

@function_tool(name_override="extract_youtube_transcript")
async def extract_youtube_transcript(
        video_id: str,
        language_code: str = "en",
        translate_to_language: str | None = None,
        output_format: str = "markdown",
) -> str:
    """Достаёт (и опционально переводит) субтитры YouTube-видео."""
    res = await yt_service.mcp_extract_youtube_transcript(
        video_id=video_id,
        language_code=language_code,
        translate_to_language=translate_to_language,
        output_format=output_format,
    )
    return res.message


@function_tool(name_override="search_google")
async def search_google(
        query: str,
        num_results: int = 5,
        safe_search: bool = True,
        language: str = "en",
        country: str = "us",
        output_format: str = "markdown",
) -> str:
    """Выполняет веб-поиск через Google Custom Search API."""
    res = search_service.mcp_search_google(
        query=query,
        num_results=num_results,
        safe_search=safe_search,
        language=language,
        country=country,
        output_format=output_format,
    )
    return res.message


@function_tool(name_override="execute_command")
async def execute_command(
        command: str,
        timeout: int = 30,
        output_format: str = "markdown",
) -> str:
    """Выполняет команду терминала с таймаутом."""
    res = await terminal_service.mcp_execute_command(
        command=command,
        timeout=timeout,
        output_format=output_format,
    )
    return res.message


@function_tool(name_override="search_papers")
async def search_papers(
        query: str,
        max_results: int = 5,
        sort_by: str = "relevance",
        sort_order: str = "descending",
        output_format: str = "markdown",
) -> str:
    """Ищет статьи на ArXiv по заданному запросу."""
    res = await arxiv_service.mcp_search_papers(
        query=query,
        max_results=max_results,
        sort_by=sort_by,
        sort_order=sort_order,
        output_format=output_format,
    )
    return res.message

@function_tool(name_override="wiki_search")
def wiki_search(
        query: str,
        limit: int = 5,
        language: str = "en",
        output_format: str = "markdown",
) -> str:
    """Search Wikipedia articles and return formatted list of hits."""
    resp = wiki_service.mcp_search_wikipedia(
        query=query,
        limit=limit,
        language=language,
        output_format=output_format,
    )
    return resp.message


@function_tool(name_override="wiki_get_summary")
def wiki_get_summary(
        title: str,
        sentences: int = 5,
        language: str = "en",
        output_format: str = "markdown",
) -> str:
    """Fetch brief summary of a Wikipedia article."""
    resp = wiki_service.mcp_get_article_summary(
        title=title,
        sentences=sentences,
        language=language,
        output_format=output_format,
    )
    return resp.message


@function_tool(name_override="wiki_get_content")
def wiki_get_content(
        title: str,
        language: str = "en",
        include_full_content: bool = True,
        output_format: str = "markdown",
) -> str:
    """Retrieve full content of a Wikipedia article."""
    resp = wiki_service.mcp_get_article_content(
        title=title,
        language=language,
        include_full_content=include_full_content,
        output_format=output_format,
    )
    return resp.message


@function_tool(name_override="wiki_get_history")
def wiki_get_history(
        title: str,
        date: str,
        language: str = "en",
        auto_suggest: bool = False,
        output_format: str = "markdown",
) -> str:
    """Get the revision of an article closest to a given date (YYYY/MM/DD)."""
    resp = wiki_service.mcp_get_article_history(
        title=title,
        date=date,
        language=language,
        auto_suggest=auto_suggest,
        output_format=output_format,
    )
    return resp.message