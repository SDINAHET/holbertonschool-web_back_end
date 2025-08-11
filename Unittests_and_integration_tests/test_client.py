#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient.org"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """org should return the JSON payload and call get_json once"""
        expected = {
            "org": org_name,
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
            }
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )


class TestGithubOrgClient(unittest.TestCase):
    # tes autres tests (test_org) ...

    def test_public_repos_url(self):
        """_public_repos_url doit renvoyer repos_url depuis org (mockée)"""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch.object(
                GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, payload["repos_url"])
            mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()
