from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='f0acb0ae-1312-52d1-923d-c1ae1b9ffaf0',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmDragon.Name',
    display_name='Fairy Charm Dragon',
    searchable_by=['Fairy Charm Dragon', 'Pokémon Tool', 'FairyCharmDragon'],
    subtypes=['Pokémon Tool'],
    collector_number=177,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Dragon Pokémon-GX and Dragon Pokémon-EX. You may play as many Item cards as you like during your turn (before your attack)."),
)
