# 10 Helm Patch Generator

## Objective

Define the Helm patch generator for `KubeSage AI` to produce Helm upgrade and patch recommendations for application deployments and chart configurations.

## Architecture

- Helm patch generator consumes correlated incident context and deployment metadata.
- It generates Helm release upgrade commands and values patch suggestions.
- A template registry maps incident categories to Helm fix patterns.

## Folder Structure

```text
backend/app/services/
├── helm_patch_generator.py
├── helm_patch_templates.py
└── helm_yaml_serializer.py
```

## APIs

- `HelmPatchGenerator.generate(incident_context, release_info)`
- `HelmPatchTemplates.get_patch_template(issue_type)`

## Data Models

- `HelmPatchSuggestion`
- `HelmReleaseFix`
- `HelmValuesPatch`
- `HelmCommand`

## Implementation Steps

1. Define Helm fix categories for rollout, config, image, and resource issues.
2. Implement patch template generation for values and release upgrade commands.
3. Add support for `helm upgrade --reuse-values` and patch injection.
4. Integrate with Kubernetes collector release metadata.
5. Include explanations and validation steps.

## Best Practices

- Recommend Helm fixes that preserve release history.
- Prefer non-disruptive value changes when possible.
- Validate generated YAML against schema expectations.
- Keep patch suggestions minimal and targeted.
- Avoid generating full chart rewrites.

## Testing Strategy

- Add tests for Helm YAML patch generation.
- Validate generated upgrade command structure.
- Add tests for release metadata mapping and template selection.
- Ensure generated patches do not introduce invalid YAML.

## Acceptance Criteria

- Helm patch generator produces valid upgrade recommendations.
- Output contains values patch snippets and CLI commands.
- Generated fixes are contextualized by incident evidence.

## Future Enhancements

- Add support for Helm chart discovery within GitOps repositories.
- Add Helm diff preview generation.
- Add automated PR creation with Helm fix proposals.
