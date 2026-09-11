from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='a1bc0828-b71f-596d-8e12-a06ef6ba2838',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FightingFuryBelt.Name',
    display_name='Fighting Fury Belt',
    searchable_by=['Fighting Fury Belt', 'Pokémon Tool', 'FightingFuryBelt'],
    subtypes=['Pokémon Tool'],
    collector_number=99,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Basic Pokémon this card is attached to gets +40 HP and its attacks do 10 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). You may play as many Item cards as you like during your turn (before your attack)."),
)
