from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.models.board import BoardState


def _no_energy_attached(pokemon, carrier):
    return pokemon is carrier and not BoardState.attached_energies(pokemon)


card = PokemonCardDef(
    guid="2ddf9be4-2526-5c2e-8fbc-a548cea73342",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander","Basic","Charmander"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    family_id=4,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Ability(
            title="Agile",
            game_text="If this Pokémon has no Energy attached, it has no Retreat Cost.",
            passive=retreat_free_when(_no_energy_attached),
        ),
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)
