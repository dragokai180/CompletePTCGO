from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='e55c142b-4b16-53ba-9e76-27371d728790',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmAbility.Name',
    display_name='Fairy Charm Ability',
    searchable_by=['Fairy Charm Ability', 'Pokémon Tool', 'FairyCharmAbility'],
    subtypes=['Pokémon Tool'],
    collector_number=171,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Pokémon-GX and Pokémon-EX that have Abilities. You may play as many Item cards as you like during your turn (before your attack)."),
)
