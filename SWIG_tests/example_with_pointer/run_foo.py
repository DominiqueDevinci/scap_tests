import example
from pprint import pprint
import inspect

pprint(inspect.getmembers(example));
print(help(example));
pprint(example.sub(5, 2));
