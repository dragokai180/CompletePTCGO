from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_basic_grass_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.GRASS.value)


def _solar_transfer_condition(board, player_id, pokemon):
    in_play = board.pokemon_in_play(player_id)
    if len(in_play) < 2:
        return False
    return any(any(_is_basic_grass_energy(e) for e in p.children) for p in in_play)


async def solar_transfer(ctx):
    """Move a Basic Grass Energy from 1 of your Pokémon to another."""
    pokemon = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(
        pokemon, pokemon, predicate=_is_basic_grass_energy, max_count=1,
        prompt="Choose a Basic Grass Energy to move",
    )


card = PokemonCardDef(
    guid="bfc39012-7762-514d-808d-ed256ec36e41",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaVenusaurex.Name",
    display_name="Mega Venusaur ex",
    searchable_by=["Mega Venusaur ex","Stage 2","ex","SV_Mega","MegaVenusaurex"],
    subtypes=["Stage 2","ex","SV_Mega"],
    collector_number=3,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=380,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    family_id=1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    abilities=[
        Ability(
            title="Solar Transfer",
            game_text="As often as you like during your turn, you may use this Ability. Move a Basic Grass Energy from 1 of your Pokémon to another of your Pokémon.",
            activation=Activations.UNLIMITED,
            condition=_solar_transfer_condition,
            effect=solar_transfer,
        ),
        Attack(
            title="Jungle Dump",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 4},
            damage=240,
            effect=heal_attack(30),
        ),
    ],
)
