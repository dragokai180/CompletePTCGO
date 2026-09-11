from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid="9db92760-2c3f-5a5e-aef3-6697ab656e4c",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AmuletofHope.Name",
    display_name="Amulet of Hope",
    searchable_by=["Amulet of Hope", "Pokémon Tool", "ACE SPEC", "AmuletofHope"],
    subtypes=["Pokémon Tool", "ACE SPEC"],
    collector_number=162,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Ace,
    passive=standard_passive("If the Pokémon this card is attached to is Knocked Out by damage from an attack from your opponent's Pokémon, search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck. ACE SPEC: You can't have more than 1 ACE SPEC card in your deck."),
)
