from spirit.game.data_utils import PokemonToolCardDef, Attack, def_for
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card

CAP_NAME = "Mega Rayquaza Cap"


def _has_mega_rayquaza_cap(pokemon):
    return any(
        getattr(def_for(child.archetype_id), "display_name", None) == CAP_NAME
        for child in pokemon.children
    )


async def delta_gift(ctx):
    """For each of your Pokémon that has a Mega Rayquaza Cap attached, attach
    a Basic Energy card from your deck to that Pokémon. Then, shuffle."""
    holders = [p for p in ctx.my_pokemon_in_play() if _has_mega_rayquaza_cap(p)]
    for pokemon in holders:
        picks = await ctx.search_deck(
            is_basic_energy_card, count=1, minimum=0,
            prompt="Choose a Basic Energy card to attach.",
        )
        if picks:
            await ctx.attach_energy(picks[0], pokemon)
    await ctx.shuffle_deck()


card = PokemonToolCardDef(
    guid="a83c39c0-2957-5132-8e29-2e522a090df0",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaRayquazaCap.Name",
    display_name=CAP_NAME,
    searchable_by=["Mega Rayquaza Cap","Tool","MegaRayquazaCap"],
    subtypes=["Tool"],
    collector_number=66,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Delta Gift",
            game_text='For each of your Pokémon that has a "Mega Rayquaza Cap" attached to it, attach a Basic Energy card from your deck to that Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=delta_gift,
        ),
    ],
)
