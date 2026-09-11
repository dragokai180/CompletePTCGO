from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="b06f46a8-58a9-51bf-8104-c2a31460f8bf",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durantex.Name",
    display_name="Durant ex",
    searchable_by=["Durant ex", "Basic", "ex", "Durantex"],
    subtypes=["Basic", "ex"],
    collector_number=4,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=632,
    abilities=[
        Ability(
            title="Sudden Shearing",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may discard the top card of your opponent's deck.",
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Vengeful Crush",
            game_text="This attack does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
