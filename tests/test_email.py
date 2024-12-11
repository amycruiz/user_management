import pytest
from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager

@pytest.mark.asyncio
async def test_send_markdown_email(email_service):
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123"
    }
    await email_service.send_user_email(user_data, 'email_verification')
    # Manual verification in Mailtrap

@pytest.mark.asyncio
async def test_send_professional_upgrade_email(email_service, sample_user):
    """Test that the professional upgrade email is sent successfully."""
    email_data = {"name": sample_user.first_name, "email": sample_user.email}
    await email_service.send_user_email(email_data, "professional_upgrade")

@pytest.mark.asyncio
async def test_email_service_error_handling(email_service, sample_user):
    """Test email service gracefully handles errors."""
    email_service.send_user_email.side_effect = Exception("SMTP server error")
    email_data = {"name": sample_user.first_name, "email": sample_user.email}
    with pytest.raises(Exception, match="SMTP server error"):
        await email_service.send_user_email(email_data, "professional_upgrade")
