from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="2fbc30d8-2410-529c-9d7c-62536b198191",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BloodmoonUrsaluna.Name",
    display_name="Bloodmoon Ursaluna",
    searchable_by=["Bloodmoon Ursaluna", "Basic", "BloodmoonUrsaluna"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=901,
    abilities=[
        Ability(
            title="Battle-Hardened",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may attach up to 2 Basic Fighting Energy cards from your hand to this Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Mad Bite",
            game_text="This attack does 30 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
