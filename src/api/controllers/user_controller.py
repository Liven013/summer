from fastapi import APIRouter
from api.controllers import BaseController
from api.models.requests.users import UserRequest

class UsersController(BaseController):
    private = APIRouter(
        prefix="/users",
        tags=["users"],
        dependencies=[],
    )
    public = APIRouter(
        prefix="/users",
        tags=["users"],
        dependencies=[],
    )

    @private.get("/")
    async def get_users():
        return
    
    @private.get("/{user_id}")
    async def get_user(user_id: int):
        return
    
    @private.post("/")
    async def create_user(body: UserRequest):
        return
    
    @private.patch("/{user_id}")
    async def update_user(user_id: int, body: UserRequest):
        return
    
    @private.delete("/{user_id}")
    async def delete_user(user_id: int):
        return
    
    

    @public.post("/signup")
    async def create_user(body: UserRequest):
        return
    
    @public.post("/login")
    async def login_user(body: UserLoginRequest):
        return
    
    @public.delete("/logout")
    async def logout_user():
        return