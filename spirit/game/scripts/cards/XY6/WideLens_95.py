from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='3fc2f08d-eca4-5445-917f-671123b7bfda',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.WideLens.Name',
    display_name='Wide Lens',
    searchable_by=['Wide Lens', 'Pokémon Tool', 'WideLens'],
    subtypes=['Pokémon Tool'],
    collector_number=95,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Damage from the attacks of the Pokémon this card is attached to is affected by Weakness and Resistance for your opponent's Benched Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
)
