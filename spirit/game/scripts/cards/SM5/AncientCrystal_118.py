from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='3e83a386-39a7-5482-82bb-5a651fe574c6',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AncientCrystal.Name',
    display_name='Ancient Crystal',
    searchable_by=['Ancient Crystal', 'Pokémon Tool', 'AncientCrystal'],
    subtypes=['Pokémon Tool'],
    collector_number=118,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Regirock, Regice, Registeel, or Regigigas this card is attached to takes 30 less damage from your opponent's attacks (after applying Weakness and Resistance). You may play as many Item cards as you like during your turn (before your attack)."),
)
