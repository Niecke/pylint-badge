pylint-badge
====
A small python module to generate pylint badges directly from command line

## Install

Install pylint
```
pip install pylint
```

Install pylint-badge
```
python pip install git+https://github.com/lucasventurasc/pylint-badge
```

Go to your project root folder and generate pylint report for your code
```
pylint --output-format=html >> pylint.html
```
*pylint.html file name should not changed

```
python3 -c "from pylint_badge import generate_from_report; generate_from_report()"
```
In folder that you was run the command, will have a badge with name rating.svg

Put a badge on your README accordingly.
