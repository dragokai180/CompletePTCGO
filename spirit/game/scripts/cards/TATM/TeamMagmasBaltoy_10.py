from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2cdfa24a-4fa1-5a4f-9990-f05011e0b10c',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasBaltoy.Name',
    display_name="Team Magma's Baltoy",
    searchable_by=["Team Magma's Baltoy", 'Basic', 'TeamMagmasBaltoy'],
    subtypes=['Basic'],
    collector_number=10,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=343,
    abilities=[
        Attack(
            title='Telekinesis',
            game_text="This attack does 20 damage to 1 of your opponent's Pokémon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
