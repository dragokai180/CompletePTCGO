"""Consume products and grant their contents in one database transaction."""

from collections import Counter

from sqlalchemy import text

from spirit.database import Account, Collection, db_session
from spirit.game.models.product import Deck as DeckProduct


def open_products(account_id, products, *, purchased=False, tradable_override=None):
    """Return (product GUID, card GUIDs, tradable) rows after an atomic opening."""
    if not products:
        return []
    with db_session() as session:
        if session.bind.dialect.name == "sqlite":
            session.execute(text("BEGIN IMMEDIATE"))
        else:
            session.query(Account).filter_by(account_id=account_id).with_for_update().one()

        product_guids = {product.guid for product in products}
        owned = {row.archetype_id: row for row in session.query(Collection).filter(
            Collection.account_id == account_id,
            Collection.archetype_id.in_(product_guids)).with_for_update()}
        grants = Counter()
        opened = []
        for product in products:
            item = owned.get(product.guid)
            tradable = purchased or item is None or item.nontradable_count <= 0
            if tradable_override is not None and not isinstance(product, DeckProduct):
                tradable = bool(tradable_override)
            field = "tradable_count" if tradable else "nontradable_count"
            if not purchased:
                if item is None or getattr(item, field) <= 0:
                    raise ValueError("The account does not own enough of the requested products")
                setattr(item, field, getattr(item, field) - 1)
            contents = list(product.open(account_id if isinstance(product, DeckProduct) else "-1"))
            grants.update((guid, field) for guid in contents)
            opened.append((product.guid, contents, tradable))

        missing = {guid for guid, _ in grants} - owned.keys()
        if missing:
            owned.update({row.archetype_id: row for row in session.query(Collection).filter(
                Collection.account_id == account_id,
                Collection.archetype_id.in_(missing)).with_for_update()})
        for (guid, field), count in grants.items():
            item = owned.get(guid)
            if item is None:
                item = Collection(account_id=account_id, archetype_id=guid,
                                  tradable_count=0, nontradable_count=0)
                session.add(item)
                owned[guid] = item
            setattr(item, field, getattr(item, field) + count)
    return opened
