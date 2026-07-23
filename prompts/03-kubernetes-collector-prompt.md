# 03 Kubernetes Collector

## Objective

Build a resilient Kubernetes collector for `KubeSage AI` that gathers cluster evidence across workloads, observability, and GitOps resources. The collector must support kubectl and API-based adapters while normalizing output into a single evidence model.

## Architecture

- Collector orchestrator coordinates specialized collectors.
- Specialized collectors for Pods, Deployments, HPA, Ingress, Services, ConfigMaps, Secrets metadata, Nodes, Network Policies, PV/PVC, Istio, ArgoCD, Helm, and Kubernetes Events.
- Adapter abstraction for `kubectl`, `client-python`, and external services.
- Evidence normalization into domain-friendly models.

## Folder Structure

```text
backend/app/adapters/
├── kubernetes_adapter.py
├── helm_adapter.py
├── argocd_adapter.py
├── promises_adapter.py
├── node_metrics_adapter.py
└── cluster_inventory.py
backend/app/services/
├── collector_service.py
├── evidence_normalizer.py
└── resource_collectors/
    ├── pod_collector.py
    ├── deployment_collector.py
    ├── hpa_collector.py
    ├── ingress_collector.py
    ├── configmap_collector.py
    ├── secret_metadata_collector.py
    ├── network_policy_collector.py
    ├── pv_pvc_collector.py
    ├── argocd_collector.py
    └── helm_collector.py
```

## APIs

- Internal service APIs to request evidence types.
- Collector service methods:
  - `collect_pod_evidence()`
  - `collect_deployment_evidence()`
  - `collect_observability_evidence()`
  - `collect_gitops_evidence()`
  - `collect_security_evidence()`

## Data Models

- `PodEvidence`
- `DeploymentEvidence`
- `HpaEvidence`
- `IngressEvidence`
- `ServiceEvidence`
- `SecretMetadataEvidence`
- `NodeMetricsEvidence`
- `PrometheusMetricEvidence`
- `GrafanaDashboardEvidence`
- `AlertmanagerEvidence`
- `ArgoCdApplicationEvidence`
- `HelmReleaseEvidence`
- `NetworkPolicyEvidence`
- `PersistentVolumeEvidence`
- `PersistentVolumeClaimEvidence`
- `EventEvidence`
- `IstioResourceEvidence`

## Implementation Steps

1. Define the abstract collector interface and evidence contract.
2. Implement a `kubectl` executor adapter with retries and configurable timeouts.
3. Create core resource collectors for the required Kubernetes entities.
4. Normalize collected payloads into standard domain objects.
5. Add optional Prometheus and Grafana adapters for metrics and dashboards.
6. Implement ArgoCD and Helm collectors for GitOps state.
7. Add bulk collection flows for incident investigation.

## Best Practices

- Avoid collecting full secrets; only surface metadata and references.
- Use paginated or filtered collection for large clusters.
- Design collectors to be idempotent and retry-safe.
- Store raw evidence metadata separately from normalized domain models.
- Use explicit scopes to reduce blast radius during investigation.

## Testing Strategy

- Unit test each collector with mocked adapter responses.
- Add end-to-end integration tests for evidence normalization.
- Add failure tests for unavailable kubeconfig, API timeout, and missing resources.
- Validate secret metadata collection does not include secret data.

## Acceptance Criteria

- Collector covers the full required evidence list.
- Evidence output is normalized and consumable by AI reasoning.
- Kubernetes adapter handles error states gracefully.
- Metrics and observability adapters return structured results.
- GitOps state is available via ArgoCD and Helm collectors.

## Future Enhancements

- Add support for additional service meshes beyond Istio.
- Add cluster inventory profiling and drift detection.
- Add automated cluster snapshot caching for faster repeated investigations.
- Add Kubernetes change history and audit event correlation.
