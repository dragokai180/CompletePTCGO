from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d6d14873-200e-5db5-95e2-95b6555c39c5',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name',
    display_name='Kyogre',
    searchable_by=['Kyogre', 'Basic', 'Kyogre'],
    subtypes=['Basic'],
    collector_number=101,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    attributes={200790: {'type': 'string', 'value': 'SL6'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=382,
    abilities=[
        Attack(
            title='Destructive Tsunami',
            game_text="Flip a coin. If heads, this attack does 40 damage to each of your opponent's Pokémon. If tails, this attack does 40 damage to each of your Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 4},
            effect=standard_attack,
        ),
    ],
)
