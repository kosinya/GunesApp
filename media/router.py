from fastapi import APIRouter, UploadFile, File, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from media import service
from database import get_async_session
from auth.service import oauth2_scheme

router = APIRouter()


@router.post('/upload_image', tags=['image'])
async def upload_image(token: str = Depends(oauth2_scheme),
                       file: UploadFile = File(...), session: AsyncSession = Depends(get_async_session)):
    res = await service.upload_image(token, session, file)
    return JSONResponse(status_code=status.HTTP_200_OK, content=res)


@router.get('/get_images', tags=['image'])
async def get_images(session: AsyncSession = Depends(get_async_session)):
    return await service.get_all_images(session)


@router.delete('/delete_image', tags=['image'])
async def delete_image(token: str = Depends(oauth2_scheme),
                       session: AsyncSession = Depends(get_async_session), image_id: str = None):
    return await service.delete_image_by_id(token, session, int(image_id))


@router.post('/upload_audio', tags=['audio'])
async def upload_audio(token: str = Depends(oauth2_scheme),
                       file: UploadFile = File(...), session: AsyncSession = Depends(get_async_session)):
    res = await service.upload_audio(token, session, file)
    return JSONResponse(status_code=status.HTTP_200_OK, content=res)


@router.get('/get_audios', tags=['audio'])
async def get_audios(session: AsyncSession = Depends(get_async_session)):
    return await service.get_all_audios(session)


@router.delete('/delete_audio', tags=['audio'])
async def delete_audio(token: str = Depends(oauth2_scheme),
                       session: AsyncSession = Depends(get_async_session), audio_id: str = None):
    return await service.delete_audio_by_id(token, session, int(audio_id))


@router.post('/upload_video', tags=['video'])
async def upload_video(token: str = Depends(oauth2_scheme),
                       file: UploadFile = File(...), session: AsyncSession = Depends(get_async_session)):
    res = await service.upload_video(token, session, file)
    return JSONResponse(status_code=status.HTTP_200_OK, content=res)


@router.get('/get_videos', tags=['video'])
async def get_videos(session: AsyncSession = Depends(get_async_session)):
    return await service.get_all_videos(session)


@router.delete('/delete_video', tags=['video'])
async def delete_video(token: str = Depends(oauth2_scheme),
                       session: AsyncSession = Depends(get_async_session), video_id: str = None):
    return await service.delete_video_by_id(token, session, int(video_id))
