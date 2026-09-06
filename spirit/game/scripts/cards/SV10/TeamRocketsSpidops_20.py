from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.support_common import attach_from_discard, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_team_rockets(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Team Rocket's ")


def _count_team_rockets(ctx):
    return sum(1 for p in ctx.my_pokemon_in_play() if _is_team_rockets(p))


charging_up = attach_from_discard(
    predicate=is_basic_energy_card, count=1, target="self",
    prompt="Choose a Basic Energy card to attach.",
)


card = PokemonCardDef(
    guid="e84dd0d8-33ce-5428-8eaf-a87b0b74571c",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsSpidops.Name",
    display_name="Team Rocket's Spidops",
    searchable_by=["Team Rocket's Spidops", "Stage 1", "TeamRocketsSpidops"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsTarountula.Name",
    family_id=917,
    abilities=[
        Ability(
            title="Charging Up",
            game_text="Once during your turn, you may attach a Basic Energy card from your discard pile to this Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_discard(is_basic_energy_card),
            effect=charging_up,
        ),
        Attack(
            title="Rocket Rush",
            game_text="This attack does 30 damage for each of your Team Rocket's Pokémon in play.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(_count_team_rockets, 30),
        ),
    ],
)
