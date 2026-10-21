# CivicSense AI — LLM Package
# Owner: Arpit (Person 1)

from app.llm.client import LLMClient, OllamaClient, MockLLMClient
from app.llm.generator import OllamaComplaintGenerator
from app.llm.mock_generator import MockComplaintGenerator
from app.llm.fallback import generate_deterministic_complaint
from app.llm.guardrails import validate_and_sanitize_complaint, GuardrailViolationError
from app.llm.prompts import SYSTEM_PROMPT, build_complaint_prompt

__all__ = [
    "LLMClient",
    "OllamaClient",
    "MockLLMClient",
    "OllamaComplaintGenerator",
    "MockComplaintGenerator",
    "generate_deterministic_complaint",
    "validate_and_sanitize_complaint",
    "GuardrailViolationError",
    "SYSTEM_PROMPT",
    "build_complaint_prompt",
]
