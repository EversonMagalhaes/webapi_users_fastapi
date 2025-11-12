from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def read_root():
    return {"msg": "rota /users funcionando"}