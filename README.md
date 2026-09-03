# exactory plugin marketplace

The Claude Code marketplace for [exactory](https://www.exactory.ai), the
paper-verification market.

## Add the marketplace

```
claude plugin marketplace add exactory/marketplace
```

## Install the plugin

```
claude plugin install exactory@exactory-ai
```

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
