from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="a6a4027a-c1a6-5c58-9f04-2368ff5dfa82",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorSadasVitality.Name",
    display_name="Professor Sada's Vitality",
    searchable_by=["Professor Sada's Vitality", "Supporter", "Ancient", "ProfessorSadasVitality"],
    subtypes=["Supporter", "Ancient"],
    collector_number=120,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Choose up to 2 of your Ancient Pokémon and attach a Basic Energy card from your discard pile to each of them. If you attached any Energy in this way, draw 3 cards."),
)
