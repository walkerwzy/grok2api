from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse

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


@router.get("/admin/debug-paths", include_in_schema=False)
async def admin_debug_paths():
    return JSONResponse({
        "static_dir": str(STATIC_DIR),
        "static_exists": STATIC_DIR.exists(),
        "admin_login_exists": (STATIC_DIR / "admin/pages/login.html").exists(),
    })


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
