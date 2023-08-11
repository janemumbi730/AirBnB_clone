import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def tearDown(self):
        self.amenity = None
     
    def setUp(self):
        self.amenity = Amenity()
      
    
    def test_attributes_initialization(self):
        self.assertEqual(self.amenity.name, "")
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
    
    def test_save_method(self):
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        new_updated_at = self.amenity.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
  
    def test_str_method(self):
        amenity_str = str(self.amenity)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn("id", amenity_str)
        self.assertIn("created_at", amenity_str)
        self.assertIn("updated_at", amenity_str)

if __name__ == "__main__":
    unittest.main()
