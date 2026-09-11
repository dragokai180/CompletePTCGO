from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='1a7325dd-c11d-5260-a965-6aeb1fc35b84',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineBlindside.Name',
    display_name='Technical Machine: Blindside',
    searchable_by=['Technical Machine: Blindside', 'Pokémon Tool', 'TechnicalMachineBlindside'],
    subtypes=['Pokémon Tool'],
    collector_number=176,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Pokémon this card is attached to can use the attack on this card. (You still need the necessary Energy to use this attack.) If this card is attached to 1 of your Pokémon, discard it at the end of your turn.'),
    granted_abilities=[
        Attack(
            title='Blindside',
            game_text="This attack does 100 damage to 1 of your opponent's Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
