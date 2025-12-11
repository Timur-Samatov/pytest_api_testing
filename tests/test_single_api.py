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
    print(error_response["errorMessages"])
    assert f"{error_response["errorMessages"]}" == f"['Could not find Entity with ID {entity_id}']" , "error message should indicate entity not found"