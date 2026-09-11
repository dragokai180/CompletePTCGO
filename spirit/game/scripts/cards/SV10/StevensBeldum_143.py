from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="9fb77bff-6afc-50a5-b6fd-59c5a6e66ece",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensBeldum.Name",
    display_name="Steven's Beldum",
    searchable_by=["Steven's Beldum", "Basic", "StevensBeldum"],
    subtypes=["Basic"],
    collector_number=143,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=374,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
