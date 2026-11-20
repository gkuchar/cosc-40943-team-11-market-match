# Checkpoint 3 Fan-Out Evidence

## Release

- Tagged demo: [`v0.2.0`](https://github.com/Market-Match/MM-Version/releases/tag/v0.2.0)
- Tag commit: [`5c5037b`](https://github.com/Market-Match/MM-Version/commit/5c5037b1467755b69cfa73dcd997b51938cec4c9)
- The tag is the merge of [`MM-Version` PR #49](https://github.com/Market-Match/MM-Version/pull/49), which adds create-product behavior and the product Approval migration.

## Built Use Cases

- `UC-BRND-create-product` is built in PR #49 and shipped on `v0.2.0`.
- `UC-BRND-generate-api-key` is built and has focused WorkOS failure tests, including [`MM-Version` PR #51](https://github.com/Market-Match/MM-Version/pull/51).
- [Use cases](requirements/use-cases.md) trace the behavior; [traceability](traceability.md) keeps Build and Verify separate.

## Verification Status

- `UC-BRND-create-product`: **🟡 Partial**. PR #49 provides implementation and migration evidence, but no cited automated test covers the main flow and every extension.
- `UC-BRND-generate-api-key`: **🟡 Partial**. Existing tests cover authorization, the empty Organization case, and fail-closed WorkOS outages. They do not yet cite a passing test for the full generate, replace, revoke, and browser flows.
- The create-product, brand-scoped-storage, hidden-until-Approval, and server-checks rows must not read `✅ Verified` until passing tests cover the main flow and every extension.

## Teammate Evidence

- [The Pipeline](https://github.com/gkuchar/cosc-40943-team-11-market-match/pull/44)
- [MM-Version pipeline](https://github.com/Market-Match/MM-Version/pull/40)
- [Degradation test](https://github.com/Market-Match/MM-Version/pull/51)
- [Calibration table](https://github.com/gkuchar/cosc-40943-team-11-market-match/pull/45)
- [Measured objective](https://github.com/gkuchar/cosc-40943-team-11-market-match/pull/47)

## Slack Message

**Checkpoint 3 — Fan-out evidence**

- Use cases: https://github.com/gkuchar/cosc-40943-team-11-market-match/blob/main/docs/requirements/use-cases.md
- Traceability: https://github.com/gkuchar/cosc-40943-team-11-market-match/blob/main/docs/traceability.md
- Release: https://github.com/Market-Match/MM-Version/releases/tag/v0.2.0
- Tagged commit: https://github.com/Market-Match/MM-Version/commit/5c5037b1467755b69cfa73dcd997b51938cec4c9
- Create-product implementation: https://github.com/Market-Match/MM-Version/pull/49
- API Key degradation tests: https://github.com/Market-Match/MM-Version/pull/51

`UC-BRND-create-product` and `UC-BRND-generate-api-key` are built, but neither is fully Verified by the main flow and every extension. The create-product row is partial because no automated use-case test is cited. The API Key row is partial because tests cover authorization and WorkOS outages but not the full generate, replace, revoke, and browser flows.
