# neurosymbolic-reasoning

Positive Horn-clause inference and explainable access derivation.

## Scope

A small, inspectable, reproducible **v0.1 reference implementation**. The project is not presented as a production system or peer-reviewed research result.

## Requirements

Python 3.12

## Setup

```bash
python -m pip install pytest
```

## Run example / experiment

From the repository root:

```bash
python -m examples.access_control
```

## Test

```bash
python -m pytest -q
```

## Reproducibility

Experiments use deterministic inputs or explicitly seeded generators. See the experiment sources for assumptions and input sizes. CI exercises both tests and the example; check the Actions tab for actual run results. No empirical results are claimed without executed measurements.

## Limitations

This is a symbolic inference component. It does not yet integrate neural perception or learned scores; recursive rules may produce large closures.

## License

MIT. Contributions should include a focused regression test and an explanation of changed assumptions.

## Run without local setup

The repository is self-tested by GitHub Actions. To run validation remotely, open [CI](https://github.com/MonikaDvorackova/neurosymbolic-reasoning/actions/workflows/ci.yml), select **Run workflow**, choose `main`, and inspect the test job. You do not need to run Python, Rust, or C++ commands from your Mac. For local execution, clone this repository and run commands from its root (not `~`).

## Project showcase and feedback

Part of a public [trustworthy AI and reliable ML research engineering portfolio](https://github.com/MonikaDvorackova/MonikaDvorackova#research-engineering-projects). For project scope, test coverage and limitations, see this README and the repository's GitHub Actions. Reproducible issues and narrowly scoped contributions are welcome. These reference implementations are not certified production systems.
