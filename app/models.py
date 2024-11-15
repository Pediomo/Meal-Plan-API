from pydantic import BaseModel
from typing import List, Optional

class MealPlan(BaseModel):
    name: str
    description: Optional[str] = None
    meals: List[str]  # List of strings representing individual meals

class MealPlanInResponse(MealPlan):
    id: int  # Unique identifier for the meal plan


class MealPlanUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    meals: Optional[List[str]]
