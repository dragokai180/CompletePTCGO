from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='6c42bcab-d2ec-5e9d-a4fd-3af6f8fd5ff7',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.VengefulPunch.Name',
    display_name='Vengeful Punch',
    searchable_by=['Vengeful Punch', 'Pokémon Tool', 'VengefulPunch'],
    subtypes=['Pokémon Tool'],
    collector_number=197,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to is Knocked Out by damage from an attack from your opponent's Pokémon, put 4 damage counters on the Attacking Pokémon."),
)
