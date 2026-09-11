from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='ce1ff911-03ad-5070-9ccf-16c16af8f7a0',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LanasFishingRod.Name',
    display_name="Lana's Fishing Rod",
    searchable_by=["Lana's Fishing Rod", 'Item', 'LanasFishingRod'],
    subtypes=['Item'],
    collector_number=195,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Shuffle a Pokémon and a Pokémon Tool card from your discard pile into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Shuffle a Pokémon and a Pokémon Tool card from your discard pile into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
