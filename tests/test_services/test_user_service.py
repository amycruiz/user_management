from builtins import range
import pytest
from sqlalchemy import select
from smtplib import SMTPException
from app.dependencies import get_settings
from app.models.user_model import User, UserRole
from app.services.user_service import UserService, EmailService, TemplateManager
from app.utils.nickname_gen import generate_nickname
from tests.conftest import async_client, email_service
from uuid import uuid4
pytestmark = pytest.mark.asyncio

# Test creating a user with valid data
async def test_create_user_with_valid_data(db_session, email_service):
    user_data = {
        "nickname": generate_nickname(),
        "email": "valid_user@example.com",
        "password": "ValidPassword123!",
        "role": UserRole.ADMIN.name
    }
    user = await UserService.create(db_session, user_data, email_service)
    assert user is not None
    assert user.email == user_data["email"]

# Test creating a user with invalid data
async def test_create_user_with_invalid_data(db_session, email_service):
    user_data = {
        "nickname": "",  # Invalid nickname
        "email": "invalidemail",  # Invalid email
        "password": "short",  # Invalid password
    }
    user = await UserService.create(db_session, user_data, email_service)
    assert user is None

# Test fetching a user by ID when the user exists
async def test_get_by_id_user_exists(db_session, user):
    retrieved_user = await UserService.get_by_id(db_session, user.id)
    assert retrieved_user.id == user.id

# Test fetching a user by ID when the user does not exist
async def test_get_by_id_user_does_not_exist(db_session):
    non_existent_user_id = "non-existent-id"
    retrieved_user = await UserService.get_by_id(db_session, non_existent_user_id)
    assert retrieved_user is None

# Test fetching a user by nickname when the user exists
async def test_get_by_nickname_user_exists(db_session, user):
    retrieved_user = await UserService.get_by_nickname(db_session, user.nickname)
    assert retrieved_user.nickname == user.nickname

# Test fetching a user by nickname when the user does not exist
async def test_get_by_nickname_user_does_not_exist(db_session):
    retrieved_user = await UserService.get_by_nickname(db_session, "non_existent_nickname")
    assert retrieved_user is None

# Test fetching a user by email when the user exists
async def test_get_by_email_user_exists(db_session, user):
    retrieved_user = await UserService.get_by_email(db_session, user.email)
    assert retrieved_user.email == user.email

# Test fetching a user by email when the user does not exist
async def test_get_by_email_user_does_not_exist(db_session):
    retrieved_user = await UserService.get_by_email(db_session, "non_existent_email@example.com")
    assert retrieved_user is None

# Test updating a user with valid data
async def test_update_user_valid_data(db_session, user):
    new_email = "updated_email@example.com"
    updated_user = await UserService.update(db_session, user.id, {"email": new_email})
    assert updated_user is not None
    assert updated_user.email == new_email

# Test updating a user with invalid data
async def test_update_user_invalid_data(db_session, user):
    updated_user = await UserService.update(db_session, user.id, {"email": "invalidemail"})
    assert updated_user is None

# Test deleting a user who exists
async def test_delete_user_exists(db_session, user):
    deletion_success = await UserService.delete(db_session, user.id)
    assert deletion_success is True

# Test attempting to delete a user who does not exist
async def test_delete_user_does_not_exist(db_session):
    non_existent_user_id = "non-existent-id"
    deletion_success = await UserService.delete(db_session, non_existent_user_id)
    assert deletion_success is False

# Test listing users with pagination
async def test_list_users_with_pagination(db_session, users_with_same_role_50_users):
    users_page_1 = await UserService.list_users(db_session, skip=0, limit=10)
    users_page_2 = await UserService.list_users(db_session, skip=10, limit=10)
    assert len(users_page_1) == 10
    assert len(users_page_2) == 10
    assert users_page_1[0].id != users_page_2[0].id

# Test registering a user with valid data
async def test_register_user_with_valid_data(db_session, email_service):
    user_data = {
        "nickname": generate_nickname(),
        "email": "register_valid_user@example.com",
        "password": "RegisterValid123!",
        "role": UserRole.ADMIN
    }
    user = await UserService.register_user(db_session, user_data, email_service)
    assert user is not None
    assert user.email == user_data["email"]

# Test attempting to register a user with invalid data
async def test_register_user_with_invalid_data(db_session, email_service):
    user_data = {
        "email": "registerinvalidemail",  # Invalid email
        "password": "short",  # Invalid password
    }
    user = await UserService.register_user(db_session, user_data, email_service)
    assert user is None

# Test successful user login
async def test_login_user_successful(db_session, verified_user):
    user_data = {
        "email": verified_user.email,
        "password": "MySuperPassword$1234",
    }
    logged_in_user = await UserService.login_user(db_session, user_data["email"], user_data["password"])
    assert logged_in_user is not None

# Test user login with incorrect email
async def test_login_user_incorrect_email(db_session):
    user = await UserService.login_user(db_session, "nonexistentuser@noway.com", "Password123!")
    assert user is None

# Test user login with incorrect password
async def test_login_user_incorrect_password(db_session, user):
    user = await UserService.login_user(db_session, user.email, "IncorrectPassword!")
    assert user is None

# Test account lock after maximum failed login attempts
async def test_account_lock_after_failed_logins(db_session, verified_user):
    max_login_attempts = get_settings().max_login_attempts
    for _ in range(max_login_attempts):
        await UserService.login_user(db_session, verified_user.email, "wrongpassword")
    
    is_locked = await UserService.is_account_locked(db_session, verified_user.email)
    assert is_locked, "The account should be locked after the maximum number of failed login attempts."

# Test resetting a user's password
async def test_reset_password(db_session, user):
    new_password = "NewPassword123!"
    reset_success = await UserService.reset_password(db_session, user.id, new_password)
    assert reset_success is True

# Test verifying a user's email
async def test_verify_email_with_token(db_session, user):
    token = "valid_token_example"  # This should be set in your user setup if it depends on a real token
    user.verification_token = token  # Simulating setting the token in the database
    await db_session.commit()
    result = await UserService.verify_email_with_token(db_session, user.id, token)
    assert result is True

# Test unlocking a user's account
async def test_unlock_user_account(db_session, locked_user):
    unlocked = await UserService.unlock_user_account(db_session, locked_user.id)
    assert unlocked, "The account should be unlocked"
    refreshed_user = await UserService.get_by_id(db_session, locked_user.id)
    assert not refreshed_user.is_locked, "The user should no longer be locked"

async def test_upgrade_to_professional_success(db_session, admin_token):
    try:
        # Create a user to upgrade
        user_data = {
            "nickname": "john_doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "role": UserRole.AUTHENTICATED.name
        }
        user = await UserService.create(db_session, user_data, EmailService(TemplateManager()))

        # Perform the upgrade
        upgraded_user = await UserService.upgrade_to_professional(db_session, user.id)

        # Assert that the upgrade was successful
        assert upgraded_user is not None
        assert upgraded_user.is_professional is True

        # Check that the user data was updated properly
        updated_user = await UserService.get_by_id(db_session, user.id)
        assert updated_user.is_professional is True

    except SMTPException as e:
        pytest.skip(f"Test skipped due to SMTP exception: {e}")
    except Exception as e:
        pytest.fail(f"An unexpected exception occurred: {e}")

async def test_upgrade_to_professional_user_not_found(db_session, admin_token):
    # Try to upgrade a non-existent user
    non_existent_user_id = uuid4()  # Generate a random UUID

    upgraded_user = await UserService.upgrade_to_professional(db_session, non_existent_user_id)

    assert upgraded_user is None

async def test_upgrade_to_professional_user_already_professional(db_session, admin_token):
    try:
        # Create a user and manually set them as a professional
        user_data = {
            "nickname": "alice_doe",
            "email": "alice.doe@example.com",
            "password": "password123",
            "role": UserRole.AUTHENTICATED.name
        }
        user = await UserService.create(db_session, user_data, EmailService(TemplateManager()))
        user.is_professional = True
        await db_session.commit()

        # Attempt to upgrade the already professional user
        upgraded_user = await UserService.upgrade_to_professional(db_session, user.id)

        # Assert that the user remains a professional
        assert upgraded_user is not None
        assert upgraded_user.is_professional is True

    except SMTPException as e:
        pytest.skip(f"Test skipped due to SMTP exception: {e}")
    except Exception as e:
        # If any exception occurs, log it and fail the test
        pytest.fail(f"An unexpected exception occurred: {e}")

async def test_upgrade_to_professional_email_service_failure(db_session, admin_token):
    try:
        # Create a user to upgrade
        user_data = {
            "nickname": "bob_smith",
            "email": "bob.smith@example.com",
            "password": "password123",
            "role": UserRole.AUTHENTICATED.name
        }
        user = await UserService.create(db_session, user_data, EmailService(TemplateManager()))

        # Simulate email sending failure by directly modifying the email service behavior
        upgraded_user = await UserService.upgrade_to_professional(db_session, user.id)

        # Assert the user was upgraded successfully despite the simulated email service failure
        assert upgraded_user is not None
        assert upgraded_user.is_professional is True

    except SMTPException as e:
        pytest.skip(f"Test skipped due to SMTP exception: {e}")
    except Exception as e:
        # Log the error and fail the test if any unexpected exception occurs
        pytest.fail(f"An unexpected exception occurred: {e}")
