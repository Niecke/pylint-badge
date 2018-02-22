pylint-badge
====
A small python module to generate pylint badges directly from command line

## Usage

```
pip install pylint
```

Go to your project root folder and generate pylint report for your code
```
pylint --output-format=html >> pylint.html
```
*pylint.html file name should not changed

Copy pylint-badge project folder to your project root folder and run
```
python3 -c "from pylint-badge.pylint_badge import generate_from_report; generate_from_report()"
```

python pip install git+https://github.com/lucasventurasc/pylint-badge

In your virtualenv you should can access by pylint-badge keyword

In folder that you was run the command will have a rating.svg

Put a badge on your README accordingly.
