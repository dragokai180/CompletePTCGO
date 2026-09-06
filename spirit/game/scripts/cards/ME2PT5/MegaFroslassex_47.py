from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, count_hand, damage_per

card = PokemonCardDef(
    guid="92e36fc2-8174-509c-9590-64e4ac0e14c7",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaFroslassex.Name",
    display_name="Mega Froslass ex",
    searchable_by=["Mega Froslass ex", "Stage 1", "ex", "SV_Mega", "MegaFroslassex"],
    subtypes=["Stage 1", "ex", "SV_Mega"],
    collector_number=47,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Resentful Refrain",
            game_text="This attack does 50 damage for each card in your opponent's hand.",
            cost={PokemonTypes.WATER: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_hand("opponent"), 50),
        ),
        Attack(
            title="Absolute Snow",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
