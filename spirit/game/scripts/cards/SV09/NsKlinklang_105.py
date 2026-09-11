from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="d8256795-2a21-5bd3-81bf-41cf707b9a6b",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsKlinklang.Name",
    display_name="N's Klinklang",
    searchable_by=["N's Klinklang", "Stage 2", "NsKlinklang"],
    subtypes=["Stage 2"],
    collector_number=105,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsKlang.Name",
    family_id=599,
    abilities=[
        Attack(
            title="Magnetic Blast",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Triple Smash",
            game_text="Flip 3 coins. This attack does 120 damage for each heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
