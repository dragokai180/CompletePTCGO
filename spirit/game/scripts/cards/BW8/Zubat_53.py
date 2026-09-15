from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.models.board import BoardState

def _no_energy_attached(pokemon, carrier):
    return pokemon is carrier and not BoardState.attached_energies(pokemon)

card = PokemonCardDef(
    guid="76171ee9-444f-55b9-be06-dba5a2558e64",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    display_name="Zubat",
    searchable_by=["Zubat","Basic","Zubat"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    abilities=[
        Ability(
            title="Free Flight",
            game_text="If this Pokémon has no Energy attached to it, this Pokémon has no Retreat Cost.",
            passive=retreat_free_when(_no_energy_attached),
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
