from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="36118eac-24da-54df-8e99-1c47545c5deb",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    display_name="Toedscool",
    searchable_by=["Toedscool", "Basic", "Toedscool"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=948,
    abilities=[
        Attack(
            title="Spray Fluid",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
