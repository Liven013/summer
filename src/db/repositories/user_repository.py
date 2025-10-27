
from fastapi import Depends
from sqlalchemy import select

from gateways.database import get_db_connection


class UsersRepository:

    def __init__(self, db = Depends(get_db_connection)):
        self.db = db

    async def get_user_by_id(self, user_id: int):
        query = select(User).where(User.id == user_id)

        async with self.db as session:
            user = await session.exec(query).first()


        if not user:
            raise ValueError("User not found")
        return user