from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="922c768d-2c76-5d86-a1b2-08e2d77214d5",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarillex.Name",
    display_name="Azumarill ex",
    searchable_by=["Azumarill ex", "Stage 1", "ex", "Azumarillex"],
    subtypes=["Stage 1", "ex"],
    collector_number=84,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Ability(
            title="Bubble Gathering",
            game_text="As often as you like during your turn, you may use this Ability. Move an Energy from 1 of your other Pokémon to this Pokémon.",
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title="Energized Balloon",
            game_text="This attack does 40 more damage for each Psychic Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
