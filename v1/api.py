from fastapi import APIRouter

router = APIRouter()


@router.get("/get_prediction")
async def get_prediction(user_id):
    return {"message": "Hello World"}
