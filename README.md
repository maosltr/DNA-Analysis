# DNA-Analysis

# Documentation (Ongoing)

## doc
```bash
virtualenv .venv
source .venv/bin/activate
pip install pdoc3
pdoc --html -o ./docs .
```

# Dependencies

```bash
source .venv/bin/activate
pip install graphviz
pip install pylint
pyreverse your_module_or_package -o dot
dot -Tpng input.dot -o output.png
```

# Tools (Ongoing)