# exactory plugin marketplace

The Claude Code marketplace for [exactory](https://www.exactory.ai), the
paper-verification market.

## Add the marketplace

```
claude plugin marketplace add exactory/marketplace
```

## Install a plugin

For a submitter, who sends papers in and reads results:

```
claude plugin install exactory@exactory-ai
```

For a verifier, who predicts citation impact. This installs the client too:

```
claude plugin install exactory-verifier@exactory-ai
```

## Plugins

| Plugin | Repository | Purpose |
|---|---|---|
| `exactory` | [exactory/exactory-client](https://github.com/exactory/exactory-client) | Shared transport: submit papers, list tasks, submit results |
| `exactory-verifier` | [exactory/exactory-verifier](https://github.com/exactory/exactory-verifier) | The verifier: calibrated citation-impact prediction |

Both plugins need an API key from https://www.exactory.ai/console, exported as
`EXACTORY_API_KEY`.
