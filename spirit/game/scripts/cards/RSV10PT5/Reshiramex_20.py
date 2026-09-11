from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="11695be1-2667-5a9c-894b-bcb16725bcc9",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiramex.Name",
    display_name="Reshiram ex",
    searchable_by=["Reshiram ex", "Basic", "ex", "Reshiramex"],
    subtypes=["Basic", "ex"],
    collector_number=20,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=643,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Blazing Burst",
            game_text="This attack does 50 more damage for each Prize card your opponent has taken. Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
