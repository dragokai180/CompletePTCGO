from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='d4dd6f80-a724-57f5-8d0a-a5a149157363',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MagmaPointer.Name',
    display_name='Magma Pointer',
    searchable_by=['Magma Pointer', 'Pokémon Tool', 'MagmaPointer'],
    subtypes=['Pokémon Tool'],
    collector_number=24,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Team Magma Pokémon this card is attached to can also use the attack on this card. (You still need the necessary Energy to use this attack.) You may play as many Item cards as you like during your turn (before your attack).'),
    granted_abilities=[
        Attack(
            title='Magma Pointer',
            game_text="This attack does 20 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
    ],
)
