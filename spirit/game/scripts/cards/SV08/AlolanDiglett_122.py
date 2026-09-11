from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="3675f578-d0ae-5fef-ad74-52c15bad8a11",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    display_name="Alolan Diglett",
    searchable_by=["Alolan Diglett", "Basic", "AlolanDiglett"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=50,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
