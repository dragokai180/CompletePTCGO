from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="b378bbd6-8323-50f6-b14f-1b9591563556",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosVoltorb.Name",
    display_name="Iono's Voltorb",
    searchable_by=["Iono's Voltorb", "Basic", "IonosVoltorb"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=100,
    abilities=[
        Attack(
            title="Voltaic Chain",
            game_text="This attack does 20 more damage for each Lightning Energy attached to all of your Iono's Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
