from parser import Parser
from msd import SteepestDescentMethod
from gss import GoldenSectionSearch

parser = Parser()
gss = GoldenSectionSearch()
msd = SteepestDescentMethod(parser.function, gss)

