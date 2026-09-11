from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='72c96a35-d391-5e6f-9a4f-0cf9670a8c41',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FlyiniumZAirSlash.Name',
    display_name='Flyinium Z: Air Slash',
    searchable_by=['Flyinium Z: Air Slash', 'Pokémon Tool', 'FlyiniumZAirSlash'],
    subtypes=['Pokémon Tool'],
    collector_number=195,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('If the Pokémon this card is attached to has the Air Slash attack, it can use the GX attack on this card. (You still need the necessary Energy to use this attack.) You may play as many Item cards as you like during your turn (before your attack).'),
    granted_abilities=[
        Attack(
            title='Speeding Skystrike-GX',
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=180,
            effect=standard_attack,
            locks_next_turn=True,
            gx=True,
        ),
    ],
)
