from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="a542cfd6-6a4b-5d36-be39-7910ac1d80fa",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1", "Azumarill"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Ability(
            title="Glistening Bubbles",
            game_text="If you have any Tera Pokémon in play, this Pokémon can use the Double-Edge attack for Psychic.",
            passive=standard_passive("If you have any Tera Pokémon in play, this Pokémon can use the Double-Edge attack for Psychic."),
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 4},
            damage=230,
            effect=standard_attack,
        ),
    ],
)
