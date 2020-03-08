from django.test import TestCase
from .models import Artifact
# Create your tests here.


class ArtifactTests(TestCase):
    # Here we'll define the tests that we'll run against our
    # Artifact model

    def test_str(self):
        test_name = Artifact(name='Demon Dweller Sword')
        self.assertEqual(str(test_name), 'Demon Dweller Sword')
