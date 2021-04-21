#!/usr/bin/env python3
""" test client
"""

from unittest import mock, Testcase
from unittest.mock import patch
from parameterized import parameterized
import client


class TestGithubOrgClient(TestCase):
    """ test that GithubOrgClient.org returns the correct value
    """
    @parameterized.expand([("google"), ("abc"), ])
    @patch('client.get_json')
    def test_org(self, org, mock_test):
        """ test that GithubOrgClient.org returns the correct value
        """
        test = client.GithubOrgClient(org)
        test.org()
        mock_test.assert_called_once_with(
            f'https://api.github.com/orgs/{org}'
            )

    def test_public_repos_url(self):
        """ Test that the result of _public_repos_url
          - is the expected one based on the mocked payload
        """
        with patch(GithubOrgClient,
                          new_callable=PropertyMock,
                          return_value={"repos_url": "google"}) as mock_url:
            response = GithubOrgClient('google')
            repo_url = response._public_repos_url

        self.assertEqual(repo_url, mock_url.return_value['repos_url'])



