import allure
import functools
from typing import Callable, Any
import logging

logger = logging.getLogger(__name__)


def allure_step(title: str = None, description: str = None):
    """
    Decorator to mark a function as an Allure step.

    Args:
        title: Step title (if not provided, uses function name)
        description: Step description
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            step_title = title or func.__name__.replace('_', ' ').title()

            with allure.step(step_title):
                if description:
                    allure.attach(description, "Step Description", allure.attachment_type.TEXT)

                try:
                    result = func(*args, **kwargs)
                    logger.info(f"Step completed successfully: {step_title}")
                    return result
                except Exception as e:
                    allure.attach(str(e), "Error Details", allure.attachment_type.TEXT)
                    raise

        return wrapper

    return decorator
