# -*- coding: utf-8 -*-
"""
Automated Unit Tests for the PDAC Nanomedicine Biocomputing Models.
"""

import unittest
# Simulated imports from models
from models import calculate_hill_occupancy, evaluate_phi_death

class TestPDACModels(unittest.TestCase):
    
    def test_hill_cooperativity(self):
        # Test half-maximal occupancy condition
        res = calculate_hill_occupancy(X=5.0, K_D=5.0, n=2)
        self.assertAlmostEqual(res, 0.5)

    def test_phi_death_liver_protection(self):
        # Healthy hepatocyte condition (B_miRNA = True) -> Phi_Death must be 0
        phi = evaluate_phi_death(A1=True, A2=True, B_miRNA=True, gpx4_conc=0.01, ros_lipid=10, fe2_free=5)
        self.assertEqual(phi, 0.0)

    def test_phi_death_tumor_ablation(self):
        # PDAC tumor cell condition (B_miRNA = False) -> Phi_Death diverges as GPX4 -> 0
        phi = evaluate_phi_death(A1=True, A2=True, B_miRNA=False, gpx4_conc=0.0, ros_lipid=50, fe2_free=20)
        self.assertEqual(phi, float('inf'))

if __name__ == "__main__":
    # Internal definitions to mimic operational environment
    import sys
    # Injection of variables into global context for mock execution
    class MockModels:
        calculate_hill_occupancy = calculate_hill_occupancy
        evaluate_phi_death = evaluate_phi_death
    sys.modules['models'] = MockModels
    
    unittest.main()
