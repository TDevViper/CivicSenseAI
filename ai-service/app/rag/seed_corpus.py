# =============================================================================
# CivicSense AI — Verified Seed Civic Corpus
# =============================================================================
# Curated initial civic knowledge records.
#
# CRITICAL SOURCE RELIABILITY:
# Clearly labels official municipal charters vs. general guidance.
# Every record includes identifiable authority, title, reference, and status.
#
# Owner: Arpit (intake from Arnav's verified records)
# =============================================================================

from app.rag.ingestion import CivicDocument, DocumentSource, VerificationStatus


SEED_CIVIC_DOCUMENTS: list[CivicDocument] = [
    CivicDocument(
        id="MCD-CITIZEN-CHARTER-ROADS-01",
        category="roads",
        source=DocumentSource(
            authority_name="Municipal Corporation (Engineering Dept)",
            title="Citizen Charter & Maintenance Protocol for Public Roadways",
            reference_id="MCD/ENG/2023/CC-04",
            url=None,
            verification_status=VerificationStatus.GENERAL_GUIDANCE,
            department="Public Works & Road Infrastructure",
            jurisdiction="Municipal Limits",
        ),
        text=(
            "Citizen Charter - Road Maintenance and Pothole Repair Procedures:\n\n"
            "1. Potholes on municipal internal roads fall strictly under the jurisdiction of the "
            "Municipal Corporation Engineering Division. Major arterial highways belong to PWD / NHAI.\n\n"
            "2. Standard Operating Procedure mandates that upon verified reporting with photographic "
            "evidence and geographic coordinates, road repair work orders are prioritized based on hazard severity.\n\n"
            "3. High severity road craters and continuous road surface damage threatening vehicular and "
            "pedestrian transit must be cordoned off or temporarily patched to mitigate immediate accident hazards."
        ),
    ),
    CivicDocument(
        id="SBM-URBAN-SOLID-WASTE-02",
        category="sanitation",
        source=DocumentSource(
            authority_name="Municipal Health & Sanitation Department",
            title="Solid Waste Management Bylaws & Grievance Protocol",
            reference_id="SBM/UD/SWM-2022/SEC-9",
            url=None,
            verification_status=VerificationStatus.GENERAL_GUIDANCE,
            department="Department of Environment and Sanitation",
            jurisdiction="Municipal Limits",
        ),
        text=(
            "Solid Waste Management and Unauthorized Garbage Dump Resolution:\n\n"
            "1. Open dumping of municipal solid waste, construction debris, and plastic accumulation on "
            "public roads, footpaths, and open spaces violates municipal sanitation bylaws.\n\n"
            "2. Reports of community garbage dumps and uncollected secondary bins are routed to the Zonal "
            "Sanitation Superintendent.\n\n"
            "3. In cases where overflowing waste blocks stormwater drainage channels, emergency mechanical "
            "clearing is dispatched to prevent vector-borne disease transmission and localized water stagnation."
        ),
    ),
    CivicDocument(
        id="MCD-STREETLIGHT-SAFETY-03",
        category="electricity",
        source=DocumentSource(
            authority_name="Municipal Electrical Department & Discom Joint Cell",
            title="Public Lighting & Electrical Safety Standard Protocols",
            reference_id="MED/ELEC/2023/SL-11",
            url=None,
            verification_status=VerificationStatus.GENERAL_GUIDANCE,
            department="Electrical Maintenance Division",
            jurisdiction="Municipal Limits",
        ),
        text=(
            "Public Lighting and Streetlight Maintenance Standards:\n\n"
            "1. Streetlights on municipal roads, public alleys, and community intersections are maintained "
            "jointly by the Municipal Corporation Electrical Wing and power distribution licensees.\n\n"
            "2. Reported broken streetlights, exposed live wiring, and malfunctioning dark stretches are "
            "categorized as high public safety hazards.\n\n"
            "3. Inspection teams are dispatched to verify luminaire replacement, pole stabilization, and "
            "feeder pillar insulation."
        ),
    ),
    CivicDocument(
        id="DRAINAGE-WATERLOGGING-SOP-04",
        category="drainage",
        source=DocumentSource(
            authority_name="Stormwater Drainage & Flood Control Board",
            title="Monsoon Waterlogging Prevention & Emergency Desilting SOP",
            reference_id="FCB/DRAIN/2023/MW-02",
            url=None,
            verification_status=VerificationStatus.GENERAL_GUIDANCE,
            department="Drainage & Flood Management",
            jurisdiction="Metropolitan Area",
        ),
        text=(
            "Stormwater Drainage and Severe Water Logging Response Protocols:\n\n"
            "1. Severe water logging on public roads and low-lying intersections requires immediate "
            "intervention by the Stormwater Drainage Wing.\n\n"
            "2. When standing water coincides with road damage or submerged potholes, the area is treated as "
            "an urgent vehicular hazard.\n\n"
            "3. Mobile desilting units and diesel dewatering pump sets are deployed to clear choked catch pits "
            "and divert localized flooding into trunk drains."
        ),
    ),
    CivicDocument(
        id="CIVIC-GUIDE-COMMUNITY-REPORTING-05",
        category="general",
        source=DocumentSource(
            authority_name="Civic Awareness Initiative",
            title="General Citizen Guide on Community Reporting Best Practices",
            reference_id=None,
            url=None,
            verification_status=VerificationStatus.GENERAL_GUIDANCE,
            department=None,
            jurisdiction=None,
        ),
        text=(
            "General Civic Reporting Information:\n\n"
            "Citizens filing municipal complaints are advised to capture clear photographs under natural lighting. "
            "Including nearby landmarks, road intersections, and descriptive details assists field inspectors in locating "
            "the reported defect promptly. Note: This guide provides community reporting best practices and does not "
            "represent official municipal policy."
        ),
    ),
]
