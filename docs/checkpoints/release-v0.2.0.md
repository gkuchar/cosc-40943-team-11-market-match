# v0.2.0 release notes — draft

Not published or tagged. These notes describe the proposed release; they are not proof of a deployed version.

## For the client

The Admin can generate, replace, and revoke a Brand's API Key. A generated key is shown once. If WorkOS cannot confirm the Brand, the request fails and existing API Keys remain unchanged. This capability was introduced in the proving slice; it is not a new product-import feature.

The proposed Checkpoint 3 changes add a database readiness check and regression tests for WorkOS and database failures.

## Limits

Product sending through an API Key and the published product contract remain unfinished. The automated checks do not replace the browser checks in [the BRND test list](../design/brnd.md#tests). Static analysis currently fails; see [checkpoint evidence](checkpoint-3.md). This release does not yet demonstrate several finished use cases or a measured import SLO.

## Release procedure

After review and the required gate, record the accepted `MM-Version` commit SHA here, ensure `v0.2.0` does not already exist, create its annotated tag on that commit, push that tag, and publish client-facing notes in `Market-Match/MM-Version`. Do not tag this specification repository as the application release. Run the local demo from a clean checkout of that tag; show `git describe --tags --exact-match` and `git rev-parse HEAD`. Any deployed version also needs a recorded mapping to that SHA. Production deployment is controlled by the client.
