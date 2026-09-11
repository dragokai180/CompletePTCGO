from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cdff9678-5f4f-5745-9934-e051417ab36b',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name',
    display_name='Alolan Meowth',
    searchable_by=['Alolan Meowth', 'Basic', 'AlolanMeowth'],
    subtypes=['Basic'],
    collector_number=118,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=52,
    abilities=[
        Attack(
            title='Spoil the Fun',
            game_text='If you go second, this attack does 60 more damage during your first turn.',
            cost={},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
