# DNA-Analysis

## Setup environment

### Linux
```bash
virtualenv .venv
source .venv/bin/activate
pip install pandas
pip install html-testRunner
pip install pdoc3

chmod +x setup_env.sh
source setup_env.sh
```

### Windows
```bash
python -m venv  .venv
.\.venv\Scripts\activate
pip install pandas
pip install html-testRunner
pip install pdoc3
.\setup_env.bat
```


## Codon analysis

```bash
python src/analysis/codon_analysis.py
```

# Testing

```bash
python tests/test_codon_analysis.py
```

Test reports are saved under ./tests/reports

# Documentation (Ongoing)

## doc

```bash
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

# Tools

```bash
source .venv/bin/activate
pip freeze > requirements.txt
pip install -r requirements.txt
```
