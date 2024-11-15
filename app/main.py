from fastapi import FastAPI, HTTPException
from app.models import MealPlan, MealPlanInResponse
from typing import List


app = FastAPI()

# In-memory storage — The dictionary is populated with both dictionaries and instances of the MealPlanResponse. 
#Pydantic models are converted back to dictionaries before they are stored.
meal_plans = {
    1: {"id": 1, "name": "Plan One", "description": "Beleful Choice", "meals": ["Bread", "Egg", "Chocolate Drink"]},
    2: {"id": 2, "name": "Plan Two", "description": "A Balanced Plan", "meals": ["Amala", "Ewedu", "Smoothie"]},
    3: {"id": 3, "name": "Plan Three", "description": "Energy Boost", "meals": ["Beans", "Plantain", "Beverage"]},
    4: {"id": 4, "name": "Plan Four", "description": "Classic Combo", "meals": ["Eba", "Egusi Soup", "Zobo Drink"]},
    5: {"id": 5, "name": "Plan Five", "description": "Satisfying Feast", "meals": ["Pounded Yam", "White Soup", "Tigernut Milk"]},
    6: {"id": 6, "name": "Plan Six", "description": "Morning Start", "meals": ["Akara", "Pap", "Coffee"]},
    7: {"id": 7, "name": "Plan Seven", "description": "Weekend Delight", "meals": ["Moi Moi", "Fried Rice", "Chapman"]},
    8: {"id": 8, "name": "Plan Eight", "description": "Power Combo", "meals": ["Ofada Rice", "Ayamase Sauce", "Zobo"]},
    9: {"id": 9, "name": "Plan Nine", "description": "Balanced Diet", "meals": ["Yam Porridge", "Vegetables", "Palm Wine"]},
    10: {"id": 10, "name": "Plan Ten", "description": "Traditional Meal", "meals": ["Tuwo Shinkafa", "Miyan Kuka", "Kunu"]},
    11: {"id": 11, "name": "Plan Eleven", "description": "Quick Fix", "meals": ["Noodles", "Boiled Egg", "Orange Juice"]},
    12: {"id": 12, "name": "Plan Twelve", "description": "Protein Boost", "meals": ["Chicken Pepper Soup", "Yam", "Soya Milk"]},
    13: {"id": 13, "name": "Plan Thirteen", "description": "Classic Breakfast", "meals": ["Plantain", "Egg Sauce", "Tea"]},
    14: {"id": 14, "name": "Plan Fourteen", "description": "Comfort Meal", "meals": ["Jollof Rice", "Grilled Chicken", "Chapman"]},
    15: {"id": 15, "name": "Plan Fifteen", "description": "Sunday Special", "meals": ["Pounded Yam", "Vegetable Soup", "Palm Wine"]},
    16: {"id": 16, "name": "Plan Sixteen", "description": "Energizer", "meals": ["Beans", "Dodo", "Fruit Juice"]},
    17: {"id": 17, "name": "Plan Seventeen", "description": "Rich in Fiber", "meals": ["Okro Soup", "Eba", "Kunu"]},
    18: {"id": 18, "name": "Plan Eighteen", "description": "Quick Bites", "meals": ["Gala", "Sausage Roll", "Bottled Water"]},
    19: {"id": 19, "name": "Plan Nineteen", "description": "Festive Treat", "meals": ["Rice", "Fried Fish", "Malt"]},
    20: {"id": 20, "name": "Plan Twenty", "description": "Healthy Option", "meals": ["Salad", "Grilled Fish", "Fruit Juice"]},
    21: {"id": 21, "name": "Plan Twenty-One", "description": "Weekend Joy", "meals": ["Egusi Soup", "Fufu", "Palm Wine"]},
    22: {"id": 22, "name": "Plan Twenty-Two", "description": "Balanced Meal", "meals": ["Semo", "Okazi Soup", "Zobo"]},
    23: {"id": 23, "name": "Plan Twenty-Three", "description": "Full Day Meal", "meals": ["Spaghetti", "Meatballs", "Chapman"]},
    24: {"id": 24, "name": "Plan Twenty-Four", "description": "Nutritious Delight", "meals": ["Sweet Potatoes", "Egg Sauce", "Tea"]},
    25: {"id": 25, "name": "Plan Twenty-Five", "description": "Taste of Nigeria", "meals": ["Banga Soup", "Starch", "Palm Wine"]},
    26: {"id": 26, "name": "Plan Twenty-Six", "description": "Special Combo", "meals": ["Rice", "Stew", "Smoothie"]},
    27: {"id": 27, "name": "Plan Twenty-Seven", "description": "Energy Meal", "meals": ["Boiled Yam", "Egg Sauce", "Fruit Juice"]},
    28: {"id": 28, "name": "Plan Twenty-Eight", "description": "Snacky Day", "meals": ["Suya", "Cucumber Slices", "Water"]},
    29: {"id": 29, "name": "Plan Twenty-Nine", "description": "Traditional Delight", "meals": ["Oha Soup", "Pounded Yam", "Zobo"]},
    30: {"id": 30, "name": "Plan Thirty", "description": "Simple & Filling", "meals": ["Beans", "Yam", "Malt"]},
    31: {"id": 31, "name": "Plan Thirty-One", "description": "End of Month Treat", "meals": ["Fried Yam", "Pepper Sauce", "Zobo"]},
}
counter = 1

@app.get("/")
def read_root():
    return {"message": "Welcome to Peculiar's Meal Plan API for the Everyday Nigerian!"}


# Gets all meal plans
@app.get("/meal-plans", response_model=List[MealPlanInResponse])
def read_all_meal_plans():
    return list(meal_plans.values())

#Gets a specific meal plan
@app.get("/meal-plans/{meal_plan_id}", response_model=MealPlanInResponse)
def read_meal_plan(meal_plan_id: int):
    meal_plan = meal_plans.get(meal_plan_id)
    if not meal_plan:
        return {"error": "Meal plan not found"}
    return meal_plan


#Creates meal plans
@app.post("/meal-plans/", response_model=MealPlanInResponse)
def create_meal_plan(meal_plan: MealPlan):
    # Calculates the next available ID by getting the maximum current ID + 1
    new_id = max(meal_plans.keys(), default=0) + 1
    
    # Creates a new meal plan with the calculated ID
    meal_plan_in_response = MealPlanInResponse(id=new_id, **meal_plan.model_dump())
    
    # Stores the new meal plan in the meal_plans dictionary
    meal_plans[new_id] = meal_plan_in_response
    
    return meal_plan_in_response


#Updates meal plans
@app.put("/meal-plans/{id}")
async def update_meal_plan(id: int, updated_meal_plan: MealPlanInResponse):
    meal_plan_data = meal_plans.get(id)
    if meal_plan_data is None:
        raise HTTPException(status_code=404, detail="Meal plan not found")

    # Converts the Pydantic model to a dictionary and updates it
    meal_plan_dict = meal_plan_data.model_dump()  # Converts
    meal_plan_dict.update(updated_meal_plan.model_dump())  # Updates

    
    # Rebuilds the meal plan from the updated dictionary
    updated_plan = MealPlanInResponse(**meal_plan_dict)  # Directly use the dictionary
    meal_plans[id] = updated_plan  # Replaces the old plan with the updated one
 
    
    return updated_plan





@app.delete("/meal-plans/{id}", response_model=MealPlanInResponse)
def delete_meal_plan(id: int):
    for plan_id, plan in meal_plans.items():
        print(f"Plan Type: {type(plan)}")  
        
        if isinstance(plan, dict):  # If it's a dictionary, proceeds as usual
            if plan["id"] == id:
                deleted_plan = plan
                del meal_plans[plan_id]
                return MealPlanInResponse(**deleted_plan)  # Returns Pydantic model after converting the dictionary
            
        elif isinstance(plan, MealPlanInResponse):  # If it's a Pydantic model
            plan_model_dump = plan.model_dump()  # Uses model_dump to get dictionary representation
            if plan_model_dump["id"] == id:
                del meal_plans[plan_id]
                return plan  # Returns the Pydantic model directly
            
        else:
            print(f"Unexpected type found: {plan}")  
    
    raise HTTPException(status_code=404, detail="Meal Plan not found")







