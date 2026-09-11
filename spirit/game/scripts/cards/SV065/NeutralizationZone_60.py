from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = StadiumCardDef(
    guid="17ac267d-07d9-538e-8786-3510d0c7c2ce",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NeutralizationZone.Name",
    display_name="Neutralization Zone",
    searchable_by=["Neutralization Zone", "Stadium", "ACE SPEC", "NeutralizationZone"],
    subtypes=["Stadium", "ACE SPEC"],
    collector_number=60,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Ace,
    passive=standard_passive("You can't have more than 1 ACE SPEC card in your deck. Prevent all damage done to Pokémon that don't have a Rule Box (both yours and your opponent's) by attacks from the opponent's Pokémon ex and Pokémon V. (Pokémon ex, Pokémon V, etc. have Rule Boxes.)    This card can't be put into your hand or deck from the discard pile."),
    ability=standard_stadium_ability("You can't have more than 1 ACE SPEC card in your deck. Prevent all damage done to Pokémon that don't have a Rule Box (both yours and your opponent's) by attacks from the opponent's Pokémon ex and Pokémon V. (Pokémon ex, Pokémon V, etc. have Rule Boxes.)    This card can't be put into your hand or deck from the discard pile."),
)
