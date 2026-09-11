from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='b9cad71f-88b2-5d68-8769-ccc08ea903cf',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PoisonBarb.Name',
    display_name='Poison Barb',
    searchable_by=['Poison Barb', 'Pokémon Tool', 'PoisonBarb'],
    subtypes=['Pokémon Tool'],
    collector_number=124,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Poisoned. You may play as many Item cards as you like during your turn (before your attack)."),
)
