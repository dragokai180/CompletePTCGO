from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import heal_targets
from spirit.game.models.board import BoardState
from spirit.game.session.passives import effective_max_hp


def _has_grass_energy(pokemon):
    return any(
        energy_provides_type(e, PokemonTypes.GRASS.value)
        for e in BoardState.attached_energies(pokemon)
    )


def fermented_juice_condition(board, player_id, pokemon):
    if not _has_grass_energy(pokemon):
        return False
    return any(
        p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
        for p in board.pokemon_in_play(player_id)
    )


card = PokemonCardDef(
    guid="aa8541f0-624e-5d2d-9220-b6289084dd6f",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle","Basic","Shuckle"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    family_id=213,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Ability(
            title="Fermented Juice",
            game_text="Once during your turn, if this Pokémon has any Grass Energy attached, you may use this Ability. Heal 30 damage from 1 of your Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=fermented_juice_condition,
            effect=heal_targets(30, scope="choice"),
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
