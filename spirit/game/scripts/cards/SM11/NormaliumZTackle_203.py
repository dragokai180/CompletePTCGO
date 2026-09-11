from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='e0e79950-9af0-52af-b325-ef747d9ba488',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.NormaliumZTackle.Name',
    display_name='Normalium Z: Tackle',
    searchable_by=['Normalium Z: Tackle', 'Pokémon Tool', 'NormaliumZTackle'],
    subtypes=['Pokémon Tool'],
    collector_number=203,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('If the Pokémon this card is attached to has the Tackle attack, it can use the GX attack on this card. (You still need the necessary Energy to use this attack.) You may play as many Item cards as you like during your turn (before your attack).'),
    granted_abilities=[
        Attack(
            title='Barreling Blitz-GX',
            game_text="Flip a coin until you get tails. This attack does 40 more damage for each heads. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=200,
            damage_operator='+',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
