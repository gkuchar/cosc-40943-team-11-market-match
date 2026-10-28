# AGENTS.md

## What this is

Market Match is a swipe-based marketing and consumer feedback platform: Consumers swipe on product Cards in a Market, and Brands, Vendors, and the Admin see what Consumers liked and how they engaged. The client, Demetrie King, owns and runs it. Team 11's phase 1 work is bringing Brands' products into Market Match (by hand, by spreadsheet, or from a Brand's own system through an API) with the Admin approving each one, and capturing the Consumer data points.

This repository holds the specification. The code lives in the client's repository, `MM-Version`, on the team's branch `tcu-fall-2026-stage`. Built spec-first: the requirements in `docs/requirements/` are the contract, and the architecture-of-record is `docs/design/architectural-design.md`.

## How to run it

This repository has nothing to run. In `MM-Version`, from its root:

1. `npm install`
2. `npm run dev`: the React app and the Cloudflare Worker run together at http://localhost:5173, against a local D1 database.

The client's `CLAUDE.md` in `MM-Version` is the authority on its two Cloudflare environments and on deploying.

## How to run the tests

`MM-Version` has no test framework and no linter configured yet. Adding one is a new dependency, so a person decides it first (see below).

## Conventions

The binding conventions live once, in §8.2 of `docs/design/architectural-design.md`.

- API calls from the front end go through `services/apiService.ts` (§8.2.1, §8.2.3).
- Secrets stay outside source code: `.env.local` and `.dev.vars` locally, Cloudflare Worker secrets in production (§8.2.6).
- Every check that decides whether data is stored runs on the server, in one function every route calls (§8.2.5). Older code breaks this: `POST /api/products/bulk` checks nothing on the server, so never copy it (`TD-products-live-unchecked` in §11).
- Local development uses a local D1 database, never PostgreSQL. Migration files in `worker/migrations/` are never renamed: D1 records applied migrations by filename. New migrations continue from `0008` (§8.2.8).
- Every change to a product's Approval, an API Key's status, or a product's removal records who made it and when, and that record is never edited (§8.2.9).
- There is no test framework yet: run each test in the design-of-record's test list by hand against `npm run dev` and record the results in the pull request (§8.2.10).

**Logging** (§8.2.7). Log identifiers, never content: no secrets, tokens, API Keys, or passwords, and for a person their ID, never their email or demographic answers. Never log a whole object. Every `catch` that does not rethrow logs the exception; an empty `catch` is not allowed.

## The workflow the agent follows

- Work on a branch. Never push to `main` in this repository or to `tcu-fall-2026-stage` in `MM-Version`; every change is a pull request, described with `.github/pull_request_template.md` (at most three lines per section, never restate the diff).
- **The spec is the contract.** Before implementing anything, a documented use case must exist in `docs/requirements/use-cases.md`; if none does, it is written first. A use case gives what to build and the flows to test: its main flow and every extension.
- **The glossary fixes vocabulary.** Use the term defined in `docs/requirements/project-glossary.md` in code identifiers and UI text, never a synonym (for example API Key, not "token" or "integration"; Text Card, not "text item").
- **Challenge, never comply silently.** The spec is authoritative but not infallible. When a step is ambiguous, an assumption breaks against the code, or requirements contradict, ask or push back; don't silently comply or silently invent.
- **Never answer for the client.** A question only the client can answer goes to `docs/requirements/OPEN-ISSUES.md`.
- **Cite, never copy.** Refer to `UC-*`, `BR-*`, `FR-*`, quality attributes, and `KD-*` by ID and path.
- **Pin or derive.** If guessing a detail wrong would violate a requirement, the spec or design pins it; otherwise derive it from the conventions.
- **Code is evidence, never authority.** Behavior read back from `MM-Version` that nobody specified is not a requirement until the client calls it intended.
- **The client owns `main` in `MM-Version`.** Nothing merges into it without his consent. When pulling his changes from `main` conflicts with ours, ask him how to resolve it.

### Running more than one agent

- One agent per sub-issue, each in its own worktree and branch (`claude --worktree <name>`), each ending in its own pull request.
- Fan out only after the shared code the leaves depend on is merged.
- Never split one use case's layers across agents.
- No more agents running than pull requests you will review that day.

## What the agent must not do

- Never add a dependency until a person confirms it exists and is the one we meant.
- Never remove the `Co-Authored-By` trailer from a commit.
- Never read secrets. `.claude/settings.json` denies `.env` and `.env.*`, `.dev.vars` and `.dev.vars.*`, `secrets/`, `*.pem`, and `*.key`. Secrets live in `.env.local` and `.dev.vars` locally and as Cloudflare Worker secrets in production, never in git. Refer to a secret by its name only.
- Never push to `main` or `tcu-fall-2026-stage`, force-push, merge a pull request, or delete a repository.
- Never run a production deploy (`npm run deploy`): it ships from `main`, which only the client controls.
