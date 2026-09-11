from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='06e9fae0-f868-50ec-9137-71fdb4fe5738',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RigidBand.Name',
    display_name='Rigid Band',
    searchable_by=['Rigid Band', 'Pokémon Tool', 'RigidBand'],
    subtypes=['Pokémon Tool'],
    collector_number=165,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Stage 1 Pokémon this card is attached to takes 30 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance)."),
)
