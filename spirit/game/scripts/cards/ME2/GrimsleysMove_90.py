from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="b0d5b3d7-aecd-5795-97e6-c98c1eb54432",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GrimsleysMove.Name",
    display_name="Grimsley's Move",
    searchable_by=["Grimsley's Move", "Supporter", "GrimsleysMove"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Look at the top 7 cards of your deck and put a Darkness Pokémon you find there onto your Bench. Shuffle the other cards and put them on the bottom of your deck. You can't use this card during your first turn."),
)
