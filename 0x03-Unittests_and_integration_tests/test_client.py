import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.GithubOrgClient.get_json', return_value={"login": "expected"})
    def test_org(self, org_name, expected_json, mock_get_json):
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"login": "expected"})
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
