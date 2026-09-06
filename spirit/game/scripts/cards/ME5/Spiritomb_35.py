from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import (
    count_hide_n_sneak_in_discard,
)


async def spiritual_end(ctx):
    """If you have 13 or more Pokémon that have Hide 'n' Sneak in your discard
    pile, choose 2 of your opponent's Pokémon and quadruple the number of
    damage counters on each of them."""
    if count_hide_n_sneak_in_discard(ctx) < 13:
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, min(2, len(candidates)), minimum=1,
        prompt="Choose 2 of your opponent's Pokémon",
    )
    for pokemon in picks:
        counters = max(0, (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10)
        await ctx.set_damage_counters(pokemon, counters * 4)


card = PokemonCardDef(
    guid="5c675dd7-c3f0-5e58-8cba-e84a22acec13",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb","Basic","Spiritomb"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    family_id=442,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Spiritual End",
            game_text="If you have 13 or more Pokémon that have the Hide 'n' Sneak Ability in your discard pile, choose 2 of your opponent's Pokémon and quadruple the number of damage counters on each of them.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=spiritual_end,
        ),
    ],
)
