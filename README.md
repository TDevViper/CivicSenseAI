# CivicSense AI

**AI-Powered Civic Complaint Detection, Generation & Routing Platform**

---

## Project Overview

CivicSense AI simplifies civic complaint reporting. A citizen captures a photo of a civic issue (pothole, garbage, broken streetlight, etc.) with location context. The AI system:

1. **Detects** the civic issue from the photograph
2. **Classifies** the issue type with confidence scores
3. **Estimates** severity (LOW / MEDIUM / HIGH / CRITICAL)
4. **Resolves** the geographic location and jurisdiction
5. **Identifies** the responsible authority and department
6. **Retrieves** relevant civic knowledge via RAG
7. **Generates** a structured, professional complaint
8. **Checks** for duplicate complaints
9. **Presents** the complaint for citizen review and submission

---

## Architecture

```
CITIZEN → PHOTO + GPS
       ↓
   NEXT.JS FRONTEND
       ↓
   MAIN FASTAPI BACKEND
       ↓
   AI SERVICE (FastAPI)
       ↓
   ┌─────────────────────────────────────────────┐
   │              AI ENGINE                      │
   │                                             │
   │  ┌─────────────┐    ┌───────────────────┐   │
   │  │ PERSON 1     │    │ PERSON 2          │   │
   │  │ (Arpit)      │    │ (Arnav)           │   │
   │  │              │    │                   │   │
   │  │ Vision       │    │ Location          │   │
   │  │ Severity     │    │ Authority         │   │
   │  │ RAG          │    │ Duplicate         │   │
   │  │ LLM          │    │ Hotspots          │   │
   │  │ Decision     │    │ Trends            │   │
   │  └──────┬───────┘    └────────┬──────────┘   │
   │         └──────────┬──────────┘              │
   │                    ↓                         │
   │          STRUCTURED RESULT                   │
   └─────────────────────────────────────────────┘
       ↓
   USER REVIEW → SUBMISSION → AUTHORITY → TRACKING
```

---

## Technology Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js, React, TypeScript, Tailwind CSS |
| Main Backend | Python, FastAPI |
| Database | PostgreSQL |
| Caching | Redis |
| Computer Vision | PyTorch, Ultralytics YOLO, OpenCV |
| Machine Learning | Scikit-learn |
| NLP / LLM | Transformers, Ollama |
| Embeddings | BGE |
| Vector Database | Qdrant |
| Containerization | Docker |
| Version Control | Git / GitHub |

---

## Team Ownership

| Module | Owner | Description |
|---|---|---|
| `ai-service/app/vision/` | **Arpit** | Image preprocessing, YOLO detection, classification |
| `ai-service/app/severity/` | **Arpit** | Severity assessment engine |
| `ai-service/app/decision/` | **Arpit** | Core AI decision orchestration |
| `ai-service/app/rag/` | **Arpit** | BGE embeddings, Qdrant retrieval, RAG pipeline |
| `ai-service/app/llm/` | **Arpit** | Ollama integration, prompt architecture, complaint generation |
| `ai-service/app/location/` | **Arnav** | Reverse geocoding, geographic normalization |
| `ai-service/app/authority/` | **Arnav** | Authority routing, verified civic dataset |
| `ai-service/app/duplicate/` | **Arnav** | Duplicate complaint detection |
| `ai-service/app/analytics/` | **Arnav** | Hotspot detection, trend analysis |
| `ai-service/app/contracts/` | **Shared** | Pydantic schemas — API contract |
| `ai-service/app/core/` | **Shared** | Interfaces, config, logging, errors |

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/arpit7799/CivicSenseAI.git
cd CivicSenseAI

# 2. Create virtual environment
python3.10 -m venv civicsenseAI_env
source civicsenseAI_env/bin/activate

# 3. Install the lightweight API and test dependencies
pip install -r ai-service/requirements.txt

# Optional: install model dependencies for vision, RAG, and the full test suite
# pip install -r ai-service/requirements-ai.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your settings

# 5. Run the AI service
cd ai-service
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# 6. Test
# Install requirements-ai.txt first to run all vision/RAG tests.
pytest tests/ -v
```

Use Python 3.10 or newer.

The default `PROVIDER_MODE=mock` starts the API without downloading model weights.
Set `PROVIDER_MODE=production` only after installing `requirements-ai.txt` and
configuring the required model files and services. Person 2 civic-intelligence
providers can be enabled independently with `LOCATION_PROVIDER`,
`AUTHORITY_PROVIDER`, `DUPLICATE_PROVIDER`, and `ANALYTICS_PROVIDER` after their
corresponding data sources are configured.

Reverse geocoding is independently configured. Keep `LOCATION_PROVIDER=mock`
for offline development; set it to `nominatim` to enable the opt-in Nominatim
adapter. The public Nominatim service is limited to low-volume, user-triggered
lookups and requires an identifying User-Agent, request spacing, caching, and
OpenStreetMap attribution. Its result is the nearest suitable mapped object,
so the returned address can differ from the exact coordinate. See the
[Nominatim usage policy](https://operations.osmfoundation.org/policies/nominatim/)
and [reverse API documentation](https://nominatim.org/release-docs/latest/api/Reverse/).
The request limiter and cache are process-local; use one worker for this public
endpoint or configure a provider suitable for multi-worker production traffic.

Verified authority routing is also independently configured. Set
`AUTHORITY_PROVIDER=verified_dataset` to use the sourced Gurugram starter record.
It resolves to MCG's general civic grievance channel; the dataset deliberately
leaves the issue-specific department unset because the source does not establish
that mapping. Check the record's verification date and source before relying on
it in a live deployment.

---

## API

### Complaint index sync

The main backend owns complaint records and syncs a read-only projection to the
AI service. Configure a random `COMPLAINT_INDEX_API_KEY` and send it as a Bearer
token to `POST /api/v1/complaint-index/upsert`. The default in-memory repository
is for local development only and loses records on restart. For durable data,
install `ai-service/requirements-db.txt`, set `COMPLAINT_REPOSITORY=postgres`,
and apply `ai-service/migrations/001_complaint_index.sql` to a PostgreSQL
database with PostGIS installed.

Set `DUPLICATE_PROVIDER=engine` and `ANALYTICS_PROVIDER=engine` to use the
complaint-index-backed duplicate, hotspot, and trend implementations. Their
default remains mock mode until the application is syncing complaint records.

Example request:

```http
POST /api/v1/complaint-index/upsert
Authorization: Bearer <service-key>
Content-Type: application/json

{
  "records": [
    {
      "complaint_id": "APP-123",
      "issue_type": "pothole",
      "reported_at": "2026-10-22T10:00:00Z",
      "latitude": 28.4595,
      "longitude": 77.0266,
      "severity": "HIGH",
      "description": "Large pothole near the market",
      "city": "Gurugram",
      "state": "Haryana"
    }
  ]
}
```

### Health Check
```
GET /api/v1/health
```

### Analyze Civic Issue
```
POST /api/v1/analyze
Content-Type: application/json

{
    "image_url": "https://example.com/pothole.jpg",
    "latitude": 28.4595,
    "longitude": 77.0266,
    "user_description": "Large pothole on main road"
}
```

---

## Development Roadmap

| Phase | Name | Status |
|---|---|---|
| Phase 1 | Foundation | 🔨 In Progress |
| Phase 2 | Computer Vision | ⏳ Pending |
| Phase 3 | Severity Intelligence | ⏳ Pending |
| Phase 4 | Location Intelligence (Arnav) | ⏳ Pending |
| Phase 5 | Authority Intelligence (Arnav) | ⏳ Pending |
| Phase 6 | RAG System | ⏳ Pending |
| Phase 7 | Complaint Intelligence | ⏳ Pending |
| Phase 8 | Advanced AI (Arnav) | ⏳ Pending |
| Phase 9 | Full Integration | ⏳ Pending |

---

## License

This project is developed as part of an academic/professional collaboration.
