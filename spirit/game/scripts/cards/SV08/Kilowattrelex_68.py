from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="68ef513d-1221-5ced-919a-d44850e23ada",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kilowattrelex.Name",
    display_name="Kilowattrel ex",
    searchable_by=["Kilowattrel ex", "Stage 1", "ex", "Kilowattrelex"],
    subtypes=["Stage 1", "ex"],
    collector_number=68,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    family_id=940,
    abilities=[
        Attack(
            title="Return Charge",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. If you do, attach up to 2 Basic Lightning Energy cards from your hand to this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Thunder Lance",
            game_text="This attack does 40 more damage for each Lightning Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
