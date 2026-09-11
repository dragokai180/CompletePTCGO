from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='c373ff38-28c1-5aee-9e52-dee864ade3ce',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AquaDiffuser.Name',
    display_name='Aqua Diffuser',
    searchable_by=['Aqua Diffuser', 'Pokémon Tool', 'AquaDiffuser'],
    subtypes=['Pokémon Tool'],
    collector_number=23,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Team Aqua Pokémon this card is attached to can also use the attack on this card. (You still need the necessary Energy to use this attack.) You may play as many Item cards as you like during your turn (before your attack).'),
    granted_abilities=[
        Attack(
            title='Aqua Diffuser',
            game_text="Your opponent's Active Pokémon is now Confused and Poisoned.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
