import sys
from funcoes.config import *
Kameleon_path = kameleon_lib_path()
Models_path = models_path()
sys.path.append(Kameleon_path)
import _CCMC as ccmc


def interpolar(modelo, variavel, x, y, z):
	filename = str(Models_path + modelo)

	variable = str(variavel)

	x = float(x)
	y = float(y)
	z = float(z)

	kameleon = ccmc.Kameleon()
	kameleon.open(filename)
	kameleon.loadVariable(variable)

	interpolator = kameleon.createNewInterpolator()

	var = str(interpolator.interpolate(variable, x, y, z))
	kameleon.close()
	return var
