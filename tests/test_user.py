import pytest
from fastapi import HTTPException, status
from apis.v1 import route_users


@pytest.mark.asyncio
async def test_get_user_by_email(mock_thing):
    moker_data = {"username": "string", "email": "user@example.com",
                  "is_active": True, "is_superuser": True}

    mock_thing.return_value = moker_data
    print(mock_thing, "mooock thing")
    result = await route_users.get_user("user@example.com")
    assert result == moker_data


@pytest.mark.asyncio
async def test_get_user_by_email_not_found(mocker):

    exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail="Email not found2")
    mocker.patch('apis.v1.route_users.get_user_by_email',
                 side_effect=exception)

    with pytest.raises(HTTPException) as exc_info:
        res = await route_users.get_user("notanuser@example.com")
        print(res)

    print(exc_info, "response")
    assert isinstance(exc_info.value, HTTPException)
    assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND
    assert exc_info.value.detail == "Email not found2"
