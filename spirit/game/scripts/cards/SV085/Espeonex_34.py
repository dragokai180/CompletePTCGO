from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand
from spirit.game.card_effects.pokemon import TeraRulePassive, devolvable


async def psych_out(ctx):
    """160. Discard a random card from your opponent's hand."""
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)


async def amazez(ctx):
    """Devolve each of your opponent's evolved Pokémon by shuffling the
    highest Stage Evolution card on it into your opponent's deck."""
    shuffled = False
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        if not devolvable(pokemon) or ctx.effects_blocked(pokemon):
            continue
        removed = await ctx.devolve_pokemon(pokemon, steps=1, destination="deck")
        if removed:
            shuffled = True
    if shuffled:
        await ctx.shuffle_deck(ctx.opponent_id)


card = PokemonCardDef(
    guid="0bb4fd9d-d518-55ec-a470-a85e91a0c4b1",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeonex.Name",
    display_name="Espeon ex",
    searchable_by=["Espeon ex","Stage 1","ex","Tera","Espeonex"],
    subtypes=["Stage 1","ex","Tera"],
    collector_number=34,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    family_id=133,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Psych Out",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=psych_out,
        ),
        Attack(
            title="Amazez",
            game_text="Devolve each of your opponent's evolved Pokémon by shuffling the highest Stage Evolution card on it into your opponent's deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            effect=amazez,
        ),
    ],
)
