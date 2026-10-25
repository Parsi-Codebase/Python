from pydantic import BaseModel
class TopicExplanation(BaseModel):

    topic: str
    difficulty: str
    summary: str
    key_points: list[str]
    example: str
    real_world_usage: str