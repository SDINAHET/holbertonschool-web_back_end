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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """public_repos doit retourner la liste des noms depuis le payload
        mocké"""
        # 1) Mock du payload renvoyé par get_json
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        # 2) Mock de la propriété _public_repos_url
        with patch.object(
                GithubOrgClient,
                "_public_repos_url",
                new_callable=PropertyMock
                ) as mock_url:
            mock_url.return_value = "http://example.com/org/repos"

            client = GithubOrgClient("anyorg")
            self.assertEqual(
                    client.public_repos(), ["repo1", "repo2", "repo3"])

            # 3) Vérifications des appels
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                    "http://example.com/org/repos")


if __name__ == "__main__":
    unittest.main()
