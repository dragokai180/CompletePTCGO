from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='cf91b818-3007-5cb6-ae83-b961cf0135b2',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BodybuildingDumbbells.Name',
    display_name='Bodybuilding Dumbbells',
    searchable_by=['Bodybuilding Dumbbells', 'Pokémon Tool', 'BodybuildingDumbbells'],
    subtypes=['Pokémon Tool'],
    collector_number=113,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Stage 1 Pokémon this card is attached to gets +40 HP. You may play as many Item cards as you like during your turn (before your attack).'),
)
