from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='17233f34-5885-54d2-8b85-48e0f0d2ee6a',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LegendBox.Name',
    display_name='Legend Box',
    searchable_by=['Legend Box', 'Item', 'LegendBox'],
    subtypes=['Item'],
    collector_number=75,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Reveal the top 10 cards of your deck. If you reveal both halves of a Pokémon LEGEND, put those cards onto your Bench and attach all revealed Energy cards to that Pokémon LEGEND. Shuffle the other cards back into your deck. (You can play only 1 Pokémon LEGEND in this way.)'),
    condition=standard_trainer_condition('Reveal the top 10 cards of your deck. If you reveal both halves of a Pokémon LEGEND, put those cards onto your Bench and attach all revealed Energy cards to that Pokémon LEGEND. Shuffle the other cards back into your deck. (You can play only 1 Pokémon LEGEND in this way.)'),
)
