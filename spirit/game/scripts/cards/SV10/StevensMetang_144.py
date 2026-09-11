from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="03c8c728-d746-5af6-93b7-9ace963e7375",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensMetang.Name",
    display_name="Steven's Metang",
    searchable_by=["Steven's Metang", "Stage 1", "StevensMetang"],
    subtypes=["Stage 1"],
    collector_number=144,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.StevensBeldum.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Metal Slash",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
