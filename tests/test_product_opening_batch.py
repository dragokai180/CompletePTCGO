"""Product openings must commit all grants and consumption together."""

import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from spirit.database import Account, Base, Collection
from spirit.database.deck_products import open_products


class _Pack:
    guid = "pack"

    def open(self, account_id):
        return ["card", "card"]


class ProductOpeningBatchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.engine = create_engine(f"sqlite:///{Path(self.tmp.name) / 'test.db'}")
        Base.metadata.create_all(self.engine)
        factory = sessionmaker(bind=self.engine)

        @contextmanager
        def session():
            db = factory()
            try:
                yield db
                db.commit()
            except Exception:
                db.rollback()
                raise
            finally:
                db.close()

        self.session = session
        self.patch = patch("spirit.database.deck_products.db_session", session)
        self.patch.start()

    def tearDown(self):
        self.patch.stop()
        self.engine.dispose()
        self.tmp.cleanup()

    def _seed(self, count):
        with self.session() as db:
            db.add(Account(account_id="owner", username="owner", password_hash="hash",
                           screen_name="owner"))
            db.add(Collection(account_id="owner", archetype_id="pack",
                              tradable_count=count, nontradable_count=0))

    def test_two_packs_commit_as_one_batch(self):
        self._seed(2)
        opened = open_products("owner", [_Pack(), _Pack()])
        self.assertEqual(len(opened), 2)
        with self.session() as db:
            pack = db.get(Collection, ("owner", "pack"))
            card = db.get(Collection, ("owner", "card"))
            self.assertEqual(pack.tradable_count, 0)
            self.assertEqual(card.tradable_count, 4)

    def test_insufficient_stock_rolls_back_entire_batch(self):
        self._seed(1)
        with self.assertRaises(ValueError):
            open_products("owner", [_Pack(), _Pack()])
        with self.session() as db:
            self.assertEqual(db.get(Collection, ("owner", "pack")).tradable_count, 1)
            self.assertIsNone(db.get(Collection, ("owner", "card")))

    def test_purchased_pack_does_not_require_owned_inventory(self):
        self._seed(0)
        opened = open_products("owner", [_Pack()], purchased=True)
        self.assertEqual(len(opened), 1)
        with self.session() as db:
            self.assertEqual(db.get(Collection, ("owner", "pack")).tradable_count, 0)
            self.assertEqual(db.get(Collection, ("owner", "card")).tradable_count, 2)


if __name__ == "__main__":
    unittest.main()
