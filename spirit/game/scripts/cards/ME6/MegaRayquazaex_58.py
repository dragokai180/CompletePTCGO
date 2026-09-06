import random

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


async def roar_of_the_ruler(ctx):
    """Look at the top 4 cards of your deck and attach up to 1 Basic Energy
    card you find there to this Pokémon. Shuffle the other cards and put
    them on the bottom of your deck."""
    top = ctx.deck_top(4)
    matches = [c for c in top if is_basic_energy_card(c)]
    picks = []
    if top:
        picks = await ctx.choose_cards(
            matches, 1, minimum=0,
            prompt="Choose a Basic Energy card to attach to this Pokémon.",
            display_cards=top,
        )
        if picks:
            await ctx.attach_energy(picks[0], ctx.source)
    others = [c for c in top if c not in picks]
    random.shuffle(others)
    for card in others:
        await ctx.put_on_bottom_of_deck(card)


def _fire_and_lightning_energy(ctx):
    return (
        count_energy("mine", PokemonTypes.FIRE)(ctx)
        + count_energy("mine", PokemonTypes.LIGHTNING)(ctx)
    )


card = PokemonCardDef(
    guid="eb07e001-e746-510e-b835-cade4d69d31c",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaRayquazaex.Name",
    display_name="Mega Rayquaza ex",
    searchable_by=["Mega Rayquaza ex","Basic","ex","SV_Mega","MegaRayquazaex"],
    subtypes=["Basic","ex","SV_Mega"],
    collector_number=58,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=384,
    abilities=[
        Ability(
            title="Roar of the Ruler",
            game_text="You may use this Ability when you play this Pokémon from your hand onto your Bench. Look at the top 4 cards of your deck and attach up to 1 Basic Energy card you find there to this Pokémon. Shuffle the other cards and put them on the bottom of your deck.",
            trigger=Triggers.ON_PLAY,
            effect=roar_of_the_ruler,
        ),
        Attack(
            title="Storm Emeralda",
            game_text="This attack does 50 damage for each [R] Energy and [L] Energy attached to all of your Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(_fire_and_lightning_energy, 50),
        ),
    ],
)
