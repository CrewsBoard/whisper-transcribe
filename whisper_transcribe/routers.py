from fastapi.routing import APIRouter

from whisper_transcribe.controllers import TranscribeController, WsController

routes: list[APIRouter] = [
    TranscribeController().router,
    WsController().router,
]
