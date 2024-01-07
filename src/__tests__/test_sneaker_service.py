import unittest
from unittest.mock import MagicMock, patch
from fastapi import HTTPException
from src.modules.sneakers.schema import SneakerSchema
from src.services.sneaker_service import SneakerService
with patch.dict("os.environ", {"X_TOKEN": "your_mocked_token"}):
    from src.configs.auth import verify_token  # Import here

class TestSneakerService(unittest.TestCase):
    def setUp(self):
        self.db_session_mock = MagicMock()
        self.sneaker_service = SneakerService(self.db_session_mock)

    def test_get_sneakers_success(self):
        # Mocking the find_all method of sneaker_repository
        with patch("src.services.sneaker_service.SneakerRepository.find_all") as find_all_mock:
            find_all_mock.return_value = [{"id": 1, "name": "Test Sneaker"}]

            response = self.sneaker_service.get_sneakers()

            find_all_mock.assert_called_once()
            self.assertTrue(response["status"])
            self.assertEqual(response["code"], 200)
            self.assertEqual(response["message"], "Sneakers retrieved successfully")
            self.assertEqual(response["data"], [{"id": 1, "name": "Test Sneaker"}])

    # def test_get_sneakers_exception(self):
    #     # Mocking the find_all method of sneaker_repository to raise an exception
    #     with patch("src.services.sneaker_service.SneakerRepository.find_all") as find_all_mock:
    #         find_all_mock.side_effect = HTTPException(status_code=500, detail="Internal Server Error")

    #         response = self.sneaker_service.get_sneakers()

    #         find_all_mock.assert_called_once()
    #         self.assertFalse(response["status"])
    #         self.assertEqual(response["code"], 500)
    #         self.assertEqual(response["message"], "Internal server error")

    # # Similar tests for other methods...

    # def test_add_sneaker_success(self):
    #     payload = SneakerSchema(name="New Sneaker")

    #     # Mocking the necessary methods of sneaker_repository
    #     with patch("src.services.sneaker_service.SneakerRepository.find_one_by_where") as find_one_mock, \
    #          patch("src.services.sneaker_service.SneakerRepository.create") as create_mock:
    #         find_one_mock.return_value = None
    #         create_mock.return_value = {"id": 1, "name": "New Sneaker"}

    #         response = self.sneaker_service.add_sneaker(payload)

    #         find_one_mock.assert_called_once_with({"name": "New Sneaker"})
    #         create_mock.assert_called_once_with({"name": "New Sneaker"})
    #         self.assertTrue(response["status"])
    #         self.assertEqual(response["code"], 201)
    #         self.assertEqual(response["message"], "Sneakers added successfully")
    #         self.assertEqual(response["data"], {"id": 1, "name": "New Sneaker"})

    # # Similar tests for other methods...

    def tearDown(self):
        self.sneaker_service = None


if __name__ == '__main__':
    unittest.main()
