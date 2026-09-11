from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="7157626b-581d-54a7-9d7b-aaec4610b729",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dubwool.Name",
    display_name="Dubwool",
    searchable_by=["Dubwool", "Stage 1", "Dubwool"],
    subtypes=["Stage 1"],
    collector_number=125,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooloo.Name",
    family_id=831,
    abilities=[
        Ability(
            title="Soft Wool",
            game_text="This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=standard_passive("This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance)."),
        ),
        Attack(
            title="Knock Over",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
