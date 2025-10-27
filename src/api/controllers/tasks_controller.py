
class TasksController:
    private = APIRouter(
        prefix="/tasks",
        tags=["tasks"],
        dependencies=[],
    )
    public = APIRouter(
        prefix="/tasks",
        tags=["tasks"],
        dependencies=[],
    )


    @public.get("/")
    async def get_tasks():
        return
    
    @public.get("/{task_id}")
    async def get_task(task_id: int):
        return
    
    @private.post("/")
    async def create_task(body: TaskRequest):
        return
    
    @private.patch("/{task_id}")
    async def update_task(task_id: int, body: TaskRequest):
        return
    
    @private.delete("/{task_id}")
    async def delete_task(task_id: int):
        return
    
