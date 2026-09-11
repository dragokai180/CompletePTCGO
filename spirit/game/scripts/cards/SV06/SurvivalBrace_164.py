from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="caafae10-e30e-5ece-a8ae-1de60f3e39d0",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SurvivalBrace.Name",
    display_name="Survival Brace",
    searchable_by=["Survival Brace", "Pokémon Tool", "ACE SPEC", "SurvivalBrace"],
    subtypes=["Pokémon Tool", "ACE SPEC"],
    collector_number=164,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Ace,
    passive=standard_passive("You can't have more than 1 ACE SPEC card in your deck. If the Pokémon this card is attached to has full HP and would be Knocked Out by damage from an attack from your opponent's Pokémon, it is not Knocked Out, and its remaining HP becomes 10. Then, discard this card. ACE SPEC: You can't have more than 1 ACE SPEC card in your deck."),
)
