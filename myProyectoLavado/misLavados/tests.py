from django.test import TestCase
import unittest
from .models import Insumos, MisionyVision, SliderGaleria, SliderIndex
from .views import registro,User
from .static import js


# Create your tests here.


class TestInsumosymision(unittest.TestCase):

    def test_grabar_insumos(self):
        valor = 0
        try:
            insumo = Insumos(
                nombre="bateria",
                descripcion="buena",
                precio=76990,
                stock=1
            )
            insumo.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

    def test_mision_vision(self):
        valor = 0
        try:
            MisionyVision(
                ident="1",
                mision="nuestra mision es",
                vision="nuesta vision es"
            )
            MisionyVision.save()
            valor = 1
            
        except:
            valor = 0
        self.assertEqual(valor,1)


class TestValidacionSlider(unittest,TestCase):
    def testvalidarSliderIndex(self):
        valor = 0
        try:
            SliderIndex(
                ident="1",
                image="1"
            )
            SliderIndex.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)    

    def testvalidarSliderGaleria(self):
        valor = 0
        try:
            SliderGaleria(
                ident1="1",
                image="1"
            )
            SliderGaleria.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)



if __name__ == "__main__":
    unittest.main()
