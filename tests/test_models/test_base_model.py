#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_new_instance(self):
        my_model = BaseModel()

        result = my_model

        self.assertIsInstance(result, BaseModel)

    def test_str_method(self):
        my_model = BaseModel()
        expected_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        result_str = str(my_model)

        self.assertEqual(result_str, expected_str)
      
    def test_attributes_initialization(self):
        my_model = BaseModel()

        attributes = my_model.__dict__.keys()

        self.assertIn('id', attributes)
        self.assertIn('created_at', attributes)
        self.assertIn('updated_at', attributes)



    def test_to_dict_method(self):
        my_model = BaseModel()

        result_dict = my_model.to_dict()


        self.assertIsInstance(result_dict, dict)
        self.assertIn('id', result_dict)
        self.assertIn('__class__', result_dict)
        self.assertIn('created_at', result_dict)
        self.assertIn('updated_at', result_dict)


    def test_save_method(self):
        my_model = BaseModel()
        original_updated_at = my_model.updated_at

        my_model.save()
        new_updated_at = my_model.updated_at

        self.assertNotEqual(original_updated_at, new_updated_at)
      
if __name__ == '__main__':
    unittest.main()
