import sys
sys.path.append('/Users/fortecpcjp2/kameleon/lib/python2.7/site-packages/ccmc/')
import _CCMC as ccmc
import math


def interpolar(modelo, variavel, xi, yi, zi, xf, yf, zf, np, cond):
	global x, y, z
	if (len(argv) == 10):
		filename = '/Users/fortecpcjp2/Documents/python/' + modelo
		variable = variavel

		xi = float(xi)
		yi = float(yi)
		zi = float(zi)

		xf = float(xf)
		yf = float(yf)
		zf = float(zf)

		np = int(np)

		cond = str(cond)

		drx = (xf-xi)/(np-1)
		dry = (yf-yi)/(np-1)
		drz = (zf-zi)/(np-1)
		drr = math.sqrt(drx**2+dry**2+drz**2)

		kameleon = ccmc.Kameleon()
		kameleon.open(filename)
		kameleon.loadVariable(variable)

		interpolator = kameleon.createNewInterpolator()
		x = [0]*np
		y = [0]*np
		z = [0]*np
		d = [0]*np
		var = [0]*np
		for i in range(1, np+1):
			x[i-1] = xi + (i-1)*drx
			y[i-1] = yi + (i-1)*dry
			z[i-1] = zi + (i-1)*drz
			d[i-1] = (i-1)*drr


			var[i-1] = str(interpolator.interpolate(variable, x[i-1], y[i-1], z[i-1]))
			f.write('Ponto (' + str(x[i-1]) +', ' + str(y[i-1]) + ', ' + str(z[i-1]) + '): ' + str(var[i-1]) +'\n')


		f.close()

		if (cond == 'sim'):
			import matplotlib.pyplot as plt
			plt.plot(d,var)
			plt.title('Perfil sol-terra do modelo ' + argv[0] )
			plt.xlabel('Distancia')
			plt.ylabel(argv[1])
			plt.legend('Perfil sol-terra do modelo ' + argv[0] + ' e variavel ' + argv[1] + ' interpolada entre os pontos (' + str(xi) + ', ' + str(yi) + ', ' + str(zi) + ') e (' + str(xf) + ', ' + str(yf) + ', ' + str(zf) + ')')
			plt.show()

		kameleon.close()
	else:
		print 'Usage: <filename> <variable> x, y, z \n python kameleon_test rho -40 0 0'

if __name__ == '__main__':
	main(sys.argv[1:])
