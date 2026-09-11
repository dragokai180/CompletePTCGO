from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="28d72c3f-8ef1-5162-b756-ddf8faa165f7",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    display_name="Darumaka",
    searchable_by=["Darumaka", "Basic", "Darumaka"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=554,
    abilities=[
        Attack(
            title="Strength",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Fire Tackle",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
