from spirit.game.data_utils import PokemonCardDef, Attack, is_pokemon_ex
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import TeraRulePassive


async def severe_squall(ctx):
    """60 to each of your opponent's Pokémon ex. Damage isn't affected by
    Weakness or Resistance."""
    for pokemon in ctx.opponent_pokemon_in_play():
        if is_pokemon_ex(pokemon.archetype_id):
            await ctx.deal_damage(
                60, target=pokemon,
                ignore_weakness=True, ignore_resistance=True,
            )


card = PokemonCardDef(
    guid="d4c4d91b-00ee-5c36-82fa-c5d395a804b1",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeonex.Name",
    display_name="Vaporeon ex",
    searchable_by=["Vaporeon ex","Stage 1","ex","Tera","Vaporeonex"],
    subtypes=["Stage 1","ex","Tera"],
    collector_number=23,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    family_id=133,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Severe Squall",
            game_text="This attack does 60 damage to each of your opponent's Pokémon ex. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=severe_squall,
        ),
        Attack(
            title="Aquamarine",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=280,
            locks_next_turn=True,
        ),
    ],
)
