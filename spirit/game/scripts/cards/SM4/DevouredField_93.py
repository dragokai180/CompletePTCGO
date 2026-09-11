from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='e0b9123a-cf4c-5030-a17e-c52760d66796',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DevouredField.Name',
    display_name='Devoured Field',
    searchable_by=['Devoured Field', 'Stadium', 'DevouredField'],
    subtypes=['Stadium'],
    collector_number=93,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The attacks of Darkness Pokémon and Dragon Pokémon (both yours and your opponent's) do 10 more damage to the opponent's Active Pokémon (before applying Weakness and Resistance). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("The attacks of Darkness Pokémon and Dragon Pokémon (both yours and your opponent's) do 10 more damage to the opponent's Active Pokémon (before applying Weakness and Resistance). This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
