# 02 FastAPI Backend

## Objective

Design the backend service for `KubeSage AI` using FastAPI. The backend orchestrates Kubernetes evidence collection, AI reasoning, incident correlation, and recommendation generation in a modular, dependency-injected architecture.

## Architecture

- Presentation Layer: FastAPI routers and HTTP controllers.
- Application Layer: use cases and orchestration services.
- Domain Layer: business entities, repositories, and rules.
- Infrastructure Layer: adapters for Kubernetes, observability, storage, and AI APIs.

## Folder Structure

```text
backend/
├── app/
│   ├── adapters/
│   │   ├── kubernetes_adapter.py
│   │   ├── prometheus_adapter.py
│   │   ├── chroma_adapter.py
│   │   └── openrouter_adapter.py
│   ├── controllers/
│   │   ├── incident_controller.py
│   │   └── health_controller.py
│   ├── domain/
│   │   ├── models.py
│   │   ├── services.py
│   │   └── repositories.py
│   ├── repositories/
│   │   ├── incident_repository.py
│   │   └── knowledge_repository.py
│   ├── schemas/
│   │   ├── incident.py
│   │   ├── recommendation.py
│   │   └── auth.py
│   ├── services/
│   │   ├── investigation_service.py
│   │   └── reasoning_service.py
│   ├── config.py
│   ├── container.py
│   └── main.py
├── tests/
└── requirements.txt
```

## APIs

- `GET /health` – service readiness
- `POST /api/v1/incidents/investigate` – start investigation
- `GET /api/v1/incidents/{incident_id}` – retrieve incident report
- `GET /api/v1/incidents/{incident_id}/recommendations` – retrieve remediation guidance
- `GET /api/v1/knowledge/search` – query RAG knowledge base
- `POST /api/v1/auth/login` – authenticate user

## Data Models

- `IncidentPayload` – cluster identifiers, namespaces, filters, and investigation scope.
- `EvidenceBundle` – collected cluster state, metrics, events, logs, and metadata.
- `RootCauseReport` – explanation, confidence, and correlated causes.
- `RecommendationPayload` – kubectl, Helm, Terraform, GitHub Actions fixes.
- `RagQuery` – knowledge base prompt and vector metadata.

## Implementation Steps

1. Define FastAPI app entrypoint and route modules.
2. Build typed Pydantic schemas for request and response contracts.
3. Implement dependency injection container using `fastapi.Depends` and a central `container.py`.
4. Create application services to orchestrate investigation and AI reasoning.
5. Add health and readiness endpoints.
6. Add basic request validation and structured error handling.

## Best Practices

- Keep request/response models separate from domain entities.
- Use `FastAPI` dependency injection for adapter wiring.
- Apply strict typing for all service interfaces.
- Use structured logging in JSON format for operational visibility.
- Avoid business logic in controllers; delegate to services.

## Testing Strategy

- Add unit tests for controller input validation and service orchestration.
- Add contract tests for adapter interfaces.
- Add functional tests for endpoint behavior using `httpx.AsyncClient`.
- Use mocks for Kubernetes and AI API dependencies.

## Acceptance Criteria

- Backend module layout follows clean architecture.
- API surface is defined with typed schemas.
- Orchestration service contracts are documented.
- Health endpoint responds correctly.
- Dependency graph is wired through container modules.

## Future Enhancements

- Add multi-tenant request routing and policy enforcement.
- Add rate limiting and quota management.
- Add streaming responses for live investigation progress.
- Add OpenTelemetry tracing for cross-service workflows.
