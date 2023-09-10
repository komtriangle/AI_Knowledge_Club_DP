from fastapi import APIRouter
from pyspark.ml.recommendation import ALS, ALSModel
from pyspark.sql import SparkSession

router = APIRouter()

spark = SparkSession.builder \
    .master('local[*]') \
    .config("spark.driver.memory", "5g") \
    .config("spark.dynamicAllocation.minExecutors", "4")\
    .appName('Recommender_system') \
    .getOrCreate()

save_path = "C:\\Хакатоны\ЦП_НН\\"

model = ALSModel.load(f'{save_path}saved_model')


@router.get("/get_prediction")
async def get_prediction(user_id):
    return model.recommendForUserSubset([user_id], 10)
