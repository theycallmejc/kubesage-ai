# 11 Terraform Fix Generator

## Objective

Define the Terraform fix generator for `KubeSage AI` to create infrastructure remediation recommendations and deployment fixes in Terraform configuration terms.

## Architecture

- Terraform fix generator maps incident context to Terraform resource repair patterns.
- It generates HCL patch suggestions and change guidance.
- Outputs include targeted resource updates, module guidance, and verification steps.

## Folder Structure

```text
backend/app/services/
├── terraform_fix_generator.py
├── terraform_template_registry.py
└── hcl_serializer.py
```

## APIs

- `TerraformFixGenerator.generate(incident_context)`
- `TerraformTemplateRegistry.get_template(template_name)`

## Data Models

- `TerraformFixSuggestion`
- `HclPatch`
- `TerraformCommand`
- `ModuleReference`

## Implementation Steps

1. Define Terraform remediation categories: networking, autoscaling, resource sizing, and cluster config.
2. Implement template-driven HCL patch generation.
3. Create guidance for applying Terraform changes and validating plan.
4. Integrate with incident evidence to select accurate resource targets.
5. Include recommendations for GitOps pipelines with Terraform.

## Best Practices

- Generate fixes that require review before apply.
- Encourage `terraform plan` and drift detection.
- Keep patches minimal and focused on the issue.
- Avoid suggesting complete state rebuilds unless necessary.
- Include module and provider context when applicable.

## Testing Strategy

- Add tests for generated HCL snippets and validity.
- Validate target resource matching logic.
- Add integration tests for plan guidance content.
- Ensure generated fixes align with incident evidence.

## Acceptance Criteria

- Terraform fix generator produces readable, safe HCL suggestions.
- Output includes plan and validation guidance.
- Generated recommendations are relevant to the incident.

## Future Enhancements

- Add Terraform state drift detection integration.
- Add automated PR generation for Terraform fixes.
- Add support for multiple IaC frameworks beyond Terraform.
