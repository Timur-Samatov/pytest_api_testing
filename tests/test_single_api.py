import pytest
import requests

base_url = "https://apichallenges.eviltester.com/sim/entities"

def test_all_entities():
    response = requests.get(base_url)

    # Verify status code
    assert response.status_code == 200 

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json"

    # Verify response structure and content
    data = response.json()  
    assert isinstance(data, dict), "response should be a JSON object"
    assert "entities" in data, "response should contain 'entities' key"
    assert isinstance(data["entities"], list), "'entities' should be a list"
    for entity in data["entities"]:
        assert "id" in entity, "each entity should have an 'id' field"
        assert "name" in entity, "each entity should have an 'id' field"
        assert "description" in entity, "each entity should have an 'id' field"

def test_single_entity_by_id():
    entity_id = 1
    url = f"{base_url}/{entity_id}"
    response = requests.get(url)

    # Verify status code
    assert response.status_code == 200 

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json"

    # Verify response structure and content
    entity = response.json()  
    assert isinstance(entity, dict), "response should be a JSON object"
    assert "id" in entity, "entity should have an 'id' field"
    assert entity["id"] == entity_id, f"entity 'id' should be {entity_id}"
    assert "name" in entity, "entity should have a 'name' field"
    assert "description" in entity, "entity should have a 'description' field"

def test_single_entity_not_found():
    entity_id = 13  # Assuming this ID does not exist
    url = f"{base_url}/{entity_id}"
    response = requests.get(url)

    # Verify status code for not found
    assert response.status_code == 404 

    # Verify response structure and content
    error_response = response.json()  
    assert isinstance(error_response, dict), "response should be a JSON object"
    assert f"{error_response["errorMessages"]}" == f"['Could not find Entity with ID {entity_id}']" , "error message should indicate entity not found"

def test_create_entity():
    new_entity = {
        "name": "bob"
    }
    response = requests.post(base_url, json=new_entity)

    # Verify status code
    assert response.status_code == 201 

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json"

    # Verify response structure and content
    created_entity = response.json()  
    assert isinstance(created_entity, dict), "response should be a JSON object"
    assert "id" in created_entity, "created entity should have an 'id' field"
    assert created_entity["name"] == new_entity["name"], "created entity 'name' should match"

test_suit_data = [
    (1, "entity number 1"),
    (2, "entity number 2"),
    (3, "entity number 3"),
    (4, "entity number 4"),
    (5, "entity number 5"),
    (6, "entity number 6"),
    (7, "entity number 7"),
    (8, "entity number 8"),
    (9, "entity number 9")
]

@pytest.mark.parametrize("entity_id, entity_name", test_suit_data)
def test_get_book_various_ids(entity_id, entity_name):
    url = f"{base_url}/{entity_id}"
    response = requests.get(url)
    entity = response.json() 
    assert entity["id"] == entity_id, f"entity 'id' should be {entity_id}"
    assert entity["name"] == entity_name, f"entity 'name' should be {entity_name}"