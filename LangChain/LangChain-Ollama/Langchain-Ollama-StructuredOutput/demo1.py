from pydantic import BaseModel
class TopicExplanation(BaseModel):
    topic:str
    difficulty:str
    summary:str
    key_points:list[str]
result=TopicExplanation(
    topic='FastAPI',
    difficulty="Biginner",
    summary='A Modern python framework for building APIs',
    key_points=[
        "Fast",
        'Type-safe validation',
        'Automatic API documentation'
    ]
)
print(result)
# access the individual fields
print(result.topic)
print(result.difficulty)
print(result.summary)
print(result.key_points)