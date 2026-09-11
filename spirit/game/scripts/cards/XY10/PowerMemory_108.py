from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='3ea92e06-a056-54ae-a05d-99ccf7955aba',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PowerMemory.Name',
    display_name='Power Memory',
    searchable_by=['Power Memory', 'Pokémon Tool', 'PowerMemory'],
    subtypes=['Pokémon Tool'],
    collector_number=108,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Zygarde-EX this card is attached to can also use the attack on this card. (You still need the necessary Energy to use this attack.) You may play as many Item cards as you like during your turn (before your attack).'),
    granted_abilities=[
        Attack(
            title='All Cells Burn',
            game_text='Discard 3 Energy attached to this Pokémon.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
