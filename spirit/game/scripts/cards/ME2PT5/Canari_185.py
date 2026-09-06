from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import hand_size_at_least
from spirit.game.session.effects import is_pokemon_card


def _is_lightning_pokemon(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.LIGHTNING.value in types


async def canari(ctx):
    """Discard another card from your hand, then search for up to 4 Lightning
    Pokémon."""
    discarded = await ctx.discard_from_hand(
        1, prompt="Discard a card from your hand",
    )
    if not discarded:
        return
    picks = await ctx.search_deck(
        _is_lightning_pokemon, count=4, minimum=0,
        prompt="Choose up to 4 Lightning Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="41dda04f-f147-5b08-8934-8111e0ed2600",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Canari.Name",
    display_name="Canari",
    searchable_by=["Canari","Supporter","Canari"],
    subtypes=["Supporter"],
    collector_number=185,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=canari,
    condition=hand_size_at_least(2),
)
