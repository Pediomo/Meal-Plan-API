# Meal Plan API

This is a simple API built with FastAPI to manage meal plans. It allows users to perform CRUD (Create, Read, Update, Delete) operations on meal plans.


# Key Endpoints

- GET /meal-plans: Fetch all meal plans
- POST /meal-plans: Create a new meal plan
- PUT /meal-plans/{id}: Update an existing meal plan

  - Supports full updates or partial updates for specific fields (e.g., description, meals).
  - Allows updating only some fields while keeping others unchanged.
  - Handles validation errors like missing required fields or invalid data types.

- DELETE /meal-plans/{id}: Delete a meal plan

# Features

Validation: Ensures that all meal plans have a valid name, description, and meals list.

Error Handling: Provides clear error messages for missing fields, invalid data types, or attempts to update non-existent meal plans.

Test Coverage: Includes test cases for each endpoint to ensure that the API functions as expected under different conditions.


# Technologies

- FastAPI: Web framework for building APIs.

- Pydantic: Data validation and settings management.

- pytest: Testing framework used to ensure API correctness.

- Postman: API testing tool used to manually test and interact with the API. 

# Test

Implemented unit & Integration tests using pytest to validate the functionality of the API. These tests covers:

- Successful update of meal plans (test_update_meal_plan_success).
- Handling of non-existent meal plans (test_update_meal_plan_not_found).
- Various validation cases like missing fields, invalid data types, and empty lists.
- Keeping existing data unchanged when updating meal plans (test_update_meal_plan_keep_existing_data).
- Deprecated methods (e.g., .dict()) were replaced with the recommended .model_dump() method as part of upgrading to Pydantic V2.

# Error Handling

The API correctly handles errors such as:

- Meal plans not found.
- Missing required fields or invalid data types.
- Handling of extra fields in the request.

## How to Test the API

You can easily test the Meal Plan API by following these steps:

### 1. Access the Swagger UI
- Visit the public Swagger UI for the Meal Plan API:  
  [https://meal-plan-api-wgrv.onrender.com/docs](https://meal-plan-api-wgrv.onrender.com/docs)

### 2. Explore Available Endpoints
- The Swagger UI will display a list of all available API endpoints.
- Each endpoint provides information about its method (GET, POST, etc.), parameters, and possible responses.

### 3. Test API Endpoints
- Select the endpoint you want to test (e.g., `GET /meal-plans`).
- Click **"Try it out"** to enable the input fields for that endpoint.
- Provide any required parameters (if any).
- Click **"Execute"** to send a test request to the API.
- Review the response displayed in the UI, including the status code and data returned.

### 4. Example Testing (GET /meal-plans)
- To test retrieving all meal plans:
  1. In Swagger UI, click on the **`GET /meal-plans`** endpoint.
  2. Click **"Try it out"**.
  3. Click **"Execute"** to send the request.
  4. View the response data, which will show the list of meal plans (if available).
