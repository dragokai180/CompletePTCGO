from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='38015e59-674d-5e0d-9f98-715612ab48e2',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GiantBomb.Name',
    display_name='Giant Bomb',
    searchable_by=['Giant Bomb', 'Pokémon Tool', 'GiantBomb'],
    subtypes=['Pokémon Tool'],
    collector_number=196,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("If this card is attached to 1 of your Pokémon, discard it at the end of your opponent's turn. If the Pokémon this card is attached to is your Active Pokémon and takes 180 or more damage from an opponent's attack (even if this Pokémon is Knocked Out), put 10 damage counters on the Attacking Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
)
