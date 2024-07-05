#!/usr/bin/env python3
"""Unit tests for the client module."""
import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    patch,
)
from parameterized import parameterized
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, expected_response: Dict,
                 mock_get_json: MagicMock) -> None:
        """Ensure that the org method returns the correct response."""
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), expected_response)
        mock_get_json.assert_called_once_with(
                                    f"https://api.github.com/orgs/{org_name}")
