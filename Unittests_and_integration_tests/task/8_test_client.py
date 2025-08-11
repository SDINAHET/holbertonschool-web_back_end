#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient.

This module contains unit tests that validate how GithubOrgClient fetches
organization data and exposes public repositories via its helper methods.
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Verify that has_license returns the correct boolean."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos using fixtures."""

    @classmethod
    def setUpClass(cls):
        """Start patcher for requests.get and return fixture payloads
        by URL."""
        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()

        def side_effect(url):
            resp = Mock()
            if url == GithubOrgClient.ORG_URL.format(org="google"):
                resp.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                resp.json.return_value = cls.repos_payload
            else:
                resp.json.return_value = {}
            return resp

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """public_repos should return the expected list of repo names."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """public_repos should filter by license when provided."""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"), self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
