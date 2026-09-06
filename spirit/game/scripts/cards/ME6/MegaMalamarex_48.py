from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, damage_per, count_bench

card = PokemonCardDef(
    guid="c378183c-9eff-5945-ba58-8c483cec0f30",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaMalamarex.Name",
    display_name="Mega Malamar ex",
    searchable_by=["Mega Malamar ex","Stage 1","ex","SV_Mega","MegaMalamarex"],
    subtypes=["Stage 1","ex","SV_Mega"],
    collector_number=48,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Attack(
            title="Psycho Marionette",
            game_text="This attack does 70 damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            damage_operator="x",
            effect=damage_per(count_bench("opponent"), 70),
        ),
        Attack(
            title="Eerie Wave",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=200,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
