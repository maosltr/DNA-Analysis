# DNA-Analysis

## Setup environment

### Linux
```bash
chmod +x setup_env.sh
source setup_env.sh
```

### Windows
```bash
.\setup_env.bat
```

## Codon analysis

```bash
python src/analysis/codon_analysis.py
```

# Testing

```bash
python -m unittest tests/tests.py

```

# Documentation (Ongoing)

## doc

```bash
virtualenv .venv
source .venv/bin/activate
pip install pdoc3
pdoc --html -o ./docs .
```

# Dependencies (Ongoing)

```bash
source .venv/bin/activate
pip install graphviz
pip install pylint
pyreverse your_module_or_package -o dot
dot -Tpng input.dot -o output.png
```

# Tools (Ongoing)
