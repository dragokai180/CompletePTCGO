from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = StadiumCardDef(
    guid='b153aa0a-2aa0-5609-b220-9f77233a7231',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TeamAquasSecretBase.Name',
    display_name="Team Aqua's Secret Base",
    searchable_by=["Team Aqua's Secret Base", 'Stadium', 'TeamAquasSecretBase'],
    subtypes=['Stadium'],
    collector_number=28,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Retreat Cost of each Pokémon in play (except for Team Aqua Pokémon) is Colorless more. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
    ability=standard_stadium_ability("The Retreat Cost of each Pokémon in play (except for Team Aqua Pokémon) is Colorless more. This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card."),
)
