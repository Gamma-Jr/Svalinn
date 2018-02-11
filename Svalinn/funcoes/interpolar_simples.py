import sys
sys.path.append('/Users/fortecpcjp2/kameleon/lib/python2.7/site-packages/ccmc/')
import _CCMC as ccmc


def interpolar(modelo, variavel, x, y, z):
	filename = str('/Users/fortecpcjp2/Documents/Testes/python/' + modelo)

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
