from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='ea7c61e1-4083-504f-b87a-1f3f72395048',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DragoniumZDragonClaw.Name',
    display_name='Dragonium Z: Dragon Claw',
    searchable_by=['Dragonium Z: Dragon Claw', 'Pokémon Tool', 'DragoniumZDragonClaw'],
    subtypes=['Pokémon Tool'],
    collector_number=190,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('If the Pokémon this card is attached to has the Dragon Claw attack, it can use the GX attack on this card. (You still need the necessary Energy to use this attack.) You may play as many Item cards as you like during your turn (before your attack).'),
    granted_abilities=[
        Attack(
            title='Destructive Drake-GX',
            game_text="Discard all basic Energy from this Pokémon. This attack does 80 damage for each card you discarded in this way. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
