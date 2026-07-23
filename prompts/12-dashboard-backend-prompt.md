# 12 Dashboard Backend

## Objective

Design the dashboard backend for `KubeSage AI` to expose incident reports, investigation progress, recommendations, and knowledge search APIs for the React UI.

## Architecture

- API gateway layer handles web and dashboard requests.
- Controllers expose incident, recommendation, and knowledge endpoints.
- Caching layer supports fast query response for recent incidents.
- Authentication middleware secures dashboard APIs.

## Folder Structure

```text
backend/app/controllers/
├── dashboard_controller.py
├── incident_controller.py
└── knowledge_controller.py
backend/app/repositories/
├── incident_repository.py
├── recommendation_repository.py
└── knowledge_repository.py
backend/app/services/
├── dashboard_service.py
└── cache_service.py
```

## APIs

- `GET /api/v1/dashboard/overview`
- `GET /api/v1/dashboard/incidents`
- `GET /api/v1/incidents/{incident_id}`
- `GET /api/v1/incidents/{incident_id}/timeline`
- `POST /api/v1/knowledge/search`
- `GET /api/v1/knowledge/recent`

## Data Models

- `DashboardSummary`
- `IncidentCard`
- `RecommendationCard`
- `KnowledgeSearchResult`
- `ProgressEvent`

## Implementation Steps

1. Define dashboard API contracts and response schemas.
2. Implement controllers to fetch incident summaries and detail.
3. Add caching for trending incidents and root cause metrics.
4. Implement knowledge search API integration with RAG.
5. Add operational observability metrics for API usage.

## Best Practices

- Keep dashboard APIs fast and cache-friendly.
- Use paginated endpoints for incident lists.
- Expose enough metadata for rich UI cards without over-fetching.
- Apply authentication and authorization consistently.
- Use API versioning for backward compatibility.

## Testing Strategy

- Add controller tests for response payload shapes.
- Add integration tests for dashboard query flows.
- Add cache behavior tests.
- Validate error responses for invalid requests.

## Acceptance Criteria

- Dashboard backend provides the required overview and detail endpoints.
- Knowledge search API returns semantic results.
- Incident data can be surfaced to the React frontend.
- API responses are typed and stable.

## Future Enhancements

- Add streaming progress updates via WebSocket or Server-Sent Events.
- Add customizable dashboard filters and saved views.
- Add health and SLA dashboard endpoints.
