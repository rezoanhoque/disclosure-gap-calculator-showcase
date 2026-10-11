# Disclosure Gap Calculator

A browser research tool by **M. R. Hoque** for comparing two English disclosures using descriptive tone, uncertainty and readability measurements.

[Open the calculator](https://rezoanhoque.github.io/tools/disclosure-gap/) · [See the animated pipeline](https://rezoanhoque.github.io/demos/disclosure-calculator-pipeline/) · [Methods](https://rezoanhoque.github.io/tools/reproducibility/)

## Features

- Compare category rates and net tone between two passages.
- Inspect matching words and descriptive readability measurements.
- Import a research dictionary and export measurements with dictionary/version information and input fingerprints.
- Process text inside the browser; calculator inputs are not sent to the literature synthesis API.

The production interface is built with Astro and TypeScript. This public repository contains a project summary and a deliberately small teaching example. The complete project source is maintained privately.

## Reproduce the central calculation

Run `python tone_gap_example.py` with Python 3. No packages, private data or API keys are needed. The example uses invented passages and an illustrative two-word vocabulary. It implements only category-rate and net-tone differences, not the app's full tokenizer, dictionaries, readability or export features.

Category rate = 100 × matching word occurrences / total word tokens.
Net tone = positive rate − negative rate.
Disclosure gap = net tone A − net tone B (percentage points).

Equal inputs give zero gap; swapping inputs reverses its sign. A tone difference does not prove deception, contradiction, causality or investment value. Comparable reporting periods and sections matter. Research users should obtain the official Loughran–McDonald dictionary from its authors and follow its terms; it is not redistributed here.

## Scope

Only the summary and synthetic teaching example are published here. No private research datasets, proprietary word lists, credentials or backend source are included. You may copy and adapt the teaching example with attribution; see `EXAMPLE_LICENSE.txt`.

For collaboration or additional replication materials, [contact me](https://rezoanhoque.github.io/contact/).
