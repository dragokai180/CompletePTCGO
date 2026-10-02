"""Local options preserve upstream defaults and do not repeat signups."""
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from spirit import config
from spirit.database import Base, Account, accounts


class LocalRegistrationRewardsTests(unittest.TestCase):
    def test_missing_settings_preserves_defaults(self):
        with TemporaryDirectory() as tmp:
            self.assertEqual(config._read_local_settings(Path(tmp) / 'absent.json'), {})

    def test_settings_validate_currency_and_grant_types(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / 'settings.json'
            for text in ('[]', '{"coins_per_win":-1}', '{"coins_per_loss":true}',
                         '{"grant_all_cards_on_registration":"false"}'):
                path.write_text(text)
                with self.assertRaises(ValueError):
                    config._read_local_settings(path)
            path.write_text('{"coins_per_win":10,"coins_per_loss":1,"grant_all_cards_on_registration":true}')
            self.assertEqual(config._read_local_settings(path)['coins_per_win'], 10)

    def test_registration_grants_once_only_when_enabled(self):
        for enabled in (False, True):
            engine = create_engine('sqlite:///:memory:')
            Base.metadata.create_all(engine)
            factory = sessionmaker(bind=engine)
            @contextmanager
            def isolated_session():
                with factory.begin() as session:
                    yield session
            try:
                with patch.object(accounts, 'db_session', isolated_session), \
                        patch.object(accounts, 'grant_starter_content') as starter, \
                        patch.object(config, 'GRANT_ALL_CARDS_ON_REGISTRATION', enabled), \
                        patch('spirit.database.player_data.grant_all_cards', return_value=20000) as grant:
                    result = accounts.create_account('fixture', 'not-a-real-password')
                    self.assertIsNotNone(result)
                    self.assertIsNone(accounts.create_account('fixture', 'duplicate'))
                    starter.assert_called_once_with(result['account_id'])
                    if enabled:
                        grant.assert_called_once_with(result['account_id'], count=4, is_tradable=True)
                    else:
                        grant.assert_not_called()
                    with factory() as session:
                        self.assertEqual(session.query(Account).count(), 1)
            finally:
                engine.dispose()


if __name__ == '__main__':
    unittest.main()
