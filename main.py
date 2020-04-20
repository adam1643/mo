from parser import Parser
from msd import SteepestDescentMethod
from gss import GoldenSectionSearch

parser = Parser()
gss = GoldenSectionSearch(parser.function)
msd = SteepestDescentMethod(parser.function, gss)

