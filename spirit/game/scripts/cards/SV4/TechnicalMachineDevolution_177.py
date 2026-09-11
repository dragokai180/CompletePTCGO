from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='e711bfc8-bae6-5392-8656-eb6791b46d78',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineDevolution.Name',
    display_name='Technical Machine: Devolution',
    searchable_by=['Technical Machine: Devolution', 'Pokémon Tool', 'TechnicalMachineDevolution'],
    subtypes=['Pokémon Tool'],
    collector_number=177,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Pokémon this card is attached to can use the attack on this card. (You still need the necessary Energy to use this attack.) If this card is attached to 1 of your Pokémon, discard it at the end of your turn.'),
    granted_abilities=[
        Attack(
            title='Devolution',
            game_text="Devolve each of your opponent's evolved Pokémon by putting the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
