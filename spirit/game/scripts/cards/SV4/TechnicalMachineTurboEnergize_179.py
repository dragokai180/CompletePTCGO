from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='62a9137d-bf93-5390-a49a-a5ef41b21a15',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineTurboEnergize.Name',
    display_name='Technical Machine: Turbo Energize',
    searchable_by=['Technical Machine: Turbo Energize', 'Pokémon Tool', 'TechnicalMachineTurboEnergize'],
    subtypes=['Pokémon Tool'],
    collector_number=179,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Pokémon this card is attached to can use the attack on this card. (You still need the necessary Energy to use this attack.) If this card is attached to 1 of your Pokémon, discard it at the end of your turn.'),
    granted_abilities=[
        Attack(
            title='Turbo Energize',
            game_text='Search your deck for up to 2 Basic Energy cards and attach them to your Benched Pokémon in any way you like. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
