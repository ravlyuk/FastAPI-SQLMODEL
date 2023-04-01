async def add_like_or_dislike_service(post_like_create, postmodel, session):
    post_like_create = postmodel(post_id=post_like_create.post_id, user_id=post_like_create.user_id)
    session.add(post_like_create)
    await session.commit()
    await session.refresh(post_like_create)
    return post_like_create
