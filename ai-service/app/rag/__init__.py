# CivicSense AI — RAG Package
# Owner: Arpit (Person 1)

from app.rag.retriever import QdrantRAGRetriever
from app.rag.embeddings import EmbeddingModel, MockEmbeddingModel, BGEEmbeddingModel
from app.rag.ingestion import (
    CivicDocument,
    DocumentChunk,
    DocumentSource,
    VerificationStatus,
    chunk_document,
)
from app.rag.seed_corpus import SEED_CIVIC_DOCUMENTS

__all__ = [
    "QdrantRAGRetriever",
    "EmbeddingModel",
    "MockEmbeddingModel",
    "BGEEmbeddingModel",
    "CivicDocument",
    "DocumentChunk",
    "DocumentSource",
    "VerificationStatus",
    "chunk_document",
    "SEED_CIVIC_DOCUMENTS",
]
