from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse

router = APIRouter()

STATIC_DIR = Path(__file__).resolve().parents[2] / "static"


def _serve_page(file_path: Path):
    if not file_path.exists():
        return JSONResponse({"error": "Page not available"})
    return FileResponse(file_path)


@router.get("/admin", include_in_schema=False)
async def admin_root():
    return RedirectResponse(url="/admin/login")


@router.get("/admin/login", include_in_schema=False)
async def admin_login():
    return _serve_page(STATIC_DIR / "admin/pages/login.html")


@router.get("/admin/config", include_in_schema=False)
async def admin_config():
    return _serve_page(STATIC_DIR / "admin/pages/config.html")


@router.get("/admin/cache", include_in_schema=False)
async def admin_cache():
    return _serve_page(STATIC_DIR / "admin/pages/cache.html")


@router.get("/admin/token", include_in_schema=False)
async def admin_token():
    return _serve_page(STATIC_DIR / "admin/pages/token.html")
