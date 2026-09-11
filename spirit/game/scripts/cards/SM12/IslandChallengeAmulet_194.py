from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='dcddc8d0-1d8d-54b0-8560-28cdd0d6c8ce',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.IslandChallengeAmulet.Name',
    display_name='Island Challenge Amulet',
    searchable_by=['Island Challenge Amulet', 'Pokémon Tool', 'IslandChallengeAmulet'],
    subtypes=['Pokémon Tool'],
    collector_number=194,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Pokémon-GX or Pokémon-EX this card is attached to gets -100 HP, and when it is Knocked Out by damage from an opponent's attack, that player takes 1 fewer Prize card. You may play as many Item cards as you like during your turn (before your attack)."),
)
