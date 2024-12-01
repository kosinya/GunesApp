import os
import aiofiles

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import File, UploadFile, HTTPException, status

from media import model
from config import STATIC_FOLDER


async def upload_image(session: AsyncSession, file: UploadFile = File(...)):
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail='File must be an image')
    folder = os.path.join(STATIC_FOLDER, 'image')
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, file.filename)
    async with aiofiles.open(path, 'wb') as out:
        content = await file.read()
        await out.write(content)

    new_image = model.Image(
        filename=file.filename,
        path=path,
        url=STATIC_FOLDER + "/image/" + file.filename,
    )
    session.add(new_image)
    try:
        await session.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"File {new_image.filename} already exists")
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {'filename': file.filename, "path": path, 'url': new_image.url}


async def get_all_images(session: AsyncSession):
    images = await session.execute(select(model.Image))
    return images.scalars().all()


async def delete_image_by_id(session: AsyncSession, image_id: int):
    image = await session.execute(select(model.Image).where(model.Image.id == image_id))
    image = image.scalars().first()
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Image with id = {image_id} not found')
    os.remove(image.path)
    await session.delete(image)
    try:
        await session.commit()
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {'filename': image.filename, 'path': image.path, 'url': image.url}


async def upload_audio(session: AsyncSession, file: UploadFile = File(...)):
    if not file.content_type.startswith('audio/'):
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail='File must be an audio')
    folder = os.path.join(STATIC_FOLDER, 'audio')
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, file.filename)
    async with aiofiles.open(path, 'wb') as out:
        content = await file.read()
        await out.write(content)

    new_audio = model.Audio(
        filename=file.filename,
        path=path,
        url=STATIC_FOLDER + "/audio/" + file.filename,
    )
    session.add(new_audio)
    try:
        await session.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"File {new_audio.filename} already exists")
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {'filename': file.filename, "path": path, "url": new_audio.url}


async def get_all_audios(session: AsyncSession):
    audios = await session.execute(select(model.Audio))
    return audios.scalars().all()


async def delete_audio_by_id(session: AsyncSession, audio_id: int):
    audio = await session.execute(select(model.Audio).where(model.Audio.id == audio_id))
    audio = audio.scalars().first()
    if not audio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Audio with id = {audio_id} not found')
    os.remove(audio.path)
    await session.delete(audio)
    try:
        await session.commit()
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {'filename': audio.filename, 'path': audio.path, 'url': audio.url}


async def upload_video(session: AsyncSession, file: UploadFile = File(...)):
    if not file.content_type.startswith('video/'):
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail='File must be an video')
    folder = os.path.join(STATIC_FOLDER, 'video')
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, file.filename)
    async with aiofiles.open(path, 'wb') as out:
        content = await file.read()
        await out.write(content)

    new_video = model.Video(
        filename=file.filename,
        path=path,
        url=STATIC_FOLDER + "/video/" + file.filename,
    )
    session.add(new_video)
    try:
        await session.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"File {new_video.filename} already exists")
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {'filename': file.filename, "path": path, "url": new_video.url}


async def get_all_videos(session: AsyncSession):
    videos = await session.execute(select(model.Video))
    return videos.scalars().all()


async def delete_video_by_id(session: AsyncSession, video_id: int):
    video = await session.execute(select(model.Video).where(model.Video.id == video_id))
    video = video.scalars().first()
    if not video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Video with id = {video_id} not found')
    os.remove(video.path)
    await session.delete(video)
    try:
        await session.commit()
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {'filename': video.filename, 'path': video.path, 'url': video.url}
