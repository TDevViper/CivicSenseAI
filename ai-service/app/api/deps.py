# =============================================================================
# CivicSense AI — API Dependencies
# =============================================================================
# FastAPI dependency injection for providers and the decision engine.
#
# In Phase 1, all providers are mocks. As real implementations are built,
# the provider instantiation here is the ONLY place that changes —
# the endpoints and decision engine remain untouched.
# =============================================================================

from functools import lru_cache

from app.decision.engine import DecisionEngine

# Person 1 providers (Arpit — replaced in Phases 2–7)
from app.vision.detector import YOLODetector
from app.severity.engine import SeverityEngine
from app.rag.retriever import QdrantRAGRetriever
from app.llm.generator import OllamaComplaintGenerator

# Person 2 mocks (Arnav — replaced when Arnav delivers)
from app.core.interfaces import (
    LocationProvider,
    AuthorityProvider,
    DuplicateDetector,
    HotspotAnalyzer,
    TrendAnalyzer,
)
from app.location.mock_provider import MockLocationProvider
from app.authority.mock_provider import MockAuthorityProvider
from app.duplicate.mock_detector import MockDuplicateDetector
from app.analytics.mock_analyzer import MockHotspotAnalyzer, MockTrendAnalyzer


@lru_cache()
def get_location_provider() -> LocationProvider:
    """Return configured LocationProvider (Arnav)."""
    return MockLocationProvider()


@lru_cache()
def get_authority_provider() -> AuthorityProvider:
    """Return configured AuthorityProvider (Arnav)."""
    return MockAuthorityProvider()


@lru_cache()
def get_duplicate_detector() -> DuplicateDetector:
    """Return configured DuplicateDetector (Arnav)."""
    return MockDuplicateDetector()


@lru_cache()
def get_hotspot_analyzer() -> HotspotAnalyzer:
    """Return configured HotspotAnalyzer (Arnav)."""
    return MockHotspotAnalyzer()


@lru_cache()
def get_trend_analyzer() -> TrendAnalyzer:
    """Return configured TrendAnalyzer (Arnav)."""
    return MockTrendAnalyzer()


@lru_cache()
def get_decision_engine() -> DecisionEngine:
    """
    Build and cache the DecisionEngine with all providers.

    This is the single wiring point for dependency injection.
    To swap a mock for a real implementation:
    1. Import the real provider class
    2. Replace the Mock* instantiation in the respective getter above
    3. No other file needs to change
    """
    # Person 1 providers (Arpit)
    vision = YOLODetector()
    severity = SeverityEngine()
    rag = QdrantRAGRetriever()
    complaint = OllamaComplaintGenerator()

    # Person 2 providers (Arnav)
    location = get_location_provider()
    authority = get_authority_provider()
    duplicate = get_duplicate_detector()

    return DecisionEngine(
        vision=vision,
        severity=severity,
        location=location,
        authority=authority,
        rag=rag,
        complaint=complaint,
        duplicate=duplicate,
    )
