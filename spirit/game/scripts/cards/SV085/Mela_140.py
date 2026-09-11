from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="993fc9c3-240b-58fc-b35d-ea75bb104bb3",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mela.Name",
    display_name="Mela",
    searchable_by=["Mela", "Supporter", "Mela"],
    subtypes=["Supporter"],
    collector_number=140,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareUltra,
    effect=standard_trainer_effect("You can use this card only if any of your Pokémon were Knocked Out during your opponent's last turn.  Attach a Basic Fire Energy card from your discard pile to 1 of your Pokémon. If you do, draw cards until you have 6 cards in your hand."),
)
