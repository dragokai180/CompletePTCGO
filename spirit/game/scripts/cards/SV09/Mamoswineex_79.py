from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="33368458-bd41-568f-99e0-d69101043df4",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswineex.Name",
    display_name="Mamoswine ex",
    searchable_by=["Mamoswine ex", "Stage 2", "ex", "Mamoswineex"],
    subtypes=["Stage 2", "ex"],
    collector_number=79,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    family_id=220,
    abilities=[
        Ability(
            title="Mammoth Hauler",
            game_text="Once during your turn, you may search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Rumbling March",
            game_text="This attack does 40 more damage for each Stage 2 Pokémon on your Bench.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=180,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
