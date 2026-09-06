from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_ex
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.session.passives import carrier_pokemon


def _safeguard(calc, carrier):
    if carrier_pokemon(carrier) is not calc.target:
        return False
    return calc.attacker is not None and is_pokemon_ex(calc.attacker.archetype_id)


card = PokemonCardDef(
    guid="faa736d1-2501-5840-bc35-3591ab060b0a",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name",
    display_name="Sylveon",
    searchable_by=["Sylveon","Stage 1","Sylveon"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    family_id=133,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    abilities=[
        Ability(
            title="Safeguard",
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon ex.",
            passive=prevent_damage_when(_safeguard),
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
