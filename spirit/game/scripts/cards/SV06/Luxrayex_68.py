from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="eb4daa8a-a8cb-50d3-8bf8-d8eea223fa0e",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxrayex.Name",
    display_name="Luxray ex",
    searchable_by=["Luxray ex", "Stage 2", "ex", "Luxrayex"],
    subtypes=["Stage 2", "ex"],
    collector_number=68,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Attack(
            title="Piercing Gaze",
            game_text="Your opponent reveals their hand. Discard a card you find there.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title="Volt Strike",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=250,
            effect=standard_attack,
        ),
    ],
)
