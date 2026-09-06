from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import energy_provides_type


def _is_basic_fire_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.FIRE.value
    )


def _is_basic_lightning_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.LIGHTNING.value
    )


async def adventuring_lantern(ctx):
    """Search your deck for a Basic Fire Energy and a Basic Lightning Energy,
    reveal them, and put them into your hand. Then, shuffle your deck."""
    fire, lightning = await ctx.search_deck_groups(
        [
            (_is_basic_fire_energy, 1, "Basic Fire Energy"),
            (_is_basic_lightning_energy, 1, "Basic Lightning Energy"),
        ],
        prompt="Choose a Basic Fire Energy and a Basic Lightning Energy",
    )
    await ctx.put_in_hand(fire + lightning, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="e1e235c5-ee31-518f-8bee-9b346390de7e",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdventuringLantern.Name",
    display_name="Adventuring Lantern",
    searchable_by=["Adventuring Lantern","Item","AdventuringLantern"],
    subtypes=["Item"],
    collector_number=64,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=adventuring_lantern,
)
