from agents import function_tool
from .youtube import yt_service

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
