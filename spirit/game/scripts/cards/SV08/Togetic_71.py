from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="fcad7dfa-6ea1-5bdb-bce5-62f2c2a04c74",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    display_name="Togetic",
    searchable_by=["Togetic","Stage 1","Togetic"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    family_id=175,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    abilities=[
        Attack(
            title="Draining Kiss",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=heal_attack(30),
        ),
    ],
)
