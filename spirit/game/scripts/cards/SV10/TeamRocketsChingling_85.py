from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="6494ccc1-7a77-50f6-a29e-a48321ffdfd1",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsChingling.Name",
    display_name="Team Rocket's Chingling",
    searchable_by=["Team Rocket's Chingling", "Basic", "TeamRocketsChingling"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=433,
    abilities=[
        Attack(
            title="Chiming Commotion",
            game_text="Discard a random card from your opponent's hand.",
            cost={},
            effect=standard_attack,
        ),
    ],
)
