from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="9ddc1a5a-93fa-5b06-9b36-af909d101028",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsCramorant.Name",
    display_name="Hop's Cramorant",
    searchable_by=["Hop's Cramorant", "Basic", "HopsCramorant"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=845,
    abilities=[
        Attack(
            title="Fickle Spitting",
            game_text="If your opponent doesn't have exactly 3 or 4 Prize cards remaining, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
