from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='46315776-88a1-5d3a-93dc-43ae9ecb11d2',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BeastBringer.Name',
    display_name='Beast Bringer',
    searchable_by=['Beast Bringer', 'Pokémon Tool', 'BeastBringer'],
    subtypes=['Pokémon Tool'],
    collector_number=164,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("If you have exactly 6 Prize cards remaining, and if your opponent's Active Pokémon-GX or Pokémon-EX is Knocked Out by damage from an attack of the Ultra Beast this card is attached to, take 1 more Prize card. You may play as many Item cards as you like during your turn (before your attack)."),
)
