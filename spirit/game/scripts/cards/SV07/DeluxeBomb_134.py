from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="d45d5213-97cc-55aa-9295-122c2fefa404",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DeluxeBomb.Name",
    display_name="Deluxe Bomb",
    searchable_by=["Deluxe Bomb", "Pokémon Tool", "ACE SPEC", "DeluxeBomb"],
    subtypes=["Pokémon Tool", "ACE SPEC"],
    collector_number=134,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Ace,
    passive=standard_passive("You can't have more than 1 ACE SPEC card in your deck. If the Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 12 damage counters on the Attacking Pokémon. If you placed any damage counters in this way, discard this card."),
)
