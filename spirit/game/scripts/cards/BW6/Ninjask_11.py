from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, def_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import dimension_heal, strafe
from spirit.game.card_effects.support_common import heal_attack


def _is_shedinja(card):
    definition = def_for(card.archetype_id)
    return getattr(definition, "display_name", None) == "Shedinja"

async def cast_off_shell(ctx):
    if not await ctx.ask_yes_no("Search your deck for Shedinja and put it onto your Bench?"):
        return
    picks = await ctx.search_deck(
        _is_shedinja, count=1, minimum=0,
        prompt="Choose Shedinja to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()



card = PokemonCardDef(
    guid="caeb19f2-f937-55ac-9010-8e74f1faae44",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name",
    display_name="Ninjask",
    searchable_by=["Ninjask","Stage 1","Ninjask"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    abilities=[
        Ability(
            title="Cast-off Shell",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may search your deck for Shedinja and put it onto your Bench. Shuffle your deck afterward.",
            trigger=Triggers.ON_EVOLVE,
            effect=cast_off_shell,
        ),
        Attack(
            title="Night Slash",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=strafe,
        ),
    ],
)
