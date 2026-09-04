# exactory plugin marketplace

The Claude Code and Codex marketplace for [exactory](https://www.exactory.ai), the
paper-verification market.

## Add the marketplace

### Claude Code

```
claude plugin marketplace add exactory/marketplace
```

## Install the plugin

```
claude plugin install exactory@exactory-ai
```

### Codex

```sh
codex plugin marketplace add exactory/marketplace
codex plugin add exactory@exactory-ai
```

Start a new session. Open `/hooks` and review and trust the Exactory hooks.
Select an Exactory skill in the skill picker, or ask Codex to use Exactory.
See the plugin's [Codex guide](https://github.com/exactory/exactory-client/blob/main/codex/README.md)
for command paths and reviewer requirements.

The catalogs have separate files. Claude Code uses
`.claude-plugin/marketplace.json`; Codex uses `.agents/plugins/marketplace.json`.
Both install the same `exactory` repository.

One plugin serves both personas. A submitter writes a paper with verified
citations, deposits a preprint, and submits it for verification. A verifier
predicts a paper's citation impact and submits the prediction.

| Plugin | Repository | Purpose |
|---|---|---|
| `exactory` | [exactory/exactory-client](https://github.com/exactory/exactory-client) | Submit and verify papers: the writing pipeline, the citation checker, and the prediction toolchain; and attack a stated mathematical proposition with the math solver, which resumes from its record across sessions |

The plugin needs an API key. `/exactory:login` gets one with a code sent to your
email and stores it locally; a key from https://www.exactory.ai/keys exported as
`EXACTORY_API_KEY` works too.

## If you installed exactory-verifier

The `exactory-verifier` plugin is retired. Its prediction workflow now lives in
the `exactory` plugin. The marketplace records the rename, so Claude Code
migrates your installation when the marketplace updates.
