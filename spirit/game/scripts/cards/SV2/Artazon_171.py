from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='b13a955f-3726-5ead-ba03-d8e08fe80bfd',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Artazon.Name',
    display_name='Artazon',
    searchable_by=['Artazon', 'Stadium', 'Artazon'],
    subtypes=['Stadium'],
    collector_number=171,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("Once during each player's turn, that player may search their deck for a Basic Pokémon that doesn't have a Rule Box and put it onto their Bench. Then, that player shuffles their deck. (Pokémon ex, Pokémon V, etc. have Rule Boxes.)"),
    ability=standard_stadium_ability("Once during each player's turn, that player may search their deck for a Basic Pokémon that doesn't have a Rule Box and put it onto their Bench. Then, that player shuffles their deck. (Pokémon ex, Pokémon V, etc. have Rule Boxes.)"),
)
