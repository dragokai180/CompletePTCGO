from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    damage_per, count_discard, self_energy_discard_attack, snipe_attack,
)
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="a7c9ebe1-3394-5bf8-91a5-7e5d6f5d2c7c",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsDarmanitan.Name",
    display_name="N's Darmanitan",
    searchable_by=["N's Darmanitan", "Stage 1", "NsDarmanitan"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsDarumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Back Draft",
            game_text="This attack does 30 damage for each Basic Energy card in your opponent's discard pile.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_discard("opponent", is_basic_energy_card), 30),
        ),
        Attack(
            title="Flamebody Cannon",
            game_text="Discard all Energy from this Pokémon, and this attack also does 90 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=self_energy_discard_attack(
                all_energy=True,
                also=snipe_attack(90, pool="bench", count=1),
            ),
        ),
    ],
)
