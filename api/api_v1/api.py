import os.path

from fastapi import APIRouter, Request
from starlette.responses import FileResponse

from api.api_v1.endpoints import users, posts, oauth2
from core import get_settings

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(posts.router, prefix="/posts", tags=["posts"])
router.include_router(oauth2.router, prefix="/oauth2", tags=["oauth2"])


@router.post("/")
async def index(request: Request):
    return {"body": await request.body()}


@router.get("/files/{image}", include_in_schema=False)  # excluding as it is not jsonschema part
async def serve_image(image: str):
    return FileResponse(os.path.join(get_settings().MEDIA_ROOT, image))
