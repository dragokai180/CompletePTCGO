from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='625128f2-da71-59b3-90bd-39d1a71dd6e0',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineCrisisPunch.Name',
    display_name='Technical Machine: Crisis Punch',
    searchable_by=['Technical Machine: Crisis Punch', 'Pokémon Tool', 'TechnicalMachineCrisisPunch'],
    subtypes=['Pokémon Tool'],
    collector_number=90,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Pokémon this card is attached to can use the attack on this card. (You still need the necessary Energy to use this attack.) If this card is attached to 1 of your Pokémon, discard it at the end of your turn.'),
    granted_abilities=[
        Attack(
            title='Crisis Punch',
            game_text='You can use this attack only when your opponent has exactly 1 Prize card remaining.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=280,
            effect=standard_attack,
        ),
    ],
)
