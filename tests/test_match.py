import pytest
from phasebook.match import is_match  # Adjust the import based on your app structure

def test_is_match():
    # Test cases
    assert is_match([1, 2, 3], [2, 3]) == True
    assert is_match([1, 2, 3], [4, 5]) == False
    assert is_match([1, 2, 3], [1, 2, 3]) == True
    assert is_match([1, 2, 3], []) == True
    assert is_match([], [1, 2, 3]) == False

def test_is_match_with_duplicates():
    # Test with duplicates in lists
    assert is_match([1, 1, 2, 3], [1, 2]) == True
    assert is_match([1, 2, 3, 3], [3]) == True

@pytest.mark.parametrize('match_id,expected_status,expected_message', [
    (0, 200, 'Match found'),
    (1, 200, 'No match'),
    (-1, 404, 'Invalid match id'),
    (999, 404, 'Invalid match id'),  # Assuming 999 is out of range
])
def test_match_endpoint(client, match_id, expected_status, expected_message):
    response = client.get(f'/match/{match_id}')
    json_data = response.get_json()
    assert response.status_code == expected_status
    if response.status_code == 200:
        assert json_data['message'] == expected_message
        assert 'elapsedTime' in json_data
    else:
        assert json_data == expected_message
