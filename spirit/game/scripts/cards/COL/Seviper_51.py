from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f7fa8156-1660-51d5-acd3-8b73b29e81af',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name',
    display_name='Seviper',
    searchable_by=['Seviper', 'Basic', 'Seviper'],
    subtypes=['Basic'],
    collector_number=51,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=336,
    abilities=[
        Attack(
            title='Poison Buildup',
            game_text='Seviper is now Poisoned.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Poison Effect',
            game_text='If Seviper is Poisoned, this attack does 20 damage plus 60 more damage and remove the Special Condition Poisoned from Seviper.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
