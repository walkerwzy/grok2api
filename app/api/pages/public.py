from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse

from app.core.auth import is_public_enabled

router = APIRouter()


def _find_static_dir():
    possible_paths = [
        Path(__file__).resolve().parents[2] / "static",
        Path(__file__).resolve().parents[4] / "static",
        Path("/var/task/app/static"),
        Path("/var/task/static"),
    ]
    for p in possible_paths:
        if p.exists():
            return p
    return possible_paths[0]


STATIC_DIR = _find_static_dir()


@router.get("/debug-paths", include_in_schema=False)
async def debug_paths():
    return JSONResponse({
        "static_dir": str(STATIC_DIR),
        "static_exists": STATIC_DIR.exists(),
        "public_login_exists": (STATIC_DIR / "public/pages/login.html").exists(),
        "admin_login_exists": (STATIC_DIR / "admin/pages/login.html").exists(),
    })


@router.get("/", include_in_schema=False)
async def root():
    if is_public_enabled():
        return RedirectResponse(url="/login")
    return RedirectResponse(url="/admin/login")


@router.get("/login", include_in_schema=False)
async def public_login():
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    file_path = STATIC_DIR / "public/pages/login.html"
    if not file_path.exists():
        return JSONResponse({"error": "Login page not available"})
    return FileResponse(file_path)


@router.get("/imagine", include_in_schema=False)
async def public_imagine():
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    file_path = STATIC_DIR / "public/pages/imagine.html"
    if not file_path.exists():
        return JSONResponse({"error": "Imagine page not available"})
    return FileResponse(file_path)


@router.get("/voice", include_in_schema=False)
async def public_voice():
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    file_path = STATIC_DIR / "public/pages/voice.html"
    if not file_path.exists():
        return JSONResponse({"error": "Voice page not available"})
    return FileResponse(file_path)


@router.get("/video", include_in_schema=False)
async def public_video():
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    file_path = STATIC_DIR / "public/pages/video.html"
    if not file_path.exists():
        return JSONResponse({"error": "Video page not available"})
    return FileResponse(file_path)


@router.get("/chat", include_in_schema=False)
async def public_chat():
    if not is_public_enabled():
        raise HTTPException(status_code=404, detail="Not Found")
    file_path = STATIC_DIR / "public/pages/chat.html"
    if not file_path.exists():
        return JSONResponse({"error": "Chat page not available"})
    return FileResponse(file_path)
