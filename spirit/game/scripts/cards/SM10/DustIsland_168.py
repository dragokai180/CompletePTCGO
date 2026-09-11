from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='cf6a3667-cbcc-5ead-b1ec-1ad793af782e',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DustIsland.Name',
    display_name='Dust Island',
    searchable_by=['Dust Island', 'Stadium', 'DustIsland'],
    subtypes=['Stadium'],
    collector_number=168,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("Whenever either player switches their Poisoned Active Pokémon with 1 of their Benched Pokémon with the effect of a Trainer card, the new Active Pokémon is now affected by that Special Condition. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("Whenever either player switches their Poisoned Active Pokémon with 1 of their Benched Pokémon with the effect of a Trainer card, the new Active Pokémon is now affected by that Special Condition. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
