# Observability evidence - Checkpoint 3

## Scope and status

Market Match uses a Cloudflare Worker / Hono Application API with D1 and R2, as documented in the [architecture-of-record](design/architectural-design.md). Application code and instrumentation changes belong in `MM-Version`; this repository records the evidence.

## 1. Logs, health check, and metrics

| Item | What to verify and record | Evidence |
| --- | --- | --- |
| Logs | Open **Cloudflare → Workers & Pages → selected Worker → Observability**. Confirm a deployed API request appears and record the available retention and sampling settings. | Pending: dashboard link and example log. |
| Health check | Identify the actual deployed endpoint and state what it checks: only the Worker response, or dependencies such as D1 as well. Verify status, content type, and response body; an HTML frontend fallback returning `200` is not a valid health response. | Pending: URL, response, and checks performed. |
| Metrics | Show the available request count, errors, and timing measurements. State the Worker, time window, and each metric's meaning. CPU time is not end-to-end request latency, and runtime errors are not necessarily the same as HTTP `5xx` responses. | Pending: dashboard link or screenshot with definitions. |

The health-check route and log configuration have not been verified. If something is missing, record the gap and address it through an application pull request. Follow the client's deployment workflow; use the confirmed preview environment for controlled failures.

Cloudflare's authenticated dashboards can provide metrics evidence; a public `/metrics` endpoint and the course's Spring Boot/Azure tool stack are not required. Platform telemetry may miss browser failures, requests that never reach the Worker, or operations that fail while returning HTTP `200`.

## 2. Demonstrate one failed request

1. Open the confirmed preview Worker's Cloudflare log view.
2. Trigger a harmless, reproducible failure from a documented use-case extension using test data. Record the method, route, time with timezone, response status, and request ID if available.
3. Find the matching entry in **Cloudflare's platform logs**, using the request ID or precise time and route. Explain the cause from the recorded context.
4. Save a dashboard link and a sanitized screenshot or short recording. Document how to reproduce the request without including credentials.

An authentication or validation rejection can demonstrate a failed request, but does not prove unexpected exceptions are logged. Do not disrupt production services or add a public crash endpoint.

| Failure evidence | Result |
| --- | --- |
| Environment and deployed commit | Pending |
| Reproduction steps, method, and route | Pending |
| Timestamp, status, and correlation ID | Pending |
| Matching platform log and diagnosis | Pending |

## 3. Review log usefulness and privacy

Check an actual application error log against [architecture section 8.2.7](design/architectural-design.md). Useful context includes timestamp, severity, operation or route, request correlation, and sanitized exception details. Status, duration, and deployment version help where available. Record missing context honestly.

- Log identifiers rather than content; never log whole application objects.
- Check for emails, demographic answers, passwords, API Key values, session tokens, cookies, and authorization headers. Review exception messages and automatically recorded URLs as well as custom logs.
- Verify that catches that do not rethrow log the exception, as required by the architecture.

**Review evidence:** Pending — link the relevant logging code or PR and a safe example log, and state which fields and sensitive-data paths were checked. Redacting a screenshot does not fix sensitive data already written to logs.

## Slack submission

Link the completed version of this document in the team's Checkpoint 3 evidence message. Replace pending entries with observed results and reviewable links. Screenshots or recordings support the evidence; the checklist does not prescribe their format. Be ready to reproduce the failed request and locate its log during the live demo.

The measured SLO and dependency degradation test are **separate checkpoint items**. Link their evidence separately; this log demonstration does not satisfy them.

## References

- [Checkpoint 3 checklist and submission instructions](https://washingtonwei.github.io/cosc-40943/project/#checkpoint-3-checklist)
- [Course observability module](https://washingtonwei.github.io/cosc-40943/modules/observability/)
- [Cloudflare Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/)
