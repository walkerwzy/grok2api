from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse

from app.core.auth import is_public_enabled

router = APIRouter()


def _find_static_dir():
    possible_paths = [
        Path(__file__).resolve().parents[2] / "static",
        Path(__file__).resolve().parents[4] / "static",
    ]
    for p in possible_paths:
        if p.exists():
            return p
    return possible_paths[0]


def _get_public_dir(static_dir: Path):
    public_dir = static_dir / "public"
    if public_dir.exists():
        return public_dir
    return static_dir / "public_page"


STATIC_DIR = _find_static_dir()
PUBLIC_DIR = _get_public_dir(STATIC_DIR)


@router.get("/", include_in_schema=False)
async def root():
    if is_public_enabled():
        return RedirectResponse(url="/login")
    return RedirectResponse(url="/admin/login")


@router.get("/login", include_in_schema=False)
async def public_login():
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    file_path = PUBLIC_DIR / "pages/login.html"
    if not file_path.exists():
        return JSONResponse({"error": "Login page not available"})
    return FileResponse(file_path)


@router.get("/imagine", include_in_schema=False)
async def public_imagine():
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    file_path = PUBLIC_DIR / "pages/imagine.html"
    if not file_path.exists():
        return JSONResponse({"error": "Imagine page not available"})
    return FileResponse(file_path)


@router.get("/voice", include_in_schema=False)
async def public_voice():
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    file_path = PUBLIC_DIR / "pages/voice.html"
    if not file_path.exists():
        return JSONResponse({"error": "Voice page not available"})
    return FileResponse(file_path)


@router.get("/video", include_in_schema=False)
async def public_video():
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    file_path = PUBLIC_DIR / "pages/video.html"
    if not file_path.exists():
        return JSONResponse({"error": "Video page not available"})
    return FileResponse(file_path)


@router.get("/chat", include_in_schema=False)
async def public_chat():
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    file_path = PUBLIC_DIR / "pages/chat.html"
    if not file_path.exists():
        return JSONResponse({"error": "Chat page not available"})
    return FileResponse(file_path)
