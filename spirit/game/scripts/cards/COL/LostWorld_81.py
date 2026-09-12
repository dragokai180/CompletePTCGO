from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.card_effects.hgss_era import lost_world, lost_world_condition
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='c2564425-61ca-5231-a187-ef3842ecd9d1',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LostWorld.Name',
    display_name='Lost World',
    searchable_by=['Lost World', 'Stadium', 'LostWorld'],
    subtypes=['Stadium'],
    collector_number=81,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card. Once during each player's turn, if that player's opponent has 6 or more Pokémon in the Lost Zone, the player may choose to win the game."),
    ability=Ability(title='Lost World',
        game_text="During your turn, if your opponent has 6 or more Pokemon in the Lost Zone, you may choose to win the game.",
        activation=Activations.ONCE_PER_TURN, effect=lost_world,
        condition=lost_world_condition),
)
