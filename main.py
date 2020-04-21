from function_handler import FunctionHandler
from msd import SteepestDescentMethod
from gss import GoldenSectionSearch

f_handler = FunctionHandler()
gss = GoldenSectionSearch()
msd = SteepestDescentMethod(f_handler.function, gss)

