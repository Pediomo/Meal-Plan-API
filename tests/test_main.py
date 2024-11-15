from fastapi.testclient import TestClient
from app.main import app, meal_plans, MealPlanInResponse

client = TestClient(app)

# Prefilled test data
meal_plans[32] = MealPlanInResponse(name="Plan Thirty-Two", description="Beleful Choice", meals=["Rice"], id=32)

def test_update_meal_plan_success():
    """Test updating a meal plan successfully"""
    update_data = {
        "id": 32,  
        "name": "Updated Plan",
        "description": "Updated Description",
        "meals": ["Jollof Rice"]
    }

    response = client.put("/meal-plans/32", json=update_data)
    print(response.json())  # Debugging line to inspect response
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Plan"
    assert data["description"] == "Updated Description"
    assert data["meals"] == ["Jollof Rice"]
    assert data["id"] == 32  # Ensured 'id' remained unchanged


def test_update_meal_plan_not_found():
    """Test updating a non-existent meal plan"""
    update_data = {
        "id": 99,  # Using a non-existent id
        "name": "Non-existent Plan",
        "description": "Doesn't matter",
        "meals": ["Empty Plate"]
    }

    response = client.put("/meal-plans/99", json=update_data)
    print(response.json())  # Debugging line to inspect response
    assert response.status_code == 404
    assert response.json() == {"detail": "Meal plan not found"}


def test_update_meal_plan_empty_body():
    """Test updating with an empty request body"""
    response = client.put("/meal-plans/32", json={})
    print(response.json())  # Debugging line to inspect response
    assert response.status_code == 422  # Unprocessable Entity
    errors = response.json()
    assert errors["detail"][0]["msg"] == "Field required"  # Corrected case
    assert errors["detail"][0]["loc"][0] == "body"


def test_update_meal_plan_missing_field():
    """Test updating with a missing required field"""
    update_data = {
        "id": 32,  # Adds the id here
        "description": "Missing name",
        "meals": ["Fried Rice"]
    }

    response = client.put("/meal-plans/32", json=update_data)
    print(response.json())  # Debugging line to inspect response
    assert response.status_code == 422  # Unprocessable Entity
    errors = response.json()
    assert errors["detail"][0]["msg"] == "Field required"  # Corrected case
    assert "name" in str(errors["detail"])


def test_update_meal_plan_invalid_meals_type():
    """Test updating with invalid data type for 'meals'"""
    update_data = {
        "id": 32,  
        "name": "Invalid Meals",
        "description": "Meals should be a list",
        "meals": "Just one meal"  # Incorrect type
    }

    response = client.put("/meal-plans/32", json=update_data)
    print(response.json())  # Debugging line to inspect response
    assert response.status_code == 422  # Unprocessable Entity
    errors = response.json()
    assert errors["detail"][0]["msg"] == "Input should be a valid list"  # Corrected case
    assert "meals" in str(errors["detail"])


def test_update_meal_plan_empty_meals_list():
    """Test updating with an empty meals list"""
    update_data = {
        "id": 32,  
        "name": "No Meals Plan",
        "description": "This plan has no meals",
        "meals": []  # Empty list
    }

    response = client.put("/meal-plans/32", json=update_data)
    print(response.json())  # Debugging line to inspect response
    assert response.status_code == 200  # Valid case
    data = response.json()
    assert data["meals"] == []  # Ensures meals are updated to an empty list


def test_update_meal_plan_extra_field():
    """Test updating with an extra field not defined in the schema"""
    update_data = {
        "id": 32,  
        "name": "Extra Field Plan",
        "description": "Testing extra fields",
        "meals": ["Yam Porridge"],
        "extra_field": "Unexpected Data"  # Extra field
    }

    response = client.put("/meal-plans/32", json=update_data)
    print(response.json())  # Debugging line to inspect response
    assert response.status_code == 200  # Extra fields are ignored
    data = response.json()
    assert "extra_field" not in data  # Ensures extra_field is not included
    assert data["meals"] == ["Yam Porridge"]


def test_update_meal_plan_keep_existing_data():
    """Test updating some fields while keeping others unchanged"""
    update_data = {
        "id": 32,
        "name": "Plan Thirty-Two",  # Keeps the name the same
        "meals": ["Rice"],  # Keeps the meal the same
        "description": "Only updating the description"  # Updates only the description
    }

    response = client.put("/meal-plans/32", json=update_data)
    print(response.json())  # Debugging line to inspect response
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Only updating the description"
    assert data["name"] == "Plan Thirty-Two"  # Name remains unchanged
    assert data["meals"] == ["Rice"]  # Meals remain unchanged


def test_update_meal_plan_full_update():
    """Test updating all fields (full update), keeping only the explicitly passed fields"""
    
    update_data = {
        "id": 32,  # Including the id here for clarity
        "name": "Updated Plan Name",  # Fully updates name
        "description": "Updated Description",  # Fully updates description
        "meals": ["Pasta", "Salad"]  # Fully updates meals list
    }

    response = client.put("/meal-plans/32", json=update_data)
    print(response.json())  # Debugging line to inspect response
    
    assert response.status_code == 200
    data = response.json()
    
    # Ensure all fields are updated
    assert data["id"] == 32  # Ensures ID remains the same
    assert data["name"] == "Updated Plan Name"  # Updated name
    assert data["description"] == "Updated Description"  # Updated description
    assert data["meals"] == ["Pasta", "Salad"]  # Updated meals list
