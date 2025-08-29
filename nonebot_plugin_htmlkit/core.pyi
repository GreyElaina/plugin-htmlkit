"""
Type hints for core module of htmlkit.
"""

from typing import Callable, Any, Coroutine, Optional
import concurrent.futures
from types import TracebackType
import asyncio

def _init_fontconfig_internal() -> None:
    """
    Pre-initialize fontconfig with environment variables.

    Raises:
        RuntimeError: If fontconfig initialization fails.
    """

_ExceptionHandleFn = Callable[[BaseException, type[BaseException], TracebackType], None]
_AsyncioRunCoroutineThreadsafeFn = Callable[
    [Coroutine[Any, Any, Any], asyncio.AbstractEventLoop], concurrent.futures.Future[Any]
]
_UrlJoinFn = Callable[[str, str], str]
_FetchFn = Callable[[str], Coroutine[Any, Any, Optional[bytes]]]

def _render_internal(
    html_content: str,
    base_url: str,
    dpi: float,
    width: float,
    height: float,
    default_font_size: float,
    font_name: str,
    lang: str,
    culture: str,
    exception_fn: _ExceptionHandleFn,
    asyncio_run_coroutine_threadsafe: _AsyncioRunCoroutineThreadsafeFn,
    urljoin: _UrlJoinFn,
    loop: asyncio.AbstractEventLoop,
    img_fetch_fn: _FetchFn,
    css_fetch_fn: _FetchFn,
    /,
) -> asyncio.Future[bytes]: ...
