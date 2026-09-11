from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="2eeb284e-6b27-533d-8ea1-b55e6ceeaef8",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsSandaconda.Name",
    display_name="Hop's Sandaconda",
    searchable_by=["Hop's Sandaconda", "Stage 1", "HopsSandaconda"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsSilicobra.Name",
    family_id=843,
    abilities=[
        Attack(
            title="Rumble",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title="Break Ground",
            game_text="This attack also does 20 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
